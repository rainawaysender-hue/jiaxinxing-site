#!/usr/bin/env python3
"""
Normalize filenames (replace spaces with '-') and copy website files into ./site
Usage: python3 scripts/normalize_and_package.py [source_dir] [target_dir]
Example: python3 scripts/normalize_and_package.py . site
"""
import sys
from pathlib import Path
import shutil
import re

def normalize_name(name: str) -> str:
    # replace spaces with '-', collapse multiple hyphens, lowercase
    s = re.sub(r"\s+", "-", name)
    s = re.sub(r"-+", "-", s)
    return s

def copy_tree(src: Path, dst: Path):
    if not dst.exists():
        dst.mkdir(parents=True)
    for p in src.iterdir():
        if p.name.startswith('.git'):
            continue
        if p.is_dir():
            copy_tree(p, dst / normalize_name(p.name))
        else:
            new_name = normalize_name(p.name)
            shutil.copy2(p, dst / new_name)

def update_html_links(site_dir: Path):
    # Replace occurrences of filenames with normalized names in HTML files
    for html in site_dir.rglob('*.html'):
        text = html.read_text(encoding='utf-8')
        for p in site_dir.rglob('*'):
            if p.is_file():
                orig = p.name
                norm = normalize_name(orig)
                if orig != norm:
                    text = text.replace(orig, norm)
        html.write_text(text, encoding='utf-8')

def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('site')
    src = src.resolve()
    dst = dst.resolve()
    print(f'Copying from {src} to {dst} with normalized filenames...')
    copy_tree(src, dst)
    print('Updating HTML links...')
    update_html_links(dst)
    print('Done. Review files in', dst)

if __name__ == '__main__':
    main()
