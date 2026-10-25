// Additional deliberately bounded TypeScript AST interpretation of CEM metadata.
const fs=require('fs'),ts=require('../validation-probes/ts-tool/node_modules/typescript');
function parse(text){const sf=ts.createSourceFile('type.ts','type T='+text+';',ts.ScriptTarget.Latest,true);if(sf.parseDiagnostics.length)throw Error('UNSUPPORTED: invalid type text');
 function norm(n){if(n.kind===ts.SyntaxKind.StringKeyword)return {kind:'string'};if(n.kind===ts.SyntaxKind.BooleanKeyword)return {kind:'boolean'};if(n.kind===ts.SyntaxKind.NumberKeyword)return {kind:'number'};
 if(ts.isUnionTypeNode(n)&&n.types.length===2&&n.types.some(t=>t.kind===ts.SyntaxKind.UndefinedKeyword)){return {kind:'optional',item:norm(n.types.find(t=>t.kind!==ts.SyntaxKind.UndefinedKeyword))};}
 if(ts.isTypeReferenceNode(n)&&n.typeName.getText(sf)==='Array'&&n.typeArguments?.length===1)return {kind:'array',item:norm(n.typeArguments[0])};
 if(ts.isTypeLiteralNode(n)){const fields={};for(const m of n.members){if(!ts.isPropertySignature(m)||!ts.isIdentifier(m.name)||!m.type||fields[m.name.text])throw Error('UNSUPPORTED: record member');fields[m.name.text]={type:norm(m.type),optional:!!m.questionToken};}return {kind:'record',fields};}
 throw Error('UNSUPPORTED: '+ts.SyntaxKind[n.kind]);}
 const t=sf.statements[0].type;if(ts.isTypeReferenceNode(t)&&t.typeName.getText(sf)==='CustomEvent'&&t.typeArguments?.length===1)return {kind:'event',payload:norm(t.typeArguments[0])};return norm(t);}
try{const cem=JSON.parse(fs.readFileSync(0,'utf8')),d=cem.modules[0].declarations[0];const out={typescript:ts.version,members:{},events:{}};for(const m of d.members||[])out.members[m.name]=parse(m.type.text);for(const e of d.events||[])out.events[e.name]=parse(e.type.text);process.stdout.write(JSON.stringify(out));}catch(e){process.stdout.write(JSON.stringify({error:String(e)}));process.exitCode=1;}
