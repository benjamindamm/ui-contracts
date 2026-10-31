#!/usr/bin/env python3
"""Verify declared UX capabilities with allowlisted, bounded source/native contract probes."""
import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from lxml import html
from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/libraries'))
from manage import library_root
from library_report import emit
spec = importlib.util.spec_from_file_location('library_checks', ROOT / 'tools/libraries/check.py')
library_checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(library_checks)
strict, digest = library_checks.strict, library_checks.digest

COMMON = {'role': 'choice', 'valueDomain': 'listed-keys', 'valueDisplayEditable': False,
          'searchMode': 'none', 'selectionCardinality': 'one', 'preservesSuppliedOrder': True,
          'completionMode': 'none', 'interactionIntent': 'fixed-choice', 'querySurface': 'none',
          'unknownInputPolicy': 'reject-commit'}
PROFILES = {
    'composed-autocomplete/1': {**COMMON, 'valueDisplayEditable': True, 'searchMode': 'query-provider', 'completionMode': 'label-on-confirm', 'interactionIntent': 'completion-assistance', 'querySurface': 'value-editor'},
    'single-select/1': COMMON,
    'separate-search-select/1': {**COMMON, 'searchMode': 'query-provider', 'querySurface': 'separate-filter'},
    'text-input/1': {'role': 'input', 'valueDomain': 'free-text', 'valueDisplayEditable': True,
                     'searchMode': 'none', 'selectionCardinality': 'not-applicable',
                     'preservesSuppliedOrder': False, 'completionMode': 'none',
                     'interactionIntent': 'text-entry', 'querySurface': 'none', 'unknownInputPolicy': 'retain-text'}
}


