#!/usr/bin/env python3
import copy,hashlib,json,tempfile,shutil,subprocess,sys,importlib.metadata
from pathlib import Path
import evaluate as adapter
HERE=Path(__file__).resolve().parent;STUDY=HERE.parents[1];ROOT=STUDY.parents[3];C=HERE/'candidate';OUT=HERE/'results'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,v:p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
OUT.mkdir(exist_ok=False)
files=[p for p in HERE.rglob('*') if p.is_file() and not any(x in p.parts for x in ['results','__pycache__']) and p.name!='freeze.json']
frozen={str(p.relative_to(HERE)):sha(p) for p in sorted(files)}
write(HERE/'freeze.json',{'phase':'before measurement; after disclosed exploratory schema/bridge preparation, no blind agent review','files':frozen,'baselineSha256':sha(STUDY/'baseline.json'),'previousRuntimeManifestSha256':sha(STUDY/'runs/03/results/runtime.json')})
profile=load(C/'ux-profile.json');expected=load(HERE/'expected.json')['cases'];rows=[];checks=[]
def check(id,ok,details):checks.append({'id':id,'expectationMet':bool(ok),'details':details})
for case in expected:
 request=load(HERE/case['context']);r=adapter.evaluate(request)
 rows.append({'id':case['id'],'request':request,'result':r})
 check(case['id']+'-outcome',r['overall']==case['expected'],{'expected':case['expected'],'actual':r['overall'],'diagnostic':r.get('diagnostic')})
 check(case['id']+'-native-row-evidence',r.get('nativeCalled') and len(r.get('rules',[]))==3 and all(rule['nativeRowId'] in profile['nativeRows'] and rule['evidence'] for rule in r.get('rules',[])),r.get('rules',[]))
if any(not c['expectationMet'] for c in checks):
 write(OUT/'observations.json',rows);write(OUT/'checks.json',checks);raise SystemExit('Initial context expectations failed; original observations retained.')
base=load(HERE/'contexts/existing-single.json')
exception=load(HERE/'contexts/scoped-exception.json')['exceptions'][0]
negative=[]
def reject(id,request=None,modifiedProfile=None,repo=ROOT):
 r=adapter.evaluate(request or copy.deepcopy(base),profile=modifiedProfile,repo=repo);negative.append({'id':id,'request':request,'modifiedProfile':modifiedProfile,'result':r});check(id,r['overall']=='BLOCKED' and not r['nativeCalled'],r)
request=copy.deepcopy(base);request['library']='other';reject('other-library',request)
request=copy.deepcopy(base);request['componentId']='ui-contracts:Other';reject('other-component',request)
request=copy.deepcopy(base);request['revision']='0'*64;reject('wrong-revision',request)
request=copy.deepcopy(base);request['facts']['requiresNewEntries'].pop('source');reject('missing-fact-provenance',request)
request=copy.deepcopy(base);request['facts']['unknownFact']={'value':True,'source':{'kind':'scenario-fixture','reference':'negative'}};reject('unknown-fact',request)
request=copy.deepcopy(base);request['exceptions']=[{**exception,'ruleId':'AC-UX-001'}];reject('exception-cannot-change-capability',request)
request=copy.deepcopy(base);request['exceptions']=[{**exception,'componentId':'ui-contracts:Other'}];reject('exception-wrong-component',request)
request=copy.deepcopy(base);request['exceptions']=[{**exception,'reviewer':'unlisted'}];reject('exception-unlisted-reviewer',request)
request=copy.deepcopy(base);request['exceptions']=[{**exception,'rationale':''}];reject('exception-without-rationale',request)
request=copy.deepcopy(base);request['exceptions']=[exception,exception];reject('duplicate-exception',request)
changed=copy.deepcopy(profile);changed['rules'][0]['strength']='recommendation';reject('strength-logic-mismatch',modifiedProfile=changed)
changed=copy.deepcopy(profile);changed['logic']['sha256']='0'*64;reject('changed-model',modifiedProfile=changed)
changed=copy.deepcopy(profile);changed['rules'][1]=copy.deepcopy(changed['rules'][0]);reject('duplicate-rule-id',modifiedProfile=changed)
changed=copy.deepcopy(profile);changed['nativeRows'].pop(next(iter(changed['nativeRows'])));reject('incomplete-row-map',modifiedProfile=changed)
for name in ['missing-anchor','wrong-anchor-type']:
 changed=copy.deepcopy(profile);changed['sources']={'file':'negative/'+name+'.json','sha256':sha(C/'negative'/f'{name}.json')};reject(name,modifiedProfile=changed)
