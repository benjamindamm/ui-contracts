// Demonstration adapter: fixture -> D3 geometry -> SVG -> native editable FIG -> PNG.
import{readFile,writeFile,mkdir}from'node:fs/promises';
import{resolve,join}from'node:path';import{fileURLToPath}from'node:url';import{createHash}from'node:crypto';import{execFileSync}from'node:child_process';
import{pieGeometry,sectorsSvg,xml}from'./pie.mjs';
import * as core from'../openpencil/node_modules/@open-pencil/core/dist/index.js';
import{createSVGNodes}from'../openpencil/node_modules/@open-pencil/core/dist/io/formats/svg/import.js';
import * as headless from'../openpencil/node_modules/@open-pencil/core/dist/io/formats/raster/headless.js';
const repo=resolve(fileURLToPath(new URL('../../',import.meta.url)));const [inputArg='examples/charts/pie-chart/input.json',outputArg='examples/charts/pie-chart']=process.argv.slice(2);
const input=resolve(inputArg),out=resolve(outputArg),sha=b=>createHash('sha256').update(b).digest('hex');
if(out.startsWith(join(repo,'libraries')+'/')||out.startsWith(join(repo,'examples/autocomplete')+'/')||out.startsWith(join(repo,'docs/research')+'/'))throw Error('Output must not modify definition or historical research directories');
const inputBytes=await readFile(input),fixture=JSON.parse(inputBytes);const geometry=pieGeometry(fixture.data,{radius:165});
const sourceTotal=fixture.data.reduce((s,d)=>s+d.value,0);
const legend=fixture.data.map((d,i)=>{const y=486+i*27;return `<g id="legend-${d.id}"><circle id="marker-${d.id}" cx="48" cy="${y}" r="6" fill="${d.color}"/><text id="label-${d.id}" x="63" y="${y+5}" font-family="Inter" font-size="16" fill="#4B4B4B">${xml(d.label)}</text><text id="value-${d.id}" x="517" y="${y+5}" text-anchor="end" font-family="Inter" font-size="16" fill="#4B4B4B">${xml(d.displayValue??String(d.value))}</text></g>`;}).join('');
const svg=`<svg xmlns="http://www.w3.org/2000/svg" id="pie-chart" width="562" height="590" viewBox="0 0 562 590"><text id="chart-title" x="26" y="62" font-family="Inter" font-size="24" fill="#4B4B4B">${xml(fixture.title)}</text>${sectorsSvg(geometry,{cx:277,cy:270,strokeWidth:1})}${legend}</svg>\n`;
const fontCheck=JSON.parse(execFileSync('python3',[join(repo,'tools/fonts/check.py'),'--repo',repo,'--library','example'],{encoding:'utf8'}));if(fontCheck.overall!=='PASS_LIMITED')throw Error('Font check failed');
let networkAttempts=0;globalThis.fetch=async()=>{networkAttempts++;throw Error('Network disabled for proof');};
const ck=await headless.initCanvasKit();const font=fontCheck.faces.find(f=>f.family==='Inter'&&f.weight===400),fontAsset=font.assets.find(a=>a.format==='truetype'),fontBytes=await readFile(join(repo,fontAsset.path));
if(sha(fontBytes)!==fontAsset.sha256)throw Error('Font changed');const fontBuffer=fontBytes.buffer.slice(fontBytes.byteOffset,fontBytes.byteOffset+fontBytes.byteLength);core.fontManager.markLoaded('Inter','Regular',fontBuffer,'library-asset:'+fontAsset.sha256);
const g=new core.SceneGraph(),page=g.getPages()[0];g.updateNode(page.id,{name:'Pie Chart · D3 SVG Proof'});const imported=createSVGNodes(g,page.id,svg);if(!imported)throw Error('SVG import failed');
const fig=await core.exportFigFile(g);const parsed=await core.parseFigFile(fig.buffer.slice(fig.byteOffset,fig.byteOffset+fig.byteLength),{populate:'all'});const nodes=[...parsed.getAllNodes()];
const vectors=nodes.filter(n=>n.type==='VECTOR'),texts=nodes.filter(n=>n.type==='TEXT');const samples=[];
function polygonArea(n){const net=n.vectorNetwork;let points=[];if(net.regions.length!==1||net.regions[0].loops.length!==1)throw Error('Unexpected sector topology');
 for(const index of net.regions[0].loops[0]){const s=net.segments[index],p0=net.vertices[s.start],p3=net.vertices[s.end],p1={x:p0.x+s.tangentStart.x,y:p0.y+s.tangentStart.y},p2={x:p3.x+s.tangentEnd.x,y:p3.y+s.tangentEnd.y};for(let k=0;k<1000;k++){const t=k/1000,u=1-t;points.push({x:u*u*u*p0.x+3*u*u*t*p1.x+3*u*t*t*p2.x+t*t*t*p3.x,y:u*u*u*p0.y+3*u*u*t*p1.y+3*u*t*t*p2.y+t*t*t*p3.y});}}
 return Math.abs(points.reduce((a,p,i)=>{const q=points[(i+1)%points.length];return a+p.x*q.y-q.x*p.y;},0))/2;}
