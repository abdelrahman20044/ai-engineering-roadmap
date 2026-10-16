#!/usr/bin/env python3
"""Audit all learning journeys, reading consistency, preservation and Markdown targets."""
from pathlib import Path
import hashlib,json,re,sys,tempfile
from urllib.parse import urlsplit,unquote
import render_learning
ROOT=Path(__file__).resolve().parents[1]
def anchors(s):
    result=set(re.findall(r'<[^>]+\bid=["\']([^"\']+)',s));seen={}
    s=re.sub(r'```.*?```','',s,flags=re.S)
    for h in re.findall(r'^#{1,6}\s+(.+)$',s,re.M):
        h=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',h);h=re.sub('<[^>]+>','',h)
        slug=re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-');n=seen.get(slug,0);seen[slug]=n+1
        result.add(slug+(f'-{n}' if n else ''))
    return result

def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def audit():
    c=json.loads((ROOT/'docs/RESOURCE_CATALOG.json').read_text());r={v['id']:v for v in c['resources']}
    mods=json.loads((ROOT/'curriculum.json').read_text())['modules'];plan=json.loads((ROOT/'docs/reading_plan.json').read_text());books={b['id']:b for b in plan['assignments']}
    baseline=json.loads((ROOT/'docs/learning_refactor_baseline.json').read_text());errors=[];rows=[];links=0
    def require(condition,message):
        if not condition:errors.append(message)
    require(len(mods)==19,'Expected all 19 Levels')
    require(len(plan['master_order'])==len(books) and set(plan['master_order'])==set(books),'Master order must contain each ledger assignment exactly once')
    require(len(c['verified_chapter_locators'])==30,'All 30 verified book chapter locators must remain')
    for k,old in baseline['resource_fields'].items():
        require(k in r and all(r[k].get(f)==v for f,v in old.items()),'Lost/changed original resource research: '+k)
    for k,v in r.items():
        require(bool(v.get('resource_type')) and bool(v.get('selection_verification')),'Missing type/verification boundary: '+k)
    for f,sha in baseline['protected_file_sha256'].items():require(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==sha,'Changed protected syllabus/milestone/tracker: '+f)
    observed=[]
    for n,m in enumerate(mods):
        id=m['id'];d=c['level_maps'][str(n)];ts=sorted(d['topics'],key=lambda t:t['step_position']);page=ROOT/m['path'];s=page.read_text();lib=(page.parent/'resources.md').read_text();detail=(page.parent/'details.md').read_text()
        require(digest({k:m[k] for k in baseline['protected_module_fields']})==baseline['modules'][id],id+': original prerequisite/exercise/gate contract changed')
        for old in baseline['topic_research'][str(n)]:require(any(all(t.get(k)==v for k,v in old.items()) for t in ts),id+': lost original topic research '+old['name'])
        for field in ['fast','pitfalls','questions','extras','arabic_note']:require(d.get(field)==baseline['level_research'][str(n)].get(field),id+': lost '+field)
        # One diagnostic label now correctly describes recommended review rather than a new prerequisite.
        oldchecks=[x[1] for x in baseline['level_research'][str(n)]['diagnostic']];require([x[1] for x in d['diagnostic']]==oldchecks,id+': lost diagnostic checks')
        require('## Start Here / Recommended Learning Path' in s and s.index('> **Next action:**')<2200,id+': next action not prominent')
        require(not re.search(r'^\|',s,re.M),id+': README has a resource/reference table instead of guided steps')
        require(len(re.findall(r'^### \d+\.',s,re.M))==len(ts),id+': missing ordered steps')
        for head in ['Practical exercises','Ready to move on?','What to defer','Record progress and choose the next Level']:require('## '+head in s,id+': missing '+head)
        require('Complete technical scope' in detail and 'Self-check' in detail and 'ITI provenance' in detail,id+': supporting details missing')
        require(s.count('**Primary ·')==len(ts) and s.count('**Practice:**')==len(ts) and s.count('**Completion check:**')==len(ts),id+': incomplete step contract')
        require(s.count('- [ ] **'+id+'-E')==len(m['exercises']),id+': lost assessed exercises')
        keys=set(d['extras']);seen=set();firsts=[]
        for t in ts:
            for f in ['ar','en','docs']:keys.update(t[f])
            require(t['primary_resource'] in r and t.get('primary_type') and t.get('primary_portion') and t.get('completion_check'),id+': incomplete primary selection')
            if t.get('primary_book'):require(t['primary_book'] in t['reading_ids'],id+': primary book not in step reading')
            for b in t['reading_ids']:
                require(b in books,id+': unknown book ID '+b)
                if b not in books:continue
                require(int(books[b]['first_level'][1:])<=n,id+': future book used early '+b)
                if books[b]['first_level']==id and b not in seen:firsts.append(b)
                seen.add(b)
        require(plan['step_reading_ids'][id]==[t['reading_ids'] for t in ts],id+': step ledger inconsistent')
        require(set(d['reading_now_ids'])==set(firsts) and m['reading_ids']==d['reading_now_ids'],id+': manifest/new book IDs disagree')
        observed.extend(firsts)
        require(keys==set(d['resource_guidance']),id+': resource library lost assignments')
        for k in keys:
            require(f'id="r-{k}"' in lib,id+': resource card missing '+k)
            require(d['resource_guidance'][k]['role'] in ['Primary','Alternative','Reference','Optional Advanced'],id+': invalid role '+k)
        require(lib.count('**Resource Type:**')==len(keys) and lib.count('**Assigned portion:**')==len(keys),id+': resource classification incomplete')
        rows.append(dict(level=id,steps=len(ts),resources=len(keys),readme_tables=0,first_assignments=len(firsts),arabic_resources=sum(r[k]['language'].startswith('AR') for k in keys)))
    require(observed==plan['master_order'],'Master queue does not follow actual first-use step order')
    # Re-render in isolation to catch stale README/library/book pages without modifying the checkout.
    with tempfile.TemporaryDirectory() as temp:
        dst=Path(temp);(dst/'docs').mkdir()
        for f in ['curriculum.json','docs/RESOURCE_CATALOG.json','docs/reading_plan.json','docs/CHAPTER_MAP.md','docs/iti_topics.json']:(dst/f).write_bytes((ROOT/f).read_bytes())
        for m in mods:(dst/m['path']).parent.mkdir(parents=True,exist_ok=True)
        saved=render_learning.ROOT
        try:
            render_learning.ROOT=dst;render_learning.render()
            for f in dst.rglob('*.md'):require(f.read_bytes()==(ROOT/f.relative_to(dst)).read_bytes(),'Generated content stale: '+str(f.relative_to(dst)))
        finally:render_learning.ROOT=saved
    for path in ROOT.rglob('*.md'):
        s=re.sub(r'```.*?```','',path.read_text(),flags=re.S)
        for u in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',s):
            v=urlsplit(u)
            if v.scheme:continue
            dest=(path.parent/unquote(v.path)).resolve() if v.path else path
            if dest.is_dir():dest=dest/'README.md'
            if not dest.exists():errors.append(f'{path.relative_to(ROOT)}: missing {u}');continue
            if v.fragment and dest.suffix=='.md' and unquote(v.fragment) not in anchors(dest.read_text()):errors.append(f'{path.relative_to(ROOT)}: missing fragment {u}')
            links+=1
    return dict(levels=rows,local_links_including_fragments=links,unique_resources=len(r),book_assignments=len(books),preserved_exercises=sum(len(m['exercises']) for m in mods),errors=errors)
if __name__=='__main__':
    result=audit();print(json.dumps(result,indent=2));sys.exit(bool(result['errors']))
