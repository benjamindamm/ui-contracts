// Reusable local-font proof: validate assets, register exact TTF bytes, export/read FIG, render PNG and web specimen.
import {readFile,writeFile,mkdir,readdir,realpath} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {resolve,relative,join,dirname} from 'node:path';
const repo=fileURLToPath(new URL('../../',import.meta.url));
const args=process.argv.slice(2);
if(args.length!==2)throw Error('Usage: node tools/fonts/preview.mjs LIBRARY NEW_OUTPUT_DIRECTORY');
const [library,outputArg]=args;let output=resolve(outputArg);
// Canonicalize even a new output directory before enforcing source boundaries.
let ancestor=output;while(true){try{const canonical=await realpath(ancestor);output=resolve(canonical,relative(ancestor,output));break;}catch(e){if(e.code!=='ENOENT')throw e;ancestor=dirname(ancestor);}}
const inside=(parent,p)=>p===parent||p.startsWith(parent+'/');
if(inside(join(repo,'libraries'),output)||inside(join(repo,'examples/autocomplete'),output))throw Error('Output must not overwrite library or historical examples');
await mkdir(output,{recursive:true});if((await readdir(output)).length)throw Error('Choose an empty/new output directory');
const assets=JSON.parse(execFileSync('python3',[join(repo,'tools/fonts/check.py'),'--repo',repo,'--library',library],{encoding:'utf8'}));
if(assets.overall!=='PASS_LIMITED')throw Error('Asset validation did not pass');
const core=await import(pathToFileURL(join(repo,'tools/openpencil/node_modules/@open-pencil/core/dist/index.js')));
const headless=await import(pathToFileURL(join(repo,'tools/openpencil/node_modules/@open-pencil/core/dist/io/formats/raster/headless.js')));
const sha=b=>createHash('sha256').update(b).digest('hex');
let networkAttempts=0;globalThis.fetch=async()=>{networkAttempts++;throw Error('Network disabled for local font proof');};
const ck=await headless.initCanvasKit();
const sample='Stadt auswählen – ÄÖÜ äöü ß € … 0123456789 Zürich';
const fonts=[];
for(const face of assets.faces){
 if(core.weightToStyle(face.weight)!==face.openpencilStyle)throw Error('Runtime style differs from verified weight');
 const file=face.assets.find(a=>a.format==='truetype');const bytes=await readFile(join(repo,file.path));
 if(sha(bytes)!==file.sha256)throw Error('Font changed after validation');
 const data=bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength);
 const tf=ck.Typeface.MakeFreeTypeFaceFromData(data);if(!tf||tf.getFamilyName()!==face.family)throw Error('CanvasKit rejected declared font family');
 const glyphs=Array.from(tf.getGlyphIDs(sample));if(glyphs.length!==Array.from(sample).length||glyphs.some(x=>x===0))throw Error('Missing sample glyphs');
 tf.delete();core.fontManager.markLoaded(face.family,face.openpencilStyle,data,'library-asset:'+file.sha256);
 fonts.push({family:face.family,weight:face.weight,style:face.openpencilStyle,sha256:file.sha256,sampleGlyphCount:glyphs.length,missingGlyphs:0});
}
const graph=new core.SceneGraph();const page=graph.getPages()[0];graph.updateNode(page.id,{name:'Local font assets'});
const white={type:'SOLID',color:{r:1,g:1,b:1,a:1},opacity:1,visible:true};
const dark={type:'SOLID',color:{r:0.09,g:0.17,b:0.3,a:1},opacity:1,visible:true};
const frame=graph.createNode('FRAME',page.id,{name:'Font specimen',x:0,y:0,width:920,height:72+assets.faces.length*125,fills:[white]});
const expected=[];
for(let i=0;i<assets.faces.length;i++){
 const f=assets.faces[i];
 for(const [label,text,size,dy] of [['face',`${f.family} · ${f.openpencilStyle} · ${f.weight}`,18,0],['sample',sample,24,38]]){
  graph.createNode('TEXT',frame.id,{name:`${f.family}-${f.weight}-${label}`,x:24,y:28+i*125+dy,width:870,height:42,
   text,fontFamily:f.family,fontWeight:f.weight,fontSize:size,lineHeight:36,textAutoResize:'NONE',fills:[dark]});
  expected.push({text,fontFamily:f.family,fontWeight:f.weight});
 }
}
const figBytes=await core.exportFigFile(graph);await writeFile(join(output,'fonts.fig'),figBytes,{flag:'wx'});
const parsed=await core.parseFigFile(figBytes.buffer.slice(figBytes.byteOffset,figBytes.byteOffset+figBytes.byteLength),{populate:'all'});
const textNodes=[...parsed.getAllNodes()].filter(n=>n.type==='TEXT');
if(textNodes.length!==expected.length||expected.some((e,i)=>Object.entries(e).some(([k,v])=>textNodes[i][k]!==v)))throw Error('FIG font roundtrip mismatch');
const png=await headless.headlessRenderNodes(parsed,parsed.getPages()[0].id,parsed.getPages()[0].childIds,{scale:1,format:'PNG'});
if(!png||networkAttempts)throw Error('Render failed or attempted remote font loading');
for(const f of fonts)if(core.fontManager.loadedFontSource(f.family,f.style)!=='library-asset:'+f.sha256)throw Error('Font source changed during rendering');
await writeFile(join(output,'fonts.png'),png,{flag:'wx'});
const css=assets.faces.map(f=>{const w=f.assets.find(a=>a.format==='woff2');const path=relative(output,join(repo,w.path)).split('\\').join('/');
 return `@font-face { font-family: ${JSON.stringify(f.family)}; font-style: normal; font-weight: ${f.weight}; font-display: block; src: url(${JSON.stringify(path)}) format("woff2"); }`;}).join('\n')+'\n';
await writeFile(join(output,'fonts.css'),css,{flag:'wx'});
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
const html=`<!doctype html><html lang="de"><meta charset="utf-8"><title>Lokale Library-Schriften</title><link rel="stylesheet" href="fonts.css"><style>body{padding:24px;background:white;color:#172b4d}p{font-size:24px;line-height:1.5}</style><h1>Lokale Schriftdateien</h1><div id="specimen">${assets.faces.map(f=>`<p data-family="${esc(f.family)}" data-weight="${f.weight}" style='font-family:${esc(JSON.stringify(f.family))};font-weight:${f.weight}'>${esc(f.family)} ${f.weight}: ${esc(sample)}</p>`).join('')}</div></html>`;
await writeFile(join(output,'index.html'),html,{flag:'wx'});
const receipt={overall:'PASS_LIMITED',release:false,library,scope:'local-TTF-registration-and-static-font-specimen',sample,fonts,networkAttempts,
 figReadback:{textNodes:textNodes.length,checks:expected.length*3,passed:true},
 outputs:Object.fromEntries(await Promise.all(['fonts.fig','fonts.png','fonts.css','index.html'].map(async f=>[f,sha(await readFile(join(output,f)))]))),
 notChecked:['Live editor import/font availability','Pixel identity across browsers/platforms','All Unicode glyphs','Native app embedding']};
await writeFile(join(output,'openpencil-receipt.json'),JSON.stringify(receipt,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({overall:receipt.overall,fonts:fonts.length,networkAttempts,textNodes:textNodes.length,output}));
