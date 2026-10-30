"use strict";
(() => {
    const initialOptions = [{ "key": "CH", "country": "Schweiz", "dialCode": "+41", "label": "Schweiz (+41)" }, { "key": "DE", "country": "Deutschland", "dialCode": "+49", "label": "Deutschland (+49)" }, { "key": "FR", "country": "Frankreich", "dialCode": "+33", "label": "Frankreich (+33)" }, { "key": "CA", "country": "Kanada", "dialCode": "+1", "label": "Kanada (+1)" }, { "key": "US", "country": "Vereinigte Staaten", "dialCode": "+1", "label": "Vereinigte Staaten (+1)" }, { "key": "GR", "country": "Griechenland", "dialCode": "+30", "label": "Griechenland (+30)" }, { "key": "NL", "country": "Niederlande", "dialCode": "+31", "label": "Niederlande (+31)" }, { "key": "BE", "country": "Belgien", "dialCode": "+32", "label": "Belgien (+32)" }, { "key": "ES", "country": "Spanien", "dialCode": "+34", "label": "Spanien (+34)" }, { "key": "HU", "country": "Ungarn", "dialCode": "+36", "label": "Ungarn (+36)" }, { "key": "IT", "country": "Italien", "dialCode": "+39", "label": "Italien (+39)" }, { "key": "AT", "country": "Österreich", "dialCode": "+43", "label": "Österreich (+43)" }, { "key": "GB", "country": "Vereinigtes Königreich", "dialCode": "+44", "label": "Vereinigtes Königreich (+44)" }, { "key": "DK", "country": "Dänemark", "dialCode": "+45", "label": "Dänemark (+45)" }, { "key": "SE", "country": "Schweden", "dialCode": "+46", "label": "Schweden (+46)" }, { "key": "NO", "country": "Norwegen", "dialCode": "+47", "label": "Norwegen (+47)" }, { "key": "PL", "country": "Polen", "dialCode": "+48", "label": "Polen (+48)" }, { "key": "AU", "country": "Australien", "dialCode": "+61", "label": "Australien (+61)" }, { "key": "NZ", "country": "Neuseeland", "dialCode": "+64", "label": "Neuseeland (+64)" }, { "key": "JP", "country": "Japan", "dialCode": "+81", "label": "Japan (+81)" }, { "key": "TR", "country": "Türkei", "dialCode": "+90", "label": "Türkei (+90)" }, { "key": "IN", "country": "Indien", "dialCode": "+91", "label": "Indien (+91)" }, { "key": "PT", "country": "Portugal", "dialCode": "+351", "label": "Portugal (+351)" }, { "key": "LU", "country": "Luxemburg", "dialCode": "+352", "label": "Luxemburg (+352)" }, { "key": "IE", "country": "Irland", "dialCode": "+353", "label": "Irland (+353)" }, { "key": "FI", "country": "Finnland", "dialCode": "+358", "label": "Finnland (+358)" }, { "key": "HR", "country": "Kroatien", "dialCode": "+385", "label": "Kroatien (+385)" }, { "key": "SI", "country": "Slowenien", "dialCode": "+386", "label": "Slowenien (+386)" }, { "key": "CZ", "country": "Tschechien", "dialCode": "+420", "label": "Tschechien (+420)" }, { "key": "SK", "country": "Slowakei", "dialCode": "+421", "label": "Slowakei (+421)" }];
    const el = (id) => document.getElementById(id);
    const trigger = el('country-trigger'), picker = el('country-picker'), search = el('country-search'), list = el('country-options'), hidden = el('country-key'), display = el('country-value'), empty = el('country-empty'), countryError = el('country-error'), result = el('form-result'), host = el('country-control');
    let options = [], value, opened = false, enabled = true;
    const matches = (o) => (o.label + ' ' + o.key).toLowerCase().includes(search.value.toLowerCase());
    const clearSuccess = () => { result.textContent = ''; };
    function paint() {
        hidden.value = value ?? '';
        display.textContent = options.find(o => o.key === value)?.label ?? 'Bitte wählen';
        list.replaceChildren();
        for (const o of options.filter(matches)) {
            const row = document.createElement('li');
            row.id = 'country-option-' + o.key;
            row.dataset.part = 'option';
            row.dataset.key = o.key;
            row.role = 'option';
            row.tabIndex = -1;
            row.textContent = o.label;
            row.setAttribute('aria-selected', String(o.key === value));
            if (o.disabled)
                row.setAttribute('aria-disabled', 'true');
            row.addEventListener('click', () => commit(o.key));
            list.append(row);
        }
        empty.hidden = list.children.length !== 0;
    }
    function close(restore = false) { opened = false; picker.hidden = true; trigger.setAttribute('aria-expanded', 'false'); search.value = ''; paint(); if (restore)
        trigger.focus(); }
    function open() { if (!enabled)
        return; opened = true; search.value = ''; paint(); picker.hidden = false; trigger.setAttribute('aria-expanded', 'true'); search.focus(); }
    function commit(key) { if (!enabled || !opened || !options.some(o => o.key === key && !o.disabled && matches(o)))
        return; const changed = value !== key; value = key; close(true); countryError.hidden = true; trigger.removeAttribute('aria-invalid'); trigger.setAttribute('aria-describedby', 'country-hint'); if (changed) {
        clearSuccess();
        host.dispatchEvent(new CustomEvent('value-change', { bubbles: true, detail: { value, reason: 'user' } }));
    } }
    function setOptions(next) { if (!Array.isArray(next) || !next.every((o, i, a) => o && typeof o.key === 'string' && o.key.trim() && typeof o.label === 'string' && o.label.trim() && (o.disabled === undefined || typeof o.disabled === 'boolean') && a.every((p, j) => i === j || p.key !== o.key)))
        return; options = next.map(o => ({ ...o })); if (value !== undefined && !options.some(o => o.key === value && !o.disabled)) {
        value = undefined;
        clearSuccess();
        host.dispatchEvent(new CustomEvent('value-change', { bubbles: true, detail: { value, reason: 'options-change' } }));
    } paint(); }
    function setValue(next) { if (next !== undefined && !options.some(o => o.key === next && !o.disabled))
        return; value = next; clearSuccess(); paint(); }
    function setEnabled(next) { enabled = next; trigger.disabled = !next; search.disabled = !next; close(); }
    // Component API mirrors the original setter events; user commits remain membership guarded.
    Object.assign(host, { setOptions, setValue, setEnabled });
    trigger.addEventListener('click', () => opened ? close() : open());
    el('country-close').addEventListener('click', () => close(true));
    search.addEventListener('input', () => { if (enabled) {
        clearSuccess();
        paint();
    } });
    function focusRow(index) { const rows = Array.from(list.querySelectorAll('[role=option]:not([aria-disabled=true])')); if (!rows.length)
        return; rows.forEach(r => r.tabIndex = -1); const row = rows[Math.max(0, Math.min(index, rows.length - 1))]; row.tabIndex = 0; row.focus(); row.scrollIntoView({ block: 'nearest' }); }
    picker.addEventListener('keydown', e => { if (e.key === 'Escape') {
        e.preventDefault();
        close(true);
        return;
    } const rows = Array.from(list.querySelectorAll('[role=option]:not([aria-disabled=true])')); const index = rows.indexOf(document.activeElement); if (e.target === search) {
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            focusRow(0);
        }
        else if (e.key === 'Enter')
            e.preventDefault();
        return;
    } if (index < 0)
        return; if (['ArrowDown', 'ArrowUp', 'Home', 'End'].includes(e.key)) {
        e.preventDefault();
        focusRow(e.key === 'Home' ? 0 : e.key === 'End' ? rows.length - 1 : index + (e.key === 'ArrowDown' ? 1 : -1));
    }
    else if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        commit(rows[index].dataset.key);
    } });
    picker.addEventListener('focusout', e => { const next = e.relatedTarget; if (next instanceof Node && picker.contains(next))
        return; if (opened)
        close(); });
    document.addEventListener('pointerdown', e => { if (opened && !host.contains(e.target))
        close(); });
    setOptions(initialOptions);
    const form = el('personal-form');
    const fields = ['givenName', 'familyName', 'email', 'nationalNumber'].map(key => ({ key, input: el('person-' + key), error: el(key + '-error') }));
    for (const f of fields) {
        let previous = f.input.value;
        f.input.addEventListener('input', () => { if (f.input.disabled || f.input.readOnly)
            return; clearSuccess(); f.error.hidden = true; f.input.removeAttribute('aria-invalid'); f.input.removeAttribute('aria-describedby'); if (previous !== f.input.value) {
            previous = f.input.value;
            f.input.parentElement.dispatchEvent(new CustomEvent('value-change', { bubbles: true, detail: { value: previous } }));
        } });
    }
    form.addEventListener('submit', e => {
        e.preventDefault();
        clearSuccess();
        let first;
        for (const f of fields) {
            const valid = f.input.value.trim().length > 0 && f.input.validity.valid;
            f.error.hidden = valid;
            if (!valid) {
                f.error.textContent = f.input.validity.typeMismatch ? 'Bitte eine gültige E-Mail-Adresse eingeben.' : 'Bitte dieses Feld ausfüllen.';
                f.input.setAttribute('aria-invalid', 'true');
                f.input.setAttribute('aria-describedby', f.error.id);
                first ?? (first = f.input);
            }
            else {
                f.input.removeAttribute('aria-invalid');
                f.input.removeAttribute('aria-describedby');
            }
        }
        const validCountry = options.some(o => o.key === value && !o.disabled);
        countryError.hidden = validCountry;
        if (!validCountry) {
            countryError.textContent = 'Bitte eine Ländervorwahl wählen.';
            trigger.setAttribute('aria-invalid', 'true');
            trigger.setAttribute('aria-describedby', 'country-hint country-error');
            first ?? (first = trigger);
        }
        if (first) {
            first.focus();
            return;
        }
        result.textContent = 'Ihre Angaben wurden lokal geprüft. Es wurden keine Daten versendet.';
    });
})();
