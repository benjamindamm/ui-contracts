from pathlib import Path
import json,shutil
w=Path(__file__).parent
for id in ['control','visual-revision','behavior-revision']:
 d=w/'fixtures'/id;d.mkdir(parents=True,exist_ok=True)
 for f in ['foreign-cem.json','research-api.json','research-evidence-api.json','binding.json']:shutil.copyfile(Path('work/uspec-cem-ownership/fixtures/control')/f,d/f)
 for f in ['visual.css','behavior.scxml','accessibility.html']:shutil.copyfile(Path('work/four-domain/fixtures')/f,d/f)
 if id=='visual-revision':p=d/'visual.css';p.write_text(p.read_text().replace('160px','192px'))
 if id=='behavior-revision':p=d/'behavior.scxml';p.write_text(p.read_text().replace("expr=\"'alpha'\"","expr=\"'beta'\""))
(w/'cases.json').write_text(json.dumps([{'id':i,'expected':{'originalApiAccepted':True,'publicValue':v,'height':h,'unchangedOtherDomains':True,'ownApiScopeOnly':True}}for i,v,h in [('control','alpha',160),('visual-revision','alpha',192),('behavior-revision','beta',160)]],indent=2)+'\n')
