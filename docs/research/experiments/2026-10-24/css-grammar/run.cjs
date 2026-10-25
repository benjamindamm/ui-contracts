const fs=require('node:fs'),path=require('node:path');const toolDir=process.env.PROBE_CSS_TOOL||'./tool/node_modules';const css=require(toolDir+'/css-tree');
const cases=[
 {id:'cssg-01-anchor-name',property:'anchor-name',value:'--input',expected:'match'},
 {id:'cssg-02-anchor-scope',property:'anchor-scope',value:'--input',expected:'match'},
 {id:'cssg-03-position-anchor',property:'position-anchor',value:'--input',expected:'match'},
 {id:'cssg-04-relative-inset',property:'top',value:'calc(anchor(bottom) + 8px)',expected:'match'},
 {id:'cssg-05-anchor-width',property:'width',value:'anchor-size(width)',expected:'match'},
 {id:'cssg-06-height-control',property:'max-height',value:'160px',expected:'match'},
 {id:'cssg-07-bad-length',property:'max-height',value:'160bananas',expected:'mismatch'},
 {id:'cssg-08-scroll-control',property:'overflow-y',value:'auto',expected:'match'},
 {id:'cssg-09-bad-overflow',property:'overflow-y',value:'banana',expected:'mismatch'},
 {id:'cssg-10-bad-anchor-side',property:'top',value:'anchor(banana)',expected:'mismatch'},
 {id:'cssg-11-bad-anchor-name',property:'anchor-name',value:'banana',expected:'mismatch'},
 {id:'cssg-12-missing-anchor-syntactic',property:'position-anchor',value:'--missing',expected:'match'},
 {id:'cssg-14-invalid-nested-anchor',property:'top',value:'calc(anchor(banana) + 8px)',expected:'mismatch'},
 {id:'cssg-15-direct-anchor',property:'top',value:'anchor(bottom)',expected:'match'},
 {id:'cssg-16-normal-keyword',property:'position-anchor',value:'normal',expected:'match'},
 {id:'cssg-17-match-parent-keyword',property:'position-anchor',value:'match-parent',expected:'match'},
 {id:'cssg-13-variable-value',property:'max-height',value:'var(--max-height)',expected:'record'},
];
const out=cases.map(c=>{let status='parse-error',error,syntax;try{const ast=css.parse(c.value,{context:'value'});const result=css.lexer.matchProperty(c.property,ast);error=result.error?{name:result.error.name,message:result.error.message}:null;status=result.error?'mismatch':'match';const desc=css.lexer.getProperty(c.property);syntax=desc?.syntax?css.definitionSyntax.generate(desc.syntax):null;}catch(e){error={name:e.name,message:e.message};}return{...c,status,error,grammar:syntax,expected_met:c.expected==='record'?null:c.expected===status};});
const pkg=JSON.parse(fs.readFileSync(path.join(__dirname,toolDir+'/css-tree/package.json')));const mdn=JSON.parse(fs.readFileSync(path.join(__dirname,toolDir+'/mdn-data/package.json')));
fs.writeFileSync(path.join(__dirname,process.env.PROBE_CSS_OUTPUT||'results.json'),JSON.stringify({tool:'css-tree',version:css.version,npm_manifest:'https://registry.npmjs.org/css-tree/'+css.version,mdn_data:mdn.version,node:process.version,css_grammar_modified:false,dom_context_available:false,rendered:false,scope:'Original installed property dictionaries and lexer; no assertion of complete W3C draft-version equivalence',cases:out},null,2)+'\n');for(const c of out)console.log(c.id,c.status,c.grammar,c.error?.message?.split('\n')[0]??'');
