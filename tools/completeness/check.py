#!/usr/bin/env python3
"""Deterministic source-backed authoring coverage; never a semantic release gate."""
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

HERE = Path(__file__).resolve().parent
PLACEHOLDER = re.compile(r'\b(TODO|TBD|FIXME|PLACEHOLDER|UNDECIDED)\b|\?\?\?', re.I)
LIMIT = 2 * 1024 * 1024


class CoverageError(ValueError):
    pass


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strict(path):
    def pairs(items):
        data = {}
        for key, value in items:
            if key in data:
                raise CoverageError('DUPLICATE_JSON_KEY: ' + key)
            data[key] = value
        return data
    def bad(value):
        raise CoverageError('NONFINITE_JSON: ' + value)
    if path.stat().st_size > LIMIT:
        raise CoverageError('SOURCE_TOO_LARGE')
    return json.loads(path.read_text(), object_pairs_hook=pairs, parse_constant=bad)


def safe(root, base, ref):
    if not isinstance(ref, str) or not ref or Path(ref).is_absolute() or '://' in ref:
        raise CoverageError('REFERENCE_INVALID')
    raw = base / ref
    target = raw.resolve()
    if not target.is_relative_to(root):
        raise CoverageError('REFERENCE_ESCAPES_LIBRARY')
    if any(p.is_symlink() for p in [raw, *raw.parents] if p.is_relative_to(root)):
        raise CoverageError('REFERENCE_SYMLINK')
    if not target.is_file():
        raise CoverageError('SOURCE_MISSING')
    if target.stat().st_size > LIMIT:
        raise CoverageError('SOURCE_TOO_LARGE')
    return target


def sources(component):
    domains = component.get('domains', {})
    if not isinstance(domains, dict):
        raise CoverageError('DOMAINS_INVALID')
    visual = domains.get('visual', {})
    access = domains.get('accessibility', {})
    if not isinstance(visual, dict) or not isinstance(access, (dict, str)):
        raise CoverageError('DOMAINS_INVALID')
    return {'interface': domains.get('interface'), 'tokens': visual.get('tokens'),
            'css': visual.get('css'), 'behavior': domains.get('behavior'),
            'html': access if isinstance(access, str) else access.get('html'),
            'ux': component.get('ux')}


def meaningful(value):
    if value is None or isinstance(value, (dict, list)) and not value:
        return False
    if isinstance(value, str):
        return bool(value.strip()) and not PLACEHOLDER.search(value)
    if isinstance(value, dict):
        return not PLACEHOLDER.search(json.dumps(value)) and any(meaningful(v) for v in value.values())
    if isinstance(value, list):
        return all(meaningful(v) for v in value)
    return True  # false and zero are explicit decisions, not missing values.


