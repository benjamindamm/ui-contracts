from pathlib import Path
import json,hashlib,copy
w=Path(__file__).parent;f=w/'fixtures'
cem={'schemaVersion':'2.1.0','modules':[{'kind':'javascript-module','path':'autocomplete.js','declarations':[{'kind':'class','customElement':True,'name':'Autocomplete','members':[{'kind':'field','name':'value','type':{'text':'string'}}],'events':[{'name':'value-change','type':{'text':'CustomEvent<{value:string}>'}}],'cssParts':[{'name':n} for n in ['input','popup','list','option']]}]}]}
(f/'interface.json').write_text(json.dumps(cem,indent=2)+'\n')
(f/'behavior.scxml').write_text('''<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" name="Autocomplete" datamodel="ecmascript" initial="closed"><datamodel><data id="value" expr="'alpha'"/></datamodel><state id="closed"><transition event="OPEN" target="open"/></state><state id="open"><transition event="CLOSE" target="closed"/><transition event="COMMIT" target="selected"/></state><state id="selected"><onentry><send event="value-change" target="#_parent"><param name="value" expr="value"/></send></onentry><transition target="closed"/></state></scxml>\n''')
css='section { margin-bottom:260px; }\n[role="option"] { height:32px; box-sizing:border-box; }\n'
html='<main>'
instances={}
for name in ['a','b']:
 css+=f'#input-{name} {{anchor-name:--input-{name};}}\n#popup-{name} {{position:absolute;position-anchor:--input-{name};top:anchor(bottom);left:anchor(left);margin-top:8px;max-height:160px;overflow-y:auto;}}\n'
 options=''.join(f'<div id="option-{name}-{i}" role="option" aria-selected="{str(i==0).lower()}">Ergebnis {name.upper()} {i+1}</div>' for i in range(7))
 html+=f'<section><label for="input-{name}">Suche {name.upper()}</label><input id="input-{name}" role="combobox" aria-autocomplete="list" aria-expanded="true" aria-controls="list-{name}" aria-activedescendant="option-{name}-0"><div id="popup-{name}"><div id="list-{name}" role="listbox" aria-label="Ergebnisse {name.upper()}">{options}</div></div></section>'
 instances[name.upper()]={'interfaceDeclaration':'Autocomplete','behaviorDefinition':'Autocomplete','snapshotState':'open','parts':{'input':f'input-{name}','popup':f'popup-{name}','list':f'list-{name}','option':f'option-{name}-0'},'anchorName':f'--input-{name}'}
html+='</main>'
(f/'visual.css').write_text(css);(f/'accessibility.html').write_text(html+'\n')
profile={'status':'Additional experimental research binding, no selected product format','artifacts':{domain:{'file':filename,'sha256':hashlib.sha256((f/filename).read_bytes()).hexdigest()} for domain,filename in [('interface','interface.json'),('behavior','behavior.scxml'),('visual','visual.css'),('accessibility','accessibility.html')]},'instances':instances,'stateView':{'closed':{'expanded':False,'popupVisible':False},'open':{'expanded':True,'popupVisible':True},'selected':{'expanded':False,'popupVisible':False}},'publicEvent':'value-change','ownership':{'publicSignature':'interface','stateAndEmission':'behavior','geometry':'visual','rolesNamesRelations':'accessibility','crossArtifactMapping':'additional-profile'}}
(w/'profile.json').write_text(json.dumps(profile,indent=2)+'\n')
# Each mutation is a separate named static binding condition; expectations are saved before running.
cases=[{'id':'four-control','mutation':None,'expected':[]}]
for id,mutation,rule in [('wrong-source-hash','hash','source-integrity'),('missing-part-name','part-name','declared-part'),('wrong-machine-name','machine-name','behavior-definition'),('missing-state','state','state-reference'),('cross-list','list','same-instance-relation'),('cross-option','option','same-instance-relation'),('cross-anchor','anchor','same-instance-anchor'),('wrong-unit','unit','geometry-unit'),('wrong-event','event','public-event-route'),('wrong-payload','payload','public-payload-type'),('wrong-owner','owner','leading-source'),('duplicate-instance-part','duplicate','unique-instance-part')]:cases.append({'id':id,'mutation':mutation,'expected':[rule]})
(w/'cases.json').write_text(json.dumps(cases,indent=2)+'\n')
print('Prepared four independent original-syntax fixtures and 13 static research binding cases.')
