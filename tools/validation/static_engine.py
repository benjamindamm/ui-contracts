# Adapted from the preserved IP-01 static research checker. Bounded additional logic, not an original standard validator.
from pathlib import Path
import json,math,subprocess,posixpath
from lxml import etree,html
TOOLS=Path(__file__).resolve().parent
ns={'s':'http://www.w3.org/2005/07/scxml'}
import hashlib
h=lambda text:hashlib.sha256(text.encode()).hexdigest()

def check_envelope(b):
 if b.get('policy')!={'types':'T0-plus-T1-closed-record','allowedRecursiveUses':False,'allowedDimensionUnits':['px','rem'],'extraRecordFields':'reject','runtimeCandidate':'native-idlocation-plus-explicit-error-relay-not-executed-here'}:fail('POLICY_CONFLICT','policy is fixed by checker')
 for key in ['sources','targets','definitions','relations']:
  ids=[x['id']for x in b[key]]
  if len(ids)!=len(set(ids)):fail('DUPLICATE_ID',key)
 for s in b['sources']:
  expected={'cem':('interface','2.1.0'),'scxml':('behavior','1.0'),'html':('accessibility','html-host-fixture'),'css':('visual','pinned-partial-web-css'),'dtcg':('visual','2025.10')}
  if s['format'] not in expected:fail('UNSUPPORTED',s['format'])
  domain,version=expected[s['format']]
  if s['domain']!=domain:fail('OWNERSHIP_CONFLICT',s['id'])
  # DTCG's exact declared fixture label is checked by the caller's pinned profile.
 for rel in b['relations']:
  if rel['kind']=='event-type' and rel.get('field')!='value':fail('UNSUPPORTED','event field')

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


def validate(files,values,proof,xsd,cemValidator,stage):
 stage(2)
 b=load(files,'bindings.json');check_envelope(b);original=[];proof['originalChecks']=original;models={};asts={};by={s['id']:s for s in b['sources']}
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
 stage(3)
 for source in b['sources']:
  if source['format']=='cem':
   obj=models[source['id']]
   if obj.get('schemaVersion')!='2.1.0':fail('UNSUPPORTED','CEM document schemaVersion')
   if len(obj.get('modules',[]))!=1 or len(obj['modules'][0].get('declarations',[]))!=1:fail('UNSUPPORTED','only one module/declaration per pinned CEM source')
   declaration=obj['modules'][0]['declarations'][0]
   for key in ['members','events','cssParts']:
    names=[item['name']for item in declaration.get(key,[])]
    if len(names)!=len(set(names)):fail('DUPLICATE_ID',source['id']+'/'+key)
  if source['format']=='scxml':
   model=models[source['id']];ids=model.xpath('//@id')
   if len(ids)!=len(set(ids)):fail('DUPLICATE_ID',source['id'])
   states=set(model.xpath('//s:state/@id | //s:parallel/@id | //s:final/@id | //s:history/@id',namespaces=ns))
   for transition in model.xpath('//s:transition[@target]',namespaces=ns):
    if any(target not in states for target in transition.get('target').split()):fail('TARGET_MISSING',source['id']+' state target')
   for invoke in model.xpath('//s:invoke',namespaces=ns):
    if invoke.get('srcexpr') or invoke.get('type')!='scxml' or not invoke.get('src'):fail('UNSUPPORTED','dynamic or non-SCXML invoke source')
    target=posixpath.normpath(posixpath.join(posixpath.dirname(source['path']),invoke.get('src')))
    candidates=[x for x in b['sources']if x['path']==target and x['format']=='scxml']
    if len(candidates)!=1:fail('TARGET_MISSING',source['id']+' invoke '+target)
 if b['kind']!='research-binding-fixture' or b['version']!='0.1-research':fail('UNSUPPORTED','binding version')
 for s in b['sources']:
  if s['format']=='cem' and s['formatVersion']!='2.1.0':fail('UNSUPPORTED',s['id']+' version')
  if s['format']=='scxml' and s['formatVersion']!='1.0':fail('UNSUPPORTED',s['id']+' version')
  if s['format']=='cem':
   out=subprocess.run(['node',str(TOOLS/'types.cjs')],input=json.dumps(models[s['id']]),text=True,capture_output=True,timeout=15);a=json.loads(out.stdout)
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
 cssInput={s['path']:files[s['path']]for s in b['sources']if s['format']=='css'}
 out=subprocess.run(['node',str(TOOLS/'css.cjs')],input=json.dumps(cssInput),text=True,capture_output=True,timeout=15)
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
 stage(4)
 for u,d in uses.items():
  if d not in {x['id']for x in b['definitions']}:fail('DEFINITION_MISMATCH',d)
  ancestors=[uses[u[:i]]for i in range(1,len(u)) if u[:i] in uses]
  if d in ancestors:fail('UNSUPPORTED','recursive component expansion')
  if len(u)>1 and u[:-1] not in uses:fail('INSTANCE_MISMATCH','missing parent')
 proof.update(witnesses=witness,types=a,visual=visual,additionalScope='bounded static resolver/type/default/dimension checks; HTML parsed but no original ARIA validator, DOM runtime, CSS evaluation or AT')
 return 'ACCEPT'