def verify_component(root, component_path, schema, repo=ROOT):
    inspector = library_checks.Inspector(root, repo)
    component = strict(component_path)
    path = inspector.safe(component_path.parent, component['ux'], '.json')
    profile = strict(path)
    errors = list(Draft7Validator(schema).iter_errors(profile))
    if errors:
        return {'status': 'invalid', 'errors': [{'code': 'UX_SCHEMA_INVALID', 'detail': '; '.join(e.message for e in errors)}]}
    if profile['componentId'] != component['id']:
        raise ValueError('UX component identity mismatch')
    # Require all leading files, including host projection rules when declared. A caller cannot cherry-pick hashes.
    domains = component['domains']; a11y = domains['accessibility']
    a11y = {'html': a11y} if isinstance(a11y, str) else a11y
    leading = [component_path, inspector.safe(component_path.parent, domains['interface'], '.json'),
               inspector.safe(component_path.parent, domains['behavior'], '.scxml'),
               inspector.safe(component_path.parent, a11y['html'], '.html')]
    if 'rules' in a11y:
        leading.append(inspector.safe(component_path.parent, a11y['rules'], '.json'))
    sources = {}
    for ref in profile['sources']:
        target = inspector.safe(path.parent, ref['path'])
        if target in sources or digest(target) != ref['sha256']:
            raise ValueError('Duplicate or stale UX source: ' + ref['path'])
        sources[target] = ref['sha256']
    if not set(leading).issubset(sources):
        raise ValueError('UX sources omit a leading contract file')
    plan = profile['verification']['profile']
    result = {'status': 'declared', 'profile': plan, 'capabilities': profile['capabilities'],
              'sourceHashes': {str(p.relative_to(root)): h for p, h in sources.items()},
              'verifiedProperties': [], 'notChecked': ['Target implementation', 'Accessibility conformance', 'Production release']}
    if plan == 'declared-only':
        result['reason'] = 'No implemented native verification profile; do not treat as eligible proof.'
        return result
    if plan not in PROFILES:
        result.update(status='unverified', reason='Unsupported verification profile')
        return result
    # This explicit profile expectation is backed by tests below, not inferred from a component's name.
    if profile['capabilities'] != PROFILES[plan]:
        result.update(status='invalid', errors=[{'code': 'UX_PROFILE_CAPABILITY_CONFLICT', 'detail': 'Declared capabilities do not match the bounded verification profile'}])
        return result
    cem = strict(leading[1])
    declarations = [d for m in cem['modules'] for d in m.get('declarations', []) if d.get('kind') == 'class']
    if len(declarations) != 1:
        result.update(status='unverified', reason='Profile requires one explicit CEM class')
        return result
    expected = {'members': {'value': 'string', 'enabled': 'boolean', 'readOnly': 'boolean'},
                'events': {'value-change': 'CustomEvent<{value:string}>'}} if plan == 'text-input/1' else {
                'members': {'value': 'string | undefined', 'options': 'Array<{key:string;label:string;disabled?:boolean}>', 'enabled': 'boolean'},
                'events': {'value-change': 'CustomEvent<{value:string | undefined;reason:"user" | "options-change"}>'}}
    if plan == 'composed-autocomplete/1':
        expected = {'members': {'query': 'string', 'value': 'string | undefined', 'results': 'Array<{key:string;label:string;disabled?:boolean}>', 'enabled': 'boolean'}, 'events': {'value-change': 'CustomEvent<{value:string}>'}}
    if plan == 'separate-search-select/1':
        expected['members']['query'] = 'string'
    try:
        type_proc = subprocess.run(['node', str(ROOT / 'tools/ux/cem-profile.cjs')], input=json.dumps({'declaration': declarations[0], 'expected': expected}), capture_output=True, text=True, timeout=10)
        type_result = json.loads(type_proc.stdout)
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        result.update(status='unverified', reason='Type checker unavailable: ' + str(error))
        return result
    result['types'] = type_result
    if type_result.get('code') == 'TYPE_FORM_UNSUPPORTED' or type_result.get('passed') and type_result.get('typescript') != '5.9.3':
        result.update(status='unverified', reason='Type form or checker version outside the bounded profile')
        return result
    if type_proc.returncode or not type_result.get('passed') or type_result.get('typescript') != '5.9.3':
        result.update(status='invalid', errors=[{'code': 'UX_PROFILE_TYPE_CONFLICT', 'detail': type_result}])
        return result
    fields = {m['name']: m.get('type', {}).get('text', '').replace(' ', '') for m in declarations[0].get('members', [])}
    tree = html.fromstring(leading[3].read_text())
    if plan == 'text-input/1':
        static_ok = bool(tree.xpath('self::input|.//input'))
    else:
        static_ok = True
        if plan == 'composed-autocomplete/1':
            static_ok = bool(tree.xpath('.//input[@role="combobox"]')) and bool(tree.xpath('.//*[@role="listbox"]'))
        elif plan == 'single-select/1':
            controls = tree.xpath('self::select|.//select')
            static_ok = static_ok and len(controls) == 1 and 'multiple' not in controls[0].attrib and not tree.xpath('.//input[@type="search"]')
        else:
            trigger = tree.xpath('.//button[@data-part="trigger"]')
            static_ok = static_ok and len(trigger) == 1 and not trigger[0].xpath('.//input|.//textarea') and bool(tree.xpath('.//input[@data-part="search"]')) and bool(tree.xpath('.//*[@role="listbox"]'))
            if len(trigger) == 1:
                nodes = [*trigger[0].iter(), *trigger[0].iterancestors()]
                static_ok = static_ok and not any(n.get('contenteditable') is not None and n.get('contenteditable').lower() != 'false' for n in nodes)
    if not static_ok:
        result.update(status='invalid', errors=[{'code': 'UX_PROFILE_SOURCE_CONFLICT', 'detail': 'CEM/HTML does not implement the declared profile structure'}])
        return result
    native_request = {'profile': plan, 'model': str(leading[2])}
    if plan == 'composed-autocomplete/1':
        children = {}
        for role, slot in [('overlay', 'overlay'), ('scroll-area', 'overlay.scroll')]:
            child_path = inspector.safe(component_path.parent, component['composition'][slot]['component'], '.json')
            child = strict(child_path)
            model = inspector.safe(child_path.parent, child['domains']['behavior'], '.scxml')
            if not {child_path, model}.issubset(sources):
                raise ValueError('UX sources omit composed contracts')
            children[role] = str(model)
        native_request['components'] = children
    try:
        proc = subprocess.run(['node', str(ROOT / 'tools/ux/contract-probe.cjs')],
                              input=json.dumps(native_request),
                              capture_output=True, text=True, timeout=15)
        native = json.loads(proc.stdout)
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        result.update(status='unverified', reason='Native verification unavailable: ' + str(error))
        return result
    result['native'] = native
    if native.get('overall') == 'PASS_LIMITED' and native.get('runtime', {}).get('version') != '4.3.28':
        result.update(status='unverified', reason='Unsupported SCION runtime version')
        return result
    if proc.returncode or native.get('overall') != 'PASS_LIMITED':
        result.update(status='invalid', errors=[{'code': 'UX_NATIVE_CONTRACT_FAILED', 'detail': native.get('diagnostic', 'Native checks failed')}])
        return result
    if any(digest(p) != h for p, h in sources.items()):
        result.update(status='invalid', errors=[{'code': 'UX_SOURCE_CHANGED_DURING_CHECK', 'detail': 'Sources changed during probe'}])
        return result
    result.update(status='verified-limited', scope='declared-profile-source-structure-and-native-SCXML-countercases',
                  verifiedProperties=[k for k in profile['capabilities'] if k != 'interactionIntent'])
    result['declarationOnlyProperties'] = ['interactionIntent']
    return result