def extract(path, selector, domain):
    kind, value = selector['kind'], selector['value']
    if kind == 'json-pointer':
        if domain not in {'interface', 'tokens', 'ux'}:
            raise CoverageError('SELECTOR_DOMAIN_MISMATCH')
        data = strict(path)
        if not value.startswith('/') or re.search(r'~(?![01])', value):
            raise CoverageError('JSON_POINTER_INVALID')
        for part in value[1:].split('/'):
            part = part.replace('~1', '/').replace('~0', '~')
            if isinstance(data, list):
                if not re.fullmatch(r'0|[1-9][0-9]*', part):
                    raise CoverageError('JSON_POINTER_INVALID')
                data = data[int(part)]
            elif isinstance(data, dict):
                data = data[part]
            else:
                raise CoverageError('JSON_POINTER_NOT_FOUND')
        return data
    if kind == 'xpath':
        if domain not in {'behavior', 'html'}:
            raise CoverageError('SELECTOR_DOMAIN_MISMATCH')
        text = path.read_text()
        if '<!DOCTYPE' in text.upper() or '<!ENTITY' in text.upper():
            raise CoverageError('XML_DTD_UNSUPPORTED')
        if domain == 'behavior':
            tree = etree.fromstring(text.encode(), etree.XMLParser(resolve_entities=False, no_network=True))
            if tree.tag != '{http://www.w3.org/2005/07/scxml}scxml':
                raise CoverageError('SCXML_ROOT_INVALID')
        else:
            tree = html.fromstring(text)
        values = tree.xpath(value, namespaces={'s': 'http://www.w3.org/2005/07/scxml'})
        if not isinstance(values, list) or not values:
            raise CoverageError('LOCATOR_EMPTY')
        result = []
        for v in values:
            if isinstance(v, (etree._Comment, etree._ProcessingInstruction)):
                raise CoverageError('XPATH_NODE_UNSUPPORTED')
            if isinstance(v, etree._Element):
                # A bare empty element is not source-backed decision content.
                meaningful_attributes = {k: x for k, x in v.attrib.items() if k not in {'id', 'data-part', 'class'}}
                text_content = ''.join(v.itertext()).strip()
                if not meaningful_attributes and not text_content:
                    raise CoverageError('LOCATOR_EMPTY')
                result.append(etree.tostring(v, encoding='unicode', with_tail=False))
            elif isinstance(v, str):
                result.append(str(v))
            else:
                raise CoverageError('XPATH_SCALAR_UNSUPPORTED')
        return result
    if kind == 'lines':
        if domain != 'css':
            raise CoverageError('SELECTOR_DOMAIN_MISMATCH')
        match = re.fullmatch(r'([1-9][0-9]*):([1-9][0-9]*)', value)
        if not match:
            raise CoverageError('LINE_RANGE_INVALID')
        first, last = map(int, match.groups())
        lines = path.read_text().splitlines()
        if first > last or last > len(lines):
            raise CoverageError('LINE_RANGE_INVALID')
        selected = '\n'.join(lines[first-1:last])
        return re.sub(r'/\*.*?\*/', '', selected, flags=re.S)
    raise CoverageError('SELECTOR_UNSUPPORTED')


def check_shape(value, shape, source, selector):
    """Finite structural tests only; the meaning of a mapping still needs review."""
    def text(v):
        return isinstance(v, str) and bool(v.strip())
    ok = False
    if shape in {'cem-member', 'cem-event'}:
        ok = isinstance(value, dict) and text(value.get('name')) and isinstance(value.get('type'), dict) and text(value['type'].get('text'))
        if shape == 'cem-member':
            ok = ok and value.get('kind') == 'field'
    elif shape == 'dtcg-token':
        inherited = None
        node = strict(source)
        if selector['kind'] == 'json-pointer':
            for part in selector['value'][1:].split('/'):
                if isinstance(node, dict):
                    inherited = node.get('$type', inherited)
                    node = node.get(part.replace('~1', '/').replace('~0', '~'))
                else:
                    break
        ok = isinstance(value, dict) and '$value' in value and text(value.get('$type', inherited)) and meaningful(value['$value'])
    elif shape == 'text':
        ok = text(value)
    elif shape == 'css-rule':
        ok = text(value) and bool(re.search(r'[^{}]+\{[^{}]*[\w-]+\s*:[^{}]+\}', value))
    elif shape == 'state-reference':
        tree = etree.fromstring(source.read_bytes(), etree.XMLParser(resolve_entities=False, no_network=True))
        states = set(tree.xpath('//s:state/@id|//s:parallel/@id|//s:final/@id', namespaces={'s':'http://www.w3.org/2005/07/scxml'}))
        ok = isinstance(value, list) and bool(value) and all(text(v) and set(v.split()).issubset(states) for v in value)
    elif shape == 'event-transition':
        ok = isinstance(value, list) and bool(value)
        for v in value if isinstance(value, list) else []:
            if not isinstance(v, str) or not v.lstrip().startswith('<'):
                ok = False
                continue
            element = etree.fromstring(v.encode(), etree.XMLParser(resolve_entities=False, no_network=True))
            ok = ok and element.tag == '{http://www.w3.org/2005/07/scxml}transition' and text(element.get('event'))
    elif shape in {'semantic-element', 'name-association', 'decorative-hidden'}:
        tree = html.fromstring(source.read_text())
        ok = isinstance(value, list) and bool(value)
        for v in value if isinstance(value, list) else []:
            element = html.fromstring(v)
            if shape == 'semantic-element':
                good = element.tag in {'input','select','button','textarea','a','output'} or text(element.get('role'))
            elif shape == 'decorative-hidden':
                good = element.get('aria-hidden') == 'true'
            elif element.tag == 'label':
                target = element.get('for')
                good = text(''.join(element.itertext())) and target is not None and len(tree.xpath('//*[@id=$target]', target=target)) == 1
            else:
                labelled = element.get('aria-labelledby', '').split()
                good = text(element.get('aria-label')) or bool(labelled) and all(
                    len(tree.xpath('//*[@id=$target]', target=target)) == 1 and
                    text(''.join(tree.xpath('//*[@id=$target]', target=target)[0].itertext())) for target in labelled)
            ok = ok and bool(good)
    if not ok:
        raise CoverageError('EVIDENCE_SHAPE_MISMATCH')


