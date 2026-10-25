const ts=require('./ts-tool/node_modules/typescript');
const fs=require('node:fs');const path=require('node:path');const assert=require('node:assert/strict');
const manifest=JSON.parse(fs.readFileSync(path.join(__dirname,'inputs/cem-01-valid.json'),'utf8'));
const event=manifest.modules[0].declarations[0].events[0];
const cases=[
 {id:'payload-01-from-cem',event,expected:'resolved',fields:[['value','string',false]]},
 {id:'payload-02-nested-optional',event:{name:'select',type:{text:'CustomEvent<{value:string; metadata?: {id:number}}>'}},expected:'resolved'},
 {id:'payload-03-malformed-type',event:{name:'select',type:{text:'CustomEvent<!!!not-a-type'}},expected:'type-error'},
 {id:'payload-04-missing-type',event:{name:'select',type:{text:'CustomEvent<MissingPayload>',references:[{name:'MissingPayload',module:'missing.js'}]}},expected:'type-error'},
 {id:'payload-05-no-detail',event:{name:'select',type:{text:'Event'}},expected:'missing-payload-projection'},
 {id:'payload-06-invalid-name',event:{name:7,type:{text:'CustomEvent<{value:string}>'}},expected:'invalid-public-name'},
];
const results=cases.map(c=>{
 if(typeof c.event.name!=='string')return {...c,status:'invalid-public-name',policy:'Additional adapter input guard; not claimed to be original CEM root validation'};
 const file=path.join(__dirname,'payload-input.ts');const content='type EventContract = '+c.event.type.text+';\n';
 const options={noEmit:true,strict:true,target:ts.ScriptTarget.ES2022,lib:['lib.es2022.d.ts','lib.dom.d.ts']};
 const host=ts.createCompilerHost(options),baseRead=host.readFile,baseExists=host.fileExists;
 host.readFile=f=>path.resolve(f)===path.resolve(file)?content:baseRead(f);host.fileExists=f=>path.resolve(f)===path.resolve(file)||baseExists(f);
 const program=ts.createProgram([file],options,host);const diagnostics=ts.getPreEmitDiagnostics(program).map(d=>({code:d.code,message:ts.flattenDiagnosticMessageText(d.messageText,'\n')}));
 if(diagnostics.length)return {...c,status:'type-error',typescript_input:content,diagnostics};
 const sf=program.getSourceFile(file),node=sf.statements.find(ts.isTypeAliasDeclaration),checker=program.getTypeChecker();const type=checker.getTypeFromTypeNode(node.type);const detail=checker.getPropertyOfType(type,'detail');
 if(!detail)return {...c,status:'missing-payload-projection',typescript_input:content,diagnostics};
 const payload=checker.getTypeOfSymbolAtLocation(detail,node);const fields=checker.getPropertiesOfType(payload).map(s=>[s.name,checker.typeToString(checker.getTypeOfSymbolAtLocation(s,node)),!!(s.flags&ts.SymbolFlags.Optional)]);
 if(c.fields)assert.deepEqual(fields,c.fields);
 return {...c,status:'resolved',typescript_input:content,projection:'CustomEvent.detail (explicit Web/TypeScript adapter policy)',payload_type:checker.typeToString(payload),resolved_fields:fields,diagnostics};
});
for(const r of results){assert.equal(r.status,r.expected);console.log(r.id,r.status,JSON.stringify(r.resolved_fields??[]));}
fs.writeFileSync(path.join(__dirname,'payload-results.json'),JSON.stringify({typescript:ts.version,node:process.version,policy_is_additional:true,manifest_source:'inputs/cem-01-valid.json',scope:'Explicit TypeScript type.text and DOM CustomEvent.detail only; no generic resolver for every CEM type syntax or external package',cases:results},null,2)+'\n');