with tempfile.TemporaryDirectory() as tmp:
 repo=Path(tmp);lib=repo/'libraries/example';lib.parent.mkdir(parents=True);shutil.copytree(ROOT/'libraries/example',lib);f=lib/'tokens.json';f.write_bytes(f.read_bytes()+b' ');reject('mutated-definition-copy',repo=repo)
byId={r['id']:r['result'] for r in rows}
check('missing-and-null-diagnostics-remain-distinct',any(d['state']=='missing' and d['fact']=='requiresNewEntries' for d in byId['missing-creation']['factDiagnostics']) and any(d['state']=='explicit-null' and d['fact']=='requiresNewEntries' for d in byId['null-creation']['factDiagnostics']),{'missing':byId['missing-creation']['factDiagnostics'],'null':byId['null-creation']['factDiagnostics']})
check('recommendation-does-not-override-exclusion',byId['create-new']['overall']=='incompatible' and byId['create-new']['decision']['labels']=='satisfied',byId['create-new']['decision'])
check('approved-recommendation-has-native-excepted-row',any(r['nativeRowId']=='AC-UX-003_excepted' for r in byId['scoped-exception']['rules']),byId['scoped-exception']['rules'])
check('no-production-release',all(r['result']['release'] is False for r in rows+negative),True)
write(OUT/'observations.json',rows);write(OUT/'negative-observations.json',negative);write(OUT/'checks.json',checks)
assert all(sha(HERE/name)==h for name,h in frozen.items())
baseManifest=load(STUDY/'baseline.json')['definition'];assert all(sha(ROOT/baseManifest['root']/name)==h for name,h in baseManifest['files'].items())
runtime=Path('/tmp/ui-contracts-ux-rules-runtime')
write(OUT/'runtime.json',{'python':sys.version,'packages':{name:importlib.metadata.version(name) for name in ['jsonschema','lxml']},'javaVersion':subprocess.run(['/opt/homebrew/opt/openjdk/bin/java','-version'],text=True,capture_output=True).stderr,'classSha256':sha(runtime/'classes-ux/UxAuditProbe.class'),'classSourceSha256':sha(HERE/'UxAuditProbe.java'),'inheritedJarManifest':{'path':'../../runs/03/results/runtime.json','sha256':sha(STUDY/'runs/03/results/runtime.json')},'factTruthOrExceptionAuthorityVerified':False})
summary={'overall':'PASS_LIMITED' if all(c['expectationMet'] for c in checks) else 'OBSERVATIONS_WITH_UNMET_EXPECTATIONS','release':False,'checks':len(checks),'expectationsMet':sum(c['expectationMet'] for c in checks),'positiveAndSemanticContexts':len(rows),'bindingAndMetadataCountercases':len(negative),'nativeEvaluations':sum(r['result']['nativeCalled'] for r in rows+negative),'candidateInputsUnchanged':True,'originalLibraryFilesVerified':len(baseManifest['files']),'matchedTableTrace':'Native engine row IDs mapped to bound rule/evidence metadata; not synthesized by evaluating conditions a second time','notChecked':['User research proving fact values','Authenticity of declared reviewer identity','Agent forward-test','Production rule adoption','General framework conformance']}
write(OUT/'summary.json',summary);print(json.dumps(summary));raise SystemExit(0 if summary['overall']=='PASS_LIMITED' else 1)
