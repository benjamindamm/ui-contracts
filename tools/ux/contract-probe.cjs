// Bounded native SCXML contract probes. No browser, renderer or production qualification.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '../..');
const scion = require(path.join(root, 'tools/openpencil/node_modules/@scion-scxml/scxml'));
const request = JSON.parse(fs.readFileSync(0, 'utf8'));
const checks = [];
const sha = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
async function main() {
  if (request.profile === 'composed-autocomplete/1') return require('./composed-probe.cjs').run(request);
  const events = [], waiters = [];
  const model = await new Promise((yes, no) => scion.pathToModel(request.model, (e, m) => e ? no(e) : yes(m)));
  const factory = await new Promise((yes, no) => model.prepare((e, f) => e ? no(e) : yes(f)));
  const machine = new scion.core.Statechart(factory, {parentSession: {gen: e => {
    events.push(e);
    for (const waiter of waiters) waiter(e);
  }}});
  const wait = predicate => new Promise((yes, no) => {
    if (events.some(predicate)) return yes();
    const timer = setTimeout(() => no(Error('Required native event missing')), 1500);
    waiters.push(e => { if (predicate(e)) { clearTimeout(timer); yes(); } });
  });
  machine.start();
  const data = () => machine.getSnapshot()[3];
  const send = (name, data) => machine.gen({name, data});
  const check = (id, test) => { test(); checks.push({id, passed: true}); };
  if (request.profile === 'text-input/1') {
    send('USER_INPUT', {value: '0123 Straße'});
    check('input-string-roundtrip', () => assert.equal(data().value, '0123 Straße'));
    send('SET_READ_ONLY', {readOnly: true}); send('USER_INPUT', {value: 'unexpected'});
    check('readonly-rejects-user-input', () => assert.equal(data().value, '0123 Straße'));
    send('SET_VALUE', {value: 'host'});
    check('readonly-allows-host-update', () => assert.equal(data().value, 'host'));
    send('SET_VALUE', {value: 123});
    check('numeric-host-value-rejected', () => assert.equal(data().value, 'host'));
    send('SET_READ_ONLY', {readOnly: false}); send('SET_ENABLED', {enabled: false});
    send('USER_INPUT', {value: 'unexpected'});
    check('disabled-rejects-user-input', () => assert.equal(data().value, 'host'));
    await wait(e => e.name === 'value-change' && e.data.value === '0123 Straße');
    check('input-string-event', () => assert.ok(events.some(e => e.name === 'value-change' && e.data.value === '0123 Straße')));
  } else if (['single-select/1', 'separate-search-select/1'].includes(request.profile)) {
    const search = request.profile === 'separate-search-select/1';
    const options = [{key: 'B-KEY', label: 'Bravo (+1)'}, {key: 'A-KEY', label: 'Alpha (+1)'}, {key: 'OFF', label: 'Disabled', disabled: true}];
    send('SET_OPTIONS', {options});
    check('supplied-order-and-distinct-keys', () => assert.deepEqual(data().options.map(o => o.key), ['B-KEY', 'A-KEY', 'OFF']));
    send('SET_OPTIONS', {options: [options[0], options[0]]});
    check('duplicate-key-update-rejected', () => assert.equal(data().options.length, 3));
    send('SET_VALUE', {value: 'A-KEY'});
    check('valid-host-key-accepted', () => assert.equal(data().value, 'A-KEY'));
    send('SET_VALUE', {value: 'invented'});
    check('unknown-host-key-rejected', () => assert.equal(data().value, 'A-KEY'));
    if (search) send('OPEN');
    send('USER_SELECT', {value: 'invented'});
    check('unknown-user-key-rejected', () => assert.equal(data().value, 'A-KEY'));
    send('USER_SELECT', {value: 'OFF'});
    check('disabled-option-rejected', () => assert.equal(data().value, 'A-KEY'));
    if (search) {
      send('SEARCH', {query: 'bRaVo'});
      check('case-insensitive-label-match', () => assert.ok(data().matches(options.find(o => o.key === 'B-KEY'), data().query)));
      check('query-independent-of-value', () => { assert.equal(data().value, 'A-KEY'); assert.equal(data().query, 'bRaVo'); });
      send('USER_SELECT', {value: 'A-KEY'});
      check('existing-filtered-out-option-rejected', () => assert.ok(machine.isIn('opened')));
      send('SEARCH', {query: 'unknown-query'}); send('USER_SELECT', {value: 'B-KEY'});
      check('no-match-cannot-commit-an-existing-other-key', () => { assert.equal(data().value, 'A-KEY'); assert.ok(machine.isIn('opened')); });
      send('SEARCH', {query: 'a-key'});
      check('key-can-be-searched-independently-of-label', () => assert.deepEqual(data().options.filter(o => data().matches(o, data().query)).map(o => o.key), ['A-KEY']));
      send('SEARCH', {query: '+1'});
      check('matching-does-not-reorder-or-merge-options', () => assert.deepEqual(data().options.filter(o => data().matches(o, data().query)).map(o => o.key), ['B-KEY', 'A-KEY']));
      send('SEARCH', {query: 'Bravo'}); send('ACTIVE_KEY', {key: 'B-KEY'});
      check('active-key-is-not-committed', () => { assert.equal(data().activeKey, 'B-KEY'); assert.equal(data().value, 'A-KEY'); });
    }
    send('USER_SELECT', {value: 'B-KEY'});
    check('valid-user-key-commits', () => assert.equal(data().value, 'B-KEY'));
    if (search) {
      check('commit-closes-and-clears-filter', () => { assert.ok(machine.isIn('closed')); assert.equal(data().query, ''); });
      send('OPEN'); send('SEARCH', {query: 'Alpha'}); send('ESCAPE');
      check('escape-keeps-value-clears-filter', () => { assert.equal(data().value, 'B-KEY'); assert.equal(data().query, ''); assert.ok(machine.isIn('closed')); });
    }
    send('SET_ENABLED', {enabled: false});
    if (search) { send('OPEN'); send('SEARCH', {query: 'Alpha'}); }
    send('USER_SELECT', {value: 'A-KEY'});
    check('disabled-user-changes-rejected', () => assert.equal(data().value, 'B-KEY'));
    send('SET_VALUE', {value: 'A-KEY'});
    check('disabled-host-update-accepted', () => assert.equal(data().value, 'A-KEY'));
    send('SET_OPTIONS', {options: [options.find(o => o.key === 'B-KEY')]});
    check('removed-selection-invalidated', () => assert.equal(data().value, undefined));
    await Promise.all([wait(e => e.name === 'value-change' && e.data.value === 'B-KEY' && e.data.reason === 'user'), wait(e => e.name === 'value-change' && e.data.reason === 'options-change' && e.data.value === undefined)]);
    check('actual-value-and-invalidation-events', () => assert.ok(events.some(e => e.name === 'value-change' && e.data.reason === 'options-change' && e.data.value === undefined)));
  } else throw Error('Unsupported contract verification profile');
  return {overall: 'PASS_LIMITED', release: false, profile: request.profile, checks,
    modelSha256: sha(request.model), runtime: {name: '@scion-scxml/scxml', version: require(path.join(root, 'tools/openpencil/node_modules/@scion-scxml/scxml/package.json')).version},
    notChecked: ['Browser/DOM adapter', 'Full SCXML conformance', 'Screenreader', 'Production release']};
}
main().then(result => process.stdout.write(JSON.stringify(result))).catch(error => {
  process.stdout.write(JSON.stringify({overall: 'FAIL', release: false, profile: request.profile, checks, diagnostic: String(error)}));
  process.exitCode = 1;
});
