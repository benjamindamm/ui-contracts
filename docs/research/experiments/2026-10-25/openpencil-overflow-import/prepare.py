from pathlib import Path
import json,hashlib,shutil
w=Path(__file__).parent;notes=[]
for item in json.loads((w/'source-captures.json').read_text())['value']:
 t=item['text'];text=Path(t['path']).read_text() if t.get('writtenToFile') else t['value']
 if text.startswith('[UNTRUSTED_PAGE_CONTENT'):text=text.split('\n',1)[1].rsplit('\n[END_UNTRUSTED_PAGE_CONTENT',1)[0]
 dest=w/'sources'/item['path'];dest.parent.mkdir(parents=True,exist_ok=True);dest.write_text(text);notes.append({'url':item['url'],'file':str(dest.relative_to(w)),'sha256':hashlib.sha256(text.encode()).hexdigest()})
source=Path('work/op-layout/sources/packages/dom-css/src/export/projection.ts');dest=w/'sources/packages/dom-css/src/export/projection.ts';dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,dest)
notes.append({'url':'https://raw.githubusercontent.com/open-pencil/open-pencil/ab2875cc761ee6cff17d389ff1c85fedae50aeab/packages/dom-css/src/export/projection.ts','file':str(dest.relative_to(w)),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'reused_original':True})
(w/'source-notes.json').write_text(json.dumps(notes,indent=2)+'\n')
cases=[
 {'id':'visible','inlineStyle':{'overflow':'visible'},'expectedClip':False,'expectedOverflow':None},
 {'id':'hidden','inlineStyle':{'overflow':'hidden'},'expectedClip':True,'expectedOverflow':'hidden'},
 {'id':'clip','inlineStyle':{'overflow':'clip'},'expectedClip':True,'expectedOverflow':'hidden'},
 {'id':'auto','inlineStyle':{'overflow':'auto'},'expectedClip':False,'expectedOverflow':None},
 {'id':'scroll','inlineStyle':{'overflow':'scroll'},'expectedClip':False,'expectedOverflow':None},
 {'id':'axis-y-scroll','inlineStyle':{'overflow-y':'scroll'},'expectedClip':False,'expectedOverflow':None},
 {'id':'axis-x-hidden','inlineStyle':{'overflow-x':'hidden'},'expectedClip':False,'expectedOverflow':None},
 {'id':'two-keyword-overflow','inlineStyle':{'overflow':'hidden scroll'},'expectedClip':False,'expectedOverflow':None},
 {'id':'computed-hidden','inlineStyle':{'overflow':'auto'},'computedStyle':{'overflow':'hidden'},'expectedClip':True,'expectedOverflow':'hidden'},
 {'id':'computed-auto','inlineStyle':{'overflow':'hidden'},'computedStyle':{'overflow':'auto'},'expectedClip':False,'expectedOverflow':None},
 {'id':'no-overflow','inlineStyle':{},'expectedClip':False,'expectedOverflow':None},
 {'id':'preexisting-clip-not-cleared','inlineStyle':{'overflow':'visible'},'initialClip':True,'expectedClip':True,'expectedOverflow':'hidden'},
]
(w/'cases.json').write_text(json.dumps(cases,indent=2)+'\n');print({'sources':len(notes),'conditions_preregistered':len(cases)})
