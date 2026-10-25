import {readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import assert from 'node:assert/strict';
const here=path.dirname(fileURLToPath(import.meta.url)),tool=path.resolve(here,'../../../../tools/openpencil/node_modules/@open-pencil');
const {IORegistry,BUILTIN_IO_FORMATS}=await import(path.join(tool,'core/dist/io/index.js'));
const {populateAllFigPages}=await import(path.join(tool,'core/dist/io/formats/fig/index.js'));
const io=new IORegistry(BUILTIN_IO_FORMATS);
const load=async data=>{const {graph}=await io.readDocument({name:'autocomplete.fig',data});populateAllFigPages(graph);return graph;};
const g=await load(new Uint8Array(await readFile(path.join(here,'autocomplete.fig'))));
const nodes=[...g.nodes.values()],named=n=>nodes.find(v=>v.name===n),children=n=>n.childIds.map(id=>g.nodes.get(id));
assert.equal(nodes.filter(n=>n.name.startsWith('Autocomplete /')).length,10);
assert.equal(nodes.filter(n=>n.name.startsWith('option /')).length,28);
for(const box of nodes.filter(n=>n.name.startsWith('Autocomplete /'))){
 assert.equal(box.width,320);const parts=children(box),input=parts.find(n=>n.name.startsWith('input'));
 assert.equal(input.y,28);assert.equal(input.height,44);
 const surface=parts.find(n=>n.name==='overlay.surface');assert.equal(surface.y,80);
 const status=parts.find(n=>n.name.startsWith('status'));assert.equal(status.y,surface.visible?80+surface.height+8:80);
}
const box=named('Autocomplete / scroll-end'),surface=children(box).find(n=>n.name==='overlay.surface'),vp=children(surface)[0],content=children(vp)[0],list=children(content)[0];
assert.equal(vp.clipsContent,true);assert.equal(vp.height,160);assert.equal(content.y,-64);assert.equal(list.childIds.length,7);
const last=g.nodes.get(list.childIds.at(-1));assert.equal(last.y+content.y,128);assert.equal(last.height,32);assert.equal(last.fills.length,1);
const label=named('Seitentitel');assert.equal(label.type,'TEXT');g.updateNode(label.id,{text:'Editable round-trip proof'});
const file=await io.writeDocument('fig',g),again=await load(file.data);assert.equal([...again.nodes.values()].find(n=>n.name==='Seitentitel').text,'Editable round-trip proof');
console.log('PASS: 10 stories, 28 options, geometry, clipped scroll-end, editable text FIG roundtrip');
