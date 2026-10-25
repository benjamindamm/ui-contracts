from pathlib import Path
import json,hashlib,copy,subprocess,os,re
from lxml import etree,html
import jsonschema
w=Path(__file__).parent;root=Path.cwd();fixtures={n:(w/'fixtures'/f).read_text() for n,f in [('interface','interface.json'),('behavior','behavior.scxml'),('visual','visual.css'),('accessibility','accessibility.html')]};profile=json.loads((w/'profile.json').read_text());cases=json.loads((w/'cases.json').read_text());ns={'s':'http://www.w3.org/2005/07/scxml'}
class Resolver(etree.Resolver):
 def resolve(self,url,pubid,context):
  p=root/'work/scxml-probes/sources'/url.rsplit('/',1)[-1]
  if p.is_file():return self.resolve_filename(str(p),context)
  raise RuntimeError('Missing original schema include '+url)
parser=etree.XMLParser(no_network=True,resolve_entities=False);parser.resolvers.add(Resolver());xsd=etree.XMLSchema(etree.parse(str(root/'work/scxml-probes/sources/scxml.xsd'),parser));cemSchema=json.loads((root/'work/validation-probes/sources/cem.schema.json').read_text());validator=jsonschema.Draft7Validator(cemSchema)
prepared=[]
for case in cases:
 a=copy.deepcopy(fixtures);p=copy.deepcopy(profile);mutation=case['mutation']
 if mutation=='part-name':a['interface']=a['interface'].replace('"name": "input"','"name": "not-input"')
 elif mutation=='machine-name':a['behavior']=a['behavior'].replace('name="Autocomplete"','name="DifferentMachine"')
 elif mutation=='state':p['instances']['A']['snapshotState']='missing'
 elif mutation=='list':a['accessibility']=a['accessibility'].replace('aria-controls="list-a"','aria-controls="list-b"')
 elif mutation=='option':a['accessibility']=a['accessibility'].replace('aria-activedescendant="option-a-0"','aria-activedescendant="option-b-0"')
 elif mutation=='anchor':a['visual']=a['visual'].replace('position-anchor:--input-a','position-anchor:--input-b')
 elif mutation=='unit':a['visual']=a['visual'].replace('margin-top:8px','margin-top:8',1)
 elif mutation=='event':a['behavior']=a['behavior'].replace('send event="value-change"','send event="different-event"')
 elif mutation=='payload':a['behavior']=a['behavior'].replace('expr="\'alpha\'"','expr="42"')
 elif mutation=='owner':p['ownership']['geometry']='behavior'
 elif mutation=='duplicate':p['instances']['B']['parts']=copy.deepcopy(p['instances']['A']['parts']);p['instances']['B']['anchorName']=p['instances']['A']['anchorName']
 for domain in a:p['artifacts'][domain]['sha256']=hashlib.sha256(a[domain].encode()).hexdigest()
 if mutation=='hash':p['artifacts']['interface']['sha256']='0'*64
 cem=json.loads(a['interface']);decl=cem['modules'][0]['declarations'][0];xml=etree.fromstring(a['behavior'].encode(),etree.XMLParser(no_network=True,resolve_entities=False));send=xml.find('.//s:send',ns);param=send.find('s:param',ns)
 prepared.append(dict(case,artifacts=a,profile=p,publicType=decl['events'][0]['type']['text'],dataExpression=xml.find('.//s:data',ns).get('expr'),paramName=param.get('name'),paramExpression=param.get('expr'),schema={'cem':not list(validator.iter_errors(cem)),'scxml':xsd.validate(xml)},sendEvent=send.get('event')))
(w/'prepared-cases.json').write_text(json.dumps(prepared,indent=2)+'\n')
subprocess.run(['/Users/kcnpxcp/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node',str(w/'analyze.cjs')],check=True)
analysis=json.loads((w/'analysis-results.json').read_text());out=[]
for case,an in zip(prepared,analysis['cases']):
 errors=[];a=case['artifacts'];p=case['profile'];cem=json.loads(a['interface']);decl=cem['modules'][0]['declarations'][0];xml=etree.fromstring(a['behavior'].encode());dom=html.fromstring(a['accessibility']);css=an['cssRules'];declared={v['name'] for v in decl['cssParts']};states={e.get('id') for e in xml.findall('.//s:state',ns)};used={}
 def err(rule,**detail):errors.append(dict(rule=rule,**detail))
 for domain in a:
  if hashlib.sha256(a[domain].encode()).hexdigest()!=p['artifacts'][domain]['sha256']:err('source-integrity',domain=domain)
 for instance,binding in p['instances'].items():
  if binding['interfaceDeclaration']!=decl['name']:err('interface-definition',instance=instance)
  if binding['behaviorDefinition']!=xml.get('name'):err('behavior-definition',instance=instance)
  if binding['snapshotState'] not in states:err('state-reference',instance=instance)
  for part,target in binding['parts'].items():
   if part not in declared:err('declared-part',instance=instance,part=part)
   if target in used:err('unique-instance-part',instance=instance,target=target,previous=used[target])
   used[target]=instance
   if len(dom.xpath('//*[@id=$id]',id=target))!=1:err('unique-host-target',instance=instance,target=target)
  parts=binding['parts'];input=dom.get_element_by_id(parts['input']);listing=dom.get_element_by_id(parts['list']);popup=dom.get_element_by_id(parts['popup']);option=dom.get_element_by_id(parts['option'])
  if input.get('aria-controls')!=parts['list'] or input.get('aria-activedescendant')!=parts['option'] or option not in listing.iterdescendants() or listing not in popup.iterdescendants():err('same-instance-relation',instance=instance)
  ir=css.get('#'+parts['input'],{});pr=css.get('#'+parts['popup'],{})
  if ir.get('anchor-name')!=binding['anchorName'] or pr.get('position-anchor')!=binding['anchorName']:err('same-instance-anchor',instance=instance)
  if pr.get('margin-top')!='8px' or pr.get('max-height')!='160px':err('geometry-unit',instance=instance)
  view=p['stateView'].get(binding['snapshotState'])
  if view and (input.get('aria-expanded')=='true')!=view['expanded']:err('state-view-binding',instance=instance)
 if case['sendEvent']!=p['publicEvent'] or p['publicEvent'] not in {e['name'] for e in decl['events']}:err('public-event-route')
 if not an['payload']['compatible']:err('public-payload-type')
 for field,expected in profile['ownership'].items():
  if p['ownership'].get(field)!=expected:err('leading-source',field=field)
 rules=sorted(set(e['rule'] for e in errors));out.append({'id':case['id'],'mutation':case['mutation'],'schema':case['schema'],'cssGrammarAllMatched':all(v['matched'] for v in an['grammar']),'errors':errors,'actualRules':rules,'expectedRules':case['expected'],'expectationMet':rules==sorted(case['expected'])})
result={'method':'Additional static research profile; actual CEM/SCXML original schemas, original css-tree property matcher, separate TypeScript public event detail check; no actors or runtime dispatch','cases':out};(w/'binding-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if all(c['expectationMet'] for c in out) else 1)
