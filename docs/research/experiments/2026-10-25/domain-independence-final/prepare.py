from pathlib import Path
import json,shutil
w=Path(__file__).parent;cases=[]
for candidate in ['Zag','Ark UI','UXSpec','Panda CSS']:
 for revision in ['base','visual-revision']:
  id=candidate.lower().replace(' ','-')+'-'+revision;d=w/'fixtures'/id;d.mkdir(parents=True,exist_ok=True)
  for file in ['interface.json','accessibility.html'] if candidate!='Panda CSS'else ['interface.json','accessibility.html','behavior.scxml']:shutil.copyfile(Path('work/four-domain/fixtures')/file,d/file)
  css=Path('work/four-domain/fixtures/visual.css').read_text().replace('160px','192px'if revision=='visual-revision'else'160px');(d/'visual.css').write_text(css)
  if candidate in ['Zag','Ark UI']:
   # CEM describes the actual SDK input-value contribution only, not its selected-value-array API.
   cem=json.loads((d/'interface.json').read_text());decl=cem['modules'][0]['declarations'][0];decl['name']='ResearchComboboxInput';decl['members']=[{'kind':'field','name':'inputValue','type':{'text':'string'}}];decl['events']=[];(d/'interface.json').write_text(json.dumps(cem,indent=2)+'\n')
   props={'instances':{a:{'id':'research-'+a,'inputValue':'Al','open':True,'ids':{part:f'{part}-{a}'for part in ['root','label','input','control','content']}}for a in ['a','b']}}
   for a,v in props['instances'].items():v['ids']['content']='popup-'+a
   (d/'behavior.json').write_text(json.dumps(props,indent=2)+'\n')
  if candidate=='UXSpec':
   doc={'$schema':'https://raw.githubusercontent.com/johnlindquist/uxspec/20dfae0e7224d952e198afdf4ffed26d6fd67180/schema/uxspec.schema.json','$description':'Independent behavior contribution research fixture','$machine':{'id':'Autocomplete','initial':'closed','states':{'closed':{'on':{'OPEN':'open'}},'open':{'on':{'CLOSE':'closed'}}}},'$events':{'OPEN':{'source':'user'},'CLOSE':{'source':'user'}}};(d/'behavior.json').write_text(json.dumps(doc,indent=2)+'\n')
  if candidate=='Panda CSS':
   spec={'schemaVersion':1,'categories':{'sizes':[0,1]},'paths':['sizes.popup'],'tokens':{'sizes.popup':{'category':'sizes','cssVar':'--popup-max-height'}},'conditions':{},'themes':{},'values':[{'token':'sizes.popup','value':'192px'if revision=='visual-revision'else'160px'}]};(d/'visual.json').write_text(json.dumps(spec,indent=2)+'\n')
  cases.append({'id':id,'candidate':candidate,'revision':revision,'expected':{'accepted':True,'maxHeight':192 if revision=='visual-revision'else 160,'otherDomainsByteIdentical':True,'originalContributionIndependent':True}})
(w/'cases.json').write_text(json.dumps(cases,indent=2)+'\n')
