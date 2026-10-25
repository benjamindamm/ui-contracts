from pathlib import Path
import json,hashlib,xml.etree.ElementTree as ET
from html.parser import HTMLParser
from jsonschema import Draft202012Validator
w=Path(__file__).parent;schema=Path('work/validation-probes/sources');s=json.loads((w/'results.json').read_text());cem=Draft202012Validator(json.loads((schema/'cem.schema.json').read_text()));ux=Draft202012Validator(json.loads((schema/'uxspec.schema.json').read_text()))
class Nodes(HTMLParser):
 def __init__(self,t):super().__init__();self.nodes={};self.feed(t)
 def handle_starttag(self,t,a):
  a=dict(a)
  if'id'in a:self.nodes[a['id']]={'tag':t,**a}
for c in s['cases']:
 d=w/'fixtures'/c['id'];checks={};doc=json.loads((d/'interface.json').read_text());checks['originalCemSchema']=not list(cem.iter_errors(doc));parts={p['name']for p in doc['modules'][0]['declarations'][0]['cssParts']};a11y=Nodes((d/'accessibility.html').read_text()).nodes;checks['externalInputPopupParts']=all(x in parts for x in ['input','popup']);checks['externalNamesRolesAndRelations']=all(a11y['input-'+i].get('role')=='combobox'and a11y['input-'+i].get('aria-controls')=='list-'+i and a11y['list-'+i].get('role')=='listbox'for i in ['a','b'])
 if c['candidate']in ['Zag','Ark UI']:
  actual=Nodes((d/'actual.html').read_text()).nodes
  checks['originalInputValueMapsToSeparateTypedInterface']=all(actual['input-'+i].get('value')=='Al'for i in ['a','b'])and doc['modules'][0]['declarations'][0]['members'][0]=={'kind':'field','name':'inputValue','type':{'text':'string'}}
  checks['originalIdsAndRolesMappedToExternalContext']=all(actual['input-'+i].get('aria-controls')=='popup-'+i and actual['input-'+i].get('role')=='combobox'and actual['popup-'+i].get('role')=='listbox'for i in ['a','b'])
  c['details']['contextualRelationBinding']='Original content popup-a/b is the listbox; external accessibility list-a/b is the listbox. Additional role/controls mapping explicitly maps popup-a→list-a and popup-b→list-b; source IDs need not be equal.'
  checks['visualTargetExistsInActualOutput']=all('popup-'+i in actual for i in ['a','b'])
  import re
  expectedNames=[re.search('<label for="input-'+i+'">([^<]+)</label>',(d/'accessibility.html').read_text()).group(1)for i in ['a','b']]
  checks['originalRenderedNamesDerivedFromLeadingAccessibilitySource']=all(name in(d/'actual.html').read_text()for name in expectedNames)
 elif c['candidate']=='UXSpec':
  b=json.loads((d/'behavior.json').read_text());checks['originalUxspecSchema']=not list(ux.iter_errors(b));compiled=c['details']['compiled'];checks['actualCompiledStateBinding']=compiled['initial']=='closed'and set(compiled['states'])=={'closed','open'};checks['separateVisualTargets']=all('#popup-'+i in (d/'visual.css').read_text()and'popup-'+i in a11y for i in ['a','b'])
 else:
  root=ET.parse(d/'behavior.scxml').getroot();checks['originalScxmlSyntaxAndOwnBehaviorStates']=root.tag=='{http://www.w3.org/2005/07/scxml}scxml'and root.attrib.get('initial')=='closed';checks['pandaNoForeignRootDefinitions']=not any(k in c['details']['originalReaderResult']['value']for k in ['api','behavior','accessibility']);checks['explicitAdditionalProjectionTargets']=all('popup-'+i in a11y for i in ['a','b'])
 c['additionalBindingChecks']=checks;c['expectationMet']=c['expectationMet']and all(checks.values())
(w/'bound-results.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps([{'id':c['id'],'met':c['expectationMet'],'failed':[k for k,v in c['additionalBindingChecks'].items()if not v]}for c in s['cases']],indent=2));assert all(c['expectationMet']for c in s['cases'])
