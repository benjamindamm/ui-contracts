// Independent review: reads the delivered file through the original reader.
import fs from 'node:fs/promises';
import { parseFigFile } from '../../../tools/openpencil/node_modules/@open-pencil/core/dist/index.js';
const input=new URL('../output/openpencil/autocomplete.fig',import.meta.url);
const bytes=await fs.readFile(input);
const graph=await parseFigFile(bytes.buffer.slice(bytes.byteOffset,bytes.byteOffset+bytes.byteLength));
const nodes=[...graph.nodes.values()].map(n=>({id:n.id,name:n.name,type:n.type,parentId:n.parentId,x:n.x,y:n.y,width:n.width,height:n.height,visible:n.visible,text:n.text,fontSize:n.fontSize,fontFamily:n.fontFamily,fills:n.fills,strokes:n.strokes,cornerRadius:n.cornerRadius,clipsContent:n.clipsContent}));
await fs.writeFile(new URL('actual-graph.json',import.meta.url),JSON.stringify({pages:graph.getPages().map(n=>({id:n.id,name:n.name})),nodes},null,2)+'\n');
console.log(JSON.stringify(nodes.filter(n=>n.type==='FRAME').slice(0,18).map(n=>({id:n.id,name:n.name,x:n.x,y:n.y,width:n.width,height:n.height,parent:n.parentId})),null,2));
