const p=browser.page((await browser.pages.list()).find(x=>x.url==='http://127.0.0.1:8770/').pageId);
let s=await p.snapshot({mode:'interactive'});await p.fill(s.refs.find(x=>x.name==='Input'&&x.role==='textbox').ref,'0123 Straße');
await p.evaluate(async()=>{await research.capture('input-edit',{});research.controls.send('Input','SET_READ_ONLY',{readOnly:true});});
await p.press('X');await p.evaluate(async()=>research.capture('input-readonly',{}));
s=await p.snapshot({mode:'interactive'});await p.selectOption(s.refs.find(x=>x.name==='Select'&&x.role==='combobox').ref,'K3');
await p.evaluate(async()=>research.capture('select-commit',{}));
s=await p.snapshot({mode:'interactive'});await p.click(s.refs.find(x=>x.role==='button'&&x.name.includes('Ländervorwahl')).ref);
await p.waitForSelector('[data-part=dialog]:not([hidden])');
return (await p.snapshot({mode:'interactive'})).text;