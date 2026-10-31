from pathlib import Path
import json,tempfile,shutil,hashlib,importlib.util,subprocess
R=Path('/Users/kcnpxcp/Dev/GitHub/ui-contracts');O=Path('/tmp/ui-contracts-framework-audit-20261031');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();helper=R/'docs/research/studies/UX-RULES-01/studies/SELECTION-01/evaluate.py'
spec=importlib.util.spec_from_file_location('selection_evaluator',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
with tempfile.TemporaryDirectory(prefix='ux-capability-audit-') as td:
 T=Path(td);L=T/'libraries/example';shutil.copytree(R/'libraries/example',L);S=T/'study';S.mkdir();m.LIB=L;m.ROOT=T;m.HERE=S
 def bind():
  files={str(p.relative_to(L)):sha(p) for p in sorted(L.rglob('*')) if p.is_file()};revision=hashlib.sha256(json.dumps(files,sort_keys=True,separators=(',',':')).encode()).hexdigest();(S/'library-manifest.json').write_text(json.dumps({'root':'libraries/example','files':files,'revision':revision}))
 request=json.loads((helper.parent/'inputs/b.json').read_text());bind();baseline=m.evaluate(request)
 up=L/'components/select/ux.json';u=json.loads(up.read_text());before={s['path']:sha(up.parent/s['path']) for s in u['sources']};u['capabilities']['searchMode']='query-provider';up.write_text(json.dumps(u));bind();mutant=m.evaluate(request);after={s['path']:sha(up.parent/s['path']) for s in u['sources']}
 result={'scope':'Disposable copy, deliberate false capability declaration; original helper source untouched','helperSha256':sha(helper),'mutation':'Select ux.json searchMode none -> query-provider, new manifest honestly bound to this revision; no Select CEM/SCXML/HTML change','sourcesUnchanged':before==after,'baseline':baseline,'falseCapabilityResult':mutant,'expectationForSemanticValidator':'Reject unsupported declared search capability; present checker validates only declaration/schema/hash consistency','notAReleaseBypass':'Both reports explicitly release:false; this is false eligibility inside the bounded selection logic'}
 assert baseline['assessment']['choice']=='Autocomplete' and mutant['assessment']['choice']=='Select' and before==after,result
 (O/'capability-counterexample.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
# Candidate with dangling leading source references: syntax is fine, reference semantics remain unvalidated.
with tempfile.TemporaryDirectory(prefix='ux-reference-audit-') as td:
 T=Path(td);(T/'component.json').write_text(json.dumps({'format':'ui-contract-component-draft','id':'audit:Missing','domains':{'interface':'missing.json','visual':{'tokens':'missing-tokens.json','css':'missing.css'},'behavior':'missing.scxml','accessibility':{'html':'missing.html'}}}))
 p=subprocess.run(['python3',str(R/'skills/ui-contracts/scripts/contracts.py'),'inspect','--repo',str(R),'--candidate',str(T),'--output',str(O/'dangling-reference-inspect.json')],capture_output=True,text=True,timeout=60);r=json.loads(p.stdout);assert r['overall']=='BLOCKED' and not any(x['status']=='FAIL' for x in r['artifacts']);print('Counterexamples recorded: false capability changes actual DMN choice; dangling references lack specific diagnostics but remain BLOCKED.')
