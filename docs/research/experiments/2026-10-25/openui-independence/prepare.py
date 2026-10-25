from pathlib import Path
import json,shutil,hashlib
w=Path(__file__).parent;x=json.loads(Path('work/final-x06-scope/fourth-captures.json').read_text());source=next(a['text']['value']for a in x['value']if a['key']=='openui-types');(w/'original-Spec.ts').write_text(source)
for id,description in [('base','Public input value'),('interface-revision','Public committed value; original type unchanged')]:
 d=w/'fixtures'/id;d.mkdir(parents=True,exist_ok=True)
 for file in ['behavior.scxml','visual.css','accessibility.html']:shutil.copyfile(Path('work/four-domain/fixtures')/file,d/file)
 spec={'name':'ResearchInput','version':'0.0.0-research','description':'Own common-subset fixture for original OpenUI Spec type, not canonical format choice','license':'UNLICENSED','components':{'Input':{'description':'Input contribution','group':'research','props':{'value':{'type':'string','default':'alpha','description':description}}}}};(d/'interface.json').write_text(json.dumps(spec,indent=2)+'\n');(d/'typed.ts').write_text('import type {Spec} from "../../original-Spec";\nconst value:Spec='+json.dumps(spec)+';\n')
(w/'cases.json').write_text(json.dumps([{'id':i,'expected':{'accepted':True,'typedAccepted':True,'type':'string','initialValue':'alpha','otherDomainsByteIdentical':True}}for i in ['base','interface-revision']],indent=2)+'\n')
