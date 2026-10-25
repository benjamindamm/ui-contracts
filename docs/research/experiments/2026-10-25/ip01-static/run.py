from pathlib import Path
import json,hashlib,copy,subprocess,math
from lxml import etree,html
import jsonschema
w=Path(__file__).parent;repo=Path.cwd();base={str(p.relative_to(w/'package')):p.read_text() for p in (w/'package').rglob('*') if p.is_file()}
h=lambda b:hashlib.sha256(b.encode()).hexdigest()
ns={'s':'http://www.w3.org/2005/07/scxml'};xsd=etree.XMLSchema(etree.parse(str(repo/'work/scxml-probes/sources/scxml.xsd')));cemValidator=jsonschema.Draft7Validator(json.loads((repo/'work/validation-probes/sources/cem.schema.json').read_text()))
class Failure(Exception):
 def __init__(self,code,detail):self.code=code;self.detail=detail

def fail(code,detail):raise Failure(code,detail)
def load(files,p):return json.loads(files[p])
def pointer(o,p):
 try:
  for token in p.split('/')[1:]:
   token=token.replace('~1','/').replace('~0','~');o=o[int(token)] if isinstance(o,list) else o[token]
  return o
 except (KeyError,IndexError,ValueError,TypeError):fail('TARGET_MISSING',p)
def checkvalue(value,t,path):
 k=t['kind']
 if k=='optional':return checkvalue(value,t['item'],path)
 if k=='string':ok=isinstance(value,str)
 elif k=='boolean':ok=type(value) is bool
 elif k=='number':ok=type(value) in (int,float) and math.isfinite(value)
 elif k=='array':
  if not isinstance(value,list):fail('TYPE_MISMATCH',path)
  for i,v in enumerate(value):checkvalue(v,t['item'],path+'/'+str(i))
  return
 elif k=='record':
  if not isinstance(value,dict) or set(value)-set(t['fields']):fail('TYPE_MISMATCH',path)
  for n,f in t['fields'].items():
   if n not in value:
    if not f['optional']:fail('TYPE_MISMATCH',path+'/'+n)
   else:checkvalue(value[n],f['type'],path+'/'+n)
  return
 else:fail('UNSUPPORTED',path)
 if not ok:fail('TYPE_MISMATCH',path)

def repin(files):
 b=load(files,'bindings.json')
 for s in b['sources']:s['sha256']=h(files[s['path']])
 by={s['id']:s for s in b['sources']}
 for t in b['targets']:t['revision']=by[t['source']]['sha256']
 files['bindings.json']=json.dumps(b,ensure_ascii=False,indent=2)+'\n'
 return {'files':{p:h(v) for p,v in sorted(files.items())},'revision':h(json.dumps({p:h(v) for p,v in sorted(files.items())},sort_keys=True,separators=(',',':')))}

