from pathlib import Path
import json,re,subprocess,hashlib,importlib.util
R=Path('/Users/kcnpxcp/Dev/GitHub/ui-contracts');O=Path('/tmp/ui-contracts-framework-audit-20261031');tracked=subprocess.check_output(['git','ls-files','-z'],cwd=R).decode().split('\0');paths=[R/p for p in tracked if p]
active=[]
for p in paths:
 rel=str(p.relative_to(R))
 if p.suffix=='.md' and (rel in ['README.md','AGENTS.md','CLAUDE.md','GEMINI.md','TASKS.md'] or rel.startswith(('skills/','libraries/','docs/skills/','docs/ux/','docs/fonts/','docs/libraries/')) and '/frozen/' not in rel or rel.startswith('tools/') and p.name in ['README.md','PREVIEW.md']):active.append(p)
missing=[];links=0
for p in active:
 for u in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  u=u.split('#')[0].strip('<>')
  if not u or '://' in u or u.startswith('mailto:'):continue
  links+=1
  if not(p.parent/u).exists():missing.append({'file':str(p.relative_to(R)),'target':u})
manifest=json.loads((R/'libraries/example/library.json').read_text());components=[]
for name,rel in manifest['components'].items():
 p=R/'libraries/example'/rel;d=json.loads(p.read_text());ux=p.parent/'ux.json';components.append({'name':name,'path':rel,'id':d['id'],'version':d.get('version'),'uxProfile':ux.exists(),'stories':d.get('stories'),'status':d.get('status')})
spec=importlib.util.spec_from_file_location('handoffs_audit',R/'skills/ui-contracts/scripts/handoffs.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);task=R/'docs/research/studies/UX-RULES-01/studies/SELECTION-02/tasks/a.json'
try:m.validate_task(R,json.loads(task.read_text()));taskOutcome='accepted'
except m.Invalid as e:taskOutcome=str(e)
report={'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),'trackedFiles':len(paths),'activeMarkdownChecked':len(active),'activeLocalLinksChecked':links,'missingLocalTargets':missing,'registeredLibraryComponents':components,'rootFrameworkLicenseExists':(R/'LICENSE').exists() or (R/'LICENSE.md').exists(),'ciWorkflowFiles':[str(p.relative_to(R)) for p in paths if '.github/workflows/' in str(p)],'selection02SharedTaskValidatorResult':taskOutcome,'contextEntrypointBytes':{n:(R/n).stat().st_size for n in ['AGENTS.md','CLAUDE.md','GEMINI.md']}}
(O/'inventory.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
