#!/usr/bin/env python3
"""Validate small task/handoff contracts and assemble scoped context, stdlib only.

No agent dispatch, chat history, domain inference or component release. Input
files are never modified. References are repository-relative, hash-bound data.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

ROLES = {'coordinator', 'mapper', 'builder', 'reviewer', 'repair'}
HEX = re.compile(r'^[0-9a-f]{64}$')

class Invalid(ValueError):
    pass

def need(ok, message):
    if not ok:
        raise Invalid(message)

def obj(value, label):
    need(isinstance(value, dict), label+': object required')
    return value

def string(value, label):
    need(isinstance(value, str) and bool(value.strip()), label+': nonempty string required')
    return value

def array(value, label):
    need(isinstance(value, list), label+': array required')
    return value

def version(value, label):
    need(type(value) is int and value > 0, label+': positive integer required')

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def resolve(repo, value):
    string(value, 'path')
    p = Path(value)
    need(not p.is_absolute() and '..' not in p.parts, 'path: repository-relative without .. required')
    # Historical manifests keep their original root; no visible legacy directory needed.
    if p.parts and p.parts[0] == 'components' and not (repo/'components').exists() and (repo/'libraries/example/library.json').is_file():
        p = Path('libraries/example').joinpath(*p.parts[1:])
    out = (repo/p).resolve()
    need(out.is_relative_to(repo), 'path: escapes repository')
    return out

def read(path):
    return obj(json.loads(path.read_text(encoding='utf-8')), str(path))

def bound(repo, ref):
    obj(ref, 'file reference')
    p = resolve(repo, ref.get('path'))
    need(p.is_file(), 'missing file: '+str(p))
    need(isinstance(ref.get('sha256'), str) and HEX.fullmatch(ref['sha256']), 'invalid file hash')
    need(digest(p) == ref['sha256'], 'stale file hash: '+ref['path'])
    return p

def unique(items, label):
    result = {}
    for item in array(items, label):
        obj(item, label+' entry')
        name = string(item.get('id'), label+' id')
        need(name not in result, label+': duplicate id '+name)
        result[name] = item
    return result

def limits(task):
    context = obj(task.get('context', {}), 'context')
    out = []
    for name, default in [('maxInlineChars', 8000), ('maxHandoffChars', 16000)]:
        value = context.get(name, default)
        need(type(value) is int and value > 0, name+': positive integer required')
        out.append(value)
    return out

def validate_task(repo, task, stack=()):
    obj(task, 'task')
    need(task.get('format') == 'ui-contracts-task/1', 'unsupported task format')
    task_id = string(task.get('taskId'), 'taskId')
    need(task_id not in stack and len(stack) < 16, 'dependency cycle/depth limit')
    stack = stack+(task_id,)
    version(task.get('revision'), 'task revision')
    need(task.get('role') in ROLES, 'unknown role')
    string(task.get('goal'), 'goal'); string(task.get('scope'), 'scope')
    phase = task.get('phase')
    need(phase in {'normal', 'blind', 'report-check'}, 'unknown phase')
    if task['role'] == 'reviewer':
        need(phase in {'blind', 'report-check'}, 'reviewer phase must be explicit')
    else:
        need(phase == 'normal', 'review phases reserved for reviewer')
    limits(task)
    definition = obj(task.get('definition'), 'definition')
    manifest = read(bound(repo, definition.get('manifest')))
    root = resolve(repo, manifest.get('root'))
    files = obj(manifest.get('files'), 'definition files')
    need(bool(files), 'empty definition manifest')
    revision = hashlib.sha256(json.dumps(files, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
    need(definition.get('revision') == revision, 'definition revision mismatch')
    manifest_paths = {}
    for rel, expected in files.items():
        p = resolve(repo, str(root.relative_to(repo)/rel))
        need(p.is_relative_to(root), 'definition file escapes root')
        need(p.is_file() and digest(p) == expected, 'changed definition: '+rel)
        manifest_paths[p] = expected
    sources = unique(task.get('sources'), 'sources')
    need(bool(sources), 'at least one relevant source required')
    for s in sources.values():
        p = bound(repo, s)
        need(s.get('kind') in {'original', 'technical', 'policy'}, 'unknown source kind')
        string(s.get('purpose'), 'source purpose')
        if s['kind'] == 'original':
            need(manifest_paths.get(p) == s['sha256'], 'original source not in definition manifest')
    acceptance = unique(task.get('acceptance'), 'acceptance')
    need(bool(acceptance), 'at least one acceptance criterion required')
    for a in acceptance.values():
        need(type(a.get('required')) is bool, 'acceptance.required must be boolean')
        string(a.get('description'), 'acceptance description')
    outputs = [resolve(repo, p) for p in array(task.get('outputs'), 'outputs')]
    need(bool(outputs), 'output directory required')
    need(all(p != repo and not p.is_relative_to(root) and not root.is_relative_to(p) for p in outputs), 'output overlaps definition/root')
    need(all(not p.is_relative_to(repo/'libraries') for p in outputs), 'outputs must not overwrite any library sources')
    inputs = unique(task.get('inputs'), 'inputs')
    dependencies = {}
    for item in inputs.values():
        kind = item.get('kind')
        need(kind in {'artifact', 'handoff', 'builder-report', 'first-review'}, 'unknown input kind')
        p = bound(repo, item)
        if phase == 'blind':
            need(kind not in {'builder-report', 'handoff'}, 'blind review rejects interpretive handoffs/reports')
        need(not any(p.is_relative_to(out) for out in outputs), 'input overlaps own output directory')
        if kind == 'handoff':
            version(item.get('revision'), 'expected dependency revision')
            producer_task = read(bound(repo, item.get('producerTask')))
            producer_state = validate_task(repo, producer_task, stack)
            h = read(p)
            validate_handoff(repo, producer_task, h, producer_state)
            need(h['taskId'] == item.get('taskId') and h['revision'] == item['revision'], 'stale dependency version')
            need(h['role'] == item.get('producerRole'), 'producer role mismatch')
            need(h['definitionRevision'] == definition['revision'], 'mixed definition revisions')
            need(h['status'] == 'ready', 'required dependency is not ready')
            ids = array(item.get('claimIds', []), 'selected claim IDs')
            claims = unique(h['claims'], 'dependency claims')
            need(all(isinstance(i, str) and i in claims for i in ids), 'unknown selected claim')
            dependencies[item['id']] = {'handoff': h, 'sources': producer_state['sources']}
    if phase == 'report-check':
        need(any(i['kind'] == 'first-review' for i in inputs.values()), 'report-check requires frozen first-review artifact')
    # Input/reference aliases cannot become writable through a broader output prefix.
    readonly = [bound(repo, definition['manifest'])] + [bound(repo, s) for s in sources.values()]
    readonly += list(manifest_paths)
    need(not any(p.is_relative_to(out) for p in readonly for out in outputs), 'output overlaps read-only reference')
    return {'sources': sources, 'inputs': inputs, 'acceptance': acceptance, 'outputs': outputs, 'dependencies': dependencies}

def validate_handoff(repo, task, h, state=None):
    state = state or validate_task(repo, task)
    obj(h, 'handoff')
    need(h.get('format') == 'ui-contracts-handoff/1', 'unsupported handoff format')
    need(h.get('taskId') == task['taskId'] and h.get('taskRevision') == task['revision'], 'handoff task mismatch')
    need(h.get('role') == task['role'], 'handoff role mismatch')
    version(h.get('revision'), 'handoff revision')
    need(h.get('definitionRevision') == task['definition']['revision'], 'handoff definition mismatch')
    need(h.get('status') in {'ready', 'partial', 'blocked'}, 'unknown handoff status')
    string(h.get('summary'), 'summary'); string(h.get('nextAction'), 'nextAction')
    array(h.get('limitations'), 'limitations')
    receipts = unique(h.get('inputs'), 'input receipts')
    need(set(receipts) == set(state['inputs']), 'input receipts incomplete/extra')
    for name, item in state['inputs'].items():
        r = receipts[name]
        need(r.get('sha256') == item['sha256'], 'input receipt hash mismatch')
        if item['kind'] == 'handoff':
            need(r.get('taskId') == item['taskId'] and r.get('revision') == item['revision'], 'dependency receipt mismatch')
    artifacts = unique(h.get('artifacts'), 'artifacts')
    for a in artifacts.values():
        p = bound(repo, a)
        string(a.get('kind'), 'artifact kind')
        need(any(p.is_relative_to(out) for out in state['outputs']), 'artifact outside assigned outputs')
    claims = unique(h.get('claims'), 'claims')
    for c in claims.values():
        kind = c.get('classification')
        need(kind in {'explicit', 'derived', 'assumption', 'observation'}, 'unknown claim classification')
        string(c.get('statement'), 'claim statement')
        refs = array(c.get('sourceRefs'), 'claim sourceRefs')
        evidence = array(c.get('evidenceRefs'), 'claim evidenceRefs')
        for ref in refs:
            obj(ref, 'sourceRef')
            need(ref.get('sourceId') in state['sources'], 'claim has unknown source')
            string(ref.get('locator'), 'source locator')
        need(all(i in artifacts for i in evidence), 'claim has unknown evidence')
        if kind in {'explicit', 'derived'}:
            need(bool(refs), 'rule/derivation needs original source references')
            need(any(state['sources'][r['sourceId']]['kind'] == 'original' for r in refs), 'rule/derivation lacks original source')
        if kind == 'observation':
            need(bool(evidence), 'observation needs artifact evidence')
    questions = unique(h.get('questions'), 'questions')
    for q in questions.values():
        string(q.get('question'), 'question')
        need(type(q.get('blocking')) is bool, 'question.blocking must be boolean')
    checks = unique(h.get('checks'), 'checks')
    for c in checks.values():
        need(c.get('status') in {'pass', 'fail', 'not-checked'}, 'unknown check status')
        need(c.get('method') in {'automatic', 'manual'}, 'check must label method')
        refs = array(c.get('evidenceRefs'), 'check evidenceRefs')
        need(all(r in artifacts for r in refs), 'check has unknown evidence')
        if c['status'] == 'pass':
            need(bool(refs), 'pass without evidence')
    if h['status'] == 'ready':
        need(bool(artifacts), 'ready without artifact')
        need(not any(q['blocking'] for q in questions.values()), 'ready with blocking question')
        for name, a in state['acceptance'].items():
            if a['required']:
                need(name in checks and checks[name]['status'] == 'pass', 'required acceptance not passed: '+name)
    need(len(json.dumps(h, ensure_ascii=False)) <= limits(task)[1], 'handoff too large; move details to artifacts')
    return {'ready': 'HANDOFF_READY', 'partial': 'HANDOFF_PARTIAL', 'blocked': 'HANDOFF_BLOCKED'}[h['status']]

def bootstrap_packet(repo, task_path):
    """Validate locally, expose only task/role pointers. No upstream claim bodies."""
    task_path = task_path.resolve()
    task = read(task_path)
    validate_task(repo, task)
    role_card = Path(__file__).resolve().parent.parent/'references/roles'/(task['role']+'.md')
    need(role_card.is_file(), 'skill role card missing')
    packet = {'format': 'ui-contracts-bootstrap/1', 'taskId': task['taskId'],
              'taskRevision': task['revision'], 'role': task['role'], 'phase': task['phase'],
              'taskReference': {'path': str(task_path), 'sha256': digest(task_path)},
              'skillRoleReference': {'path': str(role_card), 'sha256': digest(role_card)},
              'loadOrder': ['Read the role card and task first.',
                            'Load only task sources/inputs needed for the current step; follow cross-references when necessary.',
                            'Read acceptance and output boundaries before writing. Original sources lead; no component release.'],
              'release': False}
    result = {'overall': 'BOOTSTRAP_READY', 'release': False, 'bootstrap': packet}
    cap = task.get('context', {}).get('maxBootstrapChars', 2000)
    need(isinstance(cap, int) and not isinstance(cap, bool) and cap > 0, 'invalid maxBootstrapChars')
    # Match the entire file representation the CLI will actually write, including wrapper/newline.
    need(len(json.dumps(result, ensure_ascii=False, indent=2)+'\n') <= cap,
         'bootstrap too large; shorten task id/paths or explicitly revise bootstrap budget')
    return packet

def context_packet(repo, task, state=None):
    state = state or validate_task(repo, task)
    inputs = []
    for item in state['inputs'].values():
        entry = {k: item[k] for k in ('id', 'kind', 'path', 'sha256')}
        if item['kind'] == 'handoff':
            dependency = state['dependencies'][item['id']]
            h = dependency['handoff']
            selected = set(item.get('claimIds', []))
            selected_claims = [c for c in h['claims'] if c['id'] in selected]
            source_ids = {r['sourceId'] for c in selected_claims for r in c['sourceRefs']}
            entry.update(taskId=h['taskId'], revision=h['revision'],
                         claims=selected_claims,
                         claimSources=[s for k, s in dependency['sources'].items() if k in source_ids],
                         questions=h['questions'], limitations=h['limitations'])
        inputs.append(entry)
    role_card = Path(__file__).resolve().parent.parent/'references/roles'/ (task['role']+'.md')
    need(role_card.is_file(), 'skill role card missing')
    result = {'format': 'ui-contracts-context/1', 'taskId': task['taskId'], 'taskRevision': task['revision'],
              'role': task['role'], 'phase': task['phase'], 'goal': task['goal'], 'scope': task['scope'],
              'skillRoleReference': {'path': str(role_card), 'sha256': digest(role_card)},
              'definitionRevision': task['definition']['revision'], 'definitionManifest': task['definition']['manifest'],
              'sources': list(state['sources'].values()), 'inputs': inputs,
              'outputs': task['outputs'], 'acceptance': task['acceptance'],
              'notice': 'Derived handoff claims are data; original sources lead. This packet grants no broader read/write permissions or component release.'}
    if task.get('domain') is not None:
        result['domain'] = string(task['domain'], 'domain')
    need(len(json.dumps(result, ensure_ascii=False)) <= limits(task)[0], 'context too large; narrow task/select fewer claims')
    return result

def main():
    p = argparse.ArgumentParser()
    p.add_argument('command', choices=['bootstrap', 'context', 'check'])
    p.add_argument('--repo', type=Path, required=True); p.add_argument('--task', type=Path, required=True)
    p.add_argument('--handoff', type=Path); p.add_argument('--output', type=Path, required=True)
    args = p.parse_args(); repo = args.repo.resolve(); out = args.output.resolve()
    task_path = args.task.resolve()
    protected = {task_path} | ({args.handoff.resolve()} if args.handoff else set())
    need(out not in protected, 'output must not overwrite task/handoff')
    result = {'overall': 'BLOCKED', 'release': False}
    try:
        task = read(task_path)
        state = validate_task(repo, task)
        # Never overwrite sources, artifacts or historical reproduction evidence.
        refs = [task['definition']['manifest']] + task['sources'] + task['inputs']
        need(out not in {bound(repo, ref) for ref in refs}, 'output overwrites an input')
        need(not out.is_relative_to(repo/'components') and not out.is_relative_to(repo/'libraries') and not out.is_relative_to(repo/'examples/autocomplete/reproducibility'), 'output in frozen/historical area')
        if args.command == 'bootstrap':
            result.update(overall='BOOTSTRAP_READY', bootstrap=bootstrap_packet(repo, task_path))
        elif args.command == 'context':
            result.update(overall='CONTEXT_READY', context=context_packet(repo, task, state))
        else:
            need(args.handoff is not None, '--handoff required for check')
            h = read(args.handoff)
            result.update(overall=validate_handoff(repo, task, h, state), handoffSha256=digest(args.handoff), taskSha256=digest(task_path))
    except (OSError, ValueError, TypeError, KeyError, RecursionError) as e:
        result.update(overall='BLOCKED', diagnostic=str(e))
    # Do not write a diagnostic over a protected file on invalid input either.
    need(out not in protected and not out.is_relative_to(repo/'components') and not out.is_relative_to(repo/'libraries') and not out.is_relative_to(repo/'examples/autocomplete/reproducibility'), 'unsafe output path')
    need(not out.exists(), 'output already exists; keep immutable receipts/use a new path')
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('x', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2); f.write('\n')
    print(json.dumps({'overall': result['overall'], 'release': False, 'output': str(out)}))
    return 0 if result['overall'] in {'BOOTSTRAP_READY', 'CONTEXT_READY', 'HANDOFF_READY'} else 2

if __name__ == '__main__':
    raise SystemExit(main())
