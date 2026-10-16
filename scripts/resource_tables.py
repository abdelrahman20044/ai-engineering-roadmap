#!/usr/bin/env python3
"""Render topic-scoped resource choices; keep full research in expandable notes."""
import re

def table(headers,rows):
    def cell(value):return str(value).replace('|','&#124;').replace('\n',' ')
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in rows)

def label_type(value):
    return value.replace('Single video (lesson within playlist)','Single Video (part of playlist)').replace('YouTube playlist','Playlist (YouTube)').replace('Full video course','Full Course').replace('Paid full video course','Full Course (paid)').replace('Short video course','Short Course').replace('Single course video','Single Video (course lesson)').replace('Single video','Single Video').replace('Single lecture video','Single Video').replace('Official documentation / tutorial','Documentation / tutorial')

def resource_library(mod,data,resources,groups,books):
    id=mod['id'];folder_prefix='../docs/';seen_books=set()
    def blink(k):return f'[{k} · {books[k]["book"]}{books[k]["chapter"]}](../docs/READING_GUIDE.md#{k.lower()})'
    def short(text,limit=88):
        if len(text)<=limit:return text
        return text[:limit-1].rsplit(' ',1)[0]+'…'
    s=f'# Resource Library · {id} — {mod["title"]}\n\n[← Guided learning path](README.md) · [Technical details](details.md) · [Master book order](../docs/READING_GUIDE.md) · [Chapter map](../docs/CHAPTER_MAP.md)\n\n'
    s+='**Use the topic groups below, in README step order.** Roles apply inside a group, not across the entire Level. A routing lesson and a testing lesson are not substitutes. You do **not** need to complete every listed resource.\n\n'
    s+='## How to choose\n\n- **Primary:** the default source for this group, after its assigned book slice.\n- **Alternative:** replaces only the explicitly stated overlapping explanation. The group’s remaining requirements still apply.\n- **Complementary:** a different concept, implementation step or practice. Only items named in **Required sequence** are required; other complements are as-needed support.\n- **Reference:** consult the named API/example while implementing; do not finish a documentation site.\n- **Optional Advanced:** extra depth or an optional paid route; it does not block the gate.\n\nFormat is independent of role. **Single Video (part of playlist)** assigns that video, not its playlist. Course/playlist selections below are bounded; unverified lesson identifiers/timestamps are disclosed. Provider, language and access details are retained in the notes.\n\n'
    if data['arabic_note']:s+='**Arabic availability:** '+data['arabic_note']+'\n\n'
    s+='## Topic navigation\n\n'+''.join(f'{g["step"]}. [{g["title"]}](#{g["id"]})\n' for g in groups)+'\n'
    for g in groups:
        anchor=g['id'];primary=g['primary_book'] or g['primary_resource'];primary_link=blink(primary) if g['primary_book'] else f'`{primary}`'
        s+=f'<a id="{anchor}"></a>\n\n## {g["step"]}. {g["title"]}\n\n[Return to README Step {g["step"]}](README.md#'+f'{g["step"]}-{re.sub(r"[^\w\- ]","",g["title"].lower()).replace(" ","-")}'+')\n\n'
        s+='**Topic/subtopics:** '+g['scope']+'.\n\n'
        new=[k for k in g['reading_ids'] if books[k]['first_level']==id and books[k]['action'] not in ['Previously Covered / Review Only'] and k not in seen_books]
        review=[k for k in g['reading_ids'] if k not in new]
        comp=[r for r in g['resources'] if r['required']]
        sequence=[]
        if new:sequence.append('the assigned book slice'+('s ' if len(new)>1 else ' ')+', '.join(blink(k) for k in new))
        if not g['primary_book']:sequence.append(primary_link)
        elif g['primary_book'] not in new:sequence.append('review only '+primary_link+' for this task')
        sequence.extend('`'+r['resource_id']+'` (a different required capability)' for r in comp)
        s+=('**Required sequence (default route):** ' if g['choice'] else '**Required sequence:** ')+' **THEN** '.join(sequence or ['apply the previously covered concepts to this step’s task'])+'. Stop each source at the stated portion.\n\n'
        if g['choice']:
            ch=g['choice'];s+='**Choose ONE explanation for '+ch['scope']+':** default '+primary_link+' **OR** `'+ch['alternative']+'`. '+ch['keep']+' This choice is not permission to skip the group’s other subtopics, assigned books or required complements.\n\n'
        else:s+='**Study decision:** follow the required sequence above. No full-route substitute is claimed here; the other teaching sources cover additional or partially overlapping material.\n\n'
        refs=[r['resource_id'] for r in g['resources'] if r['role']=='Reference']
        if refs:s+='**While implementing:** consult '+', '.join('`'+k+'`' for k in refs)+'. These are lookups, not more courses.\n\n'
        s+='**As needed:** other Complementary sources add only their stated scope; Optional Advanced entries can wait. Do not watch every row. The [README task and completion check](README.md#'+f'{g["step"]}-{re.sub(r"[^\w\- ]","",g["title"].lower()).replace(" ","-")}'+') are the same whichever bounded explanation you choose.\n\n'
        rows=[];notes=[]
        for k in g['reading_ids']:
            b=books[k];status=b['action'] if k in new else 'Previously Covered / Review Only'
            role='Primary' if g['primary_book']==k else ('Optional Advanced' if status=='Optional Advanced' else 'Complementary' if k in new else 'Reference')
            authors={'G':'Andrea De Mauro','F':'Alireza Parandeh','C':'Chip Huyen'}
            rows.append([blink(k)+'<br>'+authors[b['book']]+' · EN','Book Section',role,short(g['title'],55),f'[{status}: exact assigned slice](../docs/READING_GUIDE.md#{k.lower()})'])
        seen_books.update(g['reading_ids'])
        for row in g['resources']:
            k=row['resource_id'];r=resources[k];bounds=f'{anchor}-{k}';portion=row['portion']
            if k.startswith('ar-mini-'):selection='The linked video only; not its playlist.'
            elif 'not verified' in portion.lower():selection='Topic bounds; lesson IDs not verified — '+f'[details](#{bounds})'
            elif len(portion)<=96:selection=portion
            else:selection=short(portion,76)+' '+f'[bounds](#{bounds})'
            name=f'`{k}` · [{r["title"]}]({r["url"]})<br>{r["provider"]} · {r["language"]}'
            focus=short(row['focus'],60)
            role=row['role']+(' (required)' if row['required'] else ' (as needed)' if row['role']=='Complementary' else '')
            rows.append([name,label_type(r['resource_type']),role,focus,selection])
            notes.append(f'<a id="{bounds}"></a>\n\n**`{k}` — selected portion:** {portion}\n\n**Relationship:** {row["relationship"]}\n')
        s+=table(['Resource · Provider · Language','Resource Type','Role in this group','Topic / subtopic','Study only'],rows)+'\n'
        s+='<details>\n<summary>Exact selection bounds and relationship notes</summary>\n\n'+'\n'.join(notes)+'\n</details>\n\n'
    s+='## Retained source metadata and access notes\n\nThese notes preserve the comprehensive catalog research. **The topic table narrows the assignment.** A source’s broad Level-wide associations below do not create another study queue. Older `r-…` resource links remain valid here.\n\n'
    for k,old in data['resource_guidance'].items():
        v=resources[k];s+=f'<a id="r-{k}"></a>\n\n<details>\n<summary>{k} · {v["title"]} — access, scope and verification</summary>\n\n'
        s+=f'[{v["title"]}]({v["url"]}) · {v["provider"]} · {v["language"]}\n\n- **Resource Type:** {label_type(v["resource_type"])}.\n- **Access:** {v["cost"]}.\n- **Catalog scope:** {v["focus"]}\n- **Scope/version limits:** {v["limit"]}\n- **Verification boundary:** {v["selection_verification"]}\n- **Retained Level-wide topic association:** '+('; '.join(old['topics']) or 'Supplemental practice/depth')+'.\n- **Retained broad selection notes (lookup only):** '+old['assigned_portion']+'\n'
        if v.get('specific_lessons'):s+='\n**Verified direct lessons:** '+ ' · '.join(f'[{l["title"]}]({l["url"]})' for l in v['specific_lessons'])+'. Follow only the lesson for the selected concept.\n'
        s+='\n</details>\n\n'
    s+='## Practice, books and verification\n\n[Assessed exercises and completion criteria](README.md#practical-exercises) remain in the learning journey; [diagnostics and self-check answers](details.md) remain in technical details. Book rows point to the single [Master Book Reading Order](../docs/READING_GUIDE.md); [CHAPTER_MAP](../docs/CHAPTER_MAP.md) is a locator, not a second assignment list.\n\nNo new timestamps or course-lesson verification are claimed. Source outlines and the existing dated URL evidence are retained. See [resource policy](../docs/RESOURCE_POLICY.md) and [topic-group audit](../docs/RESOURCE_TABLE_AUDIT.md).\n\n[← Return to your next learning step](README.md#start-here--recommended-learning-path)\n'
    return s
