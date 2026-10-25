from pathlib import Path
import json,shutil
w=Path(__file__).parent
for id,color in [('base','#112233'),('visual-revision','#445566')]:
 d=w/'fixtures'/id;d.mkdir(parents=True,exist_ok=True)
 for f in ['interface.json','behavior.scxml','accessibility.html']:shutil.copyfile(Path('work/four-domain/fixtures')/f,d/f)
 (d/'DESIGN.md').write_text('---\nname: Independent visual research\nversion: alpha\ncolors:\n  primary: "'+color+'"\n---\n# Independent visual research\n')
(w/'cases.json').write_text(json.dumps([{'id':i,'expected':{'accepted':True,'color':c,'otherDomainsByteIdentical':True,'originalErrors':0}}for i,c in [('base','#112233'),('visual-revision','#445566')]],indent=2)+'\n')
