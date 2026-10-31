#!/usr/bin/env python3
"""Bounded structural checks for registered libraries; not a runtime release gate."""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from lxml import etree, html
from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/libraries'))
from manage import library_root
from library_report import emit


class Invalid(ValueError):
    def __init__(self, code, detail):
        self.code, self.detail = code, str(detail)
        super().__init__(self.detail)


def strict(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise Invalid('DUPLICATE_JSON_KEY', key)
            result[key] = value
        return result
    def nonfinite(value):
        raise Invalid('NONFINITE_JSON', value)
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs, parse_constant=nonfinite)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Inspector:
    def __init__(self, root, repo=ROOT):
        self.root, self.repo = Path(root).resolve(), Path(repo).resolve()
        self.errors, self.checks, self.components = [], [], {}
        schemas = ROOT / 'tools/libraries/schemas'
        self.component_schema = Draft7Validator(strict(schemas / 'component.schema.json'))
        self.index_schema = Draft7Validator(strict(schemas / 'library.schema.json'))
        self.cem_schema = Draft7Validator(strict(self.repo / 'tools/validation/schemas/cem.schema.json'))
        self.parser = etree.XMLParser(resolve_entities=False, no_network=True)
        self.scxml_schema = etree.XMLSchema(etree.parse(str(self.repo / 'tools/validation/schemas/scxml/scxml.xsd'), self.parser))

    def problem(self, code, path, detail):
        self.errors.append({'code': code, 'severity': 'blocked' if code.endswith('_UNSUPPORTED') else 'fail', 'file': str(path), 'detail': str(detail)})

    def safe(self, base, ref, suffix=None):
        if not isinstance(ref, str) or not ref or Path(ref).is_absolute() or '://' in ref:
            raise Invalid('REFERENCE_INVALID', ref)
        raw = Path(base) / ref
        path = raw.resolve()
        if not path.is_relative_to(self.root):
            raise Invalid('REFERENCE_ESCAPES_LIBRARY', ref)
        if any(p.is_symlink() for p in [raw, *raw.parents] if p.is_relative_to(self.root)):
            raise Invalid('REFERENCE_SYMLINK', ref)
        if not path.is_file():
            raise Invalid('REFERENCE_MISSING', ref)
        if suffix and path.suffix.lower() != suffix:
            raise Invalid('REFERENCE_KIND_MISMATCH', ref)
        self.checks.append({'kind': 'reference', 'file': str(path), 'sha256': digest(path)})
        return path

    @staticmethod
    def schema(validator, value):
        errors = sorted(validator.iter_errors(value), key=lambda e: str(list(e.path)))
        if errors:
            raise Invalid('OWN_SCHEMA_INVALID', '; '.join(e.message for e in errors))

    def tokens(self, path):
        data = strict(path)
        if not isinstance(data, dict):
            raise Invalid('TOKEN_ROOT_INVALID', path)
        tokens = {}
        def collect(node, parts=(), inherited=None):
            if not isinstance(node, dict):
                return
            typ = node.get('$type', inherited)
            if '$value' in node:
                tokens['.'.join(parts)] = (node['$value'], typ)
            for key, value in node.items():
                if not key.startswith('$'):
                    collect(value, (*parts, key), typ)
        collect(data)
        def nested(value, seen):
            # Alias closure only: composite member types are not inferred here.
            if isinstance(value, str) and re.fullmatch(r'\{[^{}]+\}', value):
                resolve(value[1:-1], seen)
            elif isinstance(value, dict):
                for child in value.values():
                    nested(child, seen)
            elif isinstance(value, list):
                for child in value:
                    nested(child, seen)

        def resolve(name, seen):
            if name in seen:
                raise Invalid('TOKEN_ALIAS_CYCLE', name)
            if name not in tokens:
                raise Invalid('TOKEN_ALIAS_MISSING', name)
            value, typ = tokens[name]
            if isinstance(value, str) and re.fullmatch(r'\{[^{}]+\}', value):
                target = value[1:-1]
                _, target_type = resolve(target, seen | {name})
                if typ and target_type and typ != target_type:
                    raise Invalid('TOKEN_ALIAS_TYPE_MISMATCH', name + ' -> ' + target)
                return value, target_type or typ
            nested(value, seen | {name})
            return value, typ
        for name in tokens:
            resolve(name, set())
        self.checks.append({'kind': 'token-alias-closure', 'file': str(path), 'tokens': len(tokens)})

    def component(self, path):
        component = strict(path)
        self.schema(self.component_schema, component)
        domains = component['domains']
        interface = self.safe(path.parent, domains['interface'], '.json')
        behavior = self.safe(path.parent, domains['behavior'], '.scxml')
        tokens = self.safe(path.parent, domains['visual']['tokens'], '.json')
        self.safe(path.parent, domains['visual']['css'], '.css')
        a11y = domains['accessibility']
        a11y = {'html': a11y} if isinstance(a11y, str) else a11y
        markup = self.safe(path.parent, a11y['html'], '.html')
        if 'rules' in a11y:
            rules = strict(self.safe(path.parent, a11y['rules'], '.json'))
            if not isinstance(rules, dict):
                raise Invalid('A11Y_RULES_INVALID', path)
        self.tokens(tokens)
        cem = strict(interface)
        if cem.get('schemaVersion') != '2.1.0':
            raise Invalid('CEM_VERSION_UNSUPPORTED', cem.get('schemaVersion'))
        errors = list(self.cem_schema.iter_errors(cem))
        if errors:
            raise Invalid('CEM_ORIGINAL_INVALID', '; '.join(e.message for e in errors))
        parts = set()
        declarations = []
        for module in cem['modules']:
            names = []
            for decl in module.get('declarations', []):
                name = decl.get('name')
                if name in names:
                    raise Invalid('CEM_DUPLICATE_DECLARATION', name)
                names.append(name)
                declarations.append(decl)
                for category in ['members', 'events', 'cssParts']:
                    values = [item['name'] for item in decl.get(category, [])]
                    if len(values) != len(set(values)):
                        raise Invalid('CEM_DUPLICATE_MEMBER', name + '.' + category)
                parts.update(p['name'] for p in decl.get('cssParts', []))
                for field in decl.get('members', []):
                    if field.get('type', {}).get('text') in ['boolean', 'string', 'number'] and 'default' in field:
                        try:
                            value = json.loads(field['default'])
                        except (ValueError, TypeError):
                            raise Invalid('CEM_DEFAULT_INVALID', field['name'])
                        expected = {'boolean': bool, 'string': str, 'number': (int, float)}[field['type']['text']]
                        if not isinstance(value, expected) or field['type']['text'] == 'number' and isinstance(value, bool):
                            raise Invalid('CEM_DEFAULT_TYPE_MISMATCH', field['name'])
        source = behavior.read_text()
        if '<!DOCTYPE' in source or '<!ENTITY' in source:
            raise Invalid('SCXML_DTD_UNSUPPORTED', behavior)
        machine = etree.fromstring(source.encode(), self.parser)
        if not self.scxml_schema.validate(machine):
            raise Invalid('SCXML_ORIGINAL_INVALID', str(self.scxml_schema.error_log))
        ns = {'s': 'http://www.w3.org/2005/07/scxml'}
        states = {n.get('id') for n in machine.xpath('//s:state|//s:parallel|//s:final|//s:history', namespaces=ns)}
        ids = [n.get('id') for n in machine.xpath('//*[@id]')]
        if len(ids) != len(set(ids)):
            raise Invalid('SCXML_DUPLICATE_ID', behavior)
        for node in machine.xpath('//*[@initial] | //s:transition[@target]', namespaces=ns):
            targets = node.get('target') if node.tag.endswith('transition') else node.get('initial')
            for target in targets.split():
                if target not in states:
                    raise Invalid('SCXML_TARGET_MISSING', target)
        for invoke in machine.xpath('//s:invoke[@src]', namespaces=ns):
            self.safe(behavior.parent, invoke.get('src'), '.scxml')
        # Template HTML is parsed for parts/IDs only; it is not a browser or ARIA validator.
        tree = html.fromstring(markup.read_text())
        html_ids = tree.xpath('//@id')
        if len(html_ids) != len(set(html_ids)):
            raise Invalid('HTML_DUPLICATE_ID', markup)
        if 'stories' in component:
            story_file = self.safe(path.parent, component['stories'], '.json')
            stories = strict(story_file).get('stories')
            if not isinstance(stories, list) or any(not isinstance(s, dict) or not isinstance(s.get('id'), str) or not s['id'] for s in stories):
                raise Invalid('STORIES_INVALID', story_file)
            if len({s['id'] for s in stories}) != len(stories):
                raise Invalid('STORY_DUPLICATE_ID', story_file)
        if 'ux' in component:
            ux = strict(self.safe(path.parent, component['ux'], '.json'))
            if ux.get('componentId') != component['id']:
                raise Invalid('UX_COMPONENT_ID_MISMATCH', component['id'])
        children = []
        for key, use in component.get('composition', {}).items():
            child = self.safe(path.parent, use['component'], '.json')
            target = strict(child)
            self.schema(self.component_schema, target)
            children.append(child)
            for field in ['anchorPart', 'contentPart']:
                if field in use and use[field] not in parts:
                    raise Invalid('COMPOSITION_PART_MISSING', key + '.' + use[field])
        return {'id': component['id'], 'path': path, 'children': children, 'parts': sorted(parts), 'declarations': declarations}

    def run(self, candidate=None):
        index = self.root / 'library.json'
        paths = []
        try:
            if candidate is not None:
                candidate = Path(candidate).resolve()
                paths = [candidate / 'component.json'] if candidate.is_dir() else [candidate]
            else:
                obj = strict(index)
                self.schema(self.index_schema, obj)
                paths = [self.safe(self.root, ref, '.json') for ref in obj['components'].values()]
                if len(paths) != len(set(paths)):
                    raise Invalid('COMPONENT_INDEX_DUPLICATE_PATH', index)
                if 'selection' in obj:
                    for value in obj['selection'].values():
                        self.safe(self.root, value, '.json')
            for path in paths:
                try:
                    row = self.component(path)
                    if row['id'] in self.components:
                        raise Invalid('COMPONENT_DUPLICATE_ID', row['id'])
                    self.components[row['id']] = row
                except (Invalid, OSError, ValueError, KeyError, TypeError, etree.Error) as error:
                    self.problem(getattr(error, 'code', 'COMPONENT_INVALID'), path, str(error))
            if candidate is None:
                registered = set(paths)
                for row in self.components.values():
                    for child in row['children']:
                        if child not in registered:
                            self.problem('COMPOSITION_TARGET_UNREGISTERED', row['path'], child)
                graph = {row['path']: row['children'] for row in self.components.values()}
                def visit(path, stack):
                    if path in stack:
                        raise Invalid('COMPOSITION_CYCLE', str(path))
                    for child in graph.get(path, []):
                        visit(child, stack | {path})
                for path in graph:
                    visit(path, set())
        except (Invalid, OSError, ValueError, KeyError, TypeError, etree.Error) as error:
            self.problem(getattr(error, 'code', 'LIBRARY_INVALID'), index, str(error))
        overall = 'FAIL' if any(e['severity'] == 'fail' for e in self.errors) else ('BLOCKED' if self.errors else 'PASS_LIMITED')
        return {'overall': overall, 'release': False,
                'scope': 'library-reference-identity-alias-and-selected-original-schema-checks',
                'root': str(self.root), 'componentCount': len(self.components), 'errors': self.errors,
                'checks': self.checks, 'notChecked': ['Arbitrary TypeScript type semantics', 'SCXML guards/actions and runtime equivalence',
                    'CSS-to-token variable mapping and visual rendering', 'Composite token member types, JSON Pointer references and full DTCG conformance',
                    'Accessibility conformance', 'Production release']}


def inspect(root, repo=ROOT, candidate=None):
    return Inspector(root, repo).run(candidate)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, default=ROOT)
    p.add_argument('--library', required=True)
    p.add_argument('--output', type=Path)
    p.add_argument('--details', action='store_true')
    args = p.parse_args()
    try:
        result = inspect(library_root(args.repo, args.library), args.repo)
    except (ValueError, OSError, etree.Error) as error:
        result = {'overall': 'BLOCKED', 'release': False, 'diagnostic': str(error)}
    try:
        emit(result, args.repo, args.output, args.details)
    except (ValueError, OSError) as error:
        p.error(str(error))
    return {'PASS_LIMITED': 0, 'FAIL': 1, 'BLOCKED': 2}[result['overall']]


if __name__ == '__main__':
    raise SystemExit(main())
