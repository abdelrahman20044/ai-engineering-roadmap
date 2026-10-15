#!/usr/bin/env python3
"""Validate repository links, prerequisite graph, coverage, tracker and seed data."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from progress import definitions, read_tracker, validate_rows
from build_overview import check_html

ROOT = Path(__file__).resolve().parents[1]

def check_graph(defs):
    visited, visiting = set(), set()
    def visit(id):
        if id in visiting:
            raise ValueError('Prerequisite cycle at '+id)
        if id in visited:
            return
        if id not in defs:
            raise ValueError('Unknown prerequisite '+id)
        visiting.add(id)
        for parent in defs[id]['prerequisites']:
            visit(parent)
        visiting.remove(id)
        visited.add(id)
    for id in defs:
        visit(id)

def markdown_links(root):
    errors = []
    count = 0
    for file in root.rglob('*.md'):
        body = re.sub(r'```.*?```', '', file.read_text(encoding='utf-8'), flags=re.S)
        for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', body):
            target = link.split(' "', 1)[0].strip('<> ')
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            path = (file.parent / unquote(parsed.path)).resolve()
            count += 1
            if not path.is_relative_to(root.resolve()) or not path.exists():
                errors.append(f'{file.relative_to(root)} -> {target}')
    return count, errors

def validate(root=ROOT):
    defs = definitions(root)
    check_graph(defs)
    rows = read_tracker(root/'progress/tracker.csv')
    validate_rows(rows, defs)
    for id, d in defs.items():
        if not (root/d['path']).is_file():
            raise ValueError(f'{id}: module/milestone file missing')
    topics = json.loads((root/'docs/iti_topics.json').read_text(encoding='utf-8'))
    if len(topics)!=32 or sum(t['official_hours'] for t in topics)!=696:
        raise ValueError('Native syllabus table changed: verify source and documented total conflict')
    topic_ids = {t['id'] for t in topics}
    for topic in topics:
        if not topic['modules']:
            raise ValueError('Unmapped ITI topic '+topic['id'])
        for id in topic['modules']:
            if id not in defs or topic['id'] not in defs[id]['syllabus']:
                raise ValueError('Coverage mismatch '+topic['id']+' '+id)
    for id, d in defs.items():
        if d['kind']=='module' and not set(d['syllabus']) <= topic_ids:
            raise ValueError('Unknown ITI topic in '+id)
    count, errors = markdown_links(root)
    if errors:
        raise ValueError('Broken local links:\n'+'\n'.join(errors))
    for level in defs.values():
        if level['kind'] != 'module':
            continue
        folder = root / Path(level['path']).parent
        for name in ['README.md', 'resources.md']:
            page = folder/name
            if not page.is_file() or len(page.read_text()) < 1200:
                raise ValueError('Missing or empty Level content: '+str(page))
    ET.parse(root/'assets/roadmap.svg')
    html_links = check_html(root/'OVERVIEW.html')
    corpus = [json.loads(line) for line in (root/'exercises/data/corpus.jsonl').read_text(encoding='utf-8').splitlines()]
    evidence = {f'{d["document_id"]}:{d["page"]}':d for d in corpus}
    cases = [json.loads(line) for line in (root/'exercises/data/eval_seed.jsonl').read_text(encoding='utf-8').splitlines()]
    if len({q['id'] for q in cases}) != len(cases):
        raise ValueError('Duplicate eval ID')
    for q in cases:
        if q['answerable'] and not q['evidence']:
            raise ValueError('Answerable seed missing evidence '+q['id'])
        for ref in q['evidence']:
            if ref not in evidence or evidence[ref]['owner_id'] != q['user_id']:
                raise ValueError('Unknown or cross-user evidence '+q['id'])
    forbidden = ['AI-Ready Data Engineer', 'Data Engineering specialization', 'Airflow', 'Kafka', 'lakehouse', 'dbt']
    curriculum = (root/'curriculum.json').read_text(encoding='utf-8')
    if any(term in curriculum for term in forbidden):
        raise ValueError('Unexpected out-of-scope specialization term in curriculum')
    return dict(modules=sum(d['kind']=='module' for d in defs.values()), milestones=sum(d['kind']=='milestone' for d in defs.values()), native_topics=len(topics), local_links=count, html_links=html_links, seed_cases=len(cases))

if __name__=='__main__':
    try:
        print(json.dumps(validate(), ensure_ascii=False, indent=2))
        print('PASS: structure and evidence fields validated; application skill is not assessed.')
    except (ValueError, OSError, KeyError, ET.ParseError) as error:
        print('FAIL: '+str(error), file=sys.stderr)
        raise SystemExit(1)