def verify(repo, library):
    root = library_root(repo, library)
    structure = library_checks.inspect(root, repo)
    result = {'overall': structure['overall'], 'release': False,
              'scope': 'bounded-UX-source-and-native-contract-verification', 'library': library,
              'structure': structure, 'components': {}}
    if structure['errors']:
        return result
    index = strict(root / 'library.json')
    binding = index.get('selection')
    if not binding:
        result.update(overall='BLOCKED', diagnostic={'code': 'UX_BINDING_MISSING', 'detail': 'Library has no explicit selection/schema binding'})
        return result
    inspector = library_checks.Inspector(root, repo)
    schema = strict(inspector.safe(root, binding['capabilitiesSchema'], '.json'))
    for name, relative in index['components'].items():
        path = inspector.safe(root, relative, '.json')
        if 'ux' not in strict(path):
            continue
        try:
            row = verify_component(root, path, schema, repo)
        except (ValueError, OSError, KeyError, TypeError) as error:
            row = {'status': 'invalid', 'errors': [{'code': 'UX_SOURCE_INVALID', 'detail': str(error)}]}
        result['components'][name] = row
        if row['status'] == 'invalid':
            result['overall'] = 'FAIL'
    result['statusCounts'] = {status: sum(r['status'] == status for r in result['components'].values()) for status in ['declared', 'unverified', 'invalid', 'verified-limited']}
    result['checkerHashes'] = {'python': digest(Path(__file__)), 'nativeProbe': digest(ROOT / 'tools/ux/contract-probe.cjs'), 'composedProbe': digest(ROOT / 'tools/ux/composed-probe.cjs'), 'invoker': digest(ROOT / 'tools/web/session.mjs'), 'providerGate': digest(ROOT / 'tools/web/provider.mjs'), 'typeProbe': digest(ROOT / 'tools/ux/cem-profile.cjs'), 'toolchainLock': digest(ROOT / 'tools/openpencil/package-lock.json')}
    result['notChecked'] = ['Browser adapter, focus and scrolling', 'Arbitrary capability semantics outside registered profiles', 'Production release']
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=ROOT)
    parser.add_argument('--library', required=True)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--details', action='store_true')
    args = parser.parse_args()
    try:
        result = verify(args.repo.resolve(), args.library)
    except (ValueError, OSError, KeyError, TypeError) as error:
        result = {'overall': 'BLOCKED', 'release': False, 'diagnostic': str(error)}
    try:
        emit(result, args.repo, args.output, args.details)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    return {'PASS_LIMITED': 0, 'FAIL': 1, 'BLOCKED': 2}[result['overall']]


if __name__ == '__main__':
    raise SystemExit(main())
