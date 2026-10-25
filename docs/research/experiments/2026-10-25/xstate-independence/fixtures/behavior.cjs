// Own research fixture; XState SDK configuration, not a neutral artifact schema.
module.exports = {
  id: 'Autocomplete',
  initial: 'closed',
  context: { value: 'alpha' },
  states: {
    closed: { on: { OPEN: 'open' } },
    open: { on: { CLOSE: 'closed' } }
  }
};
