from pathlib import Path
import json, re, hashlib
w=Path(__file__).parent
notes=[]
for f in sorted(w.glob('*capture*.json')):
 d=json.loads(f.read_text())['value']
 for item in d if isinstance(d,list) else [d]:
  t=item['text']
  if isinstance(t,dict):
   text=Path(t['path']).read_text() if t.get('writtenToFile') else t['value']
  else:
   if 'Full content' in t:
    path=re.search(r'saved to: (.+)$',t).group(1);text=Path(path).read_text()
   else:text=t
  # Remove only browser framing. Content remains unexecuted source data.
  if text.startswith('[UNTRUSTED_PAGE_CONTENT'):
   text=text.split('\n',1)[1].rsplit('\n[END_UNTRUSTED_PAGE_CONTENT',1)[0]
  if text.startswith('```\n'):text=text[4:]
  if text.endswith('\n```'):text=text[:-4]
  notes.append({'url':item['url'],'sha256_read_body':hashlib.sha256(text.encode()).hexdigest(),'chars':len(text),'access_failed':text.strip()=='404: Not Found'})
  if item['url'].endswith('/linter/spec-config.ts'):
   (w/'sources').mkdir(exist_ok=True);(w/'sources/spec-config.ts').write_text(text)
(w/'source-access.json').write_text(json.dumps(notes,indent=2)+'\n')
cases=[
 {'id':'original-config','mutation':'none','expectedAccepted':True},
 {'id':'units-number','mutation':'units','expectedAccepted':False},
 {'id':'type-label-number','mutation':'type-number','expectedAccepted':False},
 {'id':'invented-type-label','mutation':'type-label','expectedAccepted':True},
 {'id':'design-document-data','mutation':'document','expectedAccepted':False},
 {'id':'example-color-number','mutation':'example-color','expectedAccepted':False},
]
(w/'cases.json').write_text(json.dumps(cases,indent=2)+'\n')
print({'source_accesses':len(notes),'cases_preregistered':len(cases)})
