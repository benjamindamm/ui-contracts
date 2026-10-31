#!/usr/bin/env python3
"""Build a bounded, source-bound browser test host for explicit supported contracts."""
import argparse,hashlib,importlib.util,json,secrets,shutil,sys
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/libraries'))
from manage import library_root,manifest

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require_adapter_layout(root,index):
 # The current finite adapter supports an explicit file/layout convention. Reject
 # redirection instead of silently executing an old file beside the declared source.
 for name in ['Autocomplete','Input','Select','SelectWithSearch']:
  cp=root/index['components'][name];c=json.loads(cp.read_text());d=c['domains'];a=d['accessibility'];a={'html':a} if isinstance(a,str) else a
  if d['interface']!='interface.json' or d['behavior']!='behavior.scxml' or a['html']!='accessibility.html':raise ValueError('Adapter source layout unsupported: '+name)
  if name=='Autocomplete':
   if a.get('rules')!='accessibility.rules.json' or d['visual']['css']!='layout.css' or (cp.parent/d['visual']['tokens']).resolve()!=(root/'tokens.json').resolve():raise ValueError('Autocomplete visual/rules layout unsupported')
   for slot in ['overlay','overlay.scroll']:
    child_path=(cp.parent/c['composition'][slot]['component']).resolve();child=json.loads(child_path.read_text());cd=child['domains'];ca=cd['accessibility'];ca={'html':ca} if isinstance(ca,str) else ca
    if child_path.name!='component.json' or cd['behavior']!='behavior.scxml' or cd['visual']['css']!='layout.css' or ca['html']!='accessibility.html':raise ValueError('Composed adapter source layout unsupported')

def prepare(library,out):
 spec=importlib.util.spec_from_file_location('web_ux',ROOT/'tools/ux/check.py');ux=importlib.util.module_from_spec(spec);spec.loader.exec_module(ux)
 verification=ux.verify(ROOT,library)
 if verification['overall']!='PASS_LIMITED':raise ValueError('Resolve invalid contracts first')
 root=library_root(ROOT,library);index=json.loads((root/'library.json').read_text());require_adapter_layout(root,index);roles={}
 supported={'Autocomplete':'composed-autocomplete/1','Input':'text-input/1','Select':'single-select/1','SelectWithSearch':'separate-search-select/1'}
 for name,profile in supported.items():
  if verification['components'].get(name,{}).get('profile')!=profile or verification['components'][name]['status']!='verified-limited':raise ValueError('Bounded host needs '+name+' '+profile)
  roles[name]=str(Path(index['components'][name]).parent)
 out=out.resolve()
 if out.exists():raise ValueError('Output must be a new directory')
 if out.is_relative_to(root) or out.is_relative_to(ROOT/'docs'):raise ValueError('Keep disposable host outside contracts and research')
 out.mkdir(parents=True)
 # Copy the complete selected library: relative references and assets retain their exact paths.
 shutil.copytree(root,out/'sources')
 for name in ['host.js','controls.mjs','session.mjs','provider.mjs','error-relay.scxml','index.html','cases.json']:
  shutil.copy2(ROOT/'tools/web'/name,out/name)
 shutil.copytree(ROOT/'tools/web/browseros',out/'browseros')
 vendor=out/'vendor';vendor.mkdir()
 for src,dst in [('node_modules/@scion-scxml/scxml/dist/scxml.js','scxml.js'),('node_modules/@babel/polyfill/dist/polyfill.min.js','polyfill.js')]:
  p=ROOT/'tools/openpencil'/src
  shutil.copy2(p,vendor/dst)
 m={'format':'ui-contracts-web-test/1','preparedAt':datetime.now(timezone.utc).isoformat(),'library':library,'revision':manifest(ROOT,library)['revision'],'roles':roles,'challenge':secrets.token_hex(24),'files':{str(p.relative_to(out)):sha(p) for p in sorted(out.rglob('*')) if p.is_file()},'tools':{str(p.relative_to(ROOT)):sha(p) for p in [ROOT/'tools/web/prepare.py',ROOT/'tools/web/serve.py',ROOT/'tools/web/check.py',ROOT/'tools/openpencil/package-lock.json',ROOT/'tools/web/cases.json',ROOT/'tools/web/host.js',ROOT/'tools/web/controls.mjs',ROOT/'tools/web/session.mjs',ROOT/'tools/web/provider.mjs']},'release':False}
 (out/'manifest.json').write_text(json.dumps(m,indent=2)+'\n');(out/'native.json').write_text(json.dumps(verification,indent=2)+'\n')
 return {'overall':'PREPARED','release':False,'output':str(out),'revision':m['revision']}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--library',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 try:print(json.dumps(prepare(a.library,a.out)))
 except Exception as e:print(json.dumps({'overall':'BLOCKED','diagnostic':str(e)}));sys.exit(2)