def validate(files,values):
 b=load(files,'bindings.json');original=[];proof['originalChecks']=original;models={};asts={};by={s['id']:s for s in b['sources']}
 for s in b['sources']:
  if h(files[s['path']])!=s['sha256']:fail('SOURCE_MISMATCH',s['id'])
  obj=files[s['path']]
  if s['format']=='cem':
   obj=json.loads(obj);errors=list(cemValidator.iter_errors(obj));original.append({'source':s['id'],'validator':'original CEM schema','accepted':not errors})
   if errors:fail('ORIGINAL_INVALID',{'source':s['id'],'message':errors[0].message})
  elif s['format']=='scxml':
   obj=etree.fromstring(obj.encode());ok=xsd.validate(obj);original.append({'source':s['id'],'validator':'original SCXML XSD','accepted':ok})
   if not ok:fail('ORIGINAL_INVALID',{'source':s['id'],'message':str(xsd.error_log)})
  models[s['id']]=obj
 # Original acceptance is retained independently of any extra binding result.
 proof['originalChecks']=original
 if b['kind']!='research-binding-fixture' or b['version']!='0.1-research':fail('UNSUPPORTED','binding version')
 for s in b['sources']:
  if s['format']=='cem' and s['formatVersion']!='2.1.0':fail('UNSUPPORTED',s['id']+' version')
  if s['format']=='scxml' and s['formatVersion']!='1.0':fail('UNSUPPORTED',s['id']+' version')
  if s['format']=='cem':
   out=subprocess.run(['node',str(w/'types.cjs')],input=json.dumps(models[s['id']]),text=True,capture_output=True);a=json.loads(out.stdout)
   if out.returncode:fail('UNSUPPORTED',a)
   asts[s['id']]=a
 for d in b['definitions']:
  if d['id'].split(':')[0]!=b['namespace']:fail('DEFINITION_MISMATCH',d['id'])
  for sid in d['sources']:
   s=by[sid]
   if s['definition']!=d['id']:fail('DEFINITION_MISMATCH',sid)
   if s['format']=='cem' and models[sid]['modules'][0]['declarations'][0]['name']!=d['id'].split(':')[1]:fail('DEFINITION_MISMATCH',sid)
 resolved={}
 for t in b['targets']:
  s=by[t['source']]
  if t['definition']!=s['definition']:fail('DEFINITION_MISMATCH',t['id'])
  if t['revision']!=s['sha256']:fail('REVISION_MISMATCH',t['id'])
  if t['kind']!='part':fail('UNSUPPORTED',t['kind'])
  obj=pointer(models[t['source']],t['locator'])
  if not isinstance(obj,dict) or 'name' not in obj:fail('TARGET_KIND_MISMATCH',t['id'])
  resolved[t['id']]={**t,'name':obj['name']}
 uses={tuple(u['path']):u['definition'] for u in b['uses']}
 if len(uses)!=len(b['uses']):fail('INSTANCE_MISMATCH','duplicate use')
 for u,d in uses.items():
  if d not in {x['id']for x in b['definitions']}:fail('DEFINITION_MISMATCH',d)
  ancestors=[uses[u[:i]]for i in range(1,len(u)) if u[:i] in uses]
  if d in ancestors:fail('UNSUPPORTED','recursive component expansion')
  if len(u)>1 and u[:-1] not in uses:fail('INSTANCE_MISMATCH','missing parent')
 cssInput={s['path']:files[s['path']]for s in b['sources']if s['format']=='css'}
 out=subprocess.run(['node',str(w/'css.cjs')],input=json.dumps(cssInput),text=True,capture_output=True)
 proof['additionalCssSyntax']=json.loads(out.stdout)
 if out.returncode:fail('UNSUPPORTED','CSS syntax parse failure')
 host=html.fromstring(files[b['host']]);witness=[];visualRelations=[]
 if set(b['requiredRelations'])!={r['id']for r in b['relations']}:fail('BINDING_INCOMPLETE','required relations')
 for r in b['relations']:
  if r['kind']=='host-part':
   t=resolved[r['target']];path=tuple(r['use']);nodes=host.xpath('//*[@id=$id]',id=r['hostId'])
   if not nodes:fail('TARGET_MISSING',r['id'])
   if len(nodes)!=1:fail('TARGET_AMBIGUOUS',r['id'])
   node=nodes[0]
   if path not in uses or uses[path]!=t['definition'] or node.get('data-instance')!='/'.join(path):fail('INSTANCE_MISMATCH',r['id'])
   if node.get('data-part')!=t['name'] or node.get('role')!=r['role']:fail('TARGET_KIND_MISMATCH',r['id'])
   witness.append({'relation':r['id'],'definition':t['definition'],'instance':list(path),'part':t['name'],'hostId':r['hostId']})
  elif r['kind']=='event-type':
   a=asts[r['interfaceSource']];typ=a['events'][r['event']]['payload']['fields']['value']['type'];params=models[r['behaviorSource']].xpath(r['locator'],namespaces=ns)
   if len(params)!=1:fail('TARGET_MISSING',r['id'])
   p=params[0];sourceType=a['members'].get(p.get('expr'))
   if sourceType and sourceType['kind']=='optional' and p.getparent().getparent().get('cond')=="typeof value === 'string'":sourceType=sourceType['item']
   if sourceType!=typ:fail('TYPE_BINDING_CONFLICT',r['id'])
  elif r['kind']=='token-css':visualRelations.append(r)
  else:fail('UNSUPPORTED',r['kind'])
 for root in ['A','B']:
  inp=host.xpath('//*[@id=$id]',id=root+'-input')[0];targets=host.xpath('//*[@id=$id]',id=inp.get('aria-controls'))
  if len(targets)!=1 or targets[0].get('role')!='listbox' or targets[0].get('data-instance')!=root:fail('INSTANCE_MISMATCH','aria-controls '+root)
 # Limited explicit dimension/curly-alias projection, not a full DTCG validator.
 tokens=models['tokens'];tokens=json.loads(tokens) if isinstance(tokens,str) else tokens
 def token(path,seen=()):
  if path in seen:fail('TOKEN_ALIAS_CYCLE',path)
  obj=tokens
  try:
   for part in path.split('.'):obj=obj[part]
  except KeyError:fail('TARGET_MISSING',path)
  v=obj['$value']
  if isinstance(v,str) and v.startswith('{') and v.endswith('}'):return token(v[1:-1],seen+(path,))
  if obj.get('$type')!='dimension' or not isinstance(v,dict) or v.get('unit') not in b['policy']['allowedDimensionUnits']:fail('UNSUPPORTED',path)
  if type(v.get('value')) not in (int,float) or not math.isfinite(v['value']):fail('TYPE_MISMATCH',path)
  return v
 visual={n:token('autocomplete.'+n)for n in ['gap','maxHeight','rowHeight']}
 visualBindings=[]
 for relation in visualRelations:
  value=token(relation['tokenPath']);cssFile=by[relation['cssSource']]['path'];entry=next(x for x in proof['additionalCssSyntax']['cases']if x['file']==cssFile)
  declarations=[d for d in entry['declarations']if d['property']==relation['property']and ('var('+relation['variable']+')') in d['value']]
  if len(declarations)!=1:fail('VISUAL_BINDING_CONFLICT',relation['id'])
  visualBindings.append({'relation':relation['id'],'token':relation['tokenPath'],'value':value,'cssSource':relation['cssSource'],'variable':relation['variable'],'declaration':declarations[0]})
 proof['visualBindings']=visualBindings
 a=asts['autocomplete.interface'];members=models['autocomplete.interface']['modules'][0]['declarations'][0]['members']
 for m in members:
  if 'default' in m:
   try:default=json.loads(m['default'])
   except ValueError:fail('UNSUPPORTED','default expression')
   checkvalue(default,a['members'][m['name']],'default/'+m['name'])
 for n,t in a['members'].items():
  if n not in values:
   if t['kind']!='optional':fail('TYPE_MISMATCH','values/'+n)
  else:checkvalue(values[n],t,'values/'+n)
 keys=[x['key']for x in values['results']]
 if any(not k for k in keys) or len(keys)!=len(set(keys)):fail('DATA_KEY_CONFLICT','results keys')
 proof.update(witnesses=witness,types=a,visual=visual,additionalScope='bounded static resolver/type/default/dimension checks; HTML parsed but no original ARIA validator, DOM runtime, CSS evaluation or AT')
 return 'ACCEPT'

