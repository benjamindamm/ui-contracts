from pathlib import Path
import json
w=Path(__file__).parent;capture=json.loads((w/'final-browser-capture.json').read_text());cases=[x['value']for x in capture['cases']];expected=json.loads((w/'cases.json').read_text());assert len(cases)==len(expected)==25
for x,c in zip(cases,expected):assert x['id']==c['id']and x['expected']==c['expected']and x['expectationMet'];assert all(x['observed'].get(k)==v for k,v in c['expected'].items())
rawName=json.loads((w/'raw-name-ax-tree.json').read_text())['nodes'];rawStatus=json.loads((w/'raw-status-ax-tree.json').read_text())['nodes'];exp=json.loads((w/'ax-expectations.json').read_text())['cases'];names={(n.get('role',{}).get('value'),n.get('name',{}).get('value'))for n in rawName if not n.get('ignored')};nameobs={'names':['Search A','Search B','Results A'],'roles':['combobox','listbox'],'actualComboboxNames':[n.get('name',{}).get('value')for n in rawName if not n.get('ignored')and n.get('role',{}).get('value')=='combobox'],'actualListboxNames':[n.get('name',{}).get('value')for n in rawName if not n.get('ignored')and n.get('role',{}).get('value')=='listbox']};namemet=all(x in names for x in [('combobox','Search A'),('combobox','Search B'),('listbox','Results A')]);byid={n['nodeId']:n for n in rawStatus}
def descendants(n):
 out=[]
 for id in n.get('childIds',[]):
  child=byid[id];out.append(child);out+=descendants(child)
 return out
status=[]
for n in rawStatus:
 if not n.get('ignored')and n.get('role',{}).get('value')=='status':
  props={p['name']:p['value'].get('value')for p in n.get('properties',[])};text=''.join(x.get('name',{}).get('value','')for x in descendants(n)if x.get('role',{}).get('value')=='StaticText');status.append({'role':'status','live':props.get('live'),'atomic':props.get('atomic'),'text':text})
statusmet=any(x=={'role':'status','live':'polite','atomic':True,'text':'Selected Alpha A 1'}for x in status)and any(x['text']==''for x in status);ax=[{**exp[0],'observed':nameobs,'expectationMet':namemet},{**exp[1],'observed':{'regions':status},'expectationMet':statusmet}];assert all(c['expectationMet']for c in ax)
(w/'ax-results.json').write_text(json.dumps({'scope':'Actual browser accessibility tree via CDP on own host; SDK compact snapshot omitted static status descendants, raw AX tree verifies live/atomic properties and child StaticText; no screenreader speech or trusted keyboard','cases':ax},indent=2)+'\n')
allcases=cases+ax;out={'scope':'Actual original SCXML4.3.28 with native parent delivery, additional CEM/TypeScript-signature/DOM/CSS/ARIA mapping; native geometry/focus/synthetic keyboard and accessibility tree; no native CSS UX machine, ARIA scroll policy, production component, physical key or AT speech','cases':allcases};(w/'results.json').write_text(json.dumps(out,indent=2)+'\n')
for criterion in dict.fromkeys(c['criterion']for c in allcases):
 partition={'scope':out['scope'],'criterion':criterion,'cases':[c for c in allcases if c['criterion']==criterion]};(w/(criterion.lower()+'-results.json')).write_text(json.dumps(partition,indent=2)+'\n')
print(json.dumps({'conditions':len(allcases),'met':sum(c['expectationMet']for c in allcases),'criteria':{x:sum(c['criterion']==x for c in allcases)for x in dict.fromkeys(c['criterion']for c in allcases)},'actualAXStatusRegions':status},indent=2))
