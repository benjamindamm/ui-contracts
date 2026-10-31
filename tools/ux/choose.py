#!/usr/bin/env python3
"""Evaluate the selected library's fixed-choice DMN policy after current bounded verification."""
import argparse
import importlib.util
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('ux_verification', ROOT / 'tools/ux/check.py')
ux = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ux)
sys.path.insert(0, str(ROOT / 'tools/libraries'))
from manage import manifest, library_root
from library_report import emit


class Blocked(ValueError):
    def __init__(self, code, detail):
        self.code, self.detail = code, str(detail)
        super().__init__(self.detail)


def native(model, decision, facts, runtime, java=None):
    config_path = ROOT / '.runtime/config.json'
    config = ux.strict(config_path) if config_path.is_file() else {}
    if runtime is None:
        runtime = (ROOT / '.runtime' / config['dmn']) if config.get('dmn') else None
        java = java or config.get('java')
    if runtime is None:
        raise Blocked('UX_ENGINE_NOT_CONFIGURED', 'Supply --runtime DIR or UX_RULE_RUNTIME; no temporary or platform-specific path is assumed.')
    runtime = Path(runtime).resolve()
    lock = ux.strict(ROOT / 'tools/ux/runtime.lock.json')
    entries = (runtime / 'classpath.txt').read_text().strip().split(os.pathsep)
    paths = [Path(p).resolve() for p in entries if p]
    actual = {p.name: ux.digest(p) for p in paths}
    if len(paths) != len(actual) or actual != lock['jars']:
        raise Blocked('UX_ENGINE_LOCK_MISMATCH', 'Configured engine JAR set differs from tools/ux/runtime.lock.json')
    executable = shutil.which(java or 'java')
    if not executable:
        raise Blocked('UX_JAVA_MISSING', 'Configure Java 17+ via PATH or --java.')
    compiler = Path(executable).resolve().parent / 'javac'
    if not compiler.is_file():
        compiler = Path(shutil.which('javac') or '/nonexistent-javac')
    if not compiler.is_file():
        raise Blocked('UX_JAVAC_MISSING', 'The bridge is compiled from repository source; a JDK is required.')
    classpath = os.pathsep.join(str(p) for p in paths)
    bridge = ROOT / 'tools/ux' / lock['bridgeSource']
    with tempfile.TemporaryDirectory(prefix='ui-contracts-dmn-') as tmp:
        compiled = subprocess.run([str(compiler), '--release', str(lock['javaRelease']), '-cp', classpath,
                                   '-d', tmp, str(bridge)], capture_output=True, text=True, timeout=30)
        if compiled.returncode:
            raise Blocked('UX_BRIDGE_COMPILE_FAILED', compiled.stderr[-1500:])
        run = subprocess.run([executable, '-cp', tmp + os.pathsep + classpath, 'DmnProbe', str(model), decision],
                             input=json.dumps(facts, ensure_ascii=False), capture_output=True, text=True, timeout=30)
    if run.returncode:
        raise Blocked('UX_ENGINE_EXECUTION_FAILED', run.stderr[-1500:])
    result = json.loads(run.stdout)
    if result.get('stage') != 'evaluated' or not isinstance(result.get('value'), dict):
        raise Blocked('UX_ENGINE_DECISION_FAILED', result)
    return result, {'lockSha256': ux.digest(ROOT / 'tools/ux/runtime.lock.json'), 'bridgeSha256': ux.digest(bridge),
                    'engine': lock['engine'], 'version': lock['engineVersion'], 'java': executable}


