const p=browser.page((await browser.pages.list()).find(x=>x.url==='http://127.0.0.1:8770/').pageId);
await p.waitForSelector('body[data-ready=true]');
await p.evaluate(async()=>{await research.capture('initial',{});research.providerMode('manual');});
let s=await p.snapshot({mode:'interactive'});await p.fill(s.refs.find(x=>x.name==='Suche A'&&x.role==='combobox').ref,'Stadt');
await p.waitForSelector('[data-owner=A][data-phase=loading]');
await p.evaluate(async()=>{await research.capture('ac-loading',{});research.deliver(research.requests.at(-1).id,Array.from({length:12},(_,i)=>({key:'A-'+(i+1),label:'Stadt '+(i+1),...(i===2?{disabled:true}:{})})));});
await p.waitForSelector('[data-owner=A][data-phase=ready]');
await p.evaluate(async()=>research.capture('ac-ready',{}));
return (await p.snapshot({mode:'interactive'})).text;