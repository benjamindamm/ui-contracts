import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
const out=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(out,'../../../../..');
const pkg=path.join(root,'tools/openpencil/node_modules/@open-pencil');
const {SceneGraph}=await import(`${pkg}/scene-graph/dist/index.js`);
const {exportFigFile,parseFigFile,headlessRenderNodes}=await import(`${pkg}/core/dist/io/index.js`);
const read=async p=>JSON.parse(await fs.readFile(path.join(root,'components',p),'utf8'));
const tokens=await read('tokens.json'), stories=(await read('autocomplete/stories.json')).stories,rules=await read('autocomplete/accessibility.rules.json');
function token(n){let v=n.split('.').reduce((a,k)=>a[k],tokens).$value;if(typeof v==='string'&&v.startsWith('{'))return token(v.slice(1,-1));return v?.unit==='px'?v.value:v;}
const t=n=>token('autocomplete.'+n), col=n=>{const v=t(n);return {r:v.components[0],g:v.components[1],b:v.components[2],a:v.alpha}}, paint=n=>[{type:'SOLID',color:col(n),opacity:1,visible:true}];
const g=new SceneGraph(),page=g.getPages()[0]??g.addPage('Autocomplete');page.name='Autocomplete · zehn Darstellungsfälle';
const node=(type,parent,name,x,y,width,height,props={})=>g.createNode(type,parent.id,{name,x,y,width,height,fills:[],clipsContent:false,...props});
const frame=(p,n,x,y,w,h,props={})=>node('FRAME',p,n,x,y,w,h,props);
const text=(p,n,s,x,y,w,size=t('fontSize'),color='text',h=t('lineHeight'))=>node('TEXT',p,n,x,y,w,h,{text:s,fontFamily:t('fontFamily'),fontSize:size,fontWeight:400,lineHeight:t('lineHeight'),textAutoResize:'NONE',textAlignVertical:'TOP',fills:paint(color)});
const board=frame(page,'Autocomplete · Definitionsbibliothek',0,0,1160,1400,{fills:paint('surface')});
text(board,'Seitentitel','Autocomplete · 10 Darstellungsfälle',40,24,1080,24,'text',32);
const expectations=[];
for(const [i,s] of stories.entries()){
 const ox=40+(i%3)*376,oy=100+Math.floor(i/3)*320;
 text(board,'Falltitel · '+s.id,s.id,ox,oy,320,14,'muted');
 const p=frame(board,s.id,ox,oy+32,t('width'),280);
 text(p,'label',s.inputs.label,0,0,320);
 const inputY=t('lineHeight')+t('labelGap'), open=rules.projections[s.phase].popupVisible;
 const inp=frame(p,'input',0,inputY,320,t('inputHeight'),{fills:paint('surface'),cornerRadius:t('radius'),strokes:[{...paint(s.phase==='closed'?'border':'focus')[0],weight:t('borderWidth'),align:'INSIDE'}]});
 const inputText=s.value?s.results.find(r=>r.key===s.value).label:(s.inputs.query||s.inputs.placeholder);
 text(inp,'input.text',inputText,t('paddingInline'),(t('inputHeight')-t('lineHeight'))/2,320-2*t('paddingInline'),14,!s.inputs.enabled?'disabled':s.inputs.query?'text':'muted');
 const msg=s.value?rules.messages.selected.replace('{label}',inputText):s.phase==='ready'?rules.messages.results.replace('{count}',s.results.length):rules.messages[s.id]??rules.messages[s.phase];
 let bottom=inputY+t('inputHeight');
 if(open){
  const height=s.phase==='ready'?Math.min(s.results.length*t('rowHeight'),t('maxHeight')):t('rowHeight');
  const surface=frame(p,'overlay.surface',0,bottom+t('gap'),320,height,{fills:paint('surface'),cornerRadius:t('radius'),effects:[{type:'DROP_SHADOW',color:{r:0,g:0,b:0,a:0.2},offset:{x:0,y:2},radius:8,spread:0,visible:true}]});
  const viewport=frame(surface,'overlay.scroll.viewport',0,0,320,height,{clipsContent:true});
  const offset=s.id==='scroll-end'?s.results.length*t('rowHeight')-height:0;
  const list=frame(viewport,'list · listbox',0,-offset,320,s.phase==='ready'?s.results.length*t('rowHeight'):height);
  if(s.phase==='ready')s.results.forEach((r,j)=>{const row=frame(list,`option · ${r.key}${r.disabled?' · disabled':''}${r.key===s.activeKey?' · active':''}`,0,j*t('rowHeight'),320,t('rowHeight'),{fills:r.key===s.activeKey?paint('highlight'):[]});text(row,'option.label',r.label,t('paddingInline'),6,296,14,r.disabled?'disabled':'text');});
  else text(list,'popup.message',msg,t('paddingInline'),6,296);
  bottom+=t('gap')+height;
 }
 text(p,'status · role=status',msg,0,bottom+t('statusGap'),320,t('statusFontSize'),s.phase==='error'?'error':'muted');
 expectations.push({id:s.id,inputY,popupVisible:open,statusY:bottom+t('statusGap'),message:msg,options:open&&s.phase==='ready'?s.results.length:0});
}
const bytes=await exportFigFile(g,undefined,undefined,undefined,false);await fs.writeFile(path.join(out,'autocomplete.fig'),bytes);
const saved=await fs.readFile(path.join(out,'autocomplete.fig'));const rg=await parseFigFile(saved.buffer.slice(saved.byteOffset,saved.byteOffset+saved.byteLength),{populate:'all'});
const nodes=[...rg.getAllNodes()], find=(p,n)=>p.childIds.map(id=>rg.getNode(id)).find(x=>x.name===n);
const rb=nodes.find(n=>n.name===board.name);assert(rb);const checks=[];
for(const e of expectations){const p=find(rb,e.id);assert(p);const input=find(p,'input');assert.equal(input.y,e.inputY);assert.equal(input.width,320);assert.equal(input.height,44);const surface=find(p,'overlay.surface');assert.equal(Boolean(surface),e.popupVisible);const st=find(p,'status · role=status');assert.equal(st.text,e.message);assert.equal(st.y,e.statusY);if(surface){assert.equal(surface.x,input.x);assert.equal(surface.y,input.y+44+8);const vp=find(surface,'overlay.scroll.viewport');assert.equal(vp.clipsContent,true);const list=find(vp,'list · listbox');assert.equal(list.childIds.filter(id=>rg.getNode(id).type==='FRAME').length,e.options);if(e.id==='scroll-end'){assert.equal(list.y,-64);assert.equal(list.childIds.length,7);const last=rg.getNode(list.childIds[6]);assert.equal(last.y+list.y+last.height,160);assert(last.name.includes('active'));}}checks.push(e.id+' passed');}
assert.equal(nodes.filter(n=>n.type==='TEXT').length,[...g.getAllNodes()].filter(n=>n.type==='TEXT').length);
const png=await headlessRenderNodes(rg,rg.getPages()[0].id,[rb.id],{scale:1,format:'PNG'});assert(png);await fs.writeFile(path.join(out,'preview.png'),png);
await fs.writeFile(path.join(out,'checks.json'),JSON.stringify({writer:'@open-pencil/core exportFigFile 0.16.0',reader:'parseFigFile populate=all',bytes:saved.length,nodes:nodes.length,editableTextNodes:nodes.filter(n=>n.type==='TEXT').length,checks,expectations},null,2));
console.log(JSON.stringify({bytes:saved.length,nodes:nodes.length,checks}));
