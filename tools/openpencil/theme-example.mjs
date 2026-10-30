// New visual proposal derived from example; never edits its definition or source FIG.
import {readFile,writeFile,stat} from 'node:fs/promises';
import {resolve,join,relative} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import * as core from './node_modules/@open-pencil/core/dist/index.js';
import * as raster from './node_modules/@open-pencil/core/dist/io/formats/raster/headless.js';
import {snapshot,selectCases,caseBounds,plan,apply,assertContained,TEMPLATE_URL,STYLE} from './layout.mjs';
import {resolveCaseThemes} from './themes.mjs';
const repo=resolve(fileURLToPath(new URL('../../',import.meta.url))),out=join(repo,'examples/autocomplete/output/openpencil/theme-preview');
const sha=b=>createHash('sha256').update(b).digest('hex');
for(const name of ['autocomplete.fig','preview.png','preview-check.json']){try{await stat(join(out,name));throw Error('Existing proof must not be overwritten: '+name);}catch(e){if(e.code!=='ENOENT')throw e;}}
const sourcePath=join(repo,'examples/autocomplete/reproducibility/run-04/builder-a/autocomplete.fig'),tokenPath=join(repo,'libraries/example/tokens.json'),proposalPath=join(out,'theme-proposal.json');
const bytes=await readFile(sourcePath),sourceSha=sha(bytes),tokenBytes=await readFile(tokenPath),proposalBytes=await readFile(proposalPath),tokens=JSON.parse(tokenBytes),proposal=JSON.parse(proposalBytes);
const g=await core.parseFigFile(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),{populate:'all'}),page=g.getPages()[0],original=selectCases(g,['ready','disabled']);
const paintHex=p=>p?.type==='SOLID'?'#'+['r','g','b'].map(k=>Math.round(p.color[k]*255).toString(16).padStart(2,'0')).join('').toUpperCase():null;
const fromHex=hex=>({r:parseInt(hex.slice(1,3),16)/255,g:parseInt(hex.slice(3,5),16)/255,b:parseInt(hex.slice(5,7),16)/255,a:1});
const replacements=new Map(Object.entries(proposal.tokens.dark).map(([key,value])=>{
 const t=tokens.autocomplete[key].$value;return ['#'+t.components.map(v=>Math.round(v*255).toString(16).padStart(2,'0')).join('').toUpperCase(),value];
}));
const cases=[],ids=Object.keys(proposal.cases),changes=[];
for(const node of original){
 for(const mode of ['light','dark']){
  const cloned=g.cloneTree(node.id,page.id,{name:mode+'-'+node.name});if(!cloned)throw Error('Clone failed');cases.push(cloned);
  if(mode==='dark'){
   const recolor=n=>{
    for(const field of ['fills','strokes']){const paints=n[field].map(p=>{const old=paintHex(p),color=replacements.get(old);if(!color)return p;changes.push({case:cloned.name,node:n.name,field,from:old,to:color});return {...p,color:fromHex(color)};});g.updateNode(n.id,{[field]:paints});}
    for(const id of n.childIds)recolor(g.getNode(id));
   };recolor(cloned);
  }
 }
}
// Normalize the newly constructed candidate by serializing before taking native invariants.
const raw=await core.exportFigFile(g),graph=await core.parseFigFile(raw.buffer.slice(raw.byteOffset,raw.byteOffset+raw.byteLength),{populate:'all'});
const selected=selectCases(graph,ids),before=selected.map(n=>snapshot(graph,n)),themes=resolveCaseThemes(ids,proposal.cases,proposal.tokens,STYLE),layout=plan(selected.map(n=>caseBounds(graph,n)));
const fonts=JSON.parse(execFileSync('python3',[join(repo,'tools/fonts/check.py'),'--library','example'],{encoding:'utf8'}));if(fonts.overall!=='PASS_LIMITED')throw Error('Fonts unavailable');
apply(graph,selected,ids,layout,{title:'Autocomplete · Light / Dark',subtitle:'example · Darkmode-Farben als separater Vorschlag · keine Änderung der Definition',fontFamily:'Inter',caseThemes:themes});
let networkAttempts=0;globalThis.fetch=async()=>{networkAttempts++;throw Error('Network disabled');};
await raster.initCanvasKit();
for(const f of fonts.faces){const a=f.assets.find(a=>a.format==='truetype'),b=await readFile(join(repo,a.path));if(sha(b)!==a.sha256)throw Error('Font hash mismatch');core.fontManager.markLoaded(f.family,f.openpencilStyle,b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),'library-asset:'+a.sha256);}
const fig=await core.exportFigFile(graph),readback=await core.parseFigFile(fig.buffer.slice(fig.byteOffset,fig.byteOffset+fig.byteLength),{populate:'all'}),readCases=ids.map(id=>[...readback.getAllNodes()].find(n=>n.name===id));
const verify=()=>{assertContained(readback,readCases,layout,themes);for(let i=0;i<ids.length;i++)if(JSON.stringify(before[i])!==JSON.stringify(snapshot(readback,readCases[i])))throw Error('Presentation changed candidate component: '+ids[i]);};verify();
const p=readback.getPages()[0],png=await raster.headlessRenderNodes(readback,p.id,p.childIds,{scale:1,format:'PNG'});if(!png||networkAttempts)throw Error('Rendering failed');verify();
if(sha(await readFile(sourcePath))!==sourceSha||sha(await readFile(tokenPath))!==sha(tokenBytes))throw Error('Original input changed');
await writeFile(join(out,'autocomplete.fig'),fig,{flag:'wx'});await writeFile(join(out,'preview.png'),png,{flag:'wx'});
const receipt={overall:'PASS_LIMITED',release:false,selectedLibrary:'example',scope:'separate-light-dark-presentation-proposal',
 inputs:[{path:relative(repo,sourcePath),sha256:sourceSha},{path:relative(repo,tokenPath),sha256:sha(tokenBytes)},{path:relative(repo,proposalPath),sha256:sha(proposalBytes)}],
 renderer:[fileURLToPath(TEMPLATE_URL),fileURLToPath(import.meta.url),join(repo,'tools/openpencil/layout.mjs'),join(repo,'tools/openpencil/themes.mjs')].map(path=>({path:relative(repo,path),sha256:sha(execFileSync('cat',[path]))})),
 caseThemes:ids.map((id,i)=>({id,...themes[i]})),layout,intentionalProposalColorChanges:changes,
 cases:ids.map((id,i)=>({id,beforeSha256:sha(JSON.stringify(before[i])),afterSha256:sha(JSON.stringify(snapshot(readback,readCases[i]))),presentationUnchanged:true})),networkAttempts,
 outputs:{'autocomplete.fig':sha(fig),'preview.png':sha(png)},
 notChecked:['Dark palette is a new proposal, not normative example definition','No runtime/ARIA or contrast certification','No live GUI roundtrip']};
await writeFile(join(out,'preview-check.json'),JSON.stringify(receipt,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify({overall:receipt.overall,output:out,cases:ids.length}));
