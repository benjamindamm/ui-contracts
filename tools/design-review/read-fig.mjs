// Read-only native observations; no generator, cached measurement or builder report.
import { readFile } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';
import { join } from 'node:path';
const [repo, file] = process.argv.slice(2);
const core = await import(pathToFileURL(join(repo, 'tools/openpencil/node_modules/@open-pencil/core/dist/index.js')));
const bytes = await readFile(file);
const graph = await core.parseFigFile(bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), { populate: 'all' });
const fields = ['id', 'type', 'name', 'parentId', 'childIds', 'x', 'y', 'width', 'height',
  'visible', 'locked', 'opacity', 'clipsContent', 'cornerRadius', 'fills', 'strokes',
  'text', 'fontFamily', 'fontSize', 'fontWeight', 'lineHeight'];
const nodes = [...graph.getAllNodes()].map(n => Object.fromEntries(fields.map(k => [k, n[k] ?? null])));
console.log(JSON.stringify({ nodes }));
