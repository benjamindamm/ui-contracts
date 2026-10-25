from pathlib import Path
import json,hashlib
from jsonschema import Draft202012Validator
from lxml import etree
w=Path(__file__).parent;f=w/'host/sources';schema=Path('work/validation-probes/sources/cem.schema.json');errors=[str(e)for e in Draft202012Validator(json.loads(schema.read_text())).iter_errors(json.loads((f/'interface.json').read_text()))];xsd=Path('work/scxml-probes/sources/scxml.xsd');v=etree.XMLSchema(etree.parse(str(xsd)));valid=v.validate(etree.parse(str(f/'behavior.scxml')));out={'originalCemSchemaSha256':hashlib.sha256(schema.read_bytes()).hexdigest(),'originalScxmlSchemaSha256':hashlib.sha256(xsd.read_bytes()).hexdigest(),'cemValid':not errors,'cemErrors':errors,'scxmlValid':valid,'scxmlErrors':str(v.error_log),'scope':'Original schemas on exact fixtures; preflight source validity, not counted as additional runtime conditions'};(w/'schema-results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));assert not errors and valid
