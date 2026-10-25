from pathlib import Path
import json,sys,platform,hashlib,copy
from lxml import etree
p=Path(__file__).parent
class LocalOnly(etree.Resolver):
 def resolve(self,url,pubid,context):
  f=p/'sources'/url.rsplit('/',1)[-1]
  if f.is_file():return self.resolve_filename(str(f),context)
  raise RuntimeError('Uncaptured dependency refused: '+url)
parser=etree.XMLParser(no_network=True,resolve_entities=False);parser.resolvers.add(LocalOnly())
schema=etree.XMLSchema(etree.parse(str(p/'sources/scxml.xsd'),parser))
s='''<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" datamodel="ecmascript" initial="closed"><datamodel><data id="count" expr="0"/></datamodel><state id="closed"><transition event="OPEN" cond="_event.data.allowed === true" target="open"><assign location="count" expr="count + _event.data.delta"/></transition></state><state id="open"><transition event="CLOSE" target="closed"/></state></scxml>'''
cases=[('xsd-01-valid',s,True,'Own comparison fixture against full original XSD include/import chain'),('xsd-02-no-version',s.replace(' version="1.0"',''),False,'required attribute'),('xsd-03-duplicate-state-id',s.replace('<state id="open">','<state id="closed">'),False,'duplicate XML ID'),('xsd-04-missing-target',s.replace('target="open"','target="missing-state"'),False,'reference target existence expectation'),('xsd-05-invalid-expression',s.replace('count + _event.data.delta','this !!! is not valid ecmascript'),True,'XSD does not parse ECMAScript expressions'),('xsd-06-static-send','''<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" datamodel="ecmascript" initial="selected"><datamodel><data id="value" expr="'alpha'"/></datamodel><state id="selected"><onentry><send event="value-change" target="#_parent"><param name="value" expr="value"/></send></onentry></state></scxml>''',True,'Static named event and parameter, separate from public signature')]
results=[];(p/'inputs').mkdir(exist_ok=True)
for id,text,expected,q in cases:
 (p/'inputs'/f'{id}.scxml').write_text(text+'\n');doc=etree.fromstring(text.encode(),etree.XMLParser(no_network=True,resolve_entities=False));valid=schema.validate(doc);errs=[{'line':e.line,'column':e.column,'domain':e.domain_name,'type':e.type_name,'message':e.message} for e in schema.error_log];results.append({'id':id,'input':'inputs/'+id+'.scxml','expected_valid':expected,'actual_valid':valid,'expectation_met':expected==valid,'question':q,'errors':errs});print(id,valid,'expected',expected)
report={'python':platform.python_version(),'lxml':'.'.join(map(str,etree.LXML_VERSION)),'libxml':'.'.join(map(str,etree.LIBXML_VERSION)),'schema_entry':'sources/scxml.xsd','schema_compiled':True,'network_disabled':True,'scxml_interpreter_executed':False,'ui_rendered':False,'cases':results};(p/'results.json').write_text(json.dumps(report,indent=2)+'\n');sys.exit(0 if all(r['expectation_met'] for r in results) else 1)
