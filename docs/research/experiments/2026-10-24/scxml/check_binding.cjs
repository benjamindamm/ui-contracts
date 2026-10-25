const ts=require(process.env.PROBE_TYPESCRIPT||'../ts-tool/node_modules/typescript');
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const inputs=JSON.parse(fs.readFileSync(path.join(__dirname,'binding-inputs.json'),'utf8'));
const results=inputs.map(c=>{
 if(c.send_event!==c.public_event.name)return {...c,status:'event-name-mismatch',additional_policy:'Explicit static route to the separately declared public event'};
 const file=path.join(__dirname,'binding-check.ts');
 const text=`type PublicEvent = ${c.public_event.type.text};\n`+c.declarations.map(d=>`const ${d.id} = ${d.expr};`).join('\n')+`\nconst publicPayload: PublicEvent['detail'] = {`+c.params.map(p=>`${JSON.stringify(p.name)}: ${p.expr}`).join(', ')+`};\n`;
 const options={noEmit:true,strict:true,target:ts.ScriptTarget.ES2022,lib:['lib.es2022.d.ts','lib.dom.d.ts']};const host=ts.createCompilerHost(options),read=host.readFile,exists=host.fileExists;host.readFile=f=>path.resolve(f)===file?text:read(f);host.fileExists=f=>path.resolve(f)===file||exists(f);
 const program=ts.createProgram([file],options,host);const diagnostics=ts.getPreEmitDiagnostics(program).map(d=>({code:d.code,message:ts.flattenDiagnosticMessageText(d.messageText,'\n')}));return {...c,typescript_input:text,diagnostics,status:diagnostics.length?'payload-type-error':'compatible'};
});
for(const c of results){assert.equal(c.status,c.expected);console.log(c.id,c.status);}
fs.writeFileSync(path.join(__dirname,'binding-results.json'),JSON.stringify({typescript:ts.version,node:process.version,additional_binding_policy:true,original_schemas_modified:false,scope:'Static named send + param, literal ECMAScript/TypeScript subset, external CEM public event, explicit Web CustomEvent.detail route; no interpreter or runtime host dispatch',cases:results},null,2)+'\n');
