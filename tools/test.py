#!/usr/bin/env python3
"""Common bounded test entrypoint. Browser evidence is required unless explicitly unit-only."""
import argparse,importlib.util,json,os,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);p.add_argument('--unit-only',action='store_true');p.add_argument('--browser-run',type=Path);a=p.parse_args()
 if a.out.exists():p.error('Use a new output directory')
 a.out.mkdir(parents=True);env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1';config=ROOT/'.runtime/config.json'
 if config.is_file():
  c=json.loads(config.read_text());env['UX_RULE_RUNTIME']=str(ROOT/'.runtime'/c['dmn']);env['UX_JAVA']=c['java']
 if a.browser_run:env['UI_CONTRACTS_BROWSER_RUN']=str(a.browser_run.resolve())
 py=ROOT/'tools/validation/.venv'/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
 if not py.is_file():p.error('Run python3 tools/setup.py first')
 suites=[]
 for directory,pattern in [('tools/libraries','test_*.py'),('tools/ux','test_*.py'),('tools/fonts','test_*.py'),('tools/design-review','test_*.py'),('tools','test_setup.py'),('tools/research','test_navigation.py')]:
  suites.append((directory+'/'+pattern,[str(py),'-m','unittest','discover','-s',directory,'-p',pattern]))
 suites.append(('static-countercases',[str(py),'tools/validation/run_countercases.py','--output',str(a.out.resolve()/'static-countercases.json')]))
 suites.append(('thin-context',[str(py),'-m','unittest','discover','-s','tools/skill-tests/ui-contracts','-p','test_context.py']))
 suites.append(('handoffs',[str(py),'tools/skill-tests/ui-contracts/test_handoffs.py','--output',str(a.out.resolve()/'handoffs.json')]))
 if a.browser_run:suites.append(('tools/web/test_web.py',[str(py),'-m','unittest','discover','-s','tools/web','-p','test_web.py']))
 else:suites.append(('adapter-source-bindings',[str(py),'-m','unittest','discover','-s','tools/web','-p','test_web.py','-k','AdapterBindingTests']))
 for file in ['tools/charts/test_pie.mjs','tools/openpencil/test_layout.mjs','tools/openpencil/test_themes.mjs']:suites.append((file,['node','--test',file]))
 results=[]
 for i,(name,cmd) in enumerate(suites):
  start=time.monotonic()
  try:
   r=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,text=True,timeout=300);log=r.stdout+r.stderr;status='PASS' if r.returncode==0 else 'FAIL'
   if 'skipped=' in log:status='BLOCKED'
  except subprocess.TimeoutExpired as e:log=str(e);status='BLOCKED'
  file=f'{i+1:02d}.log';(a.out/file).write_text(log);results.append({'suite':name,'status':status,'log':file,'seconds':round(time.monotonic()-start,2)});print(name+': '+status,flush=True)
 if not a.unit_only:
  if not a.browser_run:results.append({'suite':'browser','status':'BLOCKED','reason':'Supply --browser-run with fresh source-bound captures'})
  else:
   s=importlib.util.spec_from_file_location('browser_check',ROOT/'tools/web/check.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);r=m.check(a.browser_run.resolve());(a.out/'browser.json').write_text(json.dumps(r,indent=2));results.append({'suite':'browser','status':r['overall']})
 report={'overall':'PASS_LIMITED' if all(x['status'] in ['PASS','PASS_LIMITED'] for x in results) else 'FAIL' if any(x['status']=='FAIL' for x in results) else 'BLOCKED','release':False,'scope':'explicit-unit-only' if a.unit_only else 'unit-native-DMN-and-current-browser','suites':results,'notChecked':['Production release','Real screenreader output','Other operating systems/browsers']}
 (a.out/'results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'overall':report['overall'],'release':False,'report':str(a.out/'results.json')}));return 0 if report['overall']=='PASS_LIMITED' else 1
if __name__=='__main__':raise SystemExit(main())
