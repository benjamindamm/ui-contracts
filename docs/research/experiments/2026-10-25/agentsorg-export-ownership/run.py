from pathlib import Path
import json,sys,subprocess,os,copy,hashlib,re
from jsonschema import Draft202012Validator
import yaml
w=Path(__file__).resolve().parent;base=json.loads((w/'baseline.design').read_text());schema=Draft202012Validator(json.loads((w/'sources/design.v1.schema.json').read_text()));results=[];h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();env={**os.environ,'PYTHONPATH':str(w/'tool')+os.pathsep+os.environ.get('PYTHONPATH','')}
def cmd(name,args):
 r=subprocess.run([sys.executable,str(w/'sources'/name),*map(str,args)],capture_output=True,text=True,env=env);return{'args':[name,*map(str,args)],'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
for c in json.loads((w/'cases.json').read_text()):
 d=copy.deepcopy(base);kind=c['id'];folder=w/'fixtures'/kind;folder.mkdir(parents=True,exist_ok=True);old=folder/'old.design';new=folder/'new.design';old.write_text(json.dumps(base,indent=2)+'\n')
 if kind in ['token-update-and-diff','informational-diff-default','version-bump-still-regression']:d['tokens']['spacing']['popupHeight']=192
 if kind=='version-bump-still-regression':d['version']='1.1.0'
 if kind=='default-theme-value':d['themes']={'default':'wide','modes':{'wide':{'tokens':{'spacing':{'popupHeight':192}}}}}
 if kind=='shadcn-mismatch':d['integrations']['shadcn']['css_vars']['light']['primary']='#000000'
 if kind=='locked-entry-removed':d['locked']=[]
 new.write_text(json.dumps(d,indent=2)+'\n');errors=[str(e)for e in schema.iter_errors(d)];calls=[];observed={'originalSchemaValid':not errors};assert not errors,errors
 if kind in ['baseline-css','token-update-and-diff','default-theme-value','regenerate-tampered-output']:
  before=h(new);call=cmd('export_design.py',[new,'--only','css','--out-dir',folder/'out']);calls.append(call);assert call['exit']==0,call;text=(folder/'out/tokens.css').read_text();observed['cssValue']=re.search(r'--spacing-popup-height: ([^;]+);',text).group(1);observed['aliasPreserved']='--spacing-popup-max-height: var(--spacing-popup-height);'in text;observed['normativeHeader']='.design file is normative'in text
  if kind=='regenerate-tampered-output':
   originalHash=h(folder/'out/tokens.css');(folder/'out/tokens.css').write_text(text.replace('160px','999px'));calls.append(cmd('export_design.py',[new,'--only','css','--out-dir',folder/'out']));observed['sourceUnchanged']=h(new)==before;observed['originalOutputRestored']=h(folder/'out/tokens.css')==originalHash;observed['cssValue']=re.search(r'--spacing-popup-height: ([^;]+);',(folder/'out/tokens.css').read_text()).group(1)
 if kind=='shadcn-mismatch':
  call=cmd('export_design.py',[new,'--only','shadcn_registry','--out-dir',folder/'out']);calls.append(call);assert call['exit']==0;registry=json.loads((folder/'out/theme.json').read_text());observed.update(registryPrimary=registry['cssVars']['light']['primary'],sourcePrimary=d['tokens']['color']['primary'],declaredMapping=d['integrations']['shadcn']['map_from_tokens']['primary'])
 if kind in ['token-update-and-diff','locked-entry-removed','informational-diff-default','version-bump-still-regression']:
  args=[old,new]+([]if kind=='informational-diff-default'else['--fail-on-regression']);call=cmd('diff_design.py',args);calls.append(call);observed.update(diffExit=call['exit'],regression='regression: YES'in call['stdout']);
  if kind=='version-bump-still-regression':observed['versionReported']='version: 1.0.0 -> 1.1.0'in call['stdout']
 results.append({**c,'observed':observed,'calls':calls,'originalSchemaErrors':errors,'sourceHash':h(new),'expectationMet':all(observed.get(k)==v for k,v in c['expected'].items())})
sourceBefore=w/'fixtures/token-update-and-diff/old.design';sourceAfter=w/'fixtures/token-update-and-diff/new.design';beforeOut=w/'fixtures/baseline-css/out/tokens.css';afterOut=w/'fixtures/token-update-and-diff/out/tokens.css';journal={'kind':'Additional source/export change record, not native signed journal','information':'popupHeight','sourcePointer':'/tokens/spacing/popupHeight','sourceBeforeSha256':h(sourceBefore),'sourceAfterSha256':h(sourceAfter),'sourceValueBefore':160,'sourceValueAfter':192,'derivedProperty':'--spacing-popup-height','derivedBeforeSha256':h(beforeOut),'derivedAfterSha256':h(afterOut),'originalExporterSha256':h(w/'sources/export_design.py'),'originalRevision':'014a1864c641f8e9792ed76de93c95493489dd8c','otherDomainHashes':{n:h(Path('work/four-domain/fixtures')/n)for n in ['interface.json','behavior.scxml','accessibility.html']}};(w/'change-record.json').write_text(json.dumps(journal,indent=2)+'\n')
output={'revision':journal['originalRevision'],'python':sys.version,'pyyaml':yaml.__version__,'scope':'Complete original export_design.py and diff_design.py CLI on own schema-valid fixtures; no Figma sync, locked edit authorization or complete normative validator','cases':results};(w/'results.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n');print(json.dumps([{'id':c['id'],'observed':c['observed'],'met':c['expectationMet']}for c in results]));assert all(c['expectationMet']for c in results)
