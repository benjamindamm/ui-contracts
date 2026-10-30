import {readFileSync} from 'node:fs';
import {evaluate} from 'feelin';
const base=new URL('./fixtures/',import.meta.url),contexts=JSON.parse(readFileSync(new URL('contexts.json',base),'utf8'));
const typedExpression=readFileSync(new URL('typed-eligibility.feel',base),'utf8').trim();
const expression=readFileSync(new URL('eligibility.feel',base),'utf8').trim();
let calls=[];
for(const c of contexts)for(const [kind,expr] of [['raw-predicate','existingEntriesOnly and singleSelection'],['explicit-policy',expression],['typed-policy',typedExpression]]){
 try{calls.push({id:c.id,case:c.case,kind,input:c.input,expression:expr,...evaluate(expr,c.input)});}catch(e){calls.push({id:c.id,kind,error:String(e)});}
}
try{calls.push({id:'invalid-syntax',...evaluate('if ( then')});}catch(e){calls.push({id:'invalid-syntax',error:String(e)});}
console.log(JSON.stringify({engine:'feelin',version:'8.2.0',scope:'FEEL interpreter only; XML schema probe is separate, no full DMN engine claim',calls}));
