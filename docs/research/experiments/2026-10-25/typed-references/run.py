from pathlib import Path
import json,copy,hashlib,re,collections
from lxml import etree,html
import jsonschema
w=Path(__file__).parent;root=Path.cwd();base=json.loads((w/'artifacts.json').read_text());originalProfile=json.loads((w/'profile.json').read_text());ns={'s':'http://www.w3.org/2005/07/scxml'};schemaPath=root/'work/scxml-probes/sources/scxml.xsd';cemPath=root/'work/validation-probes/sources/cem.schema.json'
class Resolver(etree.Resolver):
 def resolve(self,url,pubid,context):
  p=schemaPath.parent/url.rsplit('/',1)[-1]
  if p.is_file():return self.resolve_filename(str(p),context)
  raise RuntimeError('Unpinned XSD include '+url)
parser=etree.XMLParser(no_network=True,resolve_entities=False);parser.resolvers.add(Resolver());xsd=etree.XMLSchema(etree.parse(str(schemaPath),parser));cemValidator=jsonschema.Draft7Validator(json.loads(cemPath.read_text()));out=[]
class Invalid(Exception):pass
def pointer(obj,path):
 if not isinstance(path,str) or not path.startswith('/'):raise Invalid('locator-kind')
 try:
  for raw in path[1:].split('/'):
   if re.search(r'~(?![01])',raw):raise Invalid('locator-kind')
   part=raw.replace('~1','/').replace('~0','~');obj=obj[int(part)] if isinstance(obj,list) and re.fullmatch('0|[1-9][0-9]*',part) else obj[part]
  return obj
 except (KeyError,IndexError,TypeError,ValueError):raise Invalid('missing-target')
