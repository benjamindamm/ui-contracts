from pathlib import Path
import json,hashlib
from lxml import etree
import jsonschema
w=Path(__file__).parent;root=Path.cwd();data=json.loads((w/'accepted-coordinated-public-name-change.json').read_text());c=json.loads((w/'schema-expectation.json').read_text());cempath=root/'work/validation-probes/sources/cem.schema.json';xsdpath=root/'work/scxml-probes/sources/scxml.xsd'
class Resolver(etree.Resolver):
 def resolve(self,url,pubid,context):
  p=xsdpath.parent/url.rsplit('/',1)[-1]
  if p.is_file():return self.resolve_filename(str(p),context)
  raise RuntimeError('Missing pinned include '+url)
parser=etree.XMLParser(no_network=True,resolve_entities=False);parser.resolvers.add(Resolver());schema=etree.XMLSchema(etree.parse(str(xsdpath),parser));cemErrors=list(jsonschema.Draft7Validator(json.loads(cempath.read_text())).iter_errors(json.loads(data['artifacts']['interface.json'])));valid=schema.validate(etree.fromstring(data['artifacts']['behavior.scxml'].encode(),etree.XMLParser(no_network=True,resolve_entities=False)));observed={'cem':not cemErrors,'scxml':valid};result={'method':'Previously pinned original schemas, newly changed accepted source artifacts','cases':[{**c,'observed':observed,'expectationMet':observed==c['expected'],'cemErrors':[str(e) for e in cemErrors],'scxmlErrors':str(schema.error_log)}],'schemaHashes':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [cempath,*sorted(xsdpath.parent.glob('*.xsd'))]},'jsonschemaVersion':__import__('importlib.metadata',fromlist=['version']).version('jsonschema'),'lxmlVersion':etree.LXML_VERSION};(w/'schema-results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result));raise SystemExit(0 if result['cases'][0]['expectationMet'] else 1)
