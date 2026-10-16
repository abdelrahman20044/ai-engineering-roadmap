#!/usr/bin/env python3
"""Render guided Levels and the master reading queue from retained source catalogs."""
from pathlib import Path
import json,re
from resource_tables import resource_library
ROOT=Path(__file__).resolve().parents[1]
def table(head,rows):
 def esc(s):return str(s).replace('|','&#124;').replace('\n',' ')
 return '| '+' | '.join(head)+' |\n| '+' | '.join('---' for _ in head)+' |\n'+''.join('| '+' | '.join(esc(x) for x in row)+' |\n' for row in rows)
def render():
 groups=json.loads((ROOT/'docs/RESOURCE_GROUPS.json').read_text())['levels']
 cat=json.loads((ROOT/'docs/RESOURCE_CATALOG.json').read_text());res={r['id']:r for r in cat['resources']};mods=json.loads((ROOT/'curriculum.json').read_text())['modules'];plan=json.loads((ROOT/'docs/reading_plan.json').read_text());book={b['id']:b for b in plan['assignments']};topicdata=json.loads((ROOT/'docs/iti_topics.json').read_text());topicdata=topicdata.get('topics',[]) if isinstance(topicdata,dict) else topicdata;iti={t['id']:t['title'] for t in topicdata}
 def link(k):return f'[{res[k]["title"]}]({res[k]["url"]})'
 def localres(k):return f'[resource choices](resources.md#r-{k})'
 def level_link(id):return f'[{id}](../{mods[int(id[1:])]["path"]})'
 def booklink(k,prefix='../docs/'):
  b=book[k];return f'[{k} · {b["book"]}{b["chapter"]}]({prefix}READING_GUIDE.md#{k.lower()})'
 for n,m in enumerate(mods):
  data=cat['level_maps'][str(n)];topics=sorted(data['topics'],key=lambda x:x['step_position']);directory=(ROOT/m['path']).parent;first=topics[0];nav='[← Roadmap](../README.md) · [Full resource library](resources.md) · [Technical details](details.md) · [Book order](../docs/READING_GUIDE.md) · [Progress](../progress/PROGRESS.md)'
  s=f'# {m["id"]} · {m["title"]}\n\n{nav}\n\n**Tier {m["tier"]} · {m["hours"][0]}–{m["hours"][1]} focused hours · Difficulty {m["difficulty"]}/5 · {m["priority"]}'+(' · Optional Level' if m['optional'] else '')+'**\n\n'
  s+='**You will learn:** '+' '.join(m['outcomes'])+'\n\n**Before starting:** '+(', '.join(level_link(x) for x in m['prerequisites']) or 'Use your existing backend, Python and SQL experience.')+' Pass the [quick diagnostic](details.md#prerequisites-and-quick-diagnostic); review only demonstrated gaps.\n\n'
  s+='## Start Here / Recommended Learning Path\n\n'
  firstbook=next((k for k in first['reading_ids'] if book[k]['first_level']==m['id'] and book[k]['action'] in ['Read Now','Skim','Optional Advanced']),None)
  s+='> **Next action:** '+('Open '+booklink(firstbook)+' for the assigned portion below, then ' if firstbook else '')+f'follow Step 1’s **Primary** resource and do its task. Other resources are choices, not a completion list.\n\n'
  s+='Follow these steps in order. Read each new book assignment once; later mentions explicitly say **Previously Covered / Review Only**. [Master book order](../docs/READING_GUIDE.md) is the authoritative schedule; [chapter mapping](../docs/CHAPTER_MAP.md) is the lookup index.\n\n'
  seen=set()
  for pos,t in enumerate(topics,1):
   s+=f'### {pos}. {t["name"]}\n\n**Learn:** {t["subtopics"]}.\n\n'
   s+=f'**Choose resources:** [Unit {pos:02} — topic table and study choices](resources.md#unit-{pos:02}).\n\n'
   if t['reading_ids']:
    items=[]
    for key in t['reading_ids']:
     b=book[key];isnew=b['first_level']==m['id'] and key not in seen and b['action'] not in ['Previously Covered / Review Only'];status=b['action'] if isnew else 'Previously Covered / Review Only'
     desc=b['portion'] if isnew else 'Reuse only the part needed for this step; do not restart the chapter.'
     items.append(f'{booklink(key)} — **{status}**. {desc}')
     seen.add(key)
    s+='**Required reading:**\n\n'+''.join('- '+x+'\n' for x in items)+'\n'
   else:s+='**Required book reading:** None for this step. The focused tutorial fills a gap not taught by the three books.\n\n'
   k=t['primary_resource']
   if t.get('primary_book'):s+='**Primary · Book section:** '+booklink(t['primary_book'])+'. Follow the assigned portion above; use the library references during implementation.\n\n'
   else:s+=f'**Primary · {t["primary_type"]}:** [{res[k]["title"]}]({t["primary_url"]}). {t["primary_portion"]}\n\n'
   s+='**Practice:** '+t['task']+'\n\n**Completion check:** '+t['completion_check']+'\n\n'
  s+='## Practical exercises\n\nThe step tasks feed the assessed exercises below; combine them in the same application rather than creating extra projects.\n\n'
  for i,(task,check) in enumerate(zip(m['exercises'],m['exercise_checks']),1):s+=f'- [ ] **{m["id"]}-E{i}:** {task}\n  - **Pass:** {check}\n'
  s+='\n## Ready to move on?\n\n'+''.join('- [ ] '+x+'\n' for x in ['Every numbered step has its stated output and completion check.','All assessed exercise criteria pass, including failures/permissions where relevant.','You can answer the [self-check](details.md#self-check) and explain one decision without generated code.','Evidence links include reproducible commands/configuration and remaining limitations.'])
  s+='\n**Capstone checkpoint:** '+f'[{m["milestone"]}](../project/milestones/{m["milestone"].lower()}.md). '+m['gate']+'\n\n**Keep:** '+'; '.join(m['evidence'])+'.\n\n'
  s+='## What to defer\n\n'+''.join('- '+x+'\n' for x in m['defer'])
  s+='\n## Record progress and choose the next Level\n\n```bash\n'+f'python scripts/progress.py set {m["id"]} completed --evidence "link-to-commit-and-test-report"\n'+'```\n\n'
  unlock=[x['id'] for x in mods if m['id'] in x['prerequisites']];s+='**Unlocks:** '+(', '.join(level_link(x) for x in unlock) or 'No further required Level; return to the capstone or role checklist.')+'\n\n'+nav+'\n';(directory/'README.md').write_text(s)
  # Details carry diagnostics/provenance and reasoning aids, not a second study schedule.
  d=f'# Technical Details · {m["id"]}\n\n[← Guided learning path](README.md) · [Resource library](resources.md) · [ITI coverage](../docs/ITI_COVERAGE.md)\n\nUse this page when checking readiness, diagnosing a mistake or reviewing curriculum provenance. The ordered learning instructions and book assignments live in the Level README and master book order.\n\n## Prerequisites and quick diagnostic\n\n'
  for name,check in data['diagnostic']:d+=f'- **{name}:** {check}\n'
  d+='\nUse existing CRM evidence where applicable. A gap triggers targeted review, not a beginner-course restart.\n\n## Complete technical scope\n\n'
  for t in topics:d+=f'- **{t["name"]}:** {t["subtopics"]}.\n'
  d+='\n## Common mistakes and debugging\n\n'
  for name,fix in data['pitfalls']:d+=f'### {name}\n\n{fix}\n\n'
  d+='## Self-check\n\nThese are original reasoning prompts, not confirmed ITI questions.\n\n'
  for i,(q,a) in enumerate(data['questions'],1):d+=f'{i}. {q}\n'
  d+='\n<details>\n<summary>Answer guide</summary>\n\n'
  for q,a in data['questions']:d+=f'**{q}**\n\n{a}\n\n'
  d+='</details>\n\n## ITI provenance and industry extensions\n\n'
  for id in m['syllabus']:d+=f'- **{id}:** {iti[id]} — official published module title.\n'
  d+='\nDetailed subtopics, specific tools, labs, prerequisites, learning hours and selected resources are roadmap recommendations, not an official ITI reading list. The [coverage matrix](../docs/ITI_COVERAGE.md) remains the syllabus record.\n\n## Learning objectives and evidence\n\n'
  for t in topics:d+=f'- [ ] {t["task"]}\n'
  d+='\nThe assessed exercise criteria are in [the guided page](README.md#practical-exercises). For evidence use [EVIDENCE](../templates/EVIDENCE.md) and [EXPERIMENT](../templates/EXPERIMENT.md).\n';(directory/'details.md').write_text(d)
  (directory/'resources.md').write_text(resource_library(m,data,res,groups[str(n)],book))
 # The master order is generated from the same IDs shown by every step.
 order=plan['master_order'];guide='# Master Book Reading Order\n\n[Roadmap](../README.md) · [Chapter-to-Level map](CHAPTER_MAP.md) · [Progress](../progress/PROGRESS.md)\n\n**Use this page to decide what to read next.** Follow the numbered queue below with the Level you are working on. Use the chapter map only to find a section or understand a split. An assignment has one first-reading Level; later appearances are review, not new homework.\n\n## Reading status\n\n- **Read Now:** first purposeful reading when you reach the stated Level.\n- **Read Later:** any assignment whose Level/prerequisites you have not reached. Do not front-load it.\n- **Skim:** read the named ideas selectively; skip familiar setup/theory.\n- **Previously Covered / Review Only:** look up a specific uncertainty or apply an earlier section; no restart.\n- **Optional Advanced:** outside the core completion path.\n\nG = Andrea De Mauro, *Grokking AI Applications*; F = Alireza Parandeh, *Building Generative AI Services with FastAPI*; C = Chip Huyen, *AI Engineering*. **G/C page numbers are printed pages; F numbers are PDF viewer positions starting at 1.** The supplied PDFs remain the verified source; the files are not redistributed.\n\n## How the original sequence changed\n\nThe baseline was G1–4 → F2–5 → G5–6 → F6–7 → C3–4 → F8–12 → C5–6/C10. The selected chapters remain represented, with these practical changes:\n\n1. G1 remains early. Selected C1 planning and C4 evaluation-pipeline orientation move to L00 so the project starts with a scope and evidence contract. Neither entire Chip chapter is a prerequisite to coding.\n2. F2/F4 and the pytest slice of F11 move before G2–4 are finished: existing Express experience transfers directly into a small Python API. F3/F5 are split by implementation need rather than read as one block.\n3. C3/C4 evaluation comes before retrieval improvements and agents. G4 and C6 retrieval are read when document search is built, not during a long introductory reading phase.\n4. F7 persistence precedes F6 streaming because ownership, documents and conversation state support RAG. F5 concurrency is expanded when jobs/streaming make it necessary.\n5. Context Engineering and memory precede G5/G6 agent implementation. G5/G6 then follow a working, evaluated RAG service. Fine-tuning and the rest of inference optimization stay optional.\n6. F8/F9 security is applied before tool autonomy; F12 deployment and F10 optimization follow measured behavior. C5/C6/C10 sections are introduced once at their practical decision point and reviewed later only as needed.\n\n## Chronological queue\n\nThe queue is a sensible default traversal of the prerequisite graph, not a weekly schedule. You can take unlocked branches in a different order; keep the same first-reading/review rules. **Only the first new book use in a Level is a reading task; repeated step references mean reuse.**\n\n'
 number=0
 for n,m in enumerate(mods):
  guide+=f'<a id="{m["id"].lower()}"></a>\n\n### {m["id"]} · {m["title"]}\n\n[Open this Level](../{m["path"]}). Before reaching it, its new reading is **Read Later**.\n\n'
  for key in order:
   b=book[key]
   if b['first_level']!=m['id']:continue
   number+=1;guide+=f'<a id="{key.lower()}"></a>\n\n{number}. **{key} · {b["book"]}{b["chapter"]} — {b["title"]} · {b["action"]}**\n\n   {b["portion"]}\n\n   **Purpose:** {b["why"]}\n\n'
  reviews=plan['review_by_level'][m['id']]
  if reviews:guide+='**Previously Covered / Review Only:** '+', '.join(f'[{key}](#{key.lower()})' for key in reviews)+'. Consult only for the current implementation/failure; do not read those chapters again.\n\n'
  if n==9:guide+='**Assigned article:** Anthropic’s [Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents). Read selection/rot/JIT retrieval before budgets, memory/compaction before long-history experiments, and sub-agents only as a decision boundary. L12 reviews the relevant sections.\n\n'
 guide+='## Books you do not need to finish\n\n- **G7:** KNIME/data-ecosystem setup is optional background; it is not a Data Engineering specialization or a core prerequisite.\n- **G8:** deployment/orchestration overview is optional at L13/L14; F12 and current MCP docs are the primary implementation references.\n- **F1:** optional orientation. F3 other modalities, F5 advanced serving and F6 WebSocket implementation remain deferred unless the product needs them.\n- **C1 history, C3 entropy derivations and C7–9 advanced training/serving:** selective or Optional Advanced. Finish the application evidence before expanding them.\n\nThe machine-readable source is `reading_plan.json`. Run `python scripts/audit_level_content.py` after changing assignments; it checks first owners, step IDs and generated-document consistency.\n';(ROOT/'docs/READING_GUIDE.md').write_text(guide)
 # Preserve all verified chapter locators, replacing the old competing reading schedule with associations.
 old=(ROOT/'docs/CHAPTER_MAP.md').read_text();rows=[]
 for line in old.splitlines():
  cells=[x.strip() for x in line.split('|')]
  if len(cells)>4 and re.fullmatch('[GFC]\\d+',cells[1]):rows.append((cells[1],cells[2],cells[3]))
 if cat.get('verified_chapter_locators'):rows=[tuple(x) for x in cat['verified_chapter_locators']]
 else:cat['verified_chapter_locators']=rows
 mapping='# Chapter-to-Level Map\n\n[Master reading order](READING_GUIDE.md) · [Roadmap](../README.md)\n\n**This is a reference index, not a second reading schedule.** Follow the master order or the current Level README to decide Read Now versus Read Later. The chapter locations below preserve the supplied-PDF research. Full chapter spans locate content; they do not assign every page.\n\n'
 maprows=[]
 for code,location,focus in rows:
  bs=[b for b in book.values() if b['book']+str(b['chapter'])==code];ids=', '.join(f'[{b["id"]}](READING_GUIDE.md#{b["id"].lower()})' for b in bs) or 'Optional background; no required first reading';owners=', '.join(dict.fromkeys(b['first_level'] for b in bs if b['action'] not in ['Previously Covered / Review Only'])) or 'Optional / review only'
  maprows.append([code,location,ids,owners])
 mapping+=table(['Chapter','Verified chapter locator','Exact assigned slices / statuses','First-reading Levels'],maprows)
 mapping+='\n## Why chapters are split\n\n- **F3:** model/serving orientation in B09; external API integration in B12. Other modalities remain optional.\n- **F5:** provider-call example B13; preparation B21; RAG generation B25; concurrency/jobs B31; advanced inference is optional B47. Verified examples corrected the earlier broad provider/RAG page descriptions.\n- **F11:** pytest B06 (PDF501–518); model/behavioral testing B17 (495–500, 523–528); retrieval integration B26 (519–522); E2E B38 (529–534). Later agent/release work reuses these skills.\n- **C4:** pipeline preview B03, task criteria B16, model selection B40. The preview is applied in L05, not reintroduced as a whole new chapter.\n- **C5:** prompt/context basics B14, defense B35. L09 context-budget reading is explicit review B30.\n- **C6:** retrieval foundations B20, improvements B27, memory B28, agents B36b. One chapter supports different project capabilities without a mandatory full reread.\n- **C8/C9:** bounded quality/processing/metrics slices enter the core; optional training/serving sections wait for L17.\n- **C10:** context B29, guardrails B35a, orchestration B37, observability B39a, feedback B43. The old pp.465–473 assignment is split to avoid reassigning orchestration at L14.\n\n## Retained topic associations\n\nThe original topic-to-book research is retained in each topic’s `book` field in `RESOURCE_CATALOG.json` and the manifest’s `reading_topic_notes`. These fields explain conceptual overlap; they do **not** introduce new assignments. The reading ledger is authoritative.\n';(ROOT/'docs/CHAPTER_MAP.md').write_text(mapping)
 (ROOT/'docs/RESOURCE_CATALOG.json').write_text(json.dumps(cat,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':render();print('Rendered 19 guided READMEs, 19 libraries, 19 detail pages and both book guides.')
