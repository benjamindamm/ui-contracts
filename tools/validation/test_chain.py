"""Countercases in disposable copies; never overwrite historical evidence."""
import copy,hashlib,json,shutil,tempfile
from pathlib import Path
import check
ROOT=check.ROOT;TOOLS=check.TOOLS
BASE=ROOT/'docs/research/experiments/2026-10-25/ip01-static/reference'
def dump(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def load(p):return json.loads(p.read_text())
def repin(p):
 b=load(p/'bindings.json')
 for s in b['sources']:s['sha256']=check.sha((p/s['path']).read_bytes())
 by={s['id']:s for s in b['sources']}
 for t in b['targets']:t['revision']=by[t['source']]['sha256']
 dump(p/'bindings.json',b)
 files={str(f.relative_to(p)):check.sha(f.read_bytes())for f in sorted(p.rglob('*'))if f.is_file() and f.name!='resolved.json'}
 dump(p/'resolved.json',{'files':files,'revision':check.sha(json.dumps(files,sort_keys=True,separators=(',',':')).encode())})
def mutate(p,key):
 b=load(p/'bindings.json');v=load(p/'values.json');ac=load(p/'autocomplete/interface.json');t=load(p/'visual/tokens.json');host=p/'host.html'
 if key=='valid-values':v.update(query='β',value='k2',results=[{'key':'k2','label':'Two','disabled':False}],enabled=False,limit=0)
 elif key=='omit-optionals':v.pop('value');v['results']=[{'key':'x','label':'X'}]
 elif key=='missing-label':del v['results'][0]['label']
 elif key=='wrong-query-type':v['query']=42
 elif key=='null-optional-value':v['value']=None
 elif key=='duplicate-keys':v['results'][1]['key']=v['results'][0]['key']
 elif key=='missing-target':b['targets'][0]['locator']='/modules/0/declarations/0/cssParts/99'
 elif key=='foreign-instance':b['relations'][0]['hostId']='B-input'
 elif key=='wrong-namespace':b['definitions'][0]['id']='other:Autocomplete'
 elif key=='unsupported-version':b['sources'][0]['formatVersion']='99.0'
 elif key=='event-type-conflict':ac['modules'][0]['declarations'][0]['events'][0]['type']['text']='CustomEvent<{value:number}>'
 elif key=='recursive-use':b['uses'].append({'path':['A','overlay','scroll','recursive'],'definition':'reference:Autocomplete'})
 elif key=='unsupported-type':ac['modules'][0]['declarations'][0]['members'][0]['type']['text']='string | number'
 elif key=='wrong-target-kind':b['relations'][0]['role']='listbox'
 elif key=='document-version-mismatch':ac['schemaVersion']='99.0'
 elif key=='invalid-original-cem':del ac['modules'][0]['declarations'][0]['kind']
 elif key=='invalid-original-scxml':f=p/'autocomplete/behavior.scxml';f.write_text(f.read_text().replace('version="1.0"','version="2.0"'))
 elif key=='unsupported-token-unit':t['base']['gap']['$value']['unit']='furlong'
 elif key=='wrong-default-type':ac['modules'][0]['declarations'][0]['members'][0]['default']='42'
 elif key=='token-alias-cycle':t['base']['gap']['$value']='{autocomplete.gap}'
 elif key=='missing-visual-token-target':next(x for x in b['relations']if x['kind']=='token-css')['tokenPath']='autocomplete.missing'
 elif key=='visual-css-conflict':f=p/'overlay/layout.css';f.write_text(f.read_text().replace('--gap','--unbound'))
 elif key=='missing-relation':b['relations'].pop(0)
 elif key=='unexpected-record-field':v['results'][0]['unexpected']=True
 elif key=='weaken-policy':b['policy']['extraRecordFields']='allow'
 elif key=='ownership-conflict':b['sources'][0]['domain']='behavior'
 elif key=='duplicate-target':b['targets'].append(copy.deepcopy(b['targets'][0]))
 elif key=='duplicate-use':b['uses'].append(copy.deepcopy(b['uses'][0]))
 elif key=='missing-parent':b['uses'].append({'path':['C','overlay'],'definition':'reference:Overlay'})
 elif key=='missing-invoke-source':f=p/'autocomplete/behavior.scxml';f.write_text(f.read_text().replace('../overlay/behavior.scxml','../overlay/missing.scxml'))
 elif key=='missing-state-target':f=p/'autocomplete/behavior.scxml';f.write_text(f.read_text().replace('target="closed"','target="unknown"'))
 elif key=='duplicate-state-id':f=p/'autocomplete/behavior.scxml';f.write_text(f.read_text().replace('id="open"','id="closed"'))
 elif key=='duplicate-api-member':ac['modules'][0]['declarations'][0]['members'].append(copy.deepcopy(ac['modules'][0]['declarations'][0]['members'][0]))
 elif key=='runtime-guard-unchecked':f=p/'autocomplete/behavior.scxml';f.write_text(f.read_text().replace('cond="_event.data.owner===owner &amp;&amp; _event.data.epoch===epoch"','cond="true"'))
 elif key=='cross-instance-aria' :host.write_text(host.read_text().replace('aria-controls="A-list"','aria-controls="B-list"'))
 dump(p/'bindings.json',b);dump(p/'values.json',v);dump(p/'autocomplete/interface.json',ac);dump(p/'visual/tokens.json',t);repin(p)
 if key=='target-revision-mismatch':b=load(p/'bindings.json');b['targets'][0]['revision']='0'*64;dump(p/'bindings.json',b)
 elif key=='wrong-source-hash':b=load(p/'bindings.json');b['sources'][0]['sha256']='0'*64;dump(p/'bindings.json',b)
 elif key=='source-tamper':f=p/'autocomplete/layout.css';f.write_text(f.read_text()+'\n/* unpinned */')
 elif key=='duplicate-json-key':(p/'values.json').write_text('{"query":"a","query":"b"}')
 elif key=='nonfinite-json':(p/'values.json').write_text('{"limit":NaN}')
 elif key=='xml-entity':f=p/'autocomplete/behavior.scxml';f.write_text('<!DOCTYPE scxml [<!ENTITY x SYSTEM "file:///not-read">]>'+f.read_text())
 # Keep package lock consistent for deliberately stale *inner* revision/source tests.
 if key in ['target-revision-mismatch','wrong-source-hash']:
  files={str(f.relative_to(p)):check.sha(f.read_bytes())for f in p.rglob('*')if f.is_file() and f.name!='resolved.json'};dump(p/'resolved.json',{'files':files,'revision':check.sha(json.dumps(files,sort_keys=True,separators=(',',':')).encode())})
CASES=[('baseline','PASS_LIMITED',None),('document-version-mismatch','BLOCKED','UNSUPPORTED'),('missing-invoke-source','FAIL','TARGET_MISSING'),('missing-state-target','FAIL','TARGET_MISSING'),('duplicate-state-id','FAIL','ORIGINAL_INVALID'),('duplicate-api-member','FAIL','DUPLICATE_ID'),('runtime-guard-unchecked','PASS_LIMITED',None),('valid-values','PASS_LIMITED',None),('omit-optionals','PASS_LIMITED',None),('missing-label','FAIL','TYPE_MISMATCH'),('wrong-query-type','FAIL','TYPE_MISMATCH'),('null-optional-value','FAIL','TYPE_MISMATCH'),('duplicate-keys','FAIL','DATA_KEY_CONFLICT'),('missing-target','FAIL','TARGET_MISSING'),('foreign-instance','FAIL','INSTANCE_MISMATCH'),('wrong-namespace','FAIL','profile.definitions'),('unsupported-version','FAIL','profile.sources'),('event-type-conflict','FAIL','TYPE_BINDING_CONFLICT'),('recursive-use','BLOCKED','UNSUPPORTED'),('unsupported-type','BLOCKED','UNSUPPORTED'),('wrong-target-kind','FAIL','TARGET_KIND_MISMATCH'),('invalid-original-cem','FAIL','ORIGINAL_INVALID'),('invalid-original-scxml','FAIL','ORIGINAL_INVALID'),('unsupported-token-unit','BLOCKED','UNSUPPORTED'),('wrong-default-type','FAIL','TYPE_MISMATCH'),('token-alias-cycle','FAIL','TOKEN_ALIAS_CYCLE'),('missing-visual-token-target','FAIL','TARGET_MISSING'),('visual-css-conflict','FAIL','VISUAL_BINDING_CONFLICT'),('missing-relation','FAIL','profile.relations'),('unexpected-record-field','FAIL','TYPE_MISMATCH'),('weaken-policy','FAIL','POLICY_CONFLICT'),('ownership-conflict','FAIL','profile.sources'),('duplicate-target','FAIL','profile.targets'),('duplicate-use','FAIL','INSTANCE_MISMATCH'),('missing-parent','FAIL','INSTANCE_MISMATCH'),('cross-instance-aria','FAIL','INSTANCE_MISMATCH'),('target-revision-mismatch','FAIL','REVISION_MISMATCH'),('wrong-source-hash','FAIL','SOURCE_MISMATCH'),('source-tamper','FAIL','closure.files'),('duplicate-json-key','FAIL','DUPLICATE_JSON_KEY'),('nonfinite-json','FAIL','NONFINITE_JSON'),('xml-entity','FAIL','XML_DTD_UNSUPPORTED')]
def main():
 rows=[];baseline_before={str(p):check.sha(p.read_bytes())for p in BASE.rglob('*')if p.is_file()}
 with tempfile.TemporaryDirectory(prefix='ui-contracts-validation-') as temp:
  for key,status,code in CASES:
   p=Path(temp)/key;shutil.copytree(BASE,p)
   if key!='baseline':mutate(p,key)
   result=check.run(p,'static');diag=next((s['diagnostic']['code']for s in result['stages']if 'diagnostic'in s),None)
   stops=[s['id']for s in result['stages']if s['status']in ['FAIL','BLOCKED']];deps=all(s['status']=='NOT_RUN'for s in result['stages'][:5]if stops and s['id']>stops[0])
   ok=result['overall']==status and diag==code and deps and not result['release']
   rows.append({'id':key,'expected':status,'actual':result['overall'],'expectedDiagnostic':code,'diagnostic':diag,'dependentStagesStopped':deps,'expectationMet':ok,'report':result})
   print(key,result['overall'],diag,'OK'if ok else 'UNEXPECTED',flush=True)
  for key in ['web-browser-missing','schema-missing','schema-changed','schema-unusable','npm-checker-missing']:
   tools=Path(temp)/key;tools.mkdir();shutil.copytree(TOOLS/'schemas',tools/'schemas');(tools/'node_modules').symlink_to(TOOLS/'node_modules',target_is_directory=True)
   if key=='schema-missing':(tools/'schemas/scxml/scxml.xsd').unlink()
   elif key=='schema-changed':f=tools/'schemas/cem.schema.json';f.write_text(f.read_text()+' ')
   elif key=='schema-unusable':
    f=tools/'schemas/scxml/scxml.xsd';f.write_text('<x/>');prov=load(tools/'schemas/provenance.json');next(e for e in prov['files']if e['file']=='schemas/scxml/scxml.xsd')['sha256']=check.sha(f.read_bytes());dump(tools/'schemas/provenance.json',prov)
   elif key=='npm-checker-missing':(tools/'node_modules').unlink()
   result=check.run(BASE,'web'if key=='web-browser-missing'else'static',tools);diag=next((s['diagnostic']['code']for s in result['stages']if 'diagnostic'in s),None)
   expected={'web-browser-missing':'LIVE_BROWSER_CHECKER_MISSING','schema-missing':'REQUIRED_SCHEMA_MISSING','schema-changed':'SCHEMA_INTEGRITY_MISMATCH','schema-unusable':'REQUIRED_CHECKER_UNUSABLE','npm-checker-missing':'REQUIRED_CHECKER_MISSING'}[key]
   ok=result['overall']=='BLOCKED'and diag==expected and all(s['status']=='NOT_RUN'for s in result['stages'][1:5])and not result['release'];rows.append({'id':key,'expected':'BLOCKED','actual':result['overall'],'diagnostic':diag,'expectationMet':ok,'report':result});print(key,diag,'OK'if ok else 'UNEXPECTED',flush=True)
 assert baseline_before=={str(p):check.sha(p.read_bytes())for p in BASE.rglob('*')if p.is_file()}
 out={'kind':'checker-countercases','notNewCandidateMatrixEvaluations':True,'cases':rows,'allExpectationsMet':all(c['expectationMet']for c in rows),'historicalFixtureUnchanged':True};dest=TOOLS/'evidence';dest.mkdir(exist_ok=True);dump(dest/'countercases.json',out)
 print('TOTAL',len(rows),'MET',sum(c['expectationMet']for c in rows));return 0 if out['allExpectationsMet']else 1
if __name__=='__main__':raise SystemExit(main())
