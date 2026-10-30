import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdtemp,mkdir,cp,rm,copyFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join,resolve} from 'node:path';
import {randomUUID} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {SceneGraph,exportFigFile,parseFigFile} from './node_modules/@open-pencil/core/dist/index.js';
import {resolveCaseThemes} from './themes.mjs';
import {STYLE,validateTemplate,plan,apply,snapshot,caseBounds,assertContained} from './layout.mjs';
const root=resolve(new URL('../../',import.meta.url).pathname);
const tokens={canvas:{$type:'color',$value:'#101827'},alias:{$value:'{canvas}'},white:{$value:{colorSpace:'srgb',components:[1,1,1],alpha:1}}};
const mapping={dark:{mode:'dark',backgroundToken:'alias'},light:{mode:'light',backgroundToken:'white'}};
const ids=['light','dark'];
function fixture(){const graph=new SceneGraph(),page=graph.getPages()[0];const cases=ids.map((name,i)=>{
 const n=graph.createNode('FRAME',page.id,{name,x:i*400,y:0,width:280,height:80,fills:[],clipsContent:false});
 graph.createNode('FRAME',n.id,{name:'button',x:12,y:12,width:240,height:44,cornerRadius:22,fills:[{type:'SOLID',visible:true,opacity:1,color:i?{r:.16,g:.24,b:.36,a:1}:{r:.9,g:.93,b:.97,a:1}}]});return n;
});return {graph,cases};}
test('Explicit dark/light cases resolve opaque background tokens and aliases',()=>{const themes=resolveCaseThemes(ids,mapping,tokens,STYLE);assert.equal(themes[1].background,'#101827');assert.equal(themes[1].caption,STYLE.darkCard.caption);assert.equal(themes[0].background,'#FFFFFF');});
test('Unspecified mode remains the neutral default without claiming a theme',()=>{assert.equal(resolveCaseThemes(['dark-looking-name'],{},null,STYLE)[0].mode,'unspecified');});
test('A dark case without an explicit valid background is rejected',()=>{for(const entry of [{mode:'dark'},{mode:'dark',backgroundToken:'missing'},{mode:'sepia',backgroundToken:'canvas'},{mode:'dark',backgroundToken:'canvas',guess:true}])assert.throws(()=>resolveCaseThemes(['dark'],{dark:entry},tokens,STYLE));});
test('Unknown case names, invalid maps and cyclic aliases are rejected',()=>{assert.throws(()=>resolveCaseThemes(ids,{other:mapping.dark},tokens,STYLE));for(const m of [null,[],false])assert.throws(()=>resolveCaseThemes(ids,m,tokens,STYLE));assert.throws(()=>resolveCaseThemes(['dark'],{dark:{mode:'dark',backgroundToken:'cycle'}},{cycle:{$value:'{cycle}'}},STYLE));});
test('Non-color, transparent and out-of-range tokens never silently fall back',()=>{for(const value of [{$type:'dimension',$value:'#112233'},{$value:'transparent'},{$value:{colorSpace:'srgb',components:[0,0,0],alpha:.5}},{$value:{colorSpace:'srgb',components:[-1,0,0]}}])assert.throws(()=>resolveCaseThemes(['dark'],{dark:{mode:'dark',backgroundToken:'bad'}},{bad:value},STYLE));});
test('Dark caption palette must be valid in the central template',()=>{const t=JSON.parse(JSON.stringify(STYLE));t.darkCard.caption='broken';assert.throws(()=>validateTemplate(t));});
test('Mixed-theme native FIG roundtrip preserves component subtrees and card colors',async()=>{
 let {graph,cases}=fixture();const initial=await exportFigFile(graph);graph=await parseFigFile(initial.buffer.slice(initial.byteOffset,initial.byteOffset+initial.byteLength),{populate:'all'});cases=ids.map(id=>[...graph.getAllNodes()].find(n=>n.name===id));
 const before=cases.map(n=>snapshot(graph,n)),themes=resolveCaseThemes(ids,mapping,tokens,STYLE),layout=plan(cases.map(n=>caseBounds(graph,n)));
 apply(graph,cases,ids,layout,{title:'Theme proof',subtitle:'Synthetic fixture',fontFamily:'Inter',caseThemes:themes});assertContained(graph,cases,layout,themes);
 const bytes=await exportFigFile(graph),parsed=await parseFigFile(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),{populate:'all'}),out=ids.map(id=>[...parsed.getAllNodes()].find(n=>n.name===id));
 assertContained(parsed,out,layout,themes);assert.deepEqual(out.map(n=>snapshot(parsed,n)),before);
 const board=[...parsed.getAllNodes()].find(n=>n.name==='Presentation');assert.ok(Math.abs(board.fills[0].color.r-248/255)<1e-6);
 const card=parsed.getNode(out[1].parentId);parsed.updateNode(card.id,{fills:[]});assert.throws(()=>assertContained(parsed,out,layout,themes),/theme changed/);
});
test('CLI binds theme inputs, renders mixed cards, and blocks missing dark background',async()=>{
 const temp=await mkdtemp(join(tmpdir(),'theme-card-')),libid='test-theme-'+randomUUID(),lib=join(root,'libraries',libid);
 try{
  await mkdir(join(lib,'components/control'),{recursive:true});await cp(join(root,'libraries/example/assets'),join(lib,'assets'),{recursive:true});await copyFile(join(root,'libraries/example/fonts.json'),join(lib,'fonts.json'));
  const base=JSON.parse(await readFile(join(root,'libraries/example/tokens.json'),'utf8'));Object.assign(base,tokens);await writeFile(join(lib,'tokens.json'),JSON.stringify(base));
  await writeFile(join(lib,'library.json'),JSON.stringify({components:{Control:'components/control/component.json'}}));await writeFile(join(lib,'components/control/component.json'),JSON.stringify({id:'fixture:Control',stories:'stories.json'}));await writeFile(join(lib,'components/control/stories.json'),JSON.stringify({stories:ids.map(id=>({id}))}));
  const f=fixture();for(let i=0;i<2;i++)f.graph.createNode('TEXT',f.cases[i].id,{name:'label',x:35,y:23,width:180,height:24,text:'Rounded button',fontFamily:'Inter',fontWeight:400,fontSize:16,fills:[{type:'SOLID',visible:true,opacity:1,color:i?{r:1,g:1,b:1,a:1}:{r:.1,g:.17,b:.3,a:1}}]});
  const input=join(temp,'raw.fig'),map=join(temp,'case-themes.json'),output=join(temp,'output');await writeFile(input,await exportFigFile(f.graph));await writeFile(map,JSON.stringify(mapping));
  const args=[join(root,'tools/openpencil/preview.mjs'),'--library',libid,'--component','Control','--input',input,'--output',output,'--case-themes',map];execFileSync('node',args,{stdio:'pipe'});
  const receipt=JSON.parse(await readFile(join(output,'preview-check.json'),'utf8'));assert.equal(receipt.overall,'PASS_LIMITED');assert.equal(receipt.caseThemes[1].background,'#101827');assert.equal(receipt.themeBindings.length,2);assert.ok(receipt.themeBindings.every(b=>/^[0-9a-f]{64}$/.test(b.sha256)));assert.ok(receipt.cases.every(c=>c.unchanged));assert.equal(receipt.networkAttempts,0);
  if(process.env.UI_CONTRACTS_PREVIEW_QA)await cp(output,process.env.UI_CONTRACTS_PREVIEW_QA,{recursive:true,errorOnExist:true,force:false});
  await writeFile(map,JSON.stringify({dark:{mode:'dark'}}));args[args.indexOf('--output')+1]=join(temp,'bad-output');assert.throws(()=>execFileSync('node',args,{stdio:'pipe'}));
 }finally{await rm(lib,{recursive:true,force:true});await rm(temp,{recursive:true,force:true});}
});