def evaluate(repo, library, context, runtime=None, java=None, prepare_only=False):
    repo = Path(repo).resolve()
    root = library_root(repo, library)
    revision = manifest(repo, library)['revision']
    verified = ux.verify(repo, library)
    base = {'overall': 'BLOCKED', 'release': False, 'library': library, 'libraryRevision': revision,
            'scope': 'fixed-choice-project-policy-with-bounded-contract-evidence',
            'verification': verified, 'targetValidationRequired': True}
    if verified['overall'] != 'PASS_LIMITED':
        base.update(overall=verified['overall'], diagnostic={'code': 'UX_VERIFICATION_FAILED', 'detail': 'Resolve invalid source/capability claims before selecting.'})
        return base
    index = ux.strict(root / 'library.json')
    inspector = ux.library_checks.Inspector(root, repo)
    policy_path = inspector.safe(root, index['selection']['policy'], '.json')
    policy = ux.strict(policy_path)
    if policy.get('format') != 'ui-contracts-selection-policy/0.3':
        raise Blocked('UX_POLICY_UNSUPPORTED', policy.get('format'))
    if context.get('library') != library:
        raise Blocked('UX_CONTEXT_LIBRARY_MISMATCH', 'Context must explicitly name the selected library.')
    facts = context.get('facts', {})
    if not isinstance(facts, dict):
        raise Blocked('UX_FACTS_INVALID', 'facts must be an object')
    required = ['fixedValuesRequired', 'queryEditingAllowed', 'selectedLabelEditingAllowed', 'filteringProviderAvailable']
    missing = [key for key in required if key not in facts or facts[key] is None]
    if missing:
        base.update(choice='needs-clarification', diagnostic={'code': 'UX_FACTS_INCOMPLETE', 'detail': missing})
        return base
    if any(type(facts[key]) is not bool for key in required):
        raise Blocked('UX_FACTS_INVALID', 'Required facts must be explicit booleans, not truthy strings/numbers.')
    if facts['fixedValuesRequired'] is not True:
        base.update(choice='no-supported-policy', diagnostic={'code': 'UX_POLICY_SCOPE_UNSUPPORTED', 'detail': 'This policy is for listed-key choice, not free-text writing assistance.'})
        return base
    options = context.get('options')
    if not isinstance(options, list) or any(not isinstance(o, dict) or not isinstance(o.get('key'), str) or not o['key'].strip() or not isinstance(o.get('label'), str) or not o['label'].strip() or 'disabled' in o and type(o['disabled']) is not bool for o in options):
        raise Blocked('UX_OPTIONS_INVALID', 'Supply actual keyed options with nonempty labels.')
    if len({o['key'] for o in options}) != len(options):
        raise Blocked('UX_OPTIONS_DUPLICATE_KEY', 'Country keys stay unique even when calling codes match.')
    explicit = facts.get('searchExplicitlyRequired')
    if explicit is not None and type(explicit) is not bool:
        raise Blocked('UX_FACTS_INVALID', 'searchExplicitlyRequired must be boolean or null.')
    parameters = policy['parameters']
    threshold = parameters.get('searchRequiredAbove')
    if type(threshold) is not int or threshold < 0 or set(parameters) != {'searchRequiredAbove'}:
        raise Blocked('UX_POLICY_PARAMETERS_INVALID', 'Supported parameter is nonnegative integer searchRequiredAbove.')
    inputs = {key: facts[key] for key in required}
    inputs.update(searchExplicitlyRequired=explicit, optionCount=len(options), searchRequiredAbove=threshold)
    bindings = policy.get('candidateBindings', [])
    names, variables = set(), set()
    for binding in bindings:
        name = binding['component']
        if name in names or name not in verified['components']:
            raise Blocked('UX_POLICY_BINDING_INVALID', name)
        names.add(name)
        for field in ['capabilitiesInput', 'verificationInput']:
            key = binding[field]
            if not isinstance(key, str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', key) or key in variables or key in inputs:
                raise Blocked('UX_POLICY_BINDING_INVALID', key)
            variables.add(key)
        row = verified['components'][name]
        critical = {'role', 'valueDomain', 'valueDisplayEditable', 'searchMode', 'selectionCardinality'}
        status = row['status']
        if status == 'verified-limited' and not critical.issubset(row['verifiedProperties']):
            status = 'unverified'
        inputs[binding['capabilitiesInput']] = row['capabilities']
        inputs[binding['verificationInput']] = status
    if set(policy.get('candidateComponents', [])) != names or not names:
        raise Blocked('UX_POLICY_BINDING_INVALID', 'Candidate list and input bindings differ.')
    model = inspector.safe(root, policy['logic'], '.dmn')
    base.update(inputs=inputs, policySource={'path': str(policy_path.relative_to(repo)), 'sha256': ux.digest(policy_path)},
                logicSha256=ux.digest(model), contextSha256=hashlib.sha256(json.dumps(context, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest())
    if prepare_only:
        base.update(overall='PASS_LIMITED', decisionStatus='prepared-only-not-evaluated', choice=None)
    else:
        decision, engine = native(model, policy['decision'], inputs, runtime, java)
        choice = decision['value'].get('choice')
        base.update(assessment=decision['value'], choice=choice, native=decision, engine=engine)
        if choice in names and verified['components'][choice]['status'] == 'verified-limited':
            base['overall'] = 'PASS_LIMITED'
        else:
            base['diagnostic'] = {'code': 'UX_NO_VERIFIED_CANDIDATE', 'detail': choice}
    if manifest(repo, library)['revision'] != revision:
        raise Blocked('UX_LIBRARY_CHANGED_DURING_EVALUATION', 'Repeat against stable inputs.')
    return base


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=ROOT)
    parser.add_argument('--library', required=True)
    parser.add_argument('--context', type=Path, required=True)
    parser.add_argument('--runtime', type=Path, default=os.environ.get('UX_RULE_RUNTIME'))
    parser.add_argument('--java')
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--details', action='store_true')
    args = parser.parse_args()
    try:
        result = evaluate(args.repo, args.library, ux.strict(args.context), args.runtime, args.java, args.prepare_only)
    except (Blocked, ValueError, KeyError, TypeError, OSError, subprocess.TimeoutExpired) as error:
        result = {'overall': 'BLOCKED', 'release': False,
                  'diagnostic': {'code': getattr(error, 'code', 'UX_EVALUATION_BLOCKED'), 'detail': str(error)}}
    try:
        emit(result, args.repo, args.output, args.details)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    return {'PASS_LIMITED': 0, 'FAIL': 1, 'BLOCKED': 2}[result['overall']]


if __name__ == '__main__':
    raise SystemExit(main())