def profiles():
    return strict(HERE / 'profiles.json')['profiles']


def init_record(component_path, profile):
    if profile not in profiles():
        raise CoverageError('PROFILE_UNSUPPORTED')
    component = strict(component_path)
    if component.get('format') != 'ui-contract-component-draft' or not isinstance(component.get('id'), str) or not component['id'].strip():
        raise CoverageError('DRAFT_COMPONENT_INVALID')
    return {'format': 'ui-contracts-completeness/1', 'componentId': component['id'],
            'componentSha256': sha(component_path), 'profile': profile, 'profileSha256': sha(HERE / 'profiles.json'),
            'requirements': {r['id']: {'status': 'open'} for r in profiles()[profile]['requirements']}}


def inspect(repo, library, component_ref, record_path):
    result = {'overall': 'BLOCKED', 'release': False, 'componentStatus': 'draft',
              'scope': 'Explicit profile coverage and source-locator integrity; not semantic completeness',
              'library': library, 'checks': [], 'questions': [], 'errors': [],
              'semanticReviewRequired': True, 'targetValidationRequired': True,
              'notChecked': ['Whether evidence actually answers the question', 'Suitability or exhaustiveness of selected profile',
                             'CEM/DTCG/SCXML/HTML conformance', 'Runtime, rendering and accessibility conformance',
                             'Authenticity of imported evidence or user decisions', 'Production release']}
    try:
        root = library_root(Path(repo), library)
        component_path = safe(root, root, component_ref)
        component = strict(component_path)
        record = strict(Path(record_path))
        Draft7Validator(strict(HERE / 'record.schema.json')).validate(record)
        if component.get('format') != 'ui-contract-component-draft' or not isinstance(component.get('id'), str) or not component['id'].strip():
            raise CoverageError('DRAFT_COMPONENT_INVALID')
        if record['profile'] not in profiles():
            raise CoverageError('PROFILE_UNSUPPORTED')
        if record['profileSha256'] != sha(HERE / 'profiles.json'):
            raise CoverageError('PROFILE_BINDING_STALE')
        requirements = profiles()[record['profile']]['requirements']
        ids = {r['id'] for r in requirements}
        if set(record['requirements']) - ids:
            raise CoverageError('REQUIREMENT_UNKNOWN')
        refs = sources(component)
        result.update(componentId=component['id'], profile=record['profile'],
                      bindings={'component': sha(component_path), 'record': sha(Path(record_path)),
                                'profiles': sha(HERE / 'profiles.json'), 'schema': sha(HERE / 'record.schema.json'),
                                'checker': sha(Path(__file__))})
        stale = record['componentId'] != component['id'] or record['componentSha256'] != sha(component_path)
        for requirement in requirements:
            rid, domain = requirement['id'], requirement['domain']
            entry = record['requirements'].get(rid, {'status': 'open'})
            row = {'id': rid, 'domain': domain, 'status': 'open', 'reason': 'DECISION_MISSING'}
            if stale:
                row['reason'] = 'COMPONENT_BINDING_STALE'
            elif entry['status'] == 'conflict':
                row.update(status='conflict', reason='SOURCE_CONFLICT')
            elif entry['status'] == 'mapped':
                try:
                    if not refs.get(domain):
                        raise CoverageError('DOMAIN_NOT_DEFINED')
                    source = safe(root, component_path.parent, refs[domain])
                    if not entry.get('evidence'):
                        raise CoverageError('EVIDENCE_MISSING')
                    evidence = []
                    for e in entry['evidence']:
                        if e['sha256'] != sha(source):
                            raise CoverageError('SOURCE_BINDING_STALE')
                        selected = extract(source, e['selector'], domain)
                        if not meaningful(selected):
                            raise CoverageError('EVIDENCE_EMPTY_OR_PLACEHOLDER')
                        check_shape(selected, requirement['shape'], source, e['selector'])
                        evidence.append({'source': str(source.relative_to(root)), 'sha256': sha(source),
                                         'selector': e['selector'], 'selectedSha256': hashlib.sha256(
                                             json.dumps(selected, sort_keys=True, ensure_ascii=False).encode()).hexdigest()})
                    row.update(status='mapped', reason='SOURCE_LOCATOR_CHECKED', evidence=evidence)
                except (CoverageError, OSError, ValueError, KeyError, IndexError, TypeError, etree.Error) as error:
                    row['reason'] = str(error) if isinstance(error, CoverageError) else 'SOURCE_OR_LOCATOR_INVALID'
            if 'note' in entry:
                row['note'] = entry['note']  # Untrusted author note; never overrides a requirement.
            if row['status'] != 'mapped':
                result['questions'].append({'id': rid, 'domain': domain, 'question': requirement['question'],
                                            'blocking': True, 'reason': row['reason']})
            result['checks'].append(row)
        result['overall'] = 'DRAFT_INCOMPLETE' if result['questions'] else 'COVERAGE_RECORDED'
        result['statusCounts'] = {state: sum(c['status'] == state for c in result['checks']) for state in ['mapped', 'open', 'conflict']}
    except Exception as error:
        # The CLI always produces a bounded blocker, never a traceback as a success signal.
        result['errors'].append({'code': 'COVERAGE_INPUT_INVALID', 'detail': str(error)[:500]})
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, default=ROOT)
    p.add_argument('--library', required=True)
    p.add_argument('--component', required=True, help='Path relative to explicitly selected library')
    p.add_argument('--record', type=Path, required=True)
    p.add_argument('--init', action='store_true', help='Create a new all-open coverage record; never overwrite')
    p.add_argument('--profile', help='Required only for --init')
    p.add_argument('--output', type=Path)
    p.add_argument('--details', action='store_true')
    args = p.parse_args()
    if args.init:
        if not args.profile or args.output or args.details:
            p.error('--init requires --profile; do not use --output or --details')
        try:
            root = library_root(args.repo, args.library)
            component = safe(root, root, args.component)
            data = init_record(component, args.profile)
            dest = args.record.resolve()
            if dest.is_relative_to(args.repo.resolve() / 'libraries') and not dest.is_relative_to(root):
                raise CoverageError('RECORD_OUTSIDE_SELECTED_LIBRARY')
            if any(dest.is_relative_to(args.repo.resolve() / n) for n in ['examples', 'docs/research', 'docs/libraries/frozen', 'skills', 'tools']):
                raise CoverageError('RECORD_OUTPUT_PROTECTED')
            dest.parent.mkdir(parents=True, exist_ok=True)
            with dest.open('x') as f:
                json.dump(data, f, indent=2, ensure_ascii=False); f.write('\n')
            print(json.dumps({'overall': 'DRAFT_RECORD_CREATED', 'record': str(dest), 'release': False}))
            return 0
        except (ValueError, OSError) as error:
            print(json.dumps({'overall': 'BLOCKED', 'error': str(error), 'release': False})); return 2
    if args.profile:
        p.error('The frozen record supplies --profile on subsequent checks; do not override it')
    result = inspect(args.repo, args.library, args.component, args.record)
    try:
        emit(result, args.repo, args.output, args.details)
    except (ValueError, OSError) as error:
        p.error(str(error))
    return {'COVERAGE_RECORDED': 0, 'DRAFT_INCOMPLETE': 1, 'BLOCKED': 2}[result['overall']]


if __name__ == '__main__':
    raise SystemExit(main())
