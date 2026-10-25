import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
const out=path.dirname(fileURLToPath(import.meta.url));
const root=path.resolve(out,'../../../../..');
const pkg=path.join(root,'tools/openpencil/node_modules/@open-pencil');
const {SceneGraph}=await import(path.join(pkg,'scene-graph/dist/index.js'));
const {exportFigFile,parseFigFile,headlessRenderNodes,renderNodesToSVG}=await import(path.join(pkg,'core/dist/io/index.js'));
const read=async f=>JSON.parse(await fs.readFile(path.join(root,'components',f),'utf8'));
const tokens=await read('tokens.json'), stories=(await read('autocomplete/stories.json')).stories, rules=await read('autocomplete/accessibility.rules.json');
const resolve=v=>{if(typeof v==='string'&&v.startsWith('{'))return resolve(v.slice(1,-1).split('.').reduce((a,k)=>a[k],tokens).$value);return v?.unit==='px'?v.value:v;};
const t=Object.fromEntries(Object.entries(tokens.autocomplete).map(([k,v])=>[k,resolve(v.$value)]));
const col=k=>{const v=t[k];return {r:v.components[0],g:v.components[1],b:v.components[2],a:v.alpha};};
const fill=k=>[{type:'SOLID',color:col(k),opacity:1,visible:true}];
const g=new SceneGraph();const p=g.getPages()[0]??g.addPage('Autocomplete');p.name='Autocomplete · zehn Darstellungsfälle';
const board=g.createNode('FRAME',p.id,{name:'Autocomplete · Definitionsbibliothek',width:1160,height:1390,fills:fill('surface'),clipsContent:false});
const frame=(par,name,x,y,w,h,extra={})=>g.createNode('FRAME',par.id,{name,x,y,width:w,height:h,fills:[],clipsContent:false,...extra});
const text=(par,name,str,x,y,w,size=t.fontSize,color='text')=>g.createNode('TEXT',par.id,{name,text:str,x,y,width:w,height:t.lineHeight,fontFamily:t.fontFamily,fontSize:size,fontWeight:400,lineHeight:t.lineHeight,textAutoResize:'NONE',fills:fill(color)});
text(board,'Seitentitel','Autocomplete · 0.1.0',40,24,1080);
const mapping=[];
for(const [i,s]of stories.entries()){
 const x=40+(i%3)*380,y=80+Math.floor(i/3)*330;
 text(board,`Fallbezeichnung ${s.id}`,s.id,x,y,320,t.fontSize,'muted');
 const visible=rules.projections[s.phase].popupVisible&&s.inputs.enabled;
 const h=visible?(s.phase==='ready'?Math.min(s.results.length*t.rowHeight,t.maxHeight):t.rowHeight):0;
 const inputY=t.lineHeight+t.labelGap, popupY=inputY+t.inputHeight+t.gap;
 const statusY=visible?popupY+h+t.statusGap:inputY+t.inputHeight+t.statusGap;
 const c=frame(board,`Autocomplete / ${s.id}`,x,y+28,t.width,statusY+t.lineHeight);
 text(c,'label',s.inputs.label,0,0,t.width);
 const input=frame(c,'input · role=combobox',0,inputY,t.width,t.inputHeight,{fills:fill('surface'),cornerRadius:t.radius,strokes:[{...fill(s.phase==='closed'?'border':'focus')[0],weight:t.borderWidth,align:'INSIDE'}]});
 const inputValue=s.value?s.results.find(r=>r.key===s.value).label:s.inputs.query;
 text(input,inputValue?'query':'placeholder',inputValue||s.inputs.placeholder,t.paddingInline,(t.inputHeight-t.lineHeight)/2,t.width-2*t.paddingInline,t.fontSize,!s.inputs.enabled?'disabled':inputValue?'text':'muted');
 let msg=s.value?rules.messages.selected.replace('{label}',inputValue):s.id==='disabled'?rules.messages.disabled:s.phase==='ready'?rules.messages.results.replace('{count}',s.results.length):rules.messages[s.phase];
 if(visible){
 const surface=frame(c,'overlay.surface',0,popupY,t.width,h,{fills:fill('surface'),cornerRadius:t.radius,effects:[{type:'DROP_SHADOW',color:{r:0,g:0,b:0,a:.2},offset:{x:0,y:2},radius:8,spread:0,visible:true}]});
 const viewport=frame(surface,'overlay.scroll.viewport',0,0,t.width,h,{clipsContent:true});
 const offset=s.id==='scroll-end'?s.results.length*t.rowHeight-h:0;
 const content=frame(viewport,'overlay.scroll.content',0,-offset,t.width,s.phase==='ready'?s.results.length*t.rowHeight:h);
 const list=frame(content,'list · role=listbox',0,0,t.width,content.height);
 if(s.phase==='ready')s.results.forEach((r,j)=>{const row=frame(list,`option / ${r.key}${r.key===s.activeKey?' · active':''}${r.disabled?' · disabled':''}`,0,j*t.rowHeight,t.width,t.rowHeight,{fills:r.key===s.activeKey?fill('highlight'):[]});text(row,`label / ${r.key}`,r.label,t.paddingInline,6,t.width-2*t.paddingInline,t.fontSize,r.disabled?'disabled':'text');});
 else {const row=frame(list,`message / ${s.phase}`,0,0,t.width,t.rowHeight);text(row,'message',msg,t.paddingInline,6,t.width-2*t.paddingInline);}
 }
 text(c,'status · role=status',msg,0,statusY,t.width,t.statusFontSize,s.phase==='error'?'error':'muted');
 mapping.push({id:s.id,phase:s.phase,componentId:c.id,popupVisible:visible,viewportHeight:h,statusY,activeKey:s.activeKey,value:s.value});
}
const fig=await exportFigFile(g,undefined,undefined,p.id,false);await fs.writeFile(path.join(out,'autocomplete.fig'),fig);
const saved=await fs.readFile(path.join(out,'autocomplete.fig'));
const re=await parseFigFile(saved.buffer.slice(saved.byteOffset,saved.byteOffset+saved.byteLength),{populate:'all'});
const nodes=[...re.getAllNodes()];const find=name=>nodes.find(n=>n.name===name);
assert.equal(stories.length,10);for(const s of stories)assert(find(`Autocomplete / ${s.id}`));
assert.equal(nodes.filter(n=>n.name.startsWith('option /')).length,21);
const end=find('Autocomplete / scroll-end');const surf=re.getNode(end.childIds.find(id=>re.getNode(id).name==='overlay.surface'));const vp=re.getNode(surf.childIds[0]);const cont=re.getNode(vp.childIds[0]);assert.equal(vp.height,160);assert.equal(vp.clipsContent,true);assert.equal(cont.y,-64);assert.equal(nodes.filter(n=>n.name==='option / zuerich · active').length,1);
for(const s of stories){const c=find(`Autocomplete / ${s.id}`);const inp=c.childIds.map(id=>re.getNode(id)).find(n=>n.name.startsWith('input'));assert.equal(inp.width,320);assert.equal(inp.height,44);assert.equal(inp.y,28);}
const rb=find(board.name);const rp=re.getPages()[0];
await fs.writeFile(path.join(out,'preview.svg'),renderNodesToSVG(re,rp.id,[rb.id]));
const png=await headlessRenderNodes(re,rp.id,[rb.id],{scale:1,format:'PNG'});assert(png);await fs.writeFile(path.join(out,'preview.png'),png);
const files=[];async function walk(d){for(const f of await fs.readdir(d,{withFileTypes:true})){const full=path.join(d,f.name);if(f.isDirectory())await walk(full);else files.push({source:path.relative(root,full),sha256:crypto.createHash('sha256').update(await fs.readFile(full)).digest('hex')});}}await walk(path.join(root,'components'));
await fs.writeFile(path.join(out,'checks.json'),JSON.stringify({toolVersion:'0.16.0',savedFileBytes:saved.length,reimportNodes:nodes.length,checks:{tenCases:true,twentyOneEditableOptions:true,inputGeometry:true,scrollEndClippingAndOffset:true,originalReaderReimport:true,pngFromReimport:true},cases:mapping,sources:files},null,2));
console.log(JSON.stringify({bytes:saved.length,nodes:nodes.length,pngBytes:png.length}));
