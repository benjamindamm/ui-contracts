// T0/T1 record boundary for this registered combobox profile, not an arbitrary TypeScript validator.
export function validResults(rows) {
  return Array.isArray(rows) && rows.every(row => row && typeof row === 'object' && !Array.isArray(row) &&
    Object.keys(row).every(k => ['key', 'label', 'disabled'].includes(k)) && typeof row.key === 'string' && row.key.trim().length > 0 &&
    typeof row.label === 'string' && row.label.trim().length > 0 && (row.disabled === undefined || typeof row.disabled === 'boolean')) &&
    new Set(rows.map(row => row.key)).size === rows.length;
}
