import {readFile,writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const here=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(here,'../../../..');
const tool=path.join(root,'tools/openpencil/node_modules/@open-pencil');
const {SceneGraph}=await import(path.join(tool,'scene-graph/dist/index.js'));
const {IORegistry,BUILTIN_IO_FORMATS}=await import(path.join(tool,'core/dist/io/index.js'));
const read=async p=>JSON.parse(await readFile(path.join(root,'components',p),'utf8'));
const tokens=await read('tokens.json'),stories=(await read('autocomplete/stories.json')).stories,rules=await read('autocomplete/accessibility.rules.json');
function resolveToken(p){const v=p.split('.').reduce((o,k)=>o[k],tokens).$value;return typeof v==='string'&&v.startsWith('{')?resolveToken(v.slice(1,-1)):v;}
const t=k=>resolveToken('autocomplete.'+k),d=k=>t(k).value;
const color=k=>{let v=t(k);return {r:v.components[0],g:v.components[1],b:v.components[2],a:v.alpha};};
const fill=k=>[{type:'SOLID',color:color(k),opacity:1,visible:true}];
let id=0;const graph=new SceneGraph(()=>`1:${++id}`),page=graph.getPages()[0];page.name='Autocomplete · Definitionsbibliothek';
function node(type,parent,name,x,y,width,height,extra={}){return graph.createNode(type,parent.id,{name,x,y,width,height,...extra});}
function frame(parent,name,x,y,w,h,extra={}){return node('FRAME',parent,name,x,y,w,h,extra);}
function text(parent,name,value,x,y,w,size=d('fontSize'),c='text'){return node('TEXT',parent,name,x,y,w,d('lineHeight'),{text:value,fontFamily:t('fontFamily'),fontSize:size,fontWeight:400,lineHeight:d('lineHeight'),textAutoResize:'NONE',fills:fill(c)});}
const sheet=frame(page,'Autocomplete — zehn benannte Fälle',0,0,1200,1640,{fills:fill('surface')});
text(sheet,'Seitentitel','Autocomplete · 0.1.0',40,24,1100);
text(sheet,'Hinweis','Editierbare Zustände aus components/ · statische Darstellung',40,48,1100,d('statusFontSize'),'muted');
const mappings=[];
for(const [i,s] of stories.entries()){
 const x=40+(i%3)*400,y=110+Math.floor(i/3)*380;
 text(sheet,`Falltitel / ${s.id}`,s.id,x,y,320);
 const box=frame(sheet,`Autocomplete / ${s.id}`,x,y+32,d('width'),300);
 text(box,'label',s.inputs.label,0,0,320);
 const iy=d('lineHeight')+d('labelGap'),ib=iy+d('inputHeight');
 const input=frame(box,'input · role=combobox',0,iy,320,d('inputHeight'),{fills:fill('surface'),cornerRadius:d('radius'),strokes:[{...fill(s.phase==='closed'?'border':'focus')[0],weight:d('borderWidth'),align:'INSIDE'}]});
 text(input,s.inputs.query?'query':'placeholder',s.inputs.query||s.inputs.placeholder,d('paddingInline'),12,296,d('fontSize'),s.inputs.query?(s.inputs.enabled?'text':'disabled'):'muted');
 let msg=rules.messages[s.id]??(s.phase==='ready'?rules.messages.results.replace('{count}',s.results.length):rules.messages[s.phase]);
 if(s.value)msg=rules.messages.selected.replace('{label}',s.results.find(r=>r.key===s.value).label);
 const visible=rules.projections[s.phase].popupVisible&&s.inputs.enabled;
 const vh=s.phase==='ready'?Math.min(s.results.length*d('rowHeight'),d('maxHeight')):d('rowHeight');
 const surface=frame(box,'overlay.surface',0,ib+d('gap'),320,vh,{visible,fills:fill('surface'),cornerRadius:d('radius'),effects:[{type:'DROP_SHADOW',color:{r:0,g:0,b:0,a:.2},offset:{x:0,y:2},radius:8,spread:0,visible:true}]});
 const viewport=frame(surface,'overlay.scroll.viewport · clipped',0,0,320,vh,{clipsContent:true});
 const content=frame(viewport,'overlay.scroll.content',0,s.id==='scroll-end'?vh-s.results.length*d('rowHeight'):0,320,s.phase==='ready'?s.results.length*d('rowHeight'):vh);
 const list=frame(content,'list · role=listbox',0,0,320,s.results.length*d('rowHeight'));
 for(const [j,r] of s.results.entries()){
  const option=frame(list,`option / ${r.key} · selected=${s.activeKey===r.key} · disabled=${!!r.disabled}`,0,j*d('rowHeight'),320,d('rowHeight'),{fills:s.activeKey===r.key?fill('highlight'):[]});
  text(option,'label',r.label,d('paddingInline'),6,296,d('fontSize'),r.disabled?'disabled':'text');
 }
 if(['loading','empty','error'].includes(s.phase))text(content,'popup.message',msg,12,6,296);
 const status=text(box,'status · role=status · aria-live=polite',msg,0,(visible?ib+d('gap')+vh:ib)+d('statusGap'),320,d('statusFontSize'),s.phase==='error'?'error':'muted');
 mappings.push({story:s.id,phase:s.phase,frame:box.id,input:input.id,surface:surface.id,viewport:viewport.id,list:list.id,status:status.id,popupVisible:visible,viewportHeight:vh,scrollOffset:s.id==='scroll-end'?64:0,options:s.results.map(r=>r.key),message:msg});
}
const io=new IORegistry(BUILTIN_IO_FORMATS);const out=await io.writeDocument('fig',graph);await writeFile(path.join(here,'autocomplete.fig'),out.data);
const imported=await io.readDocument({name:'autocomplete.fig',data:new Uint8Array(await readFile(path.join(here,'autocomplete.fig')))});
const {populateAllFigPages}=await import(path.join(tool,'core/dist/io/formats/fig/index.js'));populateAllFigPages(imported.graph);
const nodes=[...imported.graph.nodes.values()];
if(nodes.filter(n=>n.name.startsWith('Autocomplete /')).length!==10)throw Error('Ten frames did not survive import');
if(nodes.filter(n=>n.name.startsWith('option /')).length!==28)throw Error('Options did not survive import');
const sourceFiles=['README.md','library.json','tokens.json',...['autocomplete','overlay','scroll-area'].flatMap(c=>[`${c}/component.json`,`${c}/interface.json`,`${c}/layout.css`,`${c}/behavior.scxml`,`${c}/accessibility.html`]),'autocomplete/README.md','autocomplete/stories.json','autocomplete/accessibility.rules.json','autocomplete/error-relay.scxml'];
await writeFile(path.join(here,'verification.json'),JSON.stringify({sourceFiles,mappings,roundtrip:{nodeCount:nodes.length,storyFrames:10,editableOptionFrames:28,format:'OpenPencil fig writer / reader 0.16.0'}},null,2));
console.log(`Saved and re-imported autocomplete.fig: ${nodes.length} nodes`);
