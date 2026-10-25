from pathlib import Path
import json
w=Path(__file__).parent
cem={'schemaVersion':'2.1.0','modules':[{'kind':'javascript-module','path':'research-switch.js','declarations':[{'kind':'class','name':'ResearchSwitch','customElement':True,'members':[{'kind':'field','name':'checked','type':{'text':'boolean'}}]}]}]};(w/'interface.json').write_text(json.dumps(cem,indent=2)+'\n')
cases=[('external-boolean-reference','none',True,None),('wrong-target-kind','target',False,'interface-target-kind'),('wrong-interface-type','type',False,'interface-boolean-type'),('stale-interface-revision','stale',False,'stale-interface'),('foreign-owner','owner',False,'owner-scope'),('wrong-original-property-type','graph-type',False,'original-resolver'),('missing-original-property','missing',False,'original-resolver'),('ambiguous-original-property-name','ambiguous',False,'ambiguous-original-name'),('removed-stored-binding','removed',False,'missing-original-binding'),('renamed-original-property','rename',True,None)]
(w/'cases.json').write_text(json.dumps([{'id':id,'mutation':m,'expected':{'accepted':a,'errorClass':e}}for id,m,a,e in cases],indent=2)+'\n')
(w/'schema-expectations.json').write_text(json.dumps([{'id':'cem-valid-boolean-field','type':'boolean','expectedValid':True},{'id':'cem-valid-string-field-needs-extra-binder','type':'string','expectedValid':True}],indent=2)+'\n')
