// Read-only input FIG -> separate native presentation FIG, PNG and invariant receipt.
import {readFile,writeFile,mkdir,realpath,stat} from 'node:fs/promises';
import {resolve,dirname,relative,join} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {snapshot,selectCases,caseBounds,plan,apply,assertContained,STYLE,TEMPLATE_URL} from './layout.mjs';
import * as core from './node_modules/@open-pencil/core/dist/index.js';
import * as headless from './node_modules/@open-pencil/core/dist/io/formats/raster/headless.js';
const repo=resolve(fileURLToPath(new URL('../../',import.meta.url))),sha=b=>createHash('sha256').update(b).digest('hex');
const args=process.argv.slice(2),opt={};
if(args.length%2)throw Error('Usage: node tools/openpencil/preview.mjs --library ID --component KEY --input FILE.fig --output NEW_DIR [--definition-revision LABEL]');
for(let i=0;i<args.length;i+=2){if(!['--library','--component','--input','--output','--definition-revision'].includes(args[i])||opt[args[i]])throw Error('Unknown/duplicate option');opt[args[i]]=args[i+1];}
for(const k of ['--library','--component','--input','--output'])if(!opt[k])throw Error('Missing '+k);
if(!/^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$/.test(opt['--library']))throw Error('Invalid library id');
const lib=join(repo,'libraries',opt['--library']);if(await realpath(lib)!==lib)throw Error('Symlink library roots are unsupported');
async function boundFile(base,rel){if(typeof rel!=='string'||rel.startsWith('/')||rel.split('/').includes('..'))throw Error('Expected relative path without ..');const p=await realpath(join(base,rel));if(p!==base&&!p.startsWith(base+'/'))throw Error('Path escapes selected library');return p;}
const indexPath=await boundFile(lib,'library.json'),index=JSON.parse(await readFile(indexPath));
const cp=await boundFile(lib,index.components[opt['--component']]);const component=JSON.parse(await readFile(cp));
const storiesPath=await boundFile(dirname(cp),component.stories),stories=JSON.parse(await readFile(storiesPath));
const ids=stories.stories.map(s=>s.id),input=await realpath(resolve(opt['--input']));let output=resolve(opt['--output']);
let ancestor=output;while(true){try{output=resolve(await realpath(ancestor),relative(ancestor,output));break;}catch(e){if(e.code!=='ENOENT')throw e;ancestor=dirname(ancestor);}}
const within=(parent,p)=>p===parent||p.startsWith(parent+'/');
if([join(repo,'libraries'),join(repo,'docs/research'),join(repo,'examples/autocomplete/reproducibility'),join(repo,'examples/autocomplete/review')].some(p=>within(p,output)))throw Error('Output must be separate from input, libraries and historical research');
const stem=opt['--component'].toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')||'component';
const figName=stem+'.fig';
for(const name of [figName,'preview.png','preview-check.json']){
 const file=join(output,name);if(file===input)throw Error('Input FIG must not be overwritten; use a separate raw input filename or new output directory');
 try{await stat(file);throw Error('Output file already exists: '+file);}catch(e){if(e.code!=='ENOENT')throw e;}
}
const source=await readFile(input),sourceHash=sha(source);const graph=await core.parseFigFile(source.buffer.slice(source.byteOffset,source.byteOffset+source.byteLength),{populate:'all'});
const cases=selectCases(graph,ids);const before=cases.map(n=>snapshot(graph,n));
const layout=plan(cases.map(n=>caseBounds(graph,n)),STYLE.columns);
if(layout.width>16384||layout.height>16384||layout.width*layout.height>32000000)throw Error('Presentation exceeds bounded raster size; split into separate pages/runs');
const localFonts=JSON.parse(execFileSync('python3',[join(repo,'tools/fonts/check.py'),'--repo',repo,'--library',opt['--library']],{encoding:'utf8'}));
if(localFonts.overall!=='PASS_LIMITED')throw Error('A validated local fonts.json is required for reproducible rendering');
const family=localFonts.faces[0].family;
if(!localFonts.faces.some(f=>f.family===family&&f.weight===400)||!localFonts.faces.some(f=>f.family===family&&f.weight===700))throw Error('Presentation captions require local regular 400 and bold 700 faces');
apply(graph,cases,ids,layout,{title:opt['--component'],subtitle:`${opt['--library']} · Definition ${opt['--definition-revision']??'nicht mitgeliefert'} · ${ids.length} Zustände`,fontFamily:family});
const stable=v=>JSON.stringify(v),assertSame=(g,ns,stage)=>{for(let i=0;i<ns.length;i++)if(stable(before[i])!==stable(snapshot(g,ns[i])))throw Error('Component invariant changed at '+stage+': '+ids[i]);assertContained(g,ns,layout);};
assertSame(graph,cases,'presentation composition');
let networkAttempts=0;globalThis.fetch=async()=>{networkAttempts++;throw Error('Network disabled: fonts must be local');};
const ck=await headless.initCanvasKit(),fontRecords=[];
for(const f of localFonts.faces){const a=f.assets.find(a=>a.format==='truetype'),b=await readFile(join(repo,a.path));if(sha(b)!==a.sha256)throw Error('Font changed after validation');const buffer=b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength);core.fontManager.markLoaded(f.family,f.openpencilStyle,buffer,'library-asset:'+a.sha256);fontRecords.push({...f,buffer});}
for(const n of graph.getAllNodes())if(n.type==='TEXT'&&n.text){
 if(n.styleRuns?.length)throw Error('Styled text runs require a separately tested font adapter');
 const f=fontRecords.find(f=>f.family===n.fontFamily&&f.weight===n.fontWeight&&f.style===(n.italic?'italic':'normal'));if(!f)throw Error('No exact local font for '+n.name);
 const tf=ck.Typeface.MakeFreeTypeFaceFromData(f.buffer);const glyphs=Array.from(tf.getGlyphIDs(n.text.replace(/[\n\r\t]/g,'')));tf.delete();if(glyphs.some(g=>g===0))throw Error('Uncovered glyph in '+n.name);
}
await mkdir(output,{recursive:true}); // individual files are written exclusively; never overwrite an old proof
const fig=await core.exportFigFile(graph);await writeFile(join(output,figName),fig,{flag:'wx'});
const parsed=await core.parseFigFile(fig.buffer.slice(fig.byteOffset,fig.byteOffset+fig.byteLength),{populate:'all'});
const outCases=ids.map(id=>{const found=[...parsed.getAllNodes()].filter(n=>n.name===cases[ids.indexOf(id)].name&&['FRAME','GROUP','COMPONENT','INSTANCE'].includes(n.type));if(found.length!==1)throw Error('Ambiguous roundtrip case '+id);return found[0];});
assertSame(parsed,outCases,'FIG readback');
const page=parsed.getPages()[0],png=await headless.headlessRenderNodes(parsed,page.id,page.childIds,{scale:1,format:'PNG'});
if(!png||networkAttempts)throw Error('Render failed or attempted network access');assertSame(parsed,outCases,'PNG rendering');
for(const f of localFonts.faces){const a=f.assets.find(a=>a.format==='truetype');if(core.fontManager.loadedFontSource(f.family,f.openpencilStyle)!=='library-asset:'+a.sha256)throw Error('Font source changed');}
await writeFile(join(output,'preview.png'),png,{flag:'wx'});
if(sha(await readFile(input))!==sourceHash)throw Error('Input FIG changed during run');
const count=s=>1+s.children.reduce((n,c)=>n+count(c),0);
const receipt={overall:'PASS_LIMITED',release:false,scope:'native-presentation-and-component-invariants',style:STYLE.version,
 input:{path:relative(repo,input),sha256:sourceHash},definitionRevision:opt['--definition-revision']??null,
 selectedLibrary:opt['--library'],component:component.id,bindings:[indexPath,cp,storiesPath].map(p=>({path:relative(repo,p)})),
 layout,presentationTemplate:{path:relative(repo,fileURLToPath(TEMPLATE_URL)),sha256:sha(await readFile(TEMPLATE_URL))},networkAttempts,licenseEvidence:localFonts.licenseEvidence,
 cases:ids.map((id,i)=>({id,nodes:count(before[i]),beforeSha256:sha(stable(before[i])),afterSha256:sha(stable(snapshot(parsed,outCases[i]))),unchanged:true})),
 comparedProperties:'All own native properties recursively except node ids, parent/child id bookkeeping, root x/y, source/import metadata and documented renderer caches; child order and relative descendant x/y retained',
 ignoredProperties:['id','parentId','childIds','source','derivedLayout','textPicture','derivedTextGlyphs','textPathData','textPathBox'],
 fonts:localFonts.faces.map(f=>({family:f.family,weight:f.weight,assets:f.assets})),
 outputs:{[figName]:sha(fig),'preview.png':sha(png)},
 notChecked:['Runtime/ARIA','Figma import metadata preservation','Styled text runs, rotated/flipped nodes and multi-page input (blocked)','Pixel equality between different source component structures']};
for(const b of receipt.bindings)b.sha256=sha(await readFile(join(repo,b.path)));
await writeFile(join(output,'preview-check.json'),JSON.stringify(receipt,null,2)+'\n',{flag:'wx'});
console.log(JSON.stringify({overall:receipt.overall,release:false,cases:ids.length,componentNodes:receipt.cases.reduce((n,c)=>n+c.nodes,0),output}));
