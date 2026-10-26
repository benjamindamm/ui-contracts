"""Fresh, explicitly bound browser-run collection and fail-closed evaluation."""
import argparse,datetime,hashlib,json,mimetypes,secrets,shutil,subprocess,sys,threading,time
from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
T=Path(__file__).resolve().parent;ROOT=T.parents[1];SCRIPTS=T/'browser'
class BrowserStop(Exception):
 def __init__(self,code,detail,status='BLOCKED'):self.code,self.detail,self.status=code,detail,status

def read(p):
 import check
 return check.strict(p.read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,obj):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
def fingerprint():
 names=['check.py','static_engine.py','types.cjs','css.cjs','profile.json','browser_gate.py','browser-profile.json','package-lock.json','requirements.lock.txt','schemas/provenance.json']
 names+=['browser/'+n for n in ['evaluate.py','cases.json','required-checks.json','browser-01.js','browser-02.js','browser-03.js','browser-04.js']]
 files={}
 for name in names:
  if not (T/name).is_file():raise BrowserStop('REQUIRED_BROWSER_CHECKER_MISSING',name)
  files[name]=sha((T/name).read_bytes())
 return {'files':files,'revision':sha(json.dumps(files,sort_keys=True,separators=(',',':')).encode())}
def source_bundle():
 profile=read(T/'browser-profile.json');files={}
 for name,expected in profile['hostFiles'].items():
  src=ROOT/profile['vendorSources'][name] if name in profile['vendorSources']else ROOT/profile['historicalHostRoot']/name
  if not src.is_file():raise BrowserStop('BROWSER_DEPENDENCY_MISSING',str(src))
  data=src.read_bytes()
  if sha(data)!=expected:raise BrowserStop('BROWSER_SOURCE_CHANGED',name)
  files[name]=data
 # Only the capture envelope changes. The source change is explicit and rehashed.
 old=b'const body={name,payload,snapshot:';new=b'const body={runId:manifest.runId,challenge:manifest.challenge,name,payload,snapshot:'
 if files['host.js'].count(old)!=1:raise BrowserStop('COLLECTOR_TRANSFORM_UNSUPPORTED','host.js')
 files['host.js']=files['host.js'].replace(old,new)
 hashes={p:sha(data)for p,data in sorted(files.items())}
 revision=sha(json.dumps(hashes,sort_keys=True,separators=(',',':')).encode())
 return profile,files,hashes,revision

