from pathlib import Path
import json,copy,hashlib,subprocess,re,collections
from lxml import html
import jsonschema
w=Path(__file__).parent;h=lambda s:hashlib.sha256(s.encode()).hexdigest();base=json.loads((w/'artifacts.json').read_text());profile=json.loads((w/'profile.json').read_text());cases=json.loads((w/'cases.json').read_text());inputs=[]
for c in cases:
 a=copy.deepcopy(base);p=copy.deepcopy(profile);s=a['visual'];m=c['mutation']
 if m=='rename':s=s.replace('--input-a','--research-a')
 if m=='foreign':s=s.replace('position-anchor:--input-a','position-anchor:--input-b')
 if m=='missing':s=s.replace('position-anchor:--input-a','position-anchor:--not-present')
 if m=='duplicate':s=s.replace('anchor-name:--input-b','anchor-name:--input-a')
 if m=='part':s=s.replace('#input-a {anchor-name:','#list-a {anchor-name:')
 if m=='revision':s+='\n'
 if m=='variable':s=s.replace('position-anchor:--input-a','position-anchor:var(--target)')
 if m=='selector':s=s.replace('#input-a {anchor-name:','.input-a {anchor-name:')
 if m=='nested':s=s.replace('#input-a {anchor-name:--input-a;}','@media (min-width:0px){#input-a {anchor-name:--input-a;}}')
 if m=='scope':s+='section {anchor-scope:all;}\n'
 if m=='keyword':s=s.replace('position-anchor:--input-a','position-anchor:auto')
 if m=='reset':s+='#popup-a {position:absolute;}\n'
 if m=='named-function':s=s.replace('top:anchor(bottom)','top:anchor(--input-b bottom)',1)
 a['visual']=s
 if m!='revision':p['artifacts']['visual']['sha256']=h(s)
 inputs.append((c,a,p))
node='/Users/kcnpxcp/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node';parsed=subprocess.run([node,str(w/'parse-css.cjs')],input=json.dumps([a['visual'] for _,a,_ in inputs]),text=True,capture_output=True,check=True);css=json.loads(parsed.stdout)
cem=json.loads(base['interface']);schema=Path('work/validation-probes/sources/cem.schema.json');cem_ok=not list(jsonschema.Draft7Validator(json.loads(schema.read_text())).iter_errors(cem));assert cem_ok
def pointer(obj,loc):
 if not isinstance(loc,str) or not loc.startswith('/'):raise ValueError('locator-kind')
 for s in loc[1:].split('/'):
  s=s.replace('~1','/').replace('~0','~');obj=obj[int(s)] if isinstance(obj,list) else obj[s]
 return obj
out=[]
for (c,a,p),read in zip(inputs,css['results'],strict=True):
 issues=[];witnesses=[]
 if any(h(a[k])!=v['sha256'] for k,v in p['artifacts'].items()):issues.append('source-revision')
 if not issues:issues.extend(read['issues'])
 if not issues:
  dom=html.fromstring(a['accessibility']);rows=read['rows'];anchors=collections.defaultdict(list)
  for row in rows:
   if row['property']=='anchor-name':anchors[row['value']].append(row)
  for instance,b in p['visualBindings'].items():
   use=p['instances'][instance];df=p['definitions'][b['definition']];component=pointer(cem,df['component']['locator']['pointer']);resolved={}
   try:
    for part,selkey in [('input','inputSelector'),('popup','popupSelector')]:
     ref=df['parts'][b[part+'Part']];loc=ref['locator']['pointer'];obj=pointer(cem,loc)
     if ref['kind']!='cem.css-part' or not any(obj is partobj for partobj in component['cssParts']) or obj['name']!=part:raise ValueError('model-part-binding')
     sel=b[selkey]
     if sel!='#'+use['host'][part]:raise ValueError('host-model-binding')
     nodes=dom.xpath('//*[@id=$id]',id=use['host'][part])
     if len(nodes)!=1:raise ValueError('host-unique-target')
     resolved[part]=nodes[0]
    if resolved['input'].getparent() is not resolved['popup'].getparent():raise ValueError('same-instance-host')
    refs=[row for row in rows if row['property']=='position-anchor' and row['hostId']==use['host']['popup']]
    if len(refs)!=1:raise ValueError('nonunique-css-reference')
    ref=refs[0];targets=anchors[ref['value']]
    if not targets:raise ValueError('missing-css-anchor')
    if len(targets)!=1:raise ValueError('nonunique-css-anchor')
    target=targets[0]
    if target['hostId']!=use['host']['input']:raise ValueError('foreign-anchor-part')
    # This records declaration identity, not native eligibility of the target box.
    witnesses.append({'instance':instance,'sourceSha256':h(a['visual']),'componentPointer':df['component']['locator']['pointer'],'inputPartPointer':df['parts']['input']['locator']['pointer'],'popupPartPointer':df['parts']['popup']['locator']['pointer'],'reference':ref,'target':target,'nativeLookupExecuted':False})
   except (ValueError,KeyError,IndexError,TypeError) as e:issues.append(str(e))
 priority=['source-revision','unsupported-nesting','unsupported-scope','unsupported-selector','unsupported-cascade','unsupported-reset','unsupported-named-function','unsupported-value','css-property-syntax','nonunique-css-anchor','foreign-anchor-part','missing-css-anchor']
 status=next((s for s in priority if s in issues),issues[0] if issues else 'bound');out.append({**c,'observed':status,'issues':list(dict.fromkeys(issues)),'expectationMet':status==c['expected'],'sourceSha256':h(a['visual']),'profile':p,'cssObservation':read,'witnesses':witnesses})
result={'scope':'Additional static CSS declaration-to-CEM/host-instance binding, not native anchor lookup/cascade/layout/a11y conformance','cssTree':css['cssTree'],'originalCemSchemaAccepted':cem_ok,'originalCemSchemaSha256':hashlib.sha256(schema.read_bytes()).hexdigest(),'newConditions':len(out),'nativeLookupExecuted':False,'browserExecuted':False,'atTested':False,'cases':out};(w/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'cases':len(out),'met':sum(c['expectationMet'] for c in out),'observed':[(c['id'],c['observed']) for c in out]},ensure_ascii=False));raise SystemExit(0 if all(c['expectationMet'] for c in out) else 1)
