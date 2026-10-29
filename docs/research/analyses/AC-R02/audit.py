#!/usr/bin/env python3
"""External read-only audit. Run from any directory; writes only beside this file.

Historical reader/checker run in a disposable copy. Counterexamples alter only
in-memory measurements, never the original .fig, criteria or run-02 files.
"""
import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RUN_REL = Path('examples/autocomplete/reproducibility/run-02')
RUN = ROOT / RUN_REL

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def load(p):
    return json.loads(p.read_text())

def snapshot():
    return {str(p.relative_to(RUN)): sha(p) for p in sorted(RUN.rglob('*')) if p.is_file()}

before = snapshot()
run = load(RUN / 'run.json')
manifest = load(RUN / 'review/hashes.json')
seal = load(RUN / 'review/preregistration-seal.json')
checks = {
    'reviewManifest': {n: sha(RUN / n) == h for n, h in manifest['files'].items()},
    'criteriaSeal': {n: sha(RUN / n) == h for n, h in seal['files'].items()},
    'runArtifacts': {n: sha(RUN / n) == h for n, h in run['artifacts'].items()},
    'builderDeliveries': {b: {n: sha(RUN / b / n) == h for n, h in d['files'].items()}
                          for b, d in run['builderDeliveries'].items()},
    'definitionFiles': {n: sha(ROOT / 'components' / n) == h for n, h in run['definitionFiles'].items()},
    'toolchainLock': sha(ROOT / 'tools/openpencil/package-lock.json') == run['toolchainPackageLockSha256'],
}
revision = hashlib.sha256(json.dumps(run['definitionFiles'], sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()
checks['definitionRevision'] = revision == run['definitionRevision']
run01 = load(ROOT / 'examples/autocomplete/reproducibility/run-01/run.json')
checks['sameInputsAsRun01'] = run01['definitionFiles'] == run['definitionFiles']
checks['sameToolchainAsRun01'] = run01['toolchainPackageLockSha256'] == run['toolchainPackageLockSha256']

with tempfile.TemporaryDirectory(prefix='ac-r02-external-') as temp:
    tmp = Path(temp)
    copied = tmp / RUN_REL
    shutil.copytree(RUN, copied)
    (tmp / 'tools').symlink_to(ROOT / 'tools', target_is_directory=True)
    (tmp / 'components').symlink_to(ROOT / 'components', target_is_directory=True)
    steps = []
    for command in [
        ['node', str(RUN_REL / 'review/inspect-original.mjs')],
        ['node', str(RUN_REL / 'review/render-original.mjs')],
        ['python3', str(RUN_REL / 'review/verify.py'), '--native-only'],
        ['python3', str(RUN_REL / 'review/verify.py')],
    ]:
        proc = subprocess.run(command, cwd=tmp, capture_output=True, text=True, timeout=120)
        steps.append({'command': command, 'exit': proc.returncode,
                      'stdout': proc.stdout[-1800:], 'stderr': proc.stderr[-1500:]})
        if proc.returncode:
            raise RuntimeError(steps[-1])
    regenerated = load(copied / 'review/results.json')
    original = load(RUN / 'review/results.json')
    replay = {
        'steps': steps,
        'verdictSummary': regenerated['verdictSummary'],
        'sameCriterionEvaluations': regenerated['criteria'] == original['criteria'],
        'samePairAgreement': regenerated['pairAgreement'] == original['pairAgreement'],
        'renderHashesMatch': {x: sha(copied / f'review/render-{x}.png') == sha(RUN / f'review/render-{x}.png') for x in 'ab'},
    }
    for x in 'ab':
        d = load(copied / f'review/original-{x}.json')
        old = load(RUN / f'review/original-{x}.json')
        replay[f'sameNativeNodes{x.upper()}'] = d['nodes'] == old['nodes']

    spec = importlib.util.spec_from_file_location('historical_checker', copied / 'review/verify.py')
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    norms = {x.upper(): load(copied / f'review/normalized-{x}.json') for x in 'ab'}
    originals = {x.upper(): load(copied / f'review/original-{x}.json') for x in 'ab'}
    def reset():
        checker.NORM = copy.deepcopy(norms)
        checker.ORIG = copy.deepcopy(originals)
        checker.NATIVE = {x: checker.native(x, checker.NORM[x], checker.ORIG[x]) for x in 'AB'}
    reset()
    baseline = checker.evaluate('A')
    probes = []
    def record(name, changes, related):
        reset()
        changes(checker.NORM['A'], checker.ORIG['A'])
        checker.NATIVE['A'] = checker.native('A', checker.NORM['A'], checker.ORIG['A'])
        result = checker.evaluate('A')
        probes.append({'name': name, 'kind': 'in-memory counterexample, not an artifact finding',
                       'changedStatuses': {k: {'before': baseline[k]['status'], 'after': v['status']}
                                           for k, v in result.items() if v['status'] != baseline[k]['status']},
                       'relatedCriteria': {k: result[k] for k in related},
                       'pairScoreAfterProbe': checker.pair_agreement(result, checker.evaluate('B'))['score']})
    record('source-correct disabled placeholder #64748B',
           lambda n, o: n['cases']['disabled']['parts']['input']['textNode'].update(fill=['#64748B']),
           ['ST10', 'COL03', 'COL08'])
    record('input stroke weight 9 instead of 1',
           lambda n, o: n['cases']['ready']['parts']['input']['stroke'].update(weight=9), ['GEO08'])
    record('second ready option font size 28 instead of 14',
           lambda n, o: n['cases']['ready']['options'][1]['textFont'].update(size=28), ['TY02'])
    record('loading input value colored error-red instead of text color',
           lambda n, o: n['cases']['loading']['parts']['input']['textNode'].update(fill=['#B91C1C']), ['COL02', 'COL11'])
    reset()
    disabled = {x: {'nodeId': checker.NORM[x]['cases']['disabled']['parts']['input']['textNode']['nodeId'],
                    'text': checker.NATIVE[x]['cases']['disabled']['texts']['input'],
                    'color': checker.NATIVE[x]['cases']['disabled']['colors']['inputText'],
                    'expectedFromSource': '#64748B', 'sourceConformant': False} for x in 'AB'}

    # Direct reader observation, independent of the historical normalizer.
    js = '''
import {readFile} from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
const core=await import(pathToFileURL(process.argv[2]+'/tools/openpencil/node_modules/@open-pencil/core/dist/index.js'));
const out={};
for(const x of ['a','b']) {
 const b=await readFile(process.argv[2]+'/examples/autocomplete/reproducibility/run-02/builder-'+x+'/autocomplete.fig');
 const g=await core.parseFigFile(b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),{populate:'all'});
 const ns=[...g.getAllNodes()];
 out[x]={locked:ns.filter(n=>n.locked).map(n=>({id:n.id,name:n.name})),
         caseFrames:ns.filter(n=>/^Autocomplete \\/ /.test(n.name)).length,
         placeholderNodes:ns.filter(n=>n.type==='TEXT'&&n.text==='Stadt suchen …').map(n=>({id:n.id,name:n.name,fills:n.fills}))};
}
console.log(JSON.stringify(out));
'''
    script = tmp / 'direct-reader.mjs'
    script.write_text(js)
    proc = subprocess.run(['node', str(script), str(ROOT)], capture_output=True, text=True, check=True)
    direct = json.loads(proc.stdout)

after = snapshot()
assert before == after, 'run-02 changed during audit'
out = {
    'auditDate': '2026-10-29', 'run': 'AC-R02',
    'model': {'name': 'DeepSeek V4.1 Flash', 'source': 'user statement; absent from run-02 metadata',
              'reasoning': None, 'perRoleConfiguration': 'not recorded'},
    'method': 'Read-only source audit; replay of historical tools in temporary copy; direct original-reader observation; in-memory counterexamples.',
    'integrity': checks, 'replay': replay, 'directReader': direct,
    'sourceConformityCounterFinding': disabled, 'checkerCounterexamples': probes,
    'run02Before': before, 'run02After': after, 'run02Unchanged': before == after,
}
(HERE / 'audit-results.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'run02Unchanged': out['run02Unchanged'], 'replay': replay['verdictSummary'],
                  'sameCriterionEvaluations': replay['sameCriterionEvaluations'],
                  'renderHashesMatch': replay['renderHashesMatch'],
                  'probes': [{k:p[k] for k in ['name','changedStatuses','pairScoreAfterProbe']} for p in probes]}, indent=2))