def prepare(package,dest):
 import check
 dest=Path(dest).resolve();package=Path(package).resolve()
 if dest.exists():raise BrowserStop('RUN_DIRECTORY_EXISTS','Use a new run directory; original results are not overwritten.')
 if dest.is_relative_to(package)or dest.is_relative_to(T/'schemas'):raise BrowserStop('UNSAFE_RUN_DIRECTORY',str(dest))
 static=check.run(package,'static')
 if static['overall']!='PASS_LIMITED':raise BrowserStop('STATIC_PREREQUISITE_FAILED',static)
 profile,files,hashes,revision=source_bundle()
 closure=read(package/'resolved.json')
 if closure['revision']!=profile['staticRevision']:raise BrowserStop('PACKAGE_HOST_MAPPING_UNSUPPORTED','Only the exact static baseline is bound to this host. A changed package needs an explicit new mapping and current run.')
 dest.mkdir(parents=True);(dest/'captures').mkdir()
 request={'kind':'current-browser-request','runId':secrets.token_hex(16),'challenge':secrets.token_hex(32),'createdAt':time.time(),'packageRevision':closure['revision'],'packageHashes':static['inputHashes'],'hostRevision':revision,'hostFiles':hashes,'checker':fingerprint(),'profileId':profile['id'],'maxAgeSeconds':profile['maxRunAgeSeconds'],'previousHostRevision':profile['historicalHostRevision']}
 for name,data in files.items():p=dest/'host'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 write(dest/'host/manifest.json',{'kind':'current-bounded-browser-closure','files':hashes,'revision':revision,'runId':request['runId'],'challenge':request['challenge'],'originalRuntime':profile['originalRuntime'],'ownAdapter':True,'productFormatSelected':False})
 write(dest/'request.json',request);write(dest/'static-preflight.json',static)
 # Run the actual original validators again on the *host* inputs, not old results.
 from lxml import etree
 import jsonschema
 xsd=etree.XMLSchema(etree.parse(str(T/'schemas/scxml/scxml.xsd'),etree.XMLParser(resolve_entities=False,no_network=True)))
 cv=jsonschema.Draft7Validator(read(T/'schemas/cem.schema.json'));pre=[]
 for name,data in files.items():
  if name.endswith('.scxml'):
   model=etree.fromstring(data,etree.XMLParser(resolve_entities=False,no_network=True));ok=xsd.validate(model);pre.append({'file':name,'sha256':sha(data),'kind':'original SCXML XSD','accepted':ok,'errors':str(xsd.error_log)})
  elif name.endswith('/interface.json'):
   errors=[e.message for e in cv.iter_errors(json.loads(data))];pre.append({'file':name,'sha256':sha(data),'kind':'original CEM schema','accepted':not errors,'errors':errors})
 if not pre or not all(e['accepted']for e in pre):raise BrowserStop('HOST_ORIGINAL_SCHEMA_FAILED',pre,'FAIL')
 write(dest/'schema-preflight.json',pre)
 shutil.copyfile(SCRIPTS/'cases.json',dest/'cases.json')
 write(dest/'collection.json',{'runId':request['runId'],'requestSha256':sha((dest/'request.json').read_bytes()),'status':'PREPARED','captures':{},'operations':{}})
 return {'runDirectory':str(dest),'runId':request['runId'],'hostRevision':revision,'next':'serve this run, execute its four operation scripts through BrowserOS neo, then finalize'}

def serve(dest):
 dest=Path(dest).resolve();request=read(dest/'request.json');ledger=read(dest/'collection.json');profile,_,_,rev=source_bundle()
 if request['checker']!=fingerprint()or request['hostRevision']!=rev:raise BrowserStop('BROWSER_CHECKER_CHANGED','Prepare a new run.')
 if ledger['status']!='PREPARED':raise BrowserStop('RUN_NOT_PREPARED',ledger['status'])
 mutex=threading.Lock(); ledger['status']='RUNNING';ledger['startedAt']=time.time();write(dest/'collection.json',ledger)
 class Handler(BaseHTTPRequestHandler):
  def log_message(self,fmt,*args):pass
  def do_GET(self):
   name=self.path.split('?')[0].lstrip('/')or'index.html';p=(dest/'host'/name).resolve()
   if not p.is_relative_to(dest/'host')or not p.is_file():self.send_error(404);return
   data=p.read_bytes();self.send_response(200);self.send_header('Content-Type',mimetypes.guess_type(str(p))[0]or'application/octet-stream');self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(data)
  def do_POST(self):
   if self.path not in ['/capture','/operation']:self.send_error(404);return
   try:
    n=int(self.headers.get('Content-Length','0'))
    if n<1 or n>12_000_000:raise ValueError('invalid body length')
    import check
    c=check.strict(self.rfile.read(n).decode())
    if self.path=='/operation':
     name=c['operation'];expected='browser-'+name+'.js'
     if name not in ['01','02','03','04']or c.get('runId')!=request['runId']or c.get('challenge')!=request['challenge']or c.get('scriptSha256')!=sha((SCRIPTS/expected).read_bytes())or c.get('status')not in ['PASS','FAIL']:raise ValueError('invalid operation receipt')
     with mutex:
      if name in ledger['operations']:raise ValueError('duplicate operation')
      ledger['operations'][name]={**c,'receivedAt':time.time()};write(dest/'collection.json',ledger)
     self.send_response(200);self.end_headers();self.wfile.write(b'{}');return
    name=c['name'];required=set(read(SCRIPTS/'required-checks.json'))|{'AX-loading','AX-error','AX-closed','AX-ready'}
    if name not in required or c.get('runId')!=request['runId']or c.get('challenge')!=request['challenge']or c.get('sourceRevision')!=request['hostRevision']:raise ValueError('run challenge/source/name mismatch')
    with mutex:
     if name in ledger['captures']:raise ValueError('duplicate capture; start a fresh run after execution failure')
     write(dest/'captures'/(name+'.json'),c);ledger['captures'][name]={'sha256':sha((dest/'captures'/(name+'.json')).read_bytes()),'receivedAt':time.time()};write(dest/'collection.json',ledger)
   except Exception as e:self.send_error(400,str(e));return
   self.send_response(200);self.end_headers();self.wfile.write(b'{}')
 server=ThreadingHTTPServer(('127.0.0.1',0),Handler);url=f'http://127.0.0.1:{server.server_port}/'
 write(dest/'server.json',{'url':url,'port':server.server_port,'runId':request['runId']})
 for p in SCRIPTS.glob('browser-*.js'):
  part=p.stem[-2:];original=p.read_text().replace('__HOST_URL__',url)
  receipt=json.dumps({'operation':part,'scriptSha256':sha(p.read_bytes())})
  wrapper="""async function recordOperation(status,error){const p=browser.page((await browser.pages.list()).find(x=>x.ownership==='mine'&&x.url===URL).pageId);const result=await p.evaluate(async data=>{const response=await fetch('/operation',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({...data,runId:research.manifest.runId,challenge:research.manifest.challenge})});if(!response.ok)throw Error('operation receipt rejected');return true;},{...RECEIPT,status,error});return result;}
try{const outcome=await(async()=>{ORIGINAL})();await recordOperation('PASS',null);return outcome;}catch(error){await recordOperation('FAIL',String(error));throw error;}"""
  wrapper=wrapper.replace('URL',json.dumps(url)).replace('RECEIPT',receipt).replace('ORIGINAL',original)
  (dest/p.name).write_text(wrapper)
 print(url,flush=True)
 try:server.serve_forever()
 finally:server.server_close()

