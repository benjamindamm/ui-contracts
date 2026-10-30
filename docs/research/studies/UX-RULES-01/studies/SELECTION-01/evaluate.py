"""Focused selection-policy evaluator for the frozen study library; no UI builder or universal resolver."""
import json,hashlib,sys,subprocess
from pathlib import Path
from jsonschema import Draft7Validator
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[5];LIB=ROOT/'libraries/example'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def evaluate(context):
 try:
  manifest=load(HERE/'library-manifest.json');assert manifest['root']=='libraries/example'
  for name,h in manifest['files'].items():assert sha(LIB/name)==h,'stale library: '+name
  policy=load(LIB/'selection-policy.json');schema=load(LIB/'ux-capabilities.schema.json');capabilities={};sources=[]
  index=load(LIB/'library.json')
  for name in policy['candidateComponents']+['Input']:
   cp=LIB/index['components'][name];p=cp.parent/'ux.json';ux=load(p);Draft7Validator(schema).validate(ux);assert ux['componentId']==load(cp)['id']
   for source in ux['sources']:assert sha(cp.parent/source['path'])==source['sha256'],'stale capability claim'
   capabilities[name]=ux['capabilities'];sources.append({'component':name,'profile':str(p.relative_to(ROOT)),'sha256':sha(p)})
  options=context['options'];assert isinstance(options,list) and len({o['key'] for o in options})==len(options);assert all(isinstance(o['key'],str) and o['key'] and isinstance(o['label'],str) and o['label'] for o in options)
  facts=context['facts'];assert all(type(facts[k]) is bool for k in ['fixedValuesRequired','queryEditingAllowed','filteringProviderAvailable'])
  explicit=facts.get('searchExplicitlyRequired');assert explicit is None or type(explicit) is bool
  inputs={**facts,'searchExplicitlyRequired':explicit,'optionCount':len(options),'searchRequiredAbove':policy['parameters']['searchRequiredAbove'],'completionAssistancePreferred':policy['parameters']['completionAssistancePreferred'],'selectCapabilities':capabilities['Select'],'autocompleteCapabilities':capabilities['Autocomplete']}
  runtime=Path('/tmp/ui-contracts-ux-rules-runtime');cp=str(runtime/'classes')+':'+(runtime/'classpath.txt').read_text().strip();args=['/opt/homebrew/opt/openjdk/bin/java','-cp',cp,'DmnProbe',str(LIB/policy['logic']),policy['decision']]
  p=subprocess.run(args,input=json.dumps(inputs),text=True,capture_output=True,timeout=30);assert p.returncode==0,p.stderr;native=json.loads(p.stdout);assert native['stage']=='evaluated',native
  return {'overall':'PASS_LIMITED','release':False,'scope':'bounded selection research policy','libraryRevision':manifest['revision'],'optionCount':len(options),'inputs':inputs,'assessment':native['value'],'capabilitySources':sources,'policySource':{'path':'libraries/example/selection-policy.json','sha256':sha(LIB/'selection-policy.json')},'logicSha256':sha(LIB/policy['logic']),'native':native,'stderr':p.stderr}
 except (AssertionError,KeyError,ValueError,TypeError,OSError) as e:return {'overall':'BLOCKED','release':False,'diagnostic':str(e)}
if __name__=='__main__':
 r=evaluate(load(Path(sys.argv[1])));print(json.dumps(r,ensure_ascii=False,indent=2));raise SystemExit(2 if r['overall']=='BLOCKED' else 0)
