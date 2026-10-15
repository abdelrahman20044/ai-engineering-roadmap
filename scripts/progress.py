#!/usr/bin/env python3
"""Self-reported learning progress with prerequisite and evidence-field checks."""
import argparse
import csv
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
STATUSES = {'not_started', 'in_progress', 'completed', 'waived', 'blocked'}
ACCEPTED = {'completed', 'waived'}
ACTIVE = {'in_progress', 'completed', 'waived'}
FIELDS = ['id', 'kind', 'status', 'evidence', 'reason', 'updated_at']

def definitions(root=ROOT):
    modules = json.loads((root / 'curriculum.json').read_text(encoding='utf-8'))['modules']
    stages = json.loads((root / 'project/milestones.json').read_text(encoding='utf-8'))
    result = {m['id']: dict(m, kind='module') for m in modules}
    result.update({s['id']: dict(s, kind='milestone') for s in stages})
    return result

def read_tracker(path):
    with Path(path).open(newline='', encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            raise ValueError('Tracker columns must be: ' + ', '.join(FIELDS))
        rows = list(reader)
    if len({r['id'] for r in rows}) != len(rows):
        raise ValueError('Duplicate tracker ID')
    return rows

def validate_rows(rows, defs):
    indexed = {r['id']: r for r in rows}
    if len(indexed) != len(rows) or set(indexed) != set(defs):
        raise ValueError('Tracker IDs must match all modules and milestones exactly')
    for row in rows:
        id = row['id']
        if row['kind'] != defs[id]['kind']:
            raise ValueError(f'{id}: incorrect kind')
        if row['status'] not in STATUSES:
            raise ValueError(f'{id}: invalid status')
        if row['status'] in ACCEPTED and not row['evidence'].strip():
            raise ValueError(f'{id}: completed/waived requires evidence')
        if row['status'] in {'waived', 'blocked'} and not row['reason'].strip():
            raise ValueError(f'{id}: waived/blocked requires a reason')
        if row['status'] in ACTIVE:
            missing = [p for p in defs[id]['prerequisites'] if indexed[p]['status'] not in ACCEPTED]
            if missing:
                raise ValueError(f'{id}: prerequisites not accepted: {", ".join(missing)}')

def updated_rows(rows, defs, id, status, evidence=None, reason=None):
    if id not in defs:
        raise ValueError(f'Unknown ID: {id}')
    result = [dict(r) for r in rows]
    target = next(r for r in result if r['id'] == id)
    target['status'] = status
    if evidence is not None:
        target['evidence'] = evidence
    if reason is not None:
        target['reason'] = reason
    target['updated_at'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
    validate_rows(result, defs)  # Also catches reopening prerequisites of active descendants.
    return result

def save_tracker(path, rows):
    path = Path(path)
    fd, temporary = tempfile.mkstemp(prefix='tracker-', suffix='.csv', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', newline='', encoding='utf-8') as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

def ready_ids(rows, defs):
    states = {r['id']: r['status'] for r in rows}
    return [id for id, d in defs.items()
            if states[id] in {'not_started', 'blocked'}
            and all(states[p] in ACCEPTED for p in d['prerequisites'])]

def markdown_progress(rows, defs):
    """Generate a GitHub-readable snapshot; CSV remains the source of truth."""
    states = {r['id']: r for r in rows}
    groups = {
        'Core modules': [i for i,d in defs.items() if d['kind']=='module' and d['priority']!='P3'],
        'Optional modules': [i for i,d in defs.items() if d['kind']=='module' and d['priority']=='P3'],
        'Project milestones': [i for i,d in defs.items() if d['kind']=='milestone'],
    }
    lines = ['# Progress Dashboard', '', '[Home](../README.md) · [Tracker instructions](README.md) · [Source CSV](tracker.csv)', '',
             'Generated from tracker.csv. Completion is self-reported and evidence-linked, not an automated skill assessment.', '',
             '| Group | Completed | Waived | Total | Accepted |', '|---|---|---|---|---|']
    for title, ids in groups.items():
        done=sum(states[i]['status']=='completed' for i in ids)
        waived=sum(states[i]['status']=='waived' for i in ids)
        lines.append(f'| {title} | {done} | {waived} | {len(ids)} | {(done+waived)/len(ids):.0%} |')
    def cell(value):
        return value.replace('|', '\\|').replace('\n', ' ').replace('\r', ' ') or '—'
    for title, ids in groups.items():
        lines += ['', '## '+title, '', '| Item | Status | Evidence | Reason | Updated UTC |', '|---|---|---|---|---|']
        for id in ids:
            d=defs[id];r=states[id]
            link=f'[{id}: {d["title"]}](../{d["path"]})'
            lines.append('| '+' | '.join([link]+[cell(r[k])for k in ['status','evidence','reason','updated_at']])+' |')
    lines += ['', 'Regenerate with `python scripts/progress.py export` after manual CSV edits. The set command refreshes this dashboard automatically for the default tracker.']
    return '\n'.join(lines)+'\n'

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tracker', type=Path, default=ROOT/'progress/tracker.csv')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('status')
    sub.add_parser('next')
    sub.add_parser('export')
    change = sub.add_parser('set')
    change.add_argument('id')
    change.add_argument('status', choices=sorted(STATUSES))
    change.add_argument('--evidence')
    change.add_argument('--reason')
    args = parser.parse_args(argv)
    try:
        defs = definitions()
        rows = read_tracker(args.tracker)
        validate_rows(rows, defs)
        if args.command == 'set':
            rows = updated_rows(rows, defs, args.id.upper(), args.status, args.evidence, args.reason)
            save_tracker(args.tracker, rows)
            if args.tracker.resolve() == (ROOT/'progress/tracker.csv').resolve():
                (ROOT/'progress/PROGRESS.md').write_text(markdown_progress(rows, defs), encoding='utf-8')
            print(f'{args.id.upper()}: {args.status}. Self-reported; review evidence quality yourself.')
        elif args.command == 'export':
            output=args.tracker.parent/'PROGRESS.md'
            output.write_text(markdown_progress(rows, defs),encoding='utf-8')
            print(f'Exported GitHub table dashboard: {output}')
        elif args.command == 'next':
            for id in ready_ids(rows, defs):
                d = defs[id]
                print(f'{id} | {d["title"]} | {d["path"]}')
        else:
            states = {r['id']: r['status'] for r in rows}
            groups = {
                'Core': [i for i,d in defs.items() if d['kind']=='module' and d['priority']!='P3'],
                'Optional': [i for i,d in defs.items() if d['kind']=='module' and d['priority']=='P3'],
                'Milestones': [i for i,d in defs.items() if d['kind']=='milestone'],
            }
            for label, ids in groups.items():
                completed = sum(states[i]=='completed' for i in ids)
                waived = sum(states[i]=='waived' for i in ids)
                print(f'{label}: {completed}/{len(ids)} completed; {waived} waived; '
                      f'{(completed+waived)/len(ids):.0%} accepted (self-reported)')
            for row in rows:
                print(f'{row["id"]:4} {row["status"]:12} {row["evidence"]}')
        return 0
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print(f'Error: {error}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
