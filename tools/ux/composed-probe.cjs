const fs = require('node:fs'), path = require('node:path'), assert = require('node:assert/strict');
const {pathToFileURL} = require('node:url');
const root = path.resolve(__dirname, '../..');
const api = require(path.join(root, 'tools/openpencil/node_modules/@scion-scxml/scxml'));
exports.run = async request => {
  const {makeInvokers} = await import('../web/session.mjs');
  const {validResults} = await import('../web/provider.mjs');
  const checks = [], roots = {}, actors = [], requests = [], events = {A: [], B: []}, errors = [], waits = [];
  const data = machine => machine.getSnapshot()[3], phase = machine => machine.getConfiguration()[0];
  const signal = () => { for (const notify of waits) notify(); };
  const until = predicate => new Promise((resolve, reject) => {
    if (predicate()) return resolve();
    const timer = setTimeout(() => reject(Error('Composed contract signal deadline')), 2500);
    waits.push(() => { if (predicate()) { clearTimeout(timer); resolve(); } });
  });
  const compile = url => new Promise((resolve, reject) => api.documentStringToModel(url, fs.readFileSync(new URL(url), 'utf8'), (e, model) => e ? reject(e) : model.prepare((error, factory) => error ? reject(error) : resolve(factory))));
  const sources = Object.fromEntries(Object.entries(request.components).map(([k, v]) => [k, pathToFileURL(v).href]));
  const invokers = makeInvokers({core: api.core, compile, sources, relay: pathToFileURL(path.join(root, 'tools/web/error-relay.scxml')).href,
    current: (owner, epoch) => roots[owner] && data(roots[owner]).epoch === epoch && phase(roots[owner]) !== 'closed',
    record: (name, actor) => { if (name === 'child.created') { actors.push(actor); actor.session.on('onBigStepEnd', signal); } signal(); },
    onError: error => { errors.push(String(error)); signal(); },
    // Native contract test only: this acknowledgement is synthetic, actual DOM geometry is separately browser-tested.
    onReveal: (actor, event) => actor.session.gen({name: 'MEASURED', data: {...event.data, visible: true, offset: 32}})
  });
  for (const owner of ['A', 'B']) {
    const parent = {gen: event => {
      if (event.name === 'provider.request') requests.push({...event.data, owner, id: owner + ':' + event.data.epoch + ':' + event.data.seq});
      if (event.name === 'value-change') events[owner].push(event.data);
      signal();
    }};
    roots[owner] = new api.core.Statechart(await compile(pathToFileURL(request.model).href), {params: {owner}, parentSession: parent, invokeid: owner, invokers});
    roots[owner].on('onBigStepEnd', signal); roots[owner].on('onError', e => errors.push(String(e))); roots[owner].start();
  }
  const send = (owner, name, args) => roots[owner].gen({name, data: args});
  const check = (id, fn) => { fn(); checks.push({id, passed: true}); };
  const deliver = (r, rows) => { if (validResults(rows)) send(r.owner, 'DATA', {...r, results: rows}); else send(r.owner, 'FAILURE', {...r, message: 'Ungültige Ergebnisdaten.'}); };
  try {
    send('A', 'INPUT', {query: 'Alpha'}); await until(() => requests.length === 1);
    check('real-nested-invokes-start', () => assert.deepEqual(actors.filter(a => a.owner === 'A').map(a => a.level).sort(), ['overlay', 'scroll-area']));
    check('provider-query-is-an-actual-parent-event', () => assert.equal(requests[0].query, 'Alpha'));
    const rows = [{key: 'B-KEY', label: 'Bravo'}, {key: 'OFF', label: 'Disabled', disabled: true}, {key: 'A-KEY', label: 'Alpha'}];
    deliver(requests[0], rows);
    check('provider-order-kept', () => assert.deepEqual(data(roots.A).results.map(r => r.key), ['B-KEY', 'OFF', 'A-KEY']));
    send('A', 'ENTER'); check('text-without-active-option-does-not-commit', () => assert.equal(data(roots.A).value, undefined));
    send('A', 'NAV', {direction: 1}); send('A', 'NAV', {direction: 1});
    check('disabled-option-skipped-and-active-not-committed', () => { assert.equal(data(roots.A).activeKey, 'A-KEY'); assert.equal(data(roots.A).value, undefined); });
    await until(() => data(roots.A).visible === true);
    check('reveal-traverses-child-measure-relay', () => assert.ok(data(roots.A).revealSeq > 0));
    send('A', 'ENTER'); await until(() => events.A.length === 1);
    check('commit-key-label-and-single-event', () => { assert.equal(events.A[0].value, 'A-KEY'); assert.equal(data(roots.A).query, 'Alpha'); assert.equal(phase(roots.A), 'closed'); });
    check('cancelled-child-lifecycle', () => assert.ok(actors.filter(a => a.owner === 'A').every(a => a.session.isFinal())));
    check('other-instance-isolated', () => { assert.equal(phase(roots.B), 'closed'); assert.equal(events.B.length, 0); });
    send('A', 'SET_VALUE', {value: 'invented'});
    check('unknown-host-key-not-accepted', () => assert.equal(data(roots.A).value, 'A-KEY'));
    send('A', 'SET_VALUE', {value: 'OFF'});
    check('disabled-host-key-not-accepted', () => assert.equal(data(roots.A).value, 'A-KEY'));
    send('A', 'INPUT', {query: 'old'}); await until(() => requests.length === 2);
    const old = requests[1]; send('A', 'INPUT', {query: 'new'}); await until(() => requests.length === 3);
    const latest = requests[2]; deliver(latest, [{key: 'new', label: 'Neu'}]); const stale = data(roots.A).stale; deliver(old, [{key: 'old', label: 'Alt'}]);
    check('stale-provider-response-rejected', () => { assert.equal(data(roots.A).results[0].key, 'new'); assert.equal(data(roots.A).stale, stale + 1); });
    send('A', 'SET_ENABLED', {enabled: false}); send('A', 'INPUT', {query: 'ignored'});
    check('disabled-user-input-does-not-open', () => assert.equal(phase(roots.A), 'closed'));
    send('A', 'SET_ENABLED', {enabled: true}); send('A', 'INPUT', {query: 'bad-data'}); await until(() => requests.length === 4);
    deliver(requests[3], [{key: 'duplicate', label: 'One'}, {key: 'duplicate', label: 'Two'}]);
    check('provider-record-gate-rejects-duplicates', () => assert.equal(phase(roots.A), 'error'));
    send('A', 'CLOSE'); send('B', 'INPUT', {query: 'B'}); await until(() => requests.length === 5); deliver(requests[4], [{key: 'B-only', label: 'Nur B'}]);
    check('separate-invoke-epochs-and-data', () => { assert.equal(phase(roots.B), 'ready'); assert.equal(phase(roots.A), 'closed'); assert.equal(data(roots.B).results[0].key, 'B-only'); });
    check('no-native-runtime-errors', () => assert.deepEqual(errors, []));
    return {overall: 'PASS_LIMITED', release: false, profile: request.profile, checks, runtime: {name: '@scion-scxml/scxml', version: require(path.join(root, 'tools/openpencil/node_modules/@scion-scxml/scxml/package.json')).version},
      synthetic: ['MEASURED acknowledgement; no DOM geometry in native probe'], notChecked: ['Browser adapter', 'Screenreader', 'Real IME', 'Production release']};
  } catch (error) { return {overall: 'FAIL', release: false, profile: request.profile, checks, diagnostic: String(error), errors}; }
  finally { for (const machine of Object.values(roots)) machine.cancel(); }
};
