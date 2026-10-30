// Shared presentation template only. No component values or internal coordinates are authored here.
import {readFileSync} from 'node:fs';
import {resolveCaseThemes} from './themes.mjs';
import {computeDescendantVisualBounds} from './node_modules/@open-pencil/scene-graph/dist/geometry.js';
export const TEMPLATE_URL=new URL('./templates/presentation.json',import.meta.url);
export function validateTemplate(value){
 if(!value||value.version!=='native-presentation/1')throw Error('Unsupported presentation template version');
 for(const key of ['columns','margin','gap','padding','captionHeight','captionGap','headerHeight','footerHeight','minCardWidth','cardRadius','borderWeight'])if(!Number.isFinite(value[key])||value[key]<=0)throw Error('Invalid presentation template: '+key);
 if(!Number.isInteger(value.columns)||value.columns<1||value.columns>4)throw Error('Invalid column count');
 for(const key of ['background','surface','border','text','muted'])if(!/^#[0-9A-F]{6}$/.test(value.colors?.[key]))throw Error('Invalid presentation color: '+key);
 for(const key of ['border','caption'])if(!/^#[0-9A-F]{6}$/.test(value.darkCard?.[key]))throw Error('Invalid dark-card color: '+key);
 for(const key of ['titleSize','subtitleSize','captionSize','footerSize'])if(!Number.isFinite(value.typography?.[key])||value.typography[key]<=0)throw Error('Invalid presentation typography: '+key);
 if(![400,700].includes(value.typography.titleWeight))throw Error('Unsupported title weight');
 return Object.freeze({...value,colors:Object.freeze({...value.colors}),darkCard:Object.freeze({...value.darkCard}),typography:Object.freeze({...value.typography})});
}
export const STYLE=validateTemplate(JSON.parse(readFileSync(TEMPLATE_URL,'utf8')));
const omit=new Set(['id','parentId','childIds','source','derivedLayout','textPicture','derivedTextGlyphs','textPathData','textPathBox']);
const canonical=v=>Array.isArray(v)?v.map(canonical):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,canonical(v[k])])):v;
export function snapshot(graph,node,root=true){
 const props=Object.fromEntries(Object.entries(node).filter(([k])=>!omit.has(k)&&!(root&&['x','y'].includes(k))));
 return {props:canonical(props),children:node.childIds.map(id=>snapshot(graph,graph.getNode(id),false))};
}
export function selectCases(graph,ids){
 if(!ids.length||new Set(ids).size!==ids.length||ids.some(x=>typeof x!=='string'||!x))throw Error('Case ids must be unique nonempty strings');
 const pages=graph.getPages();if(pages.length!==1)throw Error('This adapter requires a single input page');
 const roots=pages[0].childIds.map(id=>graph.getNode(id));
 return ids.map(id=>{
  const matches=roots.filter(n=>['FRAME','COMPONENT','GROUP','INSTANCE'].includes(n.type)&&(n.name===id||n.name.endsWith(' / '+id)));
  if(matches.length!==1)throw Error(`Expected one top-level component group for case ${id}, found ${matches.length}`);
  const n=matches[0];if(!n.visible)throw Error(`Case group ${id} is hidden`);
  const walk=node=>{if(node.rotation||node.flipX||node.flipY)throw Error('Rotated/flipped nodes are not supported by this initial bounds adapter');for(const c of node.childIds)walk(graph.getNode(c));};walk(n);
  return n;
 });
}
export function caseBounds(graph,n){
 const b=computeDescendantVisualBounds([n.id],id=>graph.getNode(id),id=>graph.getAbsolutePosition(id));
 if(!b)throw Error('No visible bounds: '+n.name);const p=graph.getAbsolutePosition(n.id);
 return {minX:b.minX-p.x,minY:b.minY-p.y,maxX:b.maxX-p.x,maxY:b.maxY-p.y};
}
export function plan(bounds,columns=STYLE.columns){
 if(!Number.isInteger(columns)||columns<1||columns>4||!bounds.length)throw Error('Use 1–4 columns and at least one case');
 if(bounds.some(b=>Object.values(b).some(v=>!Number.isFinite(v))||b.maxX<b.minX||b.maxY<b.minY))throw Error('Invalid visual bounds');
 const left=Math.max(0,...bounds.map(b=>-b.minX)),top=Math.max(0,...bounds.map(b=>-b.minY));
 const cardWidth=Math.ceil(Math.max(STYLE.minCardWidth,STYLE.padding*2+left+Math.max(...bounds.map(b=>b.maxX)))/8)*8;
 const contentY=STYLE.padding+STYLE.captionHeight+STYLE.captionGap+top;
 let y=STYLE.margin+STYLE.headerHeight;const cards=[];
 for(let start=0;start<bounds.length;start+=columns){
  const row=bounds.slice(start,start+columns),height=Math.ceil((contentY+Math.max(...row.map(b=>b.maxY))+STYLE.padding)/8)*8;
  row.forEach((b,c)=>cards.push({index:start+c,x:STYLE.margin+c*(cardWidth+STYLE.gap),y,width:cardWidth,height,componentX:STYLE.padding+left,componentY:contentY}));
  y+=height+STYLE.gap;
 }
 return {style:STYLE.version,columns,width:STYLE.margin*2+Math.min(columns,bounds.length)*cardWidth+(Math.min(columns,bounds.length)-1)*STYLE.gap,
 height:y-STYLE.gap+STYLE.margin+STYLE.footerHeight,cards};
}
export function apply(graph,cases,ids,layout,{title,subtitle,fontFamily,caseThemes=resolveCaseThemes(ids,{},null,STYLE)}){
 if(caseThemes.length!==cases.length)throw Error('Case-theme count mismatch');
 const page=graph.getPages()[0],oldChildren=[...page.childIds],keep=new Set(cases.map(n=>n.id));
 const retained=new Set();const collect=n=>{retained.add(n.id);for(const id of n.childIds)collect(graph.getNode(id));};cases.forEach(collect);
 for(const id of retained){const n=graph.getNode(id);if(n.componentId&&!retained.has(n.componentId))throw Error('Component dependencies outside selected cases require a separate transfer adapter');}
 const solid=hex=>({type:'SOLID',color:{r:parseInt(hex.slice(1,3),16)/255,g:parseInt(hex.slice(3,5),16)/255,b:parseInt(hex.slice(5,7),16)/255,a:1},opacity:1,visible:true});
 const board=graph.createNode('FRAME',page.id,{name:'Presentation',x:0,y:0,width:layout.width,height:layout.height,fills:[solid(STYLE.colors.background)],clipsContent:false,layoutMode:'NONE'});
 const text=(parent,name,x,y,w,h,value,size,weight=400,color=STYLE.colors.text)=>graph.createNode('TEXT',parent,{name,x,y,width:w,height:h,text:value,fontFamily,fontWeight:weight,fontSize:size,lineHeight:Math.ceil(size*1.5),textAutoResize:'NONE',fills:[solid(color)]});
 text(board.id,'presentation/title',STYLE.margin,STYLE.margin,layout.width-STYLE.margin*2,44,title,STYLE.typography.titleSize,STYLE.typography.titleWeight);
 text(board.id,'presentation/subtitle',STYLE.margin,STYLE.margin+52,layout.width-STYLE.margin*2,28,subtitle,STYLE.typography.subtitleSize,400,STYLE.colors.muted);
 cases.forEach((node,i)=>{
  const c=layout.cards[i],theme=caseThemes[i];const card=graph.createNode('FRAME',board.id,{name:'Case / '+ids[i],x:c.x,y:c.y,width:c.width,height:c.height,
   fills:[solid(theme.background)],strokes:[{...solid(theme.border),weight:STYLE.borderWeight,align:'INSIDE'}],cornerRadius:STYLE.cardRadius,clipsContent:false,layoutMode:'NONE'});
  text(card.id,'presentation/caption',STYLE.padding,STYLE.padding,c.width-STYLE.padding*2,STYLE.captionHeight,`${String(i+1).padStart(2,'0')}  ${ids[i]}`,STYLE.typography.captionSize,400,theme.caption);
  graph.reparentNode(node.id,card.id);graph.updateNode(node.id,{x:c.componentX,y:c.componentY});
 });
 text(board.id,'presentation/footer',STYLE.margin,layout.height-STYLE.margin-24,layout.width-STYLE.margin*2,24,`Statisches Design · Originalgröße 1:1 · ${STYLE.version}`,STYLE.typography.footerSize,400,STYLE.colors.muted);
 for(const id of oldChildren)if(!keep.has(id))graph.deleteNode(id);
 graph.updateNode(page.id,{name:title+' · Übersicht'});return board;
}
export function assertContained(graph,cases,layout,caseThemes=resolveCaseThemes(cases.map(n=>n.name),{},null,STYLE)){
 if(caseThemes.length!==cases.length)throw Error('Case-theme count mismatch');
 const matches=(paint,hex)=>paint?.type==='SOLID'&&paint.visible!==false&&(paint.opacity??1)===1&&Math.abs((paint.color?.a??1)-1)<1e-6&&['r','g','b'].every((k,j)=>Math.abs(paint.color[k]-parseInt(hex.slice(1+j*2,3+j*2),16)/255)<1e-6);
 for(let i=0;i<cases.length;i++){
  const n=cases[i],b=caseBounds(graph,n),c=layout.cards[i];
  const card=graph.getNode(n.parentId),theme=caseThemes[i];
  const captions=card.childIds.map(id=>graph.getNode(id)).filter(n=>n.name==='presentation/caption');
  if(card.fills.length!==1||card.strokes.length!==1||!matches(card.fills[0],theme.background)||!matches(card.strokes[0],theme.border)||captions.length!==1||captions[0].fills.length!==1||!matches(captions[0].fills[0],theme.caption))throw Error('Presentation theme changed: '+n.name);
  if(Math.abs(n.x-c.componentX)>0.01||Math.abs(n.y-c.componentY)>0.01||card.clipsContent||card.width!==c.width||card.height!==c.height||card.x!==c.x||card.y!==c.y)throw Error('Presentation placement/card changed: '+n.name);
  if(c.componentX+b.minX<STYLE.padding-0.01||c.componentY+b.minY<STYLE.padding+STYLE.captionHeight+STYLE.captionGap-0.01||c.componentX+b.maxX>c.width-STYLE.padding+0.01||c.componentY+b.maxY>c.height-STYLE.padding+0.01)throw Error('Visible component content exceeds card: '+n.name);
 }
}
