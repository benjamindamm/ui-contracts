// Synthetic import input, not a production component or a runtime proof.
export type ChoiceValue = string | undefined;
export type Change = { value: string };
export function createChoice(emit: (event: 'value-change', detail: Change) => void) {
  let value: ChoiceValue;
  return {
    confirm(next: string) { value = next; emit('value-change', { value: next }); },
    escape() { /* No unconfirmed state is stored; committed value stays unchanged. */ },
    get value() { return value; }
  };
}
