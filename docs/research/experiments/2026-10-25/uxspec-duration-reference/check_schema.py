from pathlib import Path
import json,hashlib
from jsonschema import Draft202012Validator
w=Path(__file__).parent;schema=Path('work/validation-probes/sources/uxspec.schema.json');v=Draft202012Validator(json.loads(schema.read_text()));results=[]
for c in json.loads((w/'schema-expectations.json').read_text()):
 doc=json.loads((w/c['file']).read_text());errors=[str(e)for e in v.iter_errors(doc)];results.append({**c,'observedValid':not errors,'errors':errors,'expectationMet':(not errors)==c['valid']})
(w/'schema-results.json').write_text(json.dumps({'originalSchemaSha256':hashlib.sha256(schema.read_bytes()).hexdigest(),'cases':results},indent=2)+'\n');print(json.dumps(results));assert all(c['expectationMet']for c in results)
