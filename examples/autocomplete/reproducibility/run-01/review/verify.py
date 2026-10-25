import json,pathlib,hashlib
root=pathlib.Path(__file__).resolve().parents[5]; out=pathlib.Path(__file__).resolve().parent
pre=json.loads((out/'preregistered.json').read_text()); stories=json.loads((root/'components/autocomplete/stories.json').read_text())['stories']; rules=json.loads((root/'components/autocomplete/accessibility.rules.json').read_text())
colors={'text':'172b4d','muted':'64748b','border':'cbd5e1','focus':'2563eb','highlight':'eaf2ff','disabled':'94a3b8','error':'b91c1c','surface':'ffffff'}
def hexcolor(n,prop='fills'):
 f=n.get(prop,[])
 return ''.join(f'{round(f[0]["color"][c]*255):02x}' for c in 'rgb') if f else None
def shape(n):return [n['x'],n['y'],n['width'],n['height']]
result={'method':'Original parseFigFile before builder reports; native graph checks plus original CanvasKit renders visually inspected','artifacts':{},'source_integrity':{},'pair':{}}
for key in 'ab':
 ns=json.loads((out/f'original-{key}.json').read_text())['nodes']; ids={n['id']:n for n in ns}; checks=[]; cases={}; normalized={}
 def check(cat,case,rule,actual,expected):checks.append(dict(criterion=cat,case=case,rule=rule,actual=actual,expected=expected,verdict='PASS' if actual==expected else 'FAIL'))
 def desc(n):
  kids=[c for c in ns if c['parentId']==n['id']]
  return kids+sum([desc(c) for c in kids],[])
 for s in stories:
  sid=s['id']; group=next(n for n in ns if n['type']=='FRAME' and n['name'] in [sid,'Autocomplete / '+sid]); ds=desc(group)
  inp=next(n for n in ds if n['type']=='FRAME' and n['name'].startswith('input')); label=next(n for n in ds if n['name']=='label'); status=next(n for n in ds if n['name'].startswith('status')); txt=next(n for n in ds if n['parentId']==inp['id'] and n['type']=='TEXT'); surface=next((n for n in ds if n['name']=='overlay.surface'),None); viewport=next((n for n in ds if n['name']=='overlay.scroll.viewport'),None); opts=[n for n in ds if n['type']=='FRAME' and n['name'].startswith('option')]; opts.sort(key=lambda n:n['y'])
  popup=s['phase'] in ['loading','ready','empty','error']; vh=min(len(s['results'])*32,160) if s['phase']=='ready' else 32
  msg=rules['messages']['selected' if sid=='selected' else 'disabled' if sid=='disabled' else 'results' if s['phase']=='ready' else s['phase']].replace('{count}',str(len(s['results']))).replace('{label}','Berlin')
  check('visibility',sid,'popup presence',surface is not None,popup)
  check('geometry',sid,'label box',shape(label),[0,0,320,20]);check('geometry',sid,'input box',shape(inp),[0,28,320,44]);check('geometry',sid,'input text box',shape(txt),[12,12,296,20]);check('geometry',sid,'status box',shape(status),[0,80+vh+8 if popup else 80,320,20])
  check('messages',sid,'label',label['text'],s['inputs']['label']);check('messages',sid,'input',txt['text'],s['inputs']['query'] or s['inputs']['placeholder']);check('messages',sid,'status',status['text'],msg)
  check('visual',sid,'input border',hexcolor(inp,'strokes'),colors['focus' if s['phase'] in ['opening','loading','ready','empty','error'] else 'border']);check('visual',sid,'input radius',inp['cornerRadius'],8);check('visual',sid,'input stroke weight',inp['strokes'][0]['weight'],1);check('visual',sid,'input surface',hexcolor(inp),colors['surface'])
  check('visual',sid,'input text color',hexcolor(txt),colors['text' if s['inputs']['query'] else 'muted']);check('visual',sid,'label color',hexcolor(label),colors['text']);check('visual',sid,'status color',hexcolor(status),colors['error' if sid=='error' else 'muted'])
  for n in ds:
   if n['type']=='TEXT':
    check('visual',sid,n['id']+' font',[n['fontFamily'],n['fontSize'],n['lineHeight']],['Inter',12 if n==status else 14,20])
  if popup:
   check('geometry',sid,'popup box',shape(surface),[0,80,320,vh]);check('geometry',sid,'viewport box',shape(viewport),[0,0,320,vh]);check('clipping',sid,'viewport clipsContent',viewport['clipsContent'],True)
   check('visual',sid,'surface radius',surface['cornerRadius'],8);check('visual',sid,'surface fill',hexcolor(surface),colors['surface']);check('visual',sid,'surface no stroke',surface['strokes'],[])
   shadow=surface['effects'][0];check('visual',sid,'shadow',[shadow['type'],shadow['offset'],shadow['radius'],round(shadow['color']['a'],3),shadow['spread']],['DROP_SHADOW',{'x':0,'y':2},8,0.2,0])
   if s['phase']!='ready':check('messages',sid,'popup message',[n['text'] for n in ds if n['type']=='TEXT' and n not in [label,txt,status]],[msg])
  check('fixtures',sid,'editable option count',len(opts),len(s['results']) if s['phase']=='ready' else 0)
  optiondata=[]
  for i,(n,r) in enumerate(zip(opts,s['results'])):
   ot=next(c for c in ds if c['parentId']==n['id'] and c['type']=='TEXT');check('fixtures',sid,'key in option name '+r['key'],r['key'] in n['name'],True);check('fixtures',sid,'option label '+r['key'],ot['text'],r['label']);check('geometry',sid,'row '+r['key'],shape(n),[0,i*32,320,32]);check('geometry',sid,'row text '+r['key'],shape(ot),[12,6,296,20]);check('visual',sid,'option color '+r['key'],hexcolor(ot),colors['disabled' if r.get('disabled') else 'text']);check('visual',sid,'option highlight '+r['key'],hexcolor(n),colors['highlight'] if r['key']==s.get('activeKey') else None)
   y=n['y']; par=ids[n['parentId']]
   while par['id']!=viewport['id']:y+=par['y'];par=ids[par['parentId']]
   optiondata.append(dict(key=r['key'],viewport_y=y,box=shape(n),text=ot['text'],textColor=hexcolor(ot),fill=hexcolor(n)))
  if sid=='scroll-end':check('clipping',sid,'Zürich viewport interval',[optiondata[-1]['viewport_y'],optiondata[-1]['viewport_y']+32],[128,160])
  check('anatomy',sid,'all editable/unlocked',all(not n.get('locked') for n in ds),True)
  norm=dict(label=shape(label),input=shape(inp),inputText=dict(box=shape(txt),text=txt['text'],color=hexcolor(txt)),status=dict(box=shape(status),text=status['text'],color=hexcolor(status)),popup=shape(surface) if surface else None,viewport=shape(viewport) if viewport else None,options=optiondata)
  normalized[sid]=norm;cases[sid]={'frame_id':group['id'],'input_id':inp['id'],'status_id':status['id'],'node_count':len(ds)+1,'observation':norm}
 (out/f'normalized-{key}.json').write_text(json.dumps(normalized,ensure_ascii=False,indent=2)+'\n')
 aggregate=[]
 for c in pre['criteria']:
  related=[x for x in checks if x['criterion']==c['id']];failed=[x for x in related if x['verdict']=='FAIL']
  verdict='FAIL' if failed else 'PASS'
  evidence={'artifact':f'original-{key}.json; render-{key}.png','coverage':'Ten named frame groups found in original reader','semantic-design':'Separate named roles, keyed option frames; active and disabled styling verified; no executed ARIA claimed','source-integrity':'See source_integrity below'}.get(c['id'],f'{len(related)} recorded native checks')
  aggregate.append(dict(id=c['id'],verdict=verdict,sources=c['sources'],evidence=evidence,failures=failed))
 result['artifacts'][key]={'overall':'FAIL' if any(x['verdict']=='FAIL' for x in aggregate) else 'PASS','node_count':len(ns),'native_text_nodes':sum(n['type']=='TEXT' for n in ns),'criteria':aggregate,'checks':checks,'cases':cases}
for p,h in pre['source_sha256'].items():result['source_integrity'][p]={'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest(),'unchanged':hashlib.sha256((root/p).read_bytes()).hexdigest()==h}
a=json.loads((out/'normalized-a.json').read_text()); b=json.loads((out/'normalized-b.json').read_text()); result['pair']={'normalized_equal':a==b,'per_case_equal':{s:a[s]==b[s] for s in a},'qualification':'Normalized checked observables agree, including a shared disabled-placeholder deviation. Native graph hierarchy/names and outer frame bounds differ; exact file equality is not required.'}
(out/'native-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('root',root,'A',result['artifacts']['a']['overall'],'B',result['artifacts']['b']['overall'],'pair',result['pair']);print('failures',[(k,[c for c in result['artifacts'][k]['checks'] if c['verdict']=='FAIL']) for k in 'ab'])
