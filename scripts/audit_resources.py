#!/usr/bin/env python3
"""Recheck curated external URLs; writes a dated reachability report, not a quality score."""
import concurrent.futures,json,re,html,urllib.request
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def check(v):
    row={'id':v['id'],'url':v['url'],'checked_at':datetime.now(timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(v['url'],headers={'User-Agent':'Mozilla/5.0 (Roadmap resource verification)'})
        with urllib.request.urlopen(req,timeout=30) as response:
            body=response.read(1800000).decode('utf-8','replace');row.update(status=response.status,final_url=response.url)
        title=re.search(r'<title[^>]*>(.*?)</title>',body,re.I|re.S)
        row['page_title']=html.unescape(title[1].strip()) if title else ''
    except Exception as error:row.update(status='unresolved',error=str(error))
    return row
if __name__=='__main__':
    data=json.loads((ROOT/'docs/RESOURCE_CATALOG.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:rows=list(pool.map(check,data['resources']))
    result={'scope':'Reachability only; see RESOURCE_POLICY.md for scope verification and limitations.','results':rows}
    (ROOT/'docs/RESOURCE_VERIFICATION.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    failed=[r for r in rows if r['status']!=200]
    print(f'{len(rows)} checked; {len(rows)-len(failed)} HTTP 200; {len(failed)} unresolved')
    for row in failed:print(row['id'],row.get('error'))
    raise SystemExit(bool(failed))
