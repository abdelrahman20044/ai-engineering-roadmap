#!/usr/bin/env python3
"""Validate then package the learning repository without caches, secrets or books."""
import argparse
from pathlib import Path
import zipfile
from validate import validate
from build_overview import check_html

ROOT=Path(__file__).resolve().parents[1]

def package(destination):
    validate(ROOT)
    check_html(ROOT/'OVERVIEW.html')
    destination=Path(destination).resolve()
    destination.parent.mkdir(parents=True,exist_ok=True)
    files=[]
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or path.resolve()==destination:
            continue
        relative=path.relative_to(ROOT)
        if any(part in {'.git','.venv','__pycache__'} for part in relative.parts):
            continue
        if path.suffix.lower()in {'.pyc','.pyo','.pdf','.zip'} or path.name.startswith('.env'):
            continue
        files.append(path)
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED)as archive:
        for path in files:
            archive.write(path,arcname='ai-engineering-roadmap/'+path.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(destination)as archive:
        if archive.testzip()is not None:
            raise ValueError('ZIP integrity check failed')
        if len(archive.namelist())!=len(files):
            raise ValueError('ZIP file count mismatch')
    print(f'Packaged {len(files)} files: {destination}')
    return destination

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination',nargs='?',default=str(ROOT.parent/'output/ai-engineering-roadmap-english.zip'))
    package(parser.parse_args().destination)
