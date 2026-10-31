// Explicit fresh child factories and owner/epoch lifecycle binding. Shared by native and browser adapters.
export function makeInvokers({core, compile, sources, relay, current, record = () => {}, onStart = () => {}, onReveal = () => {}, onError = () => {}}) {
  const invokers = {};
  function invoke(parent, obj, inherited, callback) {
    (async () => {
      const url = new URL(obj.src, obj.docUrl).href;
      const level = Object.keys(sources).find(key => sources[key] === url);
      if (!level) throw Error('Invoke source not in bound composition: ' + url);
      const {owner, epoch} = obj.params;
      let factory, failed = false;
      try { factory = await compile(url); }
      catch (error) { failed = true; factory = await compile(relay); record('init.failed', {owner, epoch, level, error: String(error)}); }
      const session = new core.Statechart(factory, {parentSession: parent, invokeid: obj.id, params: {...obj.params, ...(failed ? {fault: 'Initialisierung fehlgeschlagen.'} : {})}, invokers});
      const actor = {owner, epoch, level, failed, session};
      record('child.created', actor);
      session.on('onError', error => onError(error));
      callback(null, session);
      setTimeout(() => {
        if (parent.isFinal() || !current(owner, epoch)) { session.cancel(); record('child.late.cancel', actor); return; }
        if (!failed) {
          onStart(actor);
          if (level === 'scroll-area') session.on('onBigStepEnd', event => { if (event?.name === 'REVEAL') Promise.resolve().then(() => onReveal(actor, event)).catch(onError); });
        }
        session.start(); record('child.started', actor);
      }, 0);
    })().catch(error => { onError(error); callback(error); });
  }
  for (const name of ['scxml', 'http://www.w3.org/TR/scxml/', 'http://www.w3.org/TR/scxml']) invokers[name] = invoke;
  return invokers;
}
