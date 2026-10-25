from pathlib import Path
from lxml import etree
import json
p=Path(__file__).parent
class LocalOnly(etree.Resolver):
 def resolve(self,url,pubid,context):
  f=p/'sources'/url.rsplit('/',1)[-1]
  if f.is_file():return self.resolve_filename(str(f),context)
  raise RuntimeError('Uncaptured dependency refused: '+url)
parser=etree.XMLParser(no_network=True,resolve_entities=False);parser.resolvers.add(LocalOnly());schema=etree.XMLSchema(etree.parse(str(p/'sources/scxml.xsd'),parser))
r=json.loads((p/'binding-results.json').read_text())
for c in r['cases']:
 c['original_scxml_xsd_valid']=schema.validate(etree.fromstring(c['scxml'].encode(),etree.XMLParser(no_network=True,resolve_entities=False)));assert c['original_scxml_xsd_valid'];print(c['id'],'XSD valid;',c['status'])
r['schema_validation_stage']={'original_schema_modified':False,'network_disabled':True,'lxml':'.'.join(map(str,etree.LXML_VERSION))};(p/'binding-results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
