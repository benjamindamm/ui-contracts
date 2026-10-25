from pathlib import Path
import json,platform
import jsonschema
p=Path(__file__).parent;schema=json.loads((p.parent/'sources/uxspec.schema.json').read_text());v=jsonschema.Draft202012Validator(schema);rows=[]
for f in sorted((p/'fixtures').rglob('*.json')):
 d=json.loads(f.read_text())
 if '$machine' not in d:continue
 errors=list(v.iter_errors(d));rows.append({'input':str(f.relative_to(p)),'valid':not errors,'errors':[{'path':list(e.absolute_path),'schema_path':list(e.absolute_schema_path),'validator':e.validator,'message':e.message} for e in errors]})
(p/'schema-preflight.json').write_text(json.dumps({'validator':'python-jsonschema 4.25.1 Draft202012Validator','schema_source':'original UXSpec snapshot 20dfae0e7224d952e198afdf4ffed26d6fd67180','note':'Separate fixture preflight, not invoked by the original resolver/bundler; counted as stages of the 14 cases, not extra probe cases','files':rows},indent=2)+'\n');print('UXSpec fixtures',len(rows),'schema accepted',sum(r['valid'] for r in rows),'rejected',sum(not r['valid'] for r in rows))
