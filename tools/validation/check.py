#!/usr/bin/env python3
"""Fail-closed bounded IP-01 research checker. Does not modify submitted files."""
import argparse,hashlib,importlib.metadata,json,math,os,platform,shutil,subprocess,sys
from pathlib import Path
from datetime import datetime,timezone
TOOLS=Path(__file__).resolve().parent
ROOT=TOOLS.parents[1]
PHASES={1:'profile-and-required-tools',2:'syntax-and-original-schemas',3:'references-types-units-events-instances',4:'ownership-composition-static',5:'live-behavior-events-focus-scroll-ax',6:'report-and-release'}
def sha(b):return hashlib.sha256(b).hexdigest()
class Stop(Exception):
 def __init__(self,code,detail,status='FAIL'):self.code,self.detail,self.status=code,detail,status

def strict(text):
 def pairs(items):
  d={}
  for k,v in items:
   if k in d:raise Stop('DUPLICATE_JSON_KEY',k)
   d[k]=v
  return d
 def nonfinite(s):raise Stop('NONFINITE_JSON',s)
 return json.loads(text,object_pairs_hook=pairs,parse_constant=nonfinite)

def run(package,scope='web',tool_root=TOOLS,browser_run=None):
 profile=strict((TOOLS/'profile.json').read_text()); result={'kind':'bounded-ip01-validation','reportVersion':'0.2.0','profile':profile['id'],'profileSha256':sha((TOOLS/'profile.json').read_bytes()),'scope':scope,'package':str(package),'createdAt':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'stages':[{'id':i,'name':n,'status':'NOT_RUN','checks':[]}for i,n in PHASES.items()],'warnings':list(profile['limits']),'unverified':['Live lifecycle, events, focus, scrolling and browser AX','Full original DTCG/CSS/HTML/ARIA/APG coverage','Native targets, real IME and screenreader output'],'release':False,'passedScope':[],'checkerHashes':{p.name:sha(p.read_bytes())for p in sorted(TOOLS.iterdir())if p.suffix in ['.py','.cjs'] or p.name in ['package-lock.json','requirements.lock.txt','profile.json']}}
 current=1; active=result['stages'][0]; used=set()
 def enter(n):
  nonlocal current,active
  if n!=current:
   if active['status']=='RUNNING':active['status']='PASS'
   current=n;active=result['stages'][n-1]
  used.add(n);active['status']='RUNNING'
 def check(name,actual,expected=True):
  active['checks'].append({'id':name,'actual':actual,'expected':expected})
  if actual!=expected:raise Stop(name,{'actual':actual,'expected':expected})
 def blocked(code,detail):raise Stop(code,detail,'BLOCKED')
 files={}; proof={}
 try:
  enter(1)
  # Supported dependencies are prerequisites, not optional skip-to-green checks.
  for lib,version in [('lxml','6.0.2'),('jsonschema','4.25.1')]:
   try:v=importlib.metadata.version(lib)
   except importlib.metadata.PackageNotFoundError:blocked('REQUIRED_CHECKER_MISSING',lib)
   if v!=version:blocked('CHECKER_VERSION_MISMATCH',{'checker':lib,'actual':v,'required':version})
   active['checks'].append({'id':'dependency.'+lib,'version':v})
  if not shutil.which('node'):blocked('REQUIRED_CHECKER_MISSING','node')
  probe=subprocess.run(['node','-e',"console.log(JSON.stringify({typescript:require('./node_modules/typescript/package.json').version,css:require('./node_modules/css-tree/package.json').version}))"],cwd=tool_root,capture_output=True,text=True)
  if probe.returncode:blocked('REQUIRED_CHECKER_MISSING','TypeScript/css-tree; run npm ci in tools/validation')
  versions=strict(probe.stdout);check('dependency.node-packages',versions,{'typescript':'5.9.3','css':'3.2.1'})
  provenance=strict((tool_root/'schemas/provenance.json').read_text())
  for e in provenance['files']:
   p=(tool_root/e['file']).resolve()
   if not p.is_relative_to(tool_root.resolve()) or not p.is_file():blocked('REQUIRED_SCHEMA_MISSING',e['file'])
   if sha(p.read_bytes())!=e['sha256']:blocked('SCHEMA_INTEGRITY_MISMATCH',e['file'])
  from lxml import etree
  import jsonschema
  try:
   parser=etree.XMLParser(resolve_entities=False,no_network=True)
   xsd=etree.XMLSchema(etree.parse(str(tool_root/'schemas/scxml/scxml.xsd'),parser))
   cem=strict((tool_root/'schemas/cem.schema.json').read_text());jsonschema.Draft7Validator.check_schema(cem)
   cv=jsonschema.Draft7Validator(cem)
  except Exception as e:blocked('REQUIRED_CHECKER_UNUSABLE',str(e))
  if scope=='web':
   if not (tool_root/'browser_gate.py').is_file():blocked('LIVE_BROWSER_CHECKER_MISSING','Current browser adapter missing.')
   if browser_run is None:blocked('BROWSER_RESULT_MISSING','Prepare and execute a fresh browser run, then pass --browser-run. No historical or automatic latest result is accepted.')
  if scope not in ['static','web']:blocked('UNSUPPORTED_SCOPE',scope)
  package=Path(package).resolve()
  if not package.is_dir():raise Stop('PACKAGE_MISSING',str(package))
  # Only data is read; never execute package-provided code, commands or schemas.
  enter(2)
  for p in sorted(package.rglob('*')):
   if not p.is_file():continue
   if p.is_symlink() or not p.resolve().is_relative_to(package):raise Stop('UNSAFE_PATH',str(p))
   name=p.relative_to(package).as_posix();files[name]=p.read_text(encoding='utf-8')
   if p.suffix=='.json':strict(files[name])
   if p.suffix in ('.xml','.scxml'):
    if '<!DOCTYPE' in files[name] or '<!ENTITY' in files[name]:raise Stop('XML_DTD_UNSUPPORTED',name)
    etree.fromstring(files[name].encode(),parser)
  lock=strict(files['resolved.json']); actual={p:sha(t.encode()) for p,t in files.items() if p!='resolved.json'}
  check('closure.files',actual,lock['files']);check('closure.revision',sha(json.dumps(actual,sort_keys=True,separators=(',',':')).encode()),lock['revision'])
  b=strict(files['bindings.json'])
  for source in b['sources']:
   p=source['path']
   if p not in files:raise Stop('SOURCE_MISSING',p)
  # Freeze the supported scope independently of declarations in the candidate.
  expected_sources=profile['sources']; candidate={s['id']:{k:s[k]for k in ['definition','domain','format','formatVersion','path']}for s in b['sources']}
  check('profile.sources',candidate,expected_sources)
  check('profile.requiredRelations',sorted(b['requiredRelations']),sorted(profile['requiredRelations']))
  check('profile.relations',sorted(x['id']for x in b['relations']),sorted(profile['requiredRelations']))
  check('profile.definitions',sorted(x['id']for x in b['definitions']),sorted(profile['definitionIds']))
  check('profile.targets',sorted(x['id']for x in b['targets']),sorted(profile['targetIds']))
  check('profile.relationKinds',{x['id']:x['kind']for x in b['relations']},profile['relationKinds'])
  check('profile.eventContracts',{x['id']:{k:x[k]for k in ['event','field','interfaceSource','behaviorSource','locator']}for x in b['relations']if x['kind']=='event-type'},profile['eventContracts'])
  import static_engine
  try:static_engine.validate(files,strict(files['values.json']),proof,xsd,cv,enter)
  except static_engine.Failure as e:raise Stop(e.code,e.detail,'BLOCKED' if e.code=='UNSUPPORTED' else 'FAIL')
  # Static lifecycle closure is expressly not dynamic lifecycle execution.
  check('ownership.interface-authority',all(s['domain']=='interface'for s in b['sources']if s['format']=='cem'))
  check('composition.witness-count',len(proof['witnesses']),12)
  active['status']='PASS'
  result['passedScope']=['Pinned IP-01 static fixture: original CEM/SCXML schema subset, closed T0/T1 values, references, instance projection, dimension aliases and token-CSS links, acyclic static composition']
  result['overall']='PASS_LIMITED';result['release']=False
  if scope=='web':
   enter(5)
   import browser_gate
   try:browser=browser_gate.evaluate(browser_run,package)
   except browser_gate.BrowserStop as e:raise Stop(e.code,e.detail,e.status)
   result['browser']=browser;active['checks']=browser['cases'];active['status']='PASS'
   result['release']=True;result['releaseScope']='exact-pinned-bounded-web-reference-only';result['productionRelease']=False
   result['passedScope'].append(browser['scope']);result['unverified'].remove('Live lifecycle, events, focus, scrolling and browser AX')
   result['warnings']=[x for x in result['warnings']if x not in ['No live browser executor in this entrypoint','Live browser evidence is a separate required gate in web scope']]
 except Stop as e:
  active['status']=e.status;active['diagnostic']={'code':e.code,'detail':e.detail};result['overall']=e.status
 except (OSError,ValueError,KeyError,IndexError,TypeError,AttributeError) as e:
  active['status']='FAIL';active['diagnostic']={'code':'MALFORMED_OR_UNSUPPORTED_INPUT','detail':str(e)};result['overall']='FAIL'
 except Exception as e:
  active['status']='BLOCKED';active['diagnostic']={'code':'CHECKER_ERROR','detail':type(e).__name__+': '+str(e)};result['overall']='BLOCKED'
 # Dependent steps never turn green after an error or missing checker.
 for stage in result['stages'][:5]:
  if stage['status']=='NOT_RUN':stage['reason']='outside-static-scope' if stage['id']==5 and result['overall']=='PASS_LIMITED' else 'blocked-by-prerequisite'
 result['stages'][5].update(status='PASS',checks=[{'id':'release','actual':result['release'],'scope':result.get('releaseScope','no-web-release'),'productionRelease':False}])
 result['proof']=proof;result['inputHashes']={p:sha(t.encode())for p,t in sorted(files.items())};return result

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--package',type=Path,default=ROOT/'docs/research/experiments/2026-10-25/ip01-static/reference');ap.add_argument('--scope',choices=['web','static'],default='web');ap.add_argument('--output',type=Path);ap.add_argument('--browser-run',type=Path)
 a=ap.parse_args();report=run(a.package,a.scope,browser_run=a.browser_run);text=json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
 if a.output:
  target=a.output.resolve()
  if target.is_relative_to(a.package.resolve()) or target.is_relative_to(TOOLS/'schemas') or (target.is_relative_to(TOOLS) and not target.is_relative_to(TOOLS/'evidence')) or target.is_relative_to(ROOT/'docs/research/experiments') or target.is_relative_to(ROOT/'examples/autocomplete/reproducibility') or target.is_relative_to(ROOT/'components'):ap.error('output must not overwrite package, checker criteria or historical evidence')
  target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text)
 print(text,end='');return {'PASS_LIMITED':0,'FAIL':1,'BLOCKED':2}[report['overall']]
if __name__=='__main__':sys.exit(main())