def finalize(dest):
 dest=Path(dest).resolve();request=read(dest/'request.json');ledger=read(dest/'collection.json');required=set(read(SCRIPTS/'required-checks.json'))|{'AX-loading','AX-error','AX-closed','AX-ready'}
 if set(ledger.get('operations',{}))!={'01','02','03','04'}or not all(v['status']=='PASS'for v in ledger['operations'].values()):raise BrowserStop('BROWSER_EXECUTION_INCOMPLETE_OR_FAILED',ledger.get('operations'))
 if ledger['status']!='RUNNING'or set(ledger['captures'])!=required:raise BrowserStop('BROWSER_CASES_INCOMPLETE',sorted(required-set(ledger['captures'])))
 ledger['status']='SEALED';ledger['sealedAt']=time.time();write(dest/'collection.json',ledger)
 return {'status':'SEALED','runId':request['runId'],'captures':len(ledger['captures'])}

def evaluate(dest,package):
 dest=Path(dest).resolve();package=Path(package).resolve()
 if not (dest/'request.json').is_file():raise BrowserStop('BROWSER_RESULT_MISSING',str(dest))
 request=read(dest/'request.json');ledger=read(dest/'collection.json');profile,files,expectedHashes,revision=source_bundle();now=time.time()
 age=now-request['createdAt']
 if age<0 or age>profile['maxRunAgeSeconds']:raise BrowserStop('BROWSER_RUN_STALE',{'ageSeconds':age,'maxAgeSeconds':profile['maxRunAgeSeconds']})
 if request['checker']!=fingerprint():raise BrowserStop('BROWSER_CHECKER_CHANGED','The current checker or criteria differ from this run.')
 if request['profileId']!=profile['id']or request['hostRevision']!=revision or request['hostFiles']!=expectedHashes:raise BrowserStop('BROWSER_REVISION_MISMATCH','Current prepared host/profile changed.')
 currentPackage={str(p.relative_to(package)):sha(p.read_bytes())for p in package.rglob('*')if p.is_file()}
 if request['packageHashes']!=currentPackage or request['packageRevision']!=profile['staticRevision']:raise BrowserStop('PACKAGE_HOST_MAPPING_UNSUPPORTED','Current static candidate differs from the exact tested mapping.')
 if ledger['runId']!=request['runId']or ledger['requestSha256']!=sha((dest/'request.json').read_bytes()):raise BrowserStop('BROWSER_REQUEST_CHANGED','collection/request mismatch')
 if set(ledger.get('operations',{}))!={'01','02','03','04'}or not all(v['status']=='PASS'for v in ledger['operations'].values()):raise BrowserStop('BROWSER_EXECUTION_INCOMPLETE_OR_FAILED',ledger.get('operations'))
 for part,operation in ledger['operations'].items():
  if operation['runId']!=request['runId']or operation['challenge']!=request['challenge']or operation['scriptSha256']!=sha((SCRIPTS/('browser-'+part+'.js')).read_bytes()):raise BrowserStop('BROWSER_EXECUTION_RECEIPT_CHANGED',part)
  if operation.get('operation')!=part or not ledger['startedAt']<=operation['receivedAt']<=ledger['sealedAt']:raise BrowserStop('BROWSER_EXECUTION_RECEIPT_CHANGED',part)
 if ledger['status']!='SEALED':raise BrowserStop('BROWSER_RUN_INCOMPLETE',ledger['status'])
 if not(request['createdAt']<=ledger['startedAt']<=ledger['sealedAt']<=now):raise BrowserStop('BROWSER_TIME_INVALID','collection time order')
 hostManifest=read(dest/'host/manifest.json')
 if hostManifest['files']!=expectedHashes or hostManifest['revision']!=revision or hostManifest['runId']!=request['runId']or hostManifest['challenge']!=request['challenge']:raise BrowserStop('BROWSER_REVISION_MISMATCH','served manifest')
 for name,expected in expectedHashes.items():
  if sha((dest/'host'/name).read_bytes())!=expected:raise BrowserStop('BROWSER_SOURCE_CHANGED',name)
 if sha((dest/'cases.json').read_bytes())!=sha((SCRIPTS/'cases.json').read_bytes()):raise BrowserStop('BROWSER_CRITERIA_CHANGED','cases')
 contracts=read(SCRIPTS/'required-checks.json');required=set(contracts)|{'AX-loading','AX-error','AX-closed','AX-ready'}
 if set(ledger['captures'])!=required:raise BrowserStop('BROWSER_CASES_INCOMPLETE',sorted(required-set(ledger['captures'])))
 captures={}
 for name,receipt in ledger['captures'].items():
  p=dest/'captures'/(name+'.json')
  if not p.is_file():raise BrowserStop('BROWSER_CAPTURE_MISSING',name)
  if sha(p.read_bytes())!=receipt['sha256']:raise BrowserStop('BROWSER_CAPTURE_CHANGED',name)
  c=read(p)
  if c.get('runId')!=request['runId']or c.get('challenge')!=request['challenge']:raise BrowserStop('BROWSER_RUN_MISMATCH',name)
  if c['name']!=name or c['sourceRevision']!=revision:raise BrowserStop('BROWSER_REVISION_MISMATCH',name)
  if not ledger['startedAt']<=receipt['receivedAt']<=ledger['sealedAt']:raise BrowserStop('BROWSER_TIME_INVALID',name)
  captures[name]=c
 # Do not trust an old schema preflight: original schemas are applied again to current host bytes.
 from lxml import etree
 import jsonschema
 xsd=etree.XMLSchema(etree.parse(str(T/'schemas/scxml/scxml.xsd')));cv=jsonschema.Draft7Validator(read(T/'schemas/cem.schema.json'));pre=read(dest/'schema-preflight.json')
 expectedPre={n for n in files if n.endswith('.scxml')or n.endswith('/interface.json')}
 if {x['file']for x in pre}!=expectedPre or not all(x['accepted']and x['sha256']==expectedHashes[x['file']]for x in pre):raise BrowserStop('HOST_SCHEMA_PREFLIGHT_INVALID','missing/changed host source preflight')
 for name in expectedPre:
  if name.endswith('.scxml'):ok=xsd.validate(etree.fromstring(files[name],etree.XMLParser(resolve_entities=False,no_network=True)))
  else:ok=not list(cv.iter_errors(json.loads(files[name])))
  if not ok:raise BrowserStop('HOST_ORIGINAL_SCHEMA_FAILED',name,'FAIL')
 out=subprocess.run([sys.executable,str(SCRIPTS/'evaluate.py'),str(dest)],capture_output=True,text=True,timeout=20)
 # The evaluator writes only this current run's results, never historical records.
 evaluation=read(dest/'results.json')if(dest/'results.json').is_file()else None
 if out.returncode or not evaluation:raise BrowserStop('BROWSER_EXPECTATION_FAILED',{'stderr':out.stderr[-1500:],'result':evaluation},'FAIL')
 cases=evaluation['cases']
 if [x['id']for x in cases]!=list(contracts):raise BrowserStop('BROWSER_CASES_INCOMPLETE','ordered case IDs')
 for c in cases:
  if sorted(c['checks'])!=contracts[c['id']]or not all(v is True for v in c['checks'].values()):raise BrowserStop('BROWSER_EXPECTATION_FAILED',c,'FAIL')
 # Cross-check decisive raw observations independently of payload success booleans.
 raw={};s3=captures['BR-03']['snapshot'];s4=captures['BR-04']['snapshot'];s6=captures['BR-06']['snapshot'];s20=captures['BR-20']['snapshot']
 raw['actualFocusAndNavigation']=s3['focus']=='A-input'and s3['A']['data']['activeKey']=='A-1'and s3['B']['phase']=='closed'
 raw['actualScroll']=s4['A']['data']['activeKey']=='A-7'and s4['A']['viewport']['scrollTop']>0 and s4['A']['viewport']['clientHeight']==160
 raw['actualPublicEvent']=len(s6['events']['A'])==1 and s6['events']['A'][0]['detail']=={'value':'A-7'}and s6['A']['phase']=='closed'and s6['focus']=='A-input'
 raw['actualFinalLifecycle']=bool(s20['actors'])and all(a['final']for a in s20['actors'])and not s20['errors']
 raw['actualTrustedInputJournal']=any(e['type']=='dom.key'and e.get('isTrusted')is True for e in captures['BR-20']['journal'])
 raw['actualEventRetainedExactlyOnce']=len(s20['events']['A'])==1 and not s20['events']['B']
 if not all(raw.values()):raise BrowserStop('BROWSER_RAW_EXPECTATION_FAILED',raw,'FAIL')
 return {'status':'PASS','profileId':profile['id'],'runId':request['runId'],'ageSeconds':age,'sourceRevision':revision,'packageRevision':request['packageRevision'],'checkerRevision':request['checker']['revision'],'cases':cases,'rawChecks':raw,'captureHashes':{n:v['sha256']for n,v in ledger['captures'].items()},'browserVersion':evaluation['browserVersion'],'freshExecutionEvidence':True,'scope':profile['bindingScope'],'limitations':['Local collection hashes/challenge establish run binding, not independent cryptographic attestation of a hostile operator.','No real IME, screenreader or native platform test.','Only exact pinned static-to-host mapping; no generic generator or all API/theme variants.']}

def main():
 import check
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('action',choices=['prepare','serve','finalize']);ap.add_argument('--run-dir',type=Path,required=True);ap.add_argument('--package',type=Path,default=ROOT/'docs/research/experiments/2026-10-25/ip01-static/reference');a=ap.parse_args()
 try:r=prepare(a.package,a.run_dir)if a.action=='prepare'else finalize(a.run_dir)if a.action=='finalize'else serve(a.run_dir)
 except BrowserStop as e:print(json.dumps({'status':e.status,'code':e.code,'detail':e.detail},ensure_ascii=False));return 2
 if r:print(json.dumps(r,ensure_ascii=False,indent=2))
 return 0
if __name__=='__main__':raise SystemExit(main())
