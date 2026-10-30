#!/usr/bin/env python3
"""Bounded engine observations. Own mappings/binding checks are explicitly separate."""
import json,hashlib,subprocess,sys,os,tempfile,copy,platform
from pathlib import Path
from lxml import etree,html
from rdflib import Graph,Namespace,Literal,RDF,URIRef
from pyshacl import validate
import importlib.metadata
HERE=Path(__file__).resolve().parent;STUDY=HERE.parents[1];ROOT=STUDY.parents[3]
# ROOT is repository root: docs/research/studies/UX-RULES-01 -> parents[3].
OPA=os.environ.get('OPA','/tmp/ui-contracts-ux-rules-runtime/opa')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,v:Path(p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def command(args,input=None):
 r=subprocess.run(args,input=input,text=True,capture_output=True,timeout=40)
 return {'args':args,'exitCode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}

def binding(ref,repo=ROOT):
 """Own adapter, NOT any evaluated framework's native reference resolver."""
 if ref['library']!='example':return 'wrong-library'
 baseline=load(STUDY/'baseline.json')['definition'];lib=repo/baseline['root']
 if ref['revision']!=baseline['revision']:return 'wrong-revision'
 index=load(lib/'library.json');cp=lib/index['components']['Autocomplete']
 if load(cp)['id']!=ref['component']:return 'wrong-component'
 for rel,expected in baseline['files'].items():
  if not(lib/rel).is_file() or sha(lib/rel)!=expected:return 'stale-source'
 rel=Path(ref['path'])
 if rel.is_absolute() or '..' in rel.parts:return 'unsafe-path'
 p=(lib/rel).resolve()
 if not p.is_relative_to(lib.resolve()) or ref['path'] not in baseline['files']:return 'unbound-source'
 if ref['kind']=='json-pointer':
  value=load(p)
  try:
   for part in ref['anchor'].split('/')[1:]:
    key=part.replace('~1','/').replace('~0','~');value=value[int(key)] if isinstance(value,list) else value[key]
  except (KeyError,IndexError,TypeError,ValueError):return 'missing-anchor'
  if not isinstance(value,str) or value!=ref['expected']:return 'wrong-anchor-value'
 elif ref['kind']=='scxml-state':
  tree=etree.parse(str(p),etree.XMLParser(resolve_entities=False,no_network=True))
  found=tree.xpath('//*[local-name()="state" and @id=$id]',id=ref['anchor'])
  if len(found)!=1:return 'missing-anchor'
 elif ref['kind']=='html-part':
  tree=html.fromstring(p.read_text());found=tree.xpath('//*[@data-part=$part]',part=ref['anchor'])
  if len(found)!=1 or found[0].get('role')!=ref['expected']:return 'wrong-anchor-type'
 else:return 'unsupported-anchor-kind'
 return 'bound'

def main():
 out=HERE/'results';out.mkdir(exist_ok=False)
 # Freeze hashes before the formal measurement block. Prior exploratory diagnostics remain disclosed.
 frozen={str(p.relative_to(HERE)):sha(p) for p in sorted(HERE.rglob('*')) if p.is_file() and not any(x in p.parts for x in ['node_modules','.venv','results','__pycache__']) and p.name!='freeze.json'}
 freeze={'phase':'after disclosed exploratory preparation, before measurement block; not a blind preregistration','files':frozen,'studyCasesSha256':sha(STUDY/'cases.json'),'baselineSha256':sha(STUDY/'baseline.json')};write(HERE/'freeze.json',freeze)
 ctx=load(HERE/'fixtures/contexts.json');checks=[]
 def check(id,ok,scope,actual):checks.append({'id':id,'expectationMet':bool(ok),'scope':scope,'actual':actual})
 feel=command(['node',str(HERE/'probe_feel.mjs')]);write(out/'feel-process.json',feel)
 if feel['exitCode']!=0:raise RuntimeError(feel['stderr'])
 feeldata=json.loads(feel['stdout']);write(out/'feel.json',feeldata)
 expected={'complete':'candidate','excluded':'unsuitable','missing':'unknown','explicit-null':'unknown','explicit-false':'unsuitable','wrong-type':'invalid-input'}
 for id,value in expected.items():
  row=next(r for r in feeldata['calls'] if r['id']==id and r.get('kind')=='typed-policy');check('feel-typed-'+id,row.get('value')==value,'T01-T04 / FEEL with own explicit typed policy',row)
 raw={r['id']:r for r in feeldata['calls'] if r.get('kind')=='raw-predicate'}
 check('feel-missing-has-warning',raw['missing']['value'] is None and bool(raw['missing']['warnings']),'native diagnostic',raw['missing'])
 check('feel-null-no-missing-warning',raw['explicit-null']['value'] is None and not raw['explicit-null']['warnings'],'native diagnostic',raw['explicit-null'])
 check('feel-invalid-syntax',bool(feeldata['calls'][-1].get('error')),'negative parser test',feeldata['calls'][-1])
 opa=[]
 for c in ctx:
  proc=command([OPA,'eval','--format=json','--data',str(HERE/'fixtures/policy.rego'),'--stdin-input','data.uxprobe'],json.dumps(c['input']))
  value=json.loads(proc['stdout'])['result'][0]['expressions'][0]['value'] if proc['exitCode']==0 else None
  opa.append({'id':c['id'],'input':c['input'],'process':proc,'value':value})
  # Original untyped policy deliberately treats all non-booleans as unknown, not invalid-input.
  expect=expected[c['id']] if c['id']!='wrong-type' else 'unknown'
  check('rego-'+c['id'],value is not None and value['decision']==expect,'T01-T04 / own policy in native Rego',value)
  if c['id']=='complete':check('rego-conflicting-conclusions',set(value['conclusions'])=={'recommend','exclude'},'T06 partial: native set retains both; conflict resolution not implemented',value['conclusions'])
  if c['id']=='missing':check('rego-undefined-is-absent', 'candidate' not in value,'native undefined observation',value)
 write(out/'rego.json',opa)
 shacl=[];EX=Namespace('urn:uxprobe:');SH=Namespace('http://www.w3.org/ns/shacl#')
 for c in ctx:
  graph=Graph()
  for key,v in c['input'].items():graph.add((EX.context,EX[key],URIRef('urn:uxprobe:explicit-null') if v is None else Literal(v)))
  conforms,report,text=validate(graph,shacl_graph=str(HERE/'fixtures/shapes.ttl'),inference='none',advanced=False)
  entries=[{'severity':str(report.value(n,SH.resultSeverity)),'path':str(report.value(n,SH.resultPath)),'constraint':str(report.value(n,SH.sourceConstraintComponent))} for n in report.subjects(RDF.type,SH.ValidationResult)]
  shacl.append({'id':c['id'],'conforms':conforms,'reports':entries,'text':text,'projection':'own JSON facts -> RDF; explicit null represented by a dedicated IRI'})
  graph.serialize(destination=str(out/('shacl-'+c['id']+'.ttl')),format='turtle')
  check('shacl-'+c['id'],conforms==(c['id']=='complete'),'native validation; not UX eligibility or unknown classification',{'conforms':conforms,'reports':entries})
 for allow in [False,True]:
  conforms,report,text=validate(Graph(),shacl_graph=str(HERE/'fixtures/warning.ttl'),allow_warnings=allow,inference='none')
  shacl.append({'id':'warning-allow-'+str(allow),'conforms':conforms,'text':text,'allow_warnings':allow})
  check('shacl-warning-'+str(allow),conforms==allow,'pySHACL implementation option; distinct from normative rule strength',conforms)
 write(out/'shacl.json',shacl)
 class Local(etree.Resolver):
  def resolve(self,url,pubid,context):
   if url.endswith('/XMI.xsd'):return self.resolve_filename(str(HERE/'schemas/XMI.xsd'),context)
 parser=etree.XMLParser(no_network=True,resolve_entities=False);parser.resolvers.add(Local());schemas=[]
 try:
  schema=etree.XMLSchema(etree.parse(str(HERE/'schemas/DMN15.xsd'),parser));tree=etree.parse(str(HERE/'fixtures/eligibility.dmn'),parser);ok=schema.validate(tree)
  schemas.append({'candidate':'DMN','originalSchemaAccepts':ok,'errors':str(schema.error_log),'scope':'XML only; FEEL interpreter separate, no complete DMN engine'})
  check('dmn-original-schema',ok,'XML schema',str(schema.error_log))
  tree.getroot().set('unexpectedAttribute','x');check('dmn-rejects-invalid-attribute',not schema.validate(tree),'negative schema countercase',str(schema.error_log))
 except Exception as e:schemas.append({'candidate':'DMN','blocked':str(e)})
 try:
  schema=etree.XMLSchema(etree.parse(str(HERE/'schemas/SBVR.xsd'),parser));schemas.append({'candidate':'SBVR','originalSchemaCompiled':True,'scope':'Schema compilation only; no SBVR semantic evaluator selected'})
  check('sbvr-original-schema-compiles',True,'schema availability only, no native rule execution',True)
 except Exception as e:schemas.append({'candidate':'SBVR','blocked':str(e)})
 write(out/'schemas.json',schemas)
 refs=load(HERE/'fixtures/bindings.json');bindings=[]
 for ref in refs:
  observed=binding(ref);bindings.append({'input':ref,'observed':observed});check('binding-'+ref['id'],observed=='bound','T07 / own adapter, not native framework capability',observed)
 first=refs[0]
 for label,field,value,want in [('other-library','library','other','wrong-library'),('other-component','component','ui-contracts:Other','wrong-component'),('other-revision','revision','0'*64,'wrong-revision'),('missing-anchor','anchor','/does/not/exist','missing-anchor'),('wrong-type','expected','WrongClass','wrong-anchor-value'),('path-escape','path','../outside.json','unsafe-path')]:
  ref={**first,field:value};result=binding(ref);bindings.append({'id':label,'input':ref,'observed':result});check('binding-'+label,result==want,'T08-T10 / own adapter',result)
 with tempfile.TemporaryDirectory() as tmp:
  repo=Path(tmp);lib=repo/'libraries/example';lib.mkdir(parents=True)
  import shutil
  shutil.copytree(ROOT/'libraries/example',lib,dirs_exist_ok=True)
  p=lib/'tokens.json';p.write_bytes(p.read_bytes()+b' ');observed=binding(first,repo);check('binding-mutated-source',observed=='stale-source','T09 / own hash gate',observed)
 write(out/'bindings.json',bindings)
 write(out/'checks.json',checks)
 env={'python':sys.version,'platform':platform.platform(),'node':command(['node','--version']),'opa':command([OPA,'version']),'opaSha256':sha(OPA),'packages':{n:importlib.metadata.version(n) for n in ['pyshacl','rdflib','lxml']},'pipFreeze':command([sys.executable,'-m','pip','freeze'])}
 write(out/'environment.json',env)
 changed=[name for name,h in frozen.items() if sha(HERE/name)!=h];assert not changed,changed
 summary={'overall':'PASS_LIMITED' if all(r['expectationMet'] for r in checks) else 'OBSERVATIONS_WITH_UNMET_EXPECTATIONS','release':False,'checks':len(checks),'expectationsMet':sum(r['expectationMet'] for r in checks),'schemas':schemas,'coverage':'T01-T04 partial across native engines; T06 partial in Rego; T07-T10 own binding adapter. T05/T11/T12 not yet executed. No full DMN or SBVR semantic runtime.','frozenInputsUnchanged':True,'sourceBinding':'example read-only baseline','notChecked':['UX validity of experimental eligibility assumptions','General semantic conformance','Agent forward testing','Engine licensing audit beyond supplied metadata']}
 write(out/'summary.json',summary);print(json.dumps(summary))
 return 0 if summary['overall']=='PASS_LIMITED' else 1
if __name__=='__main__':raise SystemExit(main())
