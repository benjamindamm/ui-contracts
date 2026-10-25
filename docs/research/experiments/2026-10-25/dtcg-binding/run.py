from pathlib import Path
import json,copy,hashlib,math,re
w=Path(__file__).parent;dump=lambda n,d:(w/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
base=json.loads((w/'tokens.json').read_text());profile=json.loads((w/'profile.json').read_text());out=[]
class Invalid(Exception):pass
def resolve(tree,path,seen=()):
 if path in seen:raise Invalid('alias-cycle')
 node=tree
 for part in path.split('.'):
  if not isinstance(node,dict) or part not in node:raise Invalid('missing-token')
  node=node[part]
 if not isinstance(node,dict) or '$value' not in node:raise Invalid('missing-token')
 value=node['$value'];typ=node.get('$type')
 if typ!='dimension':raise Invalid('dimension-type')
 if isinstance(value,str) and re.fullmatch(r'\{[^{}]+\}',value):return resolve(tree,value[1:-1],(*seen,path))
 if not isinstance(value,dict) or type(value.get('value')) not in [int,float] or not math.isfinite(value['value']):raise Invalid('dimension-value')
 if value.get('unit') not in ['px','rem']:raise Invalid('dimension-unit')
 return {'value':value['value'],'unit':value['unit']}
for c in json.loads((w/'cases.json').read_text()):
 t=copy.deepcopy(base);p=copy.deepcopy(profile);m=c['mutation']
 if m=='chain':t['middle']={'gap':{'$type':'dimension','$value':'{base.gap}'}};t['autocomplete']['gap']['$value']='{middle.gap}'
 elif m=='missing':t['autocomplete']['gap']['$value']='{base.missing}'
 elif m=='cycle':t['base']['gap']['$value']='{autocomplete.gap}'
 elif m=='unitless':t['base']['gap']['$value']=8
 elif m=='unit':t['base']['gap']['$value']['unit']='em'
 elif m=='number':t['base']['gap']['$value']['value']='8'
 elif m=='type':t['base']['gap']['$type']='number'
 elif m=='owner':p['tokenBindings'][0]['owner']='behavior'
 elif m=='target':p['tokenBindings'][0]['targets']=['#popup-c']
 elif m=='rem':
  for token in t['base'].values():token['$value']={'value':token['$value']['value']/16,'unit':'rem'}
 # Explicit source revision renewal for mutated fixtures, except deliberate stale binding.
 serialized=(w/'tokens.json').read_bytes() if m in ['none','owner','target','hash'] else (json.dumps(t,ensure_ascii=False,indent=2)+'\n').encode();p['artifacts']['visual']['sha256']=hashlib.sha256(serialized).hexdigest()
 if m=='hash':p['artifacts']['visual']['sha256']='0'*64
 errors=[];resolved={}
 if hashlib.sha256(serialized).hexdigest()!=p['artifacts']['visual']['sha256']:errors.append('source-integrity')
 for b,original in zip(p['tokenBindings'],profile['tokenBindings']):
  if b['owner']!='visual':errors.append('leading-source')
  if b['targets']!=original['targets']:errors.append('target-binding')
  try:resolved[b['cssVariable']]=resolve(t,b['path'])
  except Invalid as e:errors.append(str(e))
 rules=sorted(set(errors));out.append({**c,'actualRules':rules,'resolved':resolved,'expectationMet':rules==sorted(c['expectedRules']),'additionalProfile':p})
 if m in ['none','rem']:dump('resolved-'+('px' if m=='none' else 'rem')+'.json',resolved)
dump('results.json',{'method':'Own deliberately limited dimension/curly-alias translator and additional binding checks; not a DTCG original or complete validator','cases':out});print(json.dumps([{'id':c['id'],'expectationMet':c['expectationMet'],'actualRules':c['actualRules']} for c in out]));raise SystemExit(0 if all(c['expectationMet'] for c in out) else 1)
