#!/usr/bin/env python3
"""Discover and create independent UI Contract libraries; no implicit active library."""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def library_root(repo, name, must_exist=True):
    if not isinstance(name, str) or not re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', name):
        raise ValueError('Library id must be lowercase words separated by hyphens.')
    repo = repo.resolve()
    parent = repo/'libraries'
    root = parent/name
    if parent.is_symlink() or root.is_symlink() or not root.resolve().is_relative_to(repo):
        raise ValueError('Library paths must stay inside this repository without symlink roots.')
    if must_exist and not (root/'library.json').is_file():
        raise ValueError('Library not found: '+name)
    return root


def describe(repo, name):
    root = library_root(repo, name)
    if (root/'library.json').is_symlink():
        raise ValueError('Library index must not be a symlink.')
    data = json.loads((root/'library.json').read_text())
    if not isinstance(data, dict) or not isinstance(data.get('components'), dict):
        raise ValueError('Library index requires a components object: '+name)
    # Do not open component definitions just to discover a library.
    return {'id': name, 'root': str(root.relative_to(repo.resolve())),
            'index': str((root/'library.json').relative_to(repo.resolve())),
            'name': data.get('name'), 'components': list(data['components']),
            'purpose': 'example/reference' if name == 'example' else 'user-library'}


def create(repo, name, title=None):
    root = library_root(repo, name, must_exist=False)
    root.parent.mkdir(parents=True, exist_ok=True)
    root.mkdir()  # Exclusive: never merge into or overwrite an existing library.
    try:
        index = {'kind': 'ui-contract-library-draft', 'name': title or name,
                 'version': '0.1.0', 'status': 'draft', 'components': {}, 'targets': {}}
        (root/'library.json').write_text(json.dumps(index, ensure_ascii=False, indent=2)+'\n')
        (root/'tokens.json').write_text('{}\n')
        (root/'components').mkdir()
        (root/'assets').mkdir()
    except Exception:
        shutil.rmtree(root)
        raise
    return describe(repo, name)


def manifest(repo, name):
    root = library_root(repo, name)
    describe(repo, name)
    paths = sorted(root.rglob('*'))
    if any(p.is_symlink() for p in paths):
        raise ValueError('Library manifest does not follow symlinks.')
    files = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
             for p in paths if p.is_file() and p.name != '.DS_Store' and '__pycache__' not in p.parts}
    revision = hashlib.sha256(json.dumps(files, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
    return {'root': str(root.relative_to(repo.resolve())), 'files': files, 'revision': revision}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, default=ROOT)
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    for action in ['show', 'init', 'manifest']:
        cmd = sub.add_parser(action); cmd.add_argument('library')
        if action == 'init': cmd.add_argument('--name')
        if action == 'manifest': cmd.add_argument('--output', type=Path, required=True)
    a = p.parse_args(); repo = a.repo.resolve()
    try:
        if a.command == 'list':
            data = [describe(repo, d.name) for d in sorted((repo/'libraries').glob('*')) if d.is_dir() and (d/'library.json').exists()]
        elif a.command == 'init': data = create(repo, a.library, a.name)
        elif a.command == 'show': data = describe(repo, a.library)
        else:
            data = manifest(repo, a.library)
            out = a.output.resolve()
            if out.is_relative_to(repo/'libraries') or out.is_relative_to(repo/'examples') or out.is_relative_to(repo/'docs/research'):
                raise ValueError('Manifest output must not overwrite libraries or historical evidence; use a new work/temp path.')
            out.parent.mkdir(parents=True, exist_ok=True)
            with out.open('x', encoding='utf-8') as f: f.write(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
        print(json.dumps({'overall': 'READY', 'release': False, 'data': data}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError) as e:
        print(json.dumps({'overall': 'BLOCKED', 'release': False, 'diagnostic': str(e)})); return 2

if __name__ == '__main__': raise SystemExit(main())