for(const s of geometry.segments){const match=nodes.filter(n=>n.name==='slice-'+s.id);if(match.length!==1)throw Error('Missing/duplicate native slice');const n=match[0];if(n.type!=='VECTOR'||n.locked||n.visible===false||!n.vectorNetwork?.vertices.length)throw Error('Slice is not an editable native vector');
 const pos=parsed.getAbsolutePosition(n.id);const world=n.vectorNetwork.vertices.map(p=>({x:p.x+pos.x,y:p.y+pos.y}));
 const near=p=>world.some(q=>Math.hypot(p.x-q.x,p.y-q.y)<0.005);
 const at=a=>({x:277+165*Math.sin(a),y:270-165*Math.cos(a)});
 if(!near({x:277,y:270})||!near(at(s.startAngle))||!near(at(s.endAngle)))throw Error('Native sector boundary endpoints differ from D3 geometry');
 const fill=n.fills.find(f=>f.type==='SOLID');const hex='#'+['r','g','b'].map(k=>Math.round(fill.color[k]*255).toString(16).padStart(2,'0')).join('').toUpperCase();if(hex!==s.color)throw Error('Native slice color differs');
 const area=polygonArea(n),expectedArea=Math.PI*165**2*s.proportion,relativeError=Math.abs(area-expectedArea)/expectedArea;
 if(relativeError>0.001)throw Error('Native sector area not proportional to datum');
 samples.push({id:s.id,type:n.type,editable:true,displayValue:fixture.data.find(d=>d.id===s.id).displayValue,proportion:s.proportion,angleDegrees:s.angle*180/Math.PI,color:hex,centerAndBoundaryEndpointsMatch:true,nativeArea:area,expectedCircleSectorArea:expectedArea,relativeAreaError:relativeError});
}
for(const d of fixture.data)for(const [prefix,expected]of[['label-',d.label],['value-',d.displayValue??String(d.value)]]){const n=texts.find(n=>n.name===prefix+d.id);if(!n||n.text!==expected||n.fontFamily!=='Inter')throw Error('Legend text did not survive FIG roundtrip');}
if(vectors.length!==geometry.segments.length+fixture.data.length)throw Error('Unexpected vector count');
const tf=ck.Typeface.MakeFreeTypeFaceFromData(fontBuffer);for(const n of texts)if(Array.from(tf.getGlyphIDs(n.text)).some(id=>id===0))throw Error('Missing glyph');tf.delete();
const p=parsed.getPages()[0],png=await headless.headlessRenderNodes(parsed,p.id,p.childIds,{scale:1,format:'PNG'});if(!png||networkAttempts)throw Error('Render failed or attempted network');
if(core.fontManager.loadedFontSource('Inter','Regular')!=='library-asset:'+fontAsset.sha256)throw Error('Font source changed');
await mkdir(out,{recursive:true});for(const[name,data]of[['chart.svg',svg],['pie-chart.fig',fig],['preview.png',png]])await writeFile(join(out,name),data,{flag:'wx'});
const pkg=JSON.parse(await readFile(join(repo,'tools/charts/node_modules/d3-shape/package.json'))),open=JSON.parse(await readFile(join(repo,'tools/openpencil/node_modules/@open-pencil/core/package.json')));
const report={overall:'PASS_LIMITED',release:false,scope:'D3-to-SVG-to-editable-native-FIG roundtrip and render',
 input:{path:inputArg,sha256:sha(inputBytes)},provenance:fixture.provenance,sourceTotal,normalization:'Value/sum; labels retain supplied display strings',
 d3ShapeVersion:pkg.version,openPencilVersion:open.version,angleSumDegrees:geometry.segments.reduce((s,d)=>s+d.angle,0)*180/Math.PI,
 svgSegmentCount:geometry.segments.length,nativeVectorCount:vectors.length,nativeTextCount:texts.length,slices:samples,
 areaMethod:'Independent shoelace integration of native cubic Bezier contours (1000 samples per segment), tolerance 0.1% relative to analytic sector area',
 networkAttempts,font:{path:fontAsset.path,sha256:fontAsset.sha256},
 scriptSha256:sha(await readFile(new URL('./proof.mjs',import.meta.url))),geometryModuleSha256:sha(await readFile(new URL('./pie.mjs',import.meta.url))),
 chartDependencyLockSha256:sha(await readFile(join(repo,'tools/charts/package-lock.json'))),openPencilDependencyLockSha256:sha(await readFile(join(repo,'tools/openpencil/package-lock.json'))),
 outputs:{'chart.svg':sha(svg),'pie-chart.fig':sha(fig),'preview.png':sha(png)},
 notChecked:['Exact original font/colorimetry and pixel equality','Original unrounded dataset unavailable','Live editor GUI roundtrip','Interactive chart behavior or accessibility']};
await writeFile(join(out,'verification.json'),JSON.stringify(report,null,2)+'\n',{flag:'wx'});console.log(JSON.stringify({overall:report.overall,segments:samples.length,angleSumDegrees:report.angleSumDegrees,maxNativeAreaError:Math.max(...samples.map(s=>s.relativeAreaError)),out}));
