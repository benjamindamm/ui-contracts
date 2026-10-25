from pathlib import Path
import json,hashlib,math
repo=Path(__file__).resolve().parents[3];root=repo/'components';review=Path(__file__).parent
baseline=json.loads((review/'definition-baseline.json').read_text());current={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest()for p in sorted(root.rglob('*'))if p.is_file()};assert current==baseline['files']
stories=json.loads((root/'autocomplete/stories.json').read_text())['stories'];rules=json.loads((root/'autocomplete/accessibility.rules.json').read_text());tokens=json.loads((root/'tokens.json').read_text());nodes=json.loads((review/'actual-graph.json').read_text())['nodes'];by={n['id']:n for n in nodes}
def token(path):
 x=tokens
 for part in path.split('.'):x=x[part]
 v=x['$value'];return token(v[1:-1])if isinstance(v,str)and v.startswith('{')else v
def number(name):return token('autocomplete.'+name)['value']
def descendants(node):
 children=[n for n in nodes if n.get('parentId')==node['id']]
 return children+sum([descendants(c)for c in children],[])
def direct(frame,prefix):return next(n for n in nodes if n.get('parentId')==frame['id']and n['name'].startswith(prefix))
def absolute(n):
 x,y=n['x'],n['y']
 while n.get('parentId'):
  n=by[n['parentId']];x+=n['x'];y+=n['y']
 return x,y
results=[]
for story in stories:
 frame=next(n for n in nodes if n['name']=='Autocomplete / '+story['id']);ds=descendants(frame);input=direct(frame,'input');surface=direct(frame,'overlay.surface');status=direct(frame,'status');label=direct(frame,'label');vp=next(n for n in ds if n['name'].startswith('overlay.scroll.viewport'));options=[n for n in ds if n['name'].startswith('option / ')]
 pop=rules['projections'][story['phase']]['popupVisible']and story['inputs']['enabled'];expectedMessage=rules['messages']['disabled']if not story['inputs']['enabled']else rules['messages']['selected'].format(label=next(r['label']for r in story['results']if r['key']==story['value']))if 'value'in story else rules['messages']['results'].format(count=len(story['results']))if story['phase']=='ready'else rules['messages'][story['phase']]
 checks={'frameWidth':frame['width']==number('width'),'inputWidth':input['width']==number('width'),'inputHeight':input['height']==number('inputHeight'),'labelText':label['text']==story['inputs']['label'],'inputY':input['y']==number('lineHeight')+number('labelGap'),'popupVisibility':surface['visible']==pop,'statusText':status['text']==expectedMessage,'allEditableOptionsRetained':len(options)==len(story['results']),'viewportClips':vp['clipsContent'] is True}
 if pop:
  checks['anchorGap']=surface['y']-(input['y']+input['height'])==number('gap');expectedHeight=min(len(story['results'])*number('rowHeight'),number('maxHeight'))if story['results']else number('rowHeight');checks['viewportHeight']=vp['height']==expectedHeight
  checks['statusY']=status['y']==surface['y']+surface['height']+number('statusGap')
 else:checks['statusY']=status['y']==input['y']+input['height']+number('statusGap')
 for row in story['results']:
  option=next(n for n in options if n['name'].startswith('option / '+row['key']+' '));text=next(n for n in descendants(option)if n['type']=='TEXT');checks['label:'+row['key']]=text['text']==row['label'];checks['rowHeight:'+row['key']]=option['height']==number('rowHeight');checks['disabled:'+row['key']]=('disabled=true'in option['name'])==row.get('disabled',False);checks['selected:'+row['key']]=('selected=true'in option['name'])==(story.get('activeKey')==row['key'])
 if story.get('activeKey'):
  active=next(n for n in options if 'selected=true'in n['name']);ax,ay=absolute(active);vx,vy=absolute(vp);checks['activeActuallyInsideClippingViewport']=ay>=vy and ay+active['height']<=vy+vp['height'];expected=token('autocomplete.highlight')['components'];checks['activeFillFromToken']=all(abs(active['fills'][0]['color'][k]-expected[i])<1e-6 for i,k in enumerate('rgb'))
 results.append({'story':story['id'],'checks':checks,'expectationMet':all(checks.values())})
out={'reviewer':'parent agent, independent original-file reimport','definitionRevision':baseline['revision'],'definitionUnchanged':True,'file':str((repo/'examples/autocomplete/output/openpencil/autocomplete.fig').relative_to(repo)),'fileSha256':hashlib.sha256((repo/'examples/autocomplete/output/openpencil/autocomplete.fig').read_bytes()).hexdigest(),'originalReaderNodes':len(nodes),'cases':results,'allStructuralChecksMet':all(r['expectationMet']for r in results),'doesNotResolveDefinitionGaps':True,'guiOpeningConfirmed':False}
(review/'independent-results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps([{'story':r['story'],'passed':r['expectationMet']}for r in results]));assert out['allStructuralChecksMet']