for c in json.loads((w/'cases.json').read_text()):
 a=copy.deepcopy(base);p=copy.deepcopy(originalProfile);m=c['mutation'];definition=p['definitions']['autocomplete']
 if m in ['duplicate-name','foreign-part']:
  cem=json.loads(a['interface']);clone=copy.deepcopy(cem['modules'][0]);clone['path']='other-autocomplete.js';cem['modules'].append(clone);a['interface']=json.dumps(cem,indent=2)+'\n'
  if m=='foreign-part':definition['parts']['input']['locator']['pointer']='/modules/1/declarations/0/cssParts/0'
 elif m=='foreign-kind':definition['parts']['input']=copy.deepcopy(definition['states']['open'])
 elif m=='missing':definition['parts']['input']['locator']['pointer']='/modules/0/declarations/0/cssParts/999'
 elif m=='wrong-part':definition['parts']['input']['locator']['pointer']='/modules/0/declarations/0/cssParts/2'
 elif m=='ambiguous':definition['states']['open']['locator']['xpath']='./s:state'
 elif m=='data-as-state':definition['states']['open']['locator']['xpath']='./s:datamodel/s:data'
 elif m=='revision':a['behavior']+='\n'
 elif m=='cross-list':a['accessibility']=a['accessibility'].replace('aria-controls="list-a"','aria-controls="list-b"')
 elif m=='role':a['accessibility']=a['accessibility'].replace('id="list-a" role="listbox"','id="list-a" role="button"')
 elif m=='duplicate-id':a['accessibility']=a['accessibility'].replace('</main>','<div id="list-a"></div></main>')
 elif m=='state-view':a['accessibility']=a['accessibility'].replace('aria-expanded="true"','aria-expanded="false"',1)
 elif m=='machine':a['behavior']=a['behavior'].replace('name="Autocomplete"','name="OtherMachine"')
 elif m=='locator':definition['parts']['input']['locator']={'nameSearch':'input'}
 elif m=='definition':p['instances']['A']['uses']='missing-definition'
 # Renew source pins for intentional new fixture versions except the deliberately stale-revision condition.
 if m!='revision':
  for k,s in a.items():p['artifacts'][k]['sha256']=hashlib.sha256(s.encode()).hexdigest()
 cem=json.loads(a['interface']);xml=etree.fromstring(a['behavior'].encode(),etree.XMLParser(no_network=True,resolve_entities=False));dom=html.fromstring(a['accessibility']);schema={'cem':not list(cemValidator.iter_errors(cem)),'scxml':xsd.validate(xml)};errors=[];witnesses=[]
 def resolve(ref,expectedKind):
  if ref.get('kind')!=expectedKind:raise Invalid('reference-kind')
  domain='interface' if expectedKind.startswith('cem.') else 'behavior'
  if ref.get('artifact')!=domain:raise Invalid('reference-domain')
  loc=ref.get('locator',{})
  if domain=='interface':
   if set(loc)!={'pointer'}:raise Invalid('locator-kind')
   node=pointer(cem,loc['pointer']);locpath=loc['pointer']
   if expectedKind=='cem.custom-element-class':
    if not re.fullmatch(r'/modules/[0-9]+/declarations/[0-9]+',locpath) or node.get('kind')!='class' or node.get('customElement') is not True:raise Invalid('target-kind')
   elif not re.fullmatch(r'/modules/[0-9]+/declarations/[0-9]+/cssParts/[0-9]+',locpath) or not isinstance(node,dict) or not isinstance(node.get('name'),str):raise Invalid('target-kind')
  else:
   if set(loc)!={'xpath'}:raise Invalid('locator-kind')
   nodes=xml.xpath(loc['xpath'],namespaces=ns)
   if not nodes:raise Invalid('missing-target')
   if len(nodes)!=1:raise Invalid('nonunique-target')
   node=nodes[0];expectedTag='{'+ns['s']+'}'+('scxml' if expectedKind=='scxml.machine' else 'state')
   if not isinstance(node,etree._Element) or node.tag!=expectedTag:raise Invalid('target-kind')
  return node
 for domain,s in a.items():
  if hashlib.sha256(s.encode()).hexdigest()!=p['artifacts'][domain]['sha256']:errors.append('source-revision')
 if not errors:
  for key,df in p['definitions'].items():
   try:
    component=resolve(df['component'],'cem.custom-element-class');machine=resolve(df['machine'],'scxml.machine')
    if machine.get('name')!=component['name']:raise Invalid('machine-component-binding')
    for part,ref in df['parts'].items():
     node=resolve(ref,'cem.css-part')
     if not any(node is item for item in component['cssParts']):raise Invalid('foreign-component-part')
     if node['name']!=p['requiredPartNames'][part]:raise Invalid('part-name')
    for state,ref in df['states'].items():
     node=resolve(ref,'scxml.state')
     if node.getparent() is not machine or node.get('id')!=state:raise Invalid('foreign-machine-state')
    witnesses.append({'definition':key,'component':df['component'],'componentName':component['name'],'machine':df['machine'],'machineName':machine.get('name'),'parts':df['parts'],'states':df['states']})
   except Invalid as e:errors.append(str(e))
 if not errors:
  for key,binding in p['instances'].items():
   try:
    if binding['uses'] not in p['definitions']:raise Invalid('undefined-definition')
    df=p['definitions'][binding['uses']];state=binding['snapshotState']
    if state not in df['states']:raise Invalid('undefined-state')
    nodes={}
    for part,target in binding['host'].items():
     found=dom.xpath('//*[@id=$id]',id=target)
     if len(found)!=1:raise Invalid('host-unique-target')
     nodes[part]=found[0]
     role=p['requiredHostRoles'].get(part)
     if role and found[0].get('role')!=role:raise Invalid('host-role')
    input,listing,option,popup=(nodes[n] for n in ['input','list','option','popup'])
    if input.get('aria-controls')!=binding['host']['list'] or input.get('aria-activedescendant')!=binding['host']['option'] or option not in listing.iterdescendants() or listing not in popup.iterdescendants():raise Invalid('same-instance-relation')
    if (input.get('aria-expanded')=='true')!=p['stateProjection'][state]['expanded']:raise Invalid('state-projection')
    witnesses.append({'instance':key,'definition':binding['uses'],'resolvedState':df['states'][state],'hostParts':binding['host'],'relation':'input.controls -> own list; active descendant -> own option; explicit open-state projection'})
   except Invalid as e:errors.append(str(e))
 rules=sorted(set(errors));out.append({'id':c['id'],'mutation':m,'expectedRules':c['expectedRules'],'actualRules':rules,'expectationMet':rules==sorted(c['expectedRules']),'originalSchemas':schema,'sourceHashes':{k:hashlib.sha256(s.encode()).hexdigest() for k,s in a.items()},'profile':p,'witnesses':witnesses})
result={'method':'Own bounded typed cross-model reference adapter; original CEM/SCXML schemas checked separately; no original neutral ARIA model resolver claimed','cases':out};(w/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps([{'id':c['id'],'rules':c['actualRules'],'met':c['expectationMet'],'schemas':c['originalSchemas']} for c in out]));raise SystemExit(0 if all(c['expectationMet'] for c in out) else 1)
