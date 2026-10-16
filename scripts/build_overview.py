#!/usr/bin/env python3
"""Build the optional standalone English HTML reader (requires Pandoc on PATH)."""
import base64
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]

def doc_anchor(path):
    return 'doc-'+re.sub(r'[^a-z0-9]+','-',path.lower()).strip('-')

def check_html(path):
    class Check(HTMLParser):
        def __init__(self):
            super().__init__();self.ids=set();self.links=[];self.assets=[];self.duplicates=[]
        def handle_starttag(self, tag, attrs):
            a=dict(attrs)
            if 'id' in a:
                if a['id'] in self.ids:self.duplicates.append(a['id'])
                self.ids.add(a['id'])
            if tag=='a':self.links.append(a.get('href',''))
            if tag in {'script','img','link'}:
                self.assets.append(a.get('src',a.get('href','')))
    c=Check();c.feed(Path(path).read_text(encoding='utf-8'))
    missing=[x for x in c.links if x.startswith('#') and unquote(x[1:]) not in c.ids]
    external_assets=[x for x in c.assets if x and not x.startswith('data:')]
    if missing or external_assets or c.duplicates:
        raise ValueError(f'HTML has unresolved anchors/assets: {missing} {external_assets}; duplicate IDs: {c.duplicates}')
    return len(c.links)

def main():
    if not shutil.which('pandoc'):
        raise SystemExit('Optional rebuild requires Pandoc. Existing OVERVIEW.html needs no installation.')
    modules=json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'))['modules']
    files=['README.md','START_HERE.md','docs/ROADMAP.md','docs/ITI_COVERAGE.md',
           'docs/READING_GUIDE.md','docs/CHAPTER_MAP.md','project/README.md','project/ARCHITECTURE.md']
    files += [name for m in modules for name in [m['path'], str(Path(m['path']).parent/'resources.md'),str(Path(m['path']).parent/'details.md')]]
    files += [f'project/milestones/s{i}.md' for i in range(8)]
    files += ['docs/EVALUATION.md','docs/CONTEXT_ENGINEERING.md','docs/SECURITY.md',
              'docs/PACING.md','progress/README.md','progress/PROGRESS.md','docs/REPOSITORY_GUIDE.md','docs/CAREER.md','docs/LEARNING_WITH_AI.md','docs/SOURCES.md','docs/RESOURCE_POLICY.md','docs/RESOURCE_AUDIT.md','docs/REFERENCE_COMPARISON.md','docs/LEARNING_EXPERIENCE_AUDIT.md','CHANGELOG.md']
    included={Path(f).as_posix():doc_anchor(f)for f in files}
    svg=base64.b64encode((ROOT/'assets/roadmap.svg').read_bytes()).decode('ascii')
    image_seen=False
    sections=[]
    for name in files:
        path=ROOT/name
        text=path.read_text(encoding='utf-8')
        prefix=included[name]
        text=re.sub(r'(<[^>]+\bid=["\'])([^"\']+)',lambda m:m[1]+prefix+'-'+m[2],text)
        seen={}
        def heading(match):
            marks,title=match.groups()
            plain=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',title)
            slug=re.sub(r'[^\w\- ]','',re.sub('<[^>]+>','',plain).lower()).replace(' ','-')
            n=seen.get(slug,0);seen[slug]=n+1
            return f'{marks} {title} {{#{prefix}-{slug}'+(f'-{n}' if n else '')+'}'
        text=re.sub(r'^(#{1,6}) (.+)$',heading,text,flags=re.M)
        def link(match):
            nonlocal image_seen
            marker,label,url=match.groups()
            parsed=urlsplit(url)
            if parsed.scheme:
                return match.group(0)
            destination=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            if destination.is_dir():destination=destination/'README.md'
            relative=destination.relative_to(ROOT).as_posix()
            if marker:
                if relative=='assets/roadmap.svg':
                    if image_seen:return '[Visual roadmap](#visual-roadmap)'
                    image_seen=True
                    return f'<span id="visual-roadmap"></span>\n\n![{label}](data:image/svg+xml;base64,{svg})'
                return match.group(0)
            anchor=included.get(relative,'repository-files')
            if parsed.fragment and relative in included:
                anchor += '-'+unquote(parsed.fragment)
            return f'[{label}](#{anchor})'
        text=re.sub(r'(!?)\[([^\]]*)\]\(([^)]+)\)',link,text)
        text=re.sub(r'```mermaid\n.*?```','> Exact Mermaid diagrams are available in the repository Markdown; prerequisite tables remain readable here.',text,flags=re.S)
        text=re.sub(r'^(#{1,5}) ',r'\1# ',text,flags=re.M)
        sections.append(f'<span id="{included[name]}"></span>\n\n{text}')
    listing='\n'.join('- `'+str(p.relative_to(ROOT))+'`' for p in sorted(ROOT.rglob('*')) if p.is_file() and '__pycache__'not in p.parts)
    sections.append('<span id="repository-files"></span>\n\n## Repository files {#repository-file-list}\n\nThis standalone reader contains the curriculum. Editable CSV, JSON, templates, and scripts are included in the ZIP.\n\n'+listing)
    metadata='---\ntitle: AI Engineering Learning Roadmap\nlang: en\ndir: ltr\ndate: 16 October 2026\n---\n\n'
    css=(ROOT/'assets/overview.css').read_text(encoding='utf-8')
    with tempfile.TemporaryDirectory()as folder:
        md=Path(folder)/'overview.md';header=Path(folder)/'header.html'
        md.write_text(metadata+'\n\n'.join(sections),encoding='utf-8')
        header.write_text('<style>'+css+'</style>',encoding='utf-8')
        subprocess.run(['pandoc',str(md),'--standalone','--toc','--toc-depth=2',
                        '--metadata','toc-title=Repository contents','--include-in-header='+str(header),
                        '-o',str(ROOT/'OVERVIEW.html')],check=True)
    print(f'Built standalone OVERVIEW.html; {check_html(ROOT/"OVERVIEW.html")} links checked.')

if __name__=='__main__':main()
