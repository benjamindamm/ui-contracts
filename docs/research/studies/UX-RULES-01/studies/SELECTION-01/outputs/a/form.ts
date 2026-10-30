// Derived native Input/Select target. No backend, storage, or network requests.
const form = document.getElementById('personal-form') as HTMLFormElement;
const formStatus = document.getElementById('form-status') as HTMLParagraphElement;
const keys = new Set(['CH', 'DE', 'FR']);
const fields = Array.from(form.querySelectorAll<HTMLInputElement | HTMLSelectElement>('input, select'));
const previous = new Map(fields.map(field => [field.id, field.value]));
form.noValidate = true;
let attempted = false;
function validate(field: HTMLInputElement | HTMLSelectElement): boolean {
  field.setCustomValidity('');
  if (field.id === 'country' && field.value && !keys.has(field.value)) {
    field.setCustomValidity('Bitte wählen Sie ein Land aus der Liste.');
  }
  const error = document.getElementById(`${field.id}-error`)!;
  const invalid = !field.validity.valid;
  const message = field.validity.valueMissing ? 'Bitte füllen Sie dieses Feld aus.' :
    field.validity.typeMismatch ? 'Bitte geben Sie eine gültige E-Mail-Adresse ein.' :
    field.validationMessage;
  error.textContent = invalid ? message : '';
  error.hidden = !invalid;
  if (invalid) field.setAttribute('aria-invalid', 'true');
  else field.removeAttribute('aria-invalid');
  const descriptions = [document.getElementById(`${field.id}-hint`) ? `${field.id}-hint` : '', invalid ? error.id : ''].filter(Boolean);
  if (descriptions.length) field.setAttribute('aria-describedby', descriptions.join(' '));
  else field.removeAttribute('aria-describedby');
  return !invalid;
}
for (const field of fields) {
  field.addEventListener(field instanceof HTMLSelectElement ? 'change' : 'input', () => {
    if (field.disabled || (field instanceof HTMLInputElement && field.readOnly)) return;
    if (field instanceof HTMLSelectElement && field.value && !keys.has(field.value)) return;
    if (field instanceof HTMLSelectElement && field.required && !field.value && previous.get(field.id)) {
      field.value = previous.get(field.id)!;
      return;
    }
    const value = field.value;
    if (previous.get(field.id) !== value) {
      previous.set(field.id, value);
      field.dispatchEvent(new CustomEvent('value-change', { bubbles: true, detail: field instanceof HTMLSelectElement ? { value: value || undefined, reason: 'user' } : { value } }));
    }
    formStatus.textContent = '';
    if (attempted) validate(field);
  });
}
form.addEventListener('submit', event => {
  event.preventDefault();
  attempted = true;
  const results = fields.map(validate);
  const firstInvalid = results.indexOf(false);
  if (firstInvalid !== -1) {
    formStatus.textContent = 'Bitte prüfen Sie die markierten Felder.';
    fields[firstInvalid].focus();
    return;
  }
  formStatus.textContent = 'Die Angaben wurden lokal geprüft. Es wurden keine Daten versendet. Die Rufnummer wurde nicht auf internationale Gültigkeit geprüft.';
});
