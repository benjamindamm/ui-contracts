import fs from 'node:fs';
import {parseFigFile} from '../../../../../tools/openpencil/node_modules/@open-pencil/core/dist/io/formats/fig/read.js';
const dir=new URL('.',import.meta.url);
for(const label of ['a','b']) {
 const file=new URL(`../builder-${label}/autocomplete.fig`,dir);
 const bytes=fs.readFileSync(file);
 const graph=await parseFigFile(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength),{populate:'all'});
 const nodes=[...graph.getAllNodes()];
 fs.writeFileSync(new URL(`original-${label}.json`,dir),JSON.stringify({reader:'@open-pencil/core 0.16.0 parseFigFile populate:all',rootId:graph.rootId,nodes},null,2));
 console.log(label,nodes.length,nodes.map(n=>[n.id,n.type,n.name,n.parentId,n.x,n.y,n.width,n.height,n.text]).filter(n=>n[1]==='PAGE'||n[1]==='CANVAS'||n[1]==='FRAME'));
}
