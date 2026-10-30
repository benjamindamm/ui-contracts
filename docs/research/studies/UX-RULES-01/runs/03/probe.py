import os,json,hashlib,subprocess,importlib.util
from pathlib import Path
from lxml import etree
HERE=Path(__file__).resolve().parent;STUDY=HERE.parents[1];ROOT=STUDY.parents[3]
RUNTIME=Path(os.environ.get('UX_RULE_RUNTIME','/tmp/ui-contracts-ux-rules-runtime'))
JAVA='/opt/homebrew/opt/openjdk/bin/java';OPA=str(RUNTIME/'opa');CLASSPATH=str(RUNTIME/'classes')+':'+(RUNTIME/'classpath.txt').read_text().strip()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
write=lambda p,v:p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
out=HERE/'results';out.mkdir(exist_ok=False)
frozen={str(p.relative_to(HERE)):sha(p) for p in sorted(HERE.rglob('*')) if p.is_file() and 'results' not in p.parts and p.name!='freeze.json'}
write(HERE/'freeze.json',{'phase':'after exploratory bridge setup; before measurement','files':frozen,'priorRefs':{str(p.relative_to(STUDY)):sha(p) for p in [STUDY/'baseline.json',HERE.parent/'01/fixtures/contexts.json',HERE.parent/'01/fixtures/bindings.json',HERE.parent/'01/probe.py']}})
observations=[];checks=[]
def call(args,context):
 r=subprocess.run(args,input=json.dumps(context),text=True,capture_output=True,timeout=30)
 proc={'args':args,'input':context,'exitCode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
 observations.append(proc);return json.loads(r.stdout) if r.returncode==0 else {'stage':'process-error','error':r.stderr}
def check(id,ok,actual,scope):checks.append({'id':id,'expectationMet':bool(ok),'scope':scope,'actual':actual})
def dmn(file,id,context):return call([JAVA,'-cp',CLASSPATH,'DmnProbe',str(HERE/'fixtures'/file),id],context)
expected={'complete':'candidate','excluded':'unsuitable','missing':'unknown','explicit-null':'unknown','explicit-false':'unsuitable','wrong-type':'invalid-input'}
for case in load(HERE.parent/'01/fixtures/contexts.json'):
 result=dmn('eligibility.dmn','eligibility',case['input']);check('dmn-eligibility-'+case['id'],result.get('stage')=='evaluated' and result.get('value')==expected[case['id']],result,'T01-T04 native XML model evaluation')
for case in load(HERE/'fixtures/normative-contexts.json'):
 result=dmn('normative.dmn','normative',case['input']);check('dmn-normative-'+case['id'],result.get('stage')=='evaluated' and result.get('value')==case['expected'],result,'T05/T06/T08/T11 own policy in native DMN with shared decision')
 rego=call([OPA,'eval','--format=json','--data',str(HERE/'fixtures/shared.rego'),'--data',str(HERE/'fixtures/component.rego'),'--stdin-input','data.uxcomponent.assessment'],case['input'])
 try:value=rego['result'][0]['expressions'][0]['value']
 except (KeyError,IndexError):value=None
 check('rego-normative-'+case['id'],value==case['expected'],rego,'T05/T06/T08/T11 own policy in native shared/component Rego modules')
for policy in ['unique','first','collect']:
 result=dmn('conflict-'+policy+'.dmn','conflict',{'flag':True})
 good=(result.get('stage')=='evaluation-error') if policy=='unique' else result.get('value')==('recommend' if policy=='first' else ['recommend','exclude'])
 check('dmn-hit-'+policy,good,result,'Native hit policy; FIRST is order, not UX strength')
# Bind all original domain targets through our existing own adapter, then evaluate a native DMN model.
spec=importlib.util.spec_from_file_location('priorprobe',HERE.parent/'01/probe.py');prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
refs=load(HERE.parent/'01/fixtures/bindings.json')
for bad in [False,True]:
 selected=[dict(r) for r in refs]
 if bad:selected[0]['revision']='0'*64
 gates=[prior.binding(ref) for ref in selected]
 if all(g=='bound' for g in gates):result=dmn('eligibility.dmn','eligibility',{'existingEntriesOnly':True,'singleSelection':True});check('bound-native-positive',result.get('value')=='candidate',{'gates':gates,'result':result},'T07 own reference gate + native evaluation; not native URI/hash resolver')
 else:check('bound-native-stale-blocks',bad and gates[0]=='wrong-revision',{'gates':gates,'nativeEngineNotCalled':True},'T09 own reference gate')
# Original DMN XSD checks are distinct from engine results.
schema=etree.XMLSchema(etree.parse(str(HERE.parent/'01/schemas/DMN15.xsd'),etree.XMLParser(no_network=True,resolve_entities=False)))
for p in sorted((HERE/'fixtures').glob('*.dmn')):check('schema-'+p.stem,schema.validate(etree.parse(str(p))),str(schema.error_log),'Original DMN XSD; not engine conformance')
# File-level focused loading only; no model/agent forward-test claimed.
needed=[HERE/'fixtures/component.rego',HERE/'fixtures/shared.rego',HERE.parent/'01/fixtures/bindings.json']
measurement={'requestedComponent':'example/Autocomplete','loadedRuleFiles':[str(p.relative_to(STUDY)) for p in needed],'loadedBytes':sum(p.stat().st_size for p in needed),'unrelatedFileExplicitlyExcluded':str((HERE/'fixtures/unrelated.rego').relative_to(STUDY)),'dmnSingleFileBytes':(HERE/'fixtures/normative.dmn').stat().st_size,'notMeasured':['Full agent request context','Token count','Agent understanding','Performance benchmark'],'scope':'T12 file loading and byte sizes only; Rego calls succeed without loading deliberately invalid unrelated file'}
write(out/'focused-loading.json',measurement)
check('focused-lookup-does-not-load-unrelated',all(str(HERE/'fixtures/unrelated.rego') not in row['args'] for row in observations),measurement,'T12 technical loading only')
# Exact JAR bytes, resolved coordinates and bridge are pinned; binaries remain outside repository.
jars=[Path(p) for p in (RUNTIME/'classpath.txt').read_text().strip().split(':')]
write(out/'runtime.json',{'dmnEngine':'org.camunda.bpm.extension.dmn.scala:dmn-engine:1.12.6','java':subprocess.run([JAVA,'-version'],text=True,capture_output=True).stderr,'bridgeSha256':sha(HERE/'DmnProbe.java'),'bridgeClassSha256':sha(RUNTIME/'classes/DmnProbe.class'),'jars':[{'coordinatePath':str(p.relative_to(RUNTIME/'m2')),'sha256':sha(p),'bytes':p.stat().st_size} for p in jars],'opaSha256':sha(Path(OPA)),'runtimeDownloadAndCompilation':'outside Git; Maven classpath resolver, pinned pom and plugin documented in README'})
assert all(sha(HERE/name)==h for name,h in frozen.items())
write(out/'observations.json',observations);write(out/'checks.json',checks)
summary={'overall':'PASS_LIMITED' if all(c['expectationMet'] for c in checks) else 'OBSERVATIONS_WITH_UNMET_EXPECTATIONS','release':False,'checks':len(checks),'expectationsMet':sum(c['expectationMet'] for c in checks),'nativeCalls':len(observations),'frozenInputsUnchanged':True,'notChecked':['Full SBVR execution','ODRL runtime','General UX validity','Agent forward test','Universal DMN conformance','All T01-T12 across every candidate'],'scope':'Native DMN XML and Rego shared policies; own typed UX assumptions, own reference gate and file-level context measurement'}
write(out/'summary.json',summary);print(json.dumps(summary));raise SystemExit(0 if summary['overall']=='PASS_LIMITED' else 1)
