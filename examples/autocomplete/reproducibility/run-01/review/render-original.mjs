import fs from 'node:fs';
import {parseFigFile} from '../../../../../tools/openpencil/node_modules/@open-pencil/core/dist/io/formats/fig/read.js';
import {headlessRenderNodes} from '../../../../../tools/openpencil/node_modules/@open-pencil/core/dist/io/formats/raster/headless.js';
for(const label of ['a','b']) {
 try{const bytes=fs.readFileSync(new URL(`../builder-${label}/autocomplete.fig`,import.meta.url));const graph=await parseFigFile(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength));
 const png=await headlessRenderNodes(graph,'0:3',['0:4'],{scale:1,format:'PNG'});if(png)fs.writeFileSync(new URL(`render-${label}.png`,import.meta.url),png);console.log(label,png?.length);
 }catch(e){console.log(label,String(e))}
}
