#!/usr/bin/env python3
"""Audit topic/resource coverage and GitHub Markdown file/fragment links."""
from pathlib import Path
import json,re,sys
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]
def anchors(s):
    result=set(re.findall(r'<[^>]+\bid=["\']([^"\']+)',s));seen={}
    s=re.sub(r'```.*?```','',s,flags=re.S)
    for h in re.findall(r'^#{1,6}\s+(.+)$',s,re.M):
        h=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',h);h=re.sub('<[^>]+>','',h)
        slug=re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-');n=seen.get(slug,0);seen[slug]=n+1
        result.add(slug+(f'-{n}' if n else ''))
    return result

def audit():
    c=json.loads((ROOT/'docs/RESOURCE_CATALOG.json').read_text());r={v['id']:v for v in c['resources']};m=json.loads((ROOT/'curriculum.json').read_text())['modules']
    required=['Prerequisites and quick diagnostic','Learning objectives','Recommended learning path','What you learn and exactly where','Book and article focus by topic','ITI syllabus and industry additions','Practical exercises','Common mistakes and debugging guidance','Self-check before moving on','Capstone checkpoint','Completion criteria','Postpone until justified','Record completion']
    cats=['1 · Arabic','2 · English','3 · Slides','4 · Paid','5 · Your three books','6 · Practice','7 · Official','8 · Optional']
    rows=[];errors=[];link_count=0
    for n,mod in enumerate(m):
        data=c['level_maps'][str(n)];topics=data['topics'];page=ROOT/mod['path'];s=page.read_text();res=(page.parent/'resources.md').read_text();keys=set(data['extras'])
        for head in required:
            if '## '+head not in s:errors.append(f'{mod["id"]}: missing {head}')
        for cat in cats:
            if '## '+cat not in res:errors.append(f'{mod["id"]}: missing category {cat}')
        for topic in topics:
            for field in ['name','subtopics','en','docs','book','task']:
                if not topic.get(field):errors.append(f'{mod["id"]}: empty topic field {field}')
            for field in ['ar','en','docs']:keys.update(topic[field])
        missing=keys-r.keys()
        if missing:errors.append(f'{mod["id"]}: unknown resource IDs {missing}')
        if len(keys)<10:errors.append(f'{mod["id"]}: fewer than ten distinct resources; review depth')
        rows.append(dict(level=mod['id'],topics=len(topics),resources=len(keys),arabic_resources=sum(r[k]['language'].startswith('AR') for k in keys),arabic_gap_rows=sum(not t['ar'] for t in topics),partial_arabic_rows=sum(bool(t.get('arabic_scope')) for t in topics)))
    for p in ROOT.rglob('*.md'):
        s=re.sub(r'```.*?```','',p.read_text(),flags=re.S)
        for u in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',s):
            v=urlsplit(u)
            if v.scheme:continue
            dest=(p.parent/unquote(v.path)).resolve() if v.path else p
            if dest.is_dir():dest=dest/'README.md'
            if not dest.exists():errors.append(f'{p.relative_to(ROOT)}: missing {u}');continue
            if v.fragment and dest.suffix=='.md' and unquote(v.fragment) not in anchors(dest.read_text()):errors.append(f'{p.relative_to(ROOT)}: missing fragment {u}')
            link_count+=1
    return dict(levels=rows,local_links_including_fragments=link_count,unique_resources=len(r),errors=errors)
if __name__=='__main__':
    result=audit(); print(json.dumps(result,indent=2))
    if result['errors']:sys.exit(1)