results=[];plan=json.loads((w/'cases.json').read_text())
for c in plan['cases']:
 files=copy.deepcopy(base);b=load(files,'bindings.json');v=load(files,'values.json');ac=load(files,'autocomplete/interface.json');mutation=c['mutation'];proof={}
 if mutation=='valid-values':v={'query':'β','value':'k2','results':[{'key':'k2','label':'Two','disabled':False}],'enabled':False,'limit':0}
 elif mutation=='missing-label':del v['results'][0]['label']
 elif mutation=='omit-optionals':v.pop('value');v['results']=[{'key':'x','label':'X'}]
 elif mutation=='wrong-query-type':v['query']=42
 elif mutation=='null-optional-value':v['value']=None
 elif mutation=='duplicate-keys':v['results'][1]['key']=v['results'][0]['key']
 elif mutation=='nonfinite-number':v['limit']=float('inf')
 elif mutation=='missing-target':b['targets'][0]['locator']='/modules/0/declarations/0/cssParts/99'
 elif mutation=='foreign-instance':b['relations'][0]['hostId']='B-input'
 elif mutation=='wrong-namespace':b['definitions'][0]['id']='other:Autocomplete'
 elif mutation=='unsupported-version':b['sources'][0]['formatVersion']='99.0'
 elif mutation=='event-type-conflict':ac['modules'][0]['declarations'][0]['events'][0]['type']['text']='CustomEvent<{value:number}>'
 elif mutation=='recursive-use':b['uses'].append({'path':['A','overlay','scroll','recursive'],'definition':'reference:Autocomplete'})
 elif mutation=='unsupported-type':ac['modules'][0]['declarations'][0]['members'][0]['type']['text']='string | number'
 elif mutation=='wrong-target-kind':b['relations'][0]['role']='listbox'
 elif mutation=='invalid-original-cem':del ac['modules'][0]['declarations'][0]['kind']
 elif mutation=='invalid-original-scxml':files['autocomplete/behavior.scxml']=files['autocomplete/behavior.scxml'].replace('version="1.0"','version="2.0"')
 elif mutation=='unsupported-token-unit':t=load(files,'visual/tokens.json');t['base']['gap']['$value']['unit']='furlong';files['visual/tokens.json']=json.dumps(t)
 elif mutation=='wrong-default-type':ac['modules'][0]['declarations'][0]['members'][0]['default']='42'
 elif mutation=='token-alias-cycle':t=load(files,'visual/tokens.json');t['base']['gap']['$value']='{autocomplete.gap}';files['visual/tokens.json']=json.dumps(t)
 elif mutation=='missing-visual-token-target':next(r for r in b['relations']if r['kind']=='token-css')['tokenPath']='autocomplete.missing'
 elif mutation=='visual-css-conflict':files['overlay/layout.css']=files['overlay/layout.css'].replace('--gap','--unbound')
 elif mutation=='missing-relation':b['relations'].pop(0)
 elif mutation=='unexpected-record-field':v['results'][0]['unexpected']=True
 files['autocomplete/interface.json']=json.dumps(ac,ensure_ascii=False,indent=2)+'\n';files['bindings.json']=json.dumps(b,ensure_ascii=False,indent=2)+'\n'
 lock=repin(files)
 if mutation=='wrong-source-hash':b=load(files,'bindings.json');b['sources'][0]['sha256']='0'*64;files['bindings.json']=json.dumps(b);lock={'files':{p:h(v)for p,v in sorted(files.items())},'revision':h(json.dumps({p:h(v)for p,v in sorted(files.items())},sort_keys=True,separators=(',',':')))}
 # ST-08 injects a nonfinite API value; no invalid Infinity JSON is written as a source file.
 if mutation!='nonfinite-number':files['values.json']=json.dumps(v,ensure_ascii=False,indent=2)+'\n';lock=repin(files) if mutation!='wrong-source-hash' else lock
 else:proof['apiInput']='limit=positive infinity (in-memory value, not JSON transport)'
 if mutation=='target-revision-mismatch':
  b=load(files,'bindings.json');b['targets'][0]['revision']='0'*64;files['bindings.json']=json.dumps(b,ensure_ascii=False,indent=2)+'\n';lock={'files':{p:h(v)for p,v in sorted(files.items())},'revision':h(json.dumps({p:h(v)for p,v in sorted(files.items())},sort_keys=True,separators=(',',':')))}
 dest=w/'runs'/c['id'];dest.mkdir(parents=True,exist_ok=True)
 if c['id']=='ST-01':
  baseline=copy.deepcopy(files)
  for p,text in files.items():q=w/'reference'/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_text(text)
  (w/'reference'/'resolved.json').write_text(json.dumps(lock,indent=2)+'\n')
 patches={p:text for p,text in files.items()if text!=baseline[p]}
 (dest/'patch.json').write_text(json.dumps(patches,ensure_ascii=False,indent=2)+'\n')
 (dest/'resolved.json').write_text(json.dumps(lock,indent=2)+'\n')
 try:actual=validate(files,v);detail=None
 except Failure as e:actual=e.code;detail=e.detail
 results.append({**c,'actual':actual,'expectationMet':actual==c['expected'],'detail':detail,'revision':lock['revision'],'resolvedRecord':'runs/'+c['id']+'/resolved.json',**proof})
output={'kind':'static-research-reference-package','cases':results,'new_conditions':len(results),'full_runtime_executed':False,'product_format_selected':False};(w/'results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n');print(json.dumps([{k:c.get(k)for k in ['id','expected','actual','expectationMet','detail']}for c in results],ensure_ascii=False));raise SystemExit(0 if all(c['expectationMet']for c in results) else 1)
