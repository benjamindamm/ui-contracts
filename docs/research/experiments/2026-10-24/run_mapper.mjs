import { mapContainerStyle, mapElementStyle } from './sources/style-map.mts';
import fs from 'node:fs';
import { isDeepStrictEqual } from 'node:util';
const cases=[
 {id:'mapper-01-height-control',fn:'container',input:{layout:'layer',size:{maxHeight:160}},expected:{display:'flex',position:'relative',maxHeight:'160px'}},
 {id:'mapper-02-foreign-anchor',fn:'container',input:{layout:'layer',anchorTarget:'input-A',placement:'bottom',offset:{value:8,unit:'px'}},expected:{display:'flex',position:'relative'}},
 {id:'mapper-03-container-overflow',fn:'container',input:{layout:'layer',overflowY:'auto'},expected:{display:'flex',position:'relative'}},
 {id:'mapper-04-nested-style-overflow',fn:'element',input:{style:{overflowY:'auto',positionAnchor:'--input',top:'anchor(bottom)'}},expected:{}},
 {id:'mapper-05-element-overflow',fn:'element',input:{overflow:'auto',overflowX:'hidden',overflowY:'scroll'},expected:{}},
 {id:'mapper-06-relative-unit',fn:'container',input:{size:{maxHeight:{value:5,unit:'rem'}}},expected:{display:'flex',flexDirection:'column',maxHeight:'5rem'}},
];
const results=cases.map(c=>{const output=(c.fn==='container'?mapContainerStyle:mapElementStyle)(c.input);return {...c,output,expectation_met:isDeepStrictEqual(output,c.expected)}});
fs.writeFileSync(new URL('./mapper-results.json',import.meta.url),JSON.stringify({kind:'original-function-execution',node:process.version,rendered:false,source_modified:false,type_syntax_erasure:'Node native TypeScript support; runtime source body unchanged',cases:results,all_expectations_met:results.every(c=>c.expectation_met)},null,2)+'\n');
for(const c of results)console.log(c.id,JSON.stringify(c.output),c.expectation_met?'OK':'MISMATCH');
if(results.some(c=>!c.expectation_met))process.exitCode=1;
