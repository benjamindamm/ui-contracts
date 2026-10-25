const fs=require('node:fs'),css=require('../css-grammar/tool-current/node_modules/css-tree');
const profile=JSON.parse(fs.readFileSync(require('node:path').join(__dirname,'../css-original-grammar/profile.json'),'utf8'));
const lexer=css.createLexer({generic:true,types:Object.fromEntries(Object.entries(profile.types).map(([k,v])=>[k,v.grammar])),properties:Object.fromEntries(Object.entries(profile.properties).map(([k,v])=>[k,v.grammar]))});
const inputs=JSON.parse(fs.readFileSync(0,'utf8')),out=[];
for(const source of inputs){const rows=[],issues=[];let ast;try{ast=css.parse(source,{positions:true});}catch(e){out.push({issues:['css-parse'],error:String(e),rows:[]});continue;}
function visit(node,nested){if(node.type==='Atrule'){if(node.block)visit(node.block,true);return;}if(node.type==='Rule'){
 const decls=node.block.children.toArray().filter(d=>d.type==='Declaration'),relevant=decls.some(d=>['anchor-name','position-anchor','anchor-scope'].includes(d.property));
 if(relevant&&nested)issues.push('unsupported-nesting');
 const sels=node.prelude&&node.prelude.type==='SelectorList'?node.prelude.children.toArray():[],children=sels.length===1?sels[0].children.toArray():[],id=children.length===1&&children[0].type==='IdSelector'?children[0].name:null;
 if(relevant&&!id)issues.push('unsupported-selector');
 for(const d of decls){css.walk(d.value,n=>{if(n.type==='Function'&&['anchor','anchor-size'].includes(n.name)&&n.children.first?.type==='Identifier'&&n.children.first.name.startsWith('--'))issues.push('unsupported-named-function');});if(!['anchor-name','position-anchor','anchor-scope','position'].includes(d.property))continue;const value=css.generate(d.value);const row={selector:css.generate(node.prelude),hostId:id,property:d.property,value,important:!!d.important,location:d.loc.start};rows.push(row);
  if(d.property==='anchor-scope'){issues.push('unsupported-scope');continue;}
  if(d.property==='position'){if(id&&d.important)issues.push('unsupported-cascade');continue;}
  if(d.important)issues.push('unsupported-cascade');
  if(!lexer.matchProperty(d.property,d.value).matched){issues.push(/var\(/.test(value)?'unsupported-value':'css-property-syntax');continue;}
  const vals=d.value.type==='Value'?d.value.children.toArray():[];
  if(vals.length!==1||vals[0].type!=='Identifier'||!/^--[a-zA-Z][\w-]*$/.test(vals[0].name))issues.push('unsupported-value');
 }
 return;}
 if(node.children)node.children.forEach(n=>visit(n,nested));}
visit(ast,false);
for(const ref of rows.filter(r=>r.property==='position-anchor'&&r.hostId))if(rows.some(r=>r.hostId===ref.hostId&&r.property==='position'&&r.location.offset>ref.location.offset))issues.push('unsupported-reset');
out.push({issues:[...new Set(issues)],rows});}
process.stdout.write(JSON.stringify({cssTree:require('../css-grammar/tool-current/node_modules/css-tree/package.json').version,results:out}));
