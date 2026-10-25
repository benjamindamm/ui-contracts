// Additional syntax-only parser pass; not full module validation or native layout.
const fs=require('fs'),css=require('../css-grammar/tool-current/node_modules/css-tree');
const input=JSON.parse(fs.readFileSync(0,'utf8'));const out=[];
try{for(const [file,text]of Object.entries(input)){const ast=css.parse(text),declarations=[];css.walk(ast,{visit:'Declaration',enter(n){declarations.push({property:n.property,value:css.generate(n.value)})}});out.push({file,syntaxParsed:true,declarations});}process.stdout.write(JSON.stringify({version:css.version,cases:out}));}catch(e){process.stdout.write(JSON.stringify({error:String(e),cases:out}));process.exitCode=1;}
