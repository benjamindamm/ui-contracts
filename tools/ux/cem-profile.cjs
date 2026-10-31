// Bounded TypeScript metadata interpretation; never evaluates a CEM expression.
const fs = require('node:fs');
const ts = require('../validation/node_modules/typescript');
const req = JSON.parse(fs.readFileSync(0, 'utf8'));
function parse(text) {
  if (typeof text !== 'string') throw Error('Missing type');
  const file = ts.createSourceFile('profile.ts', 'type T=' + text + ';', ts.ScriptTarget.Latest, true);
  if (file.parseDiagnostics.length || file.statements.length !== 1) throw Error('Invalid type syntax');
  function norm(n) {
    if (ts.isParenthesizedTypeNode(n)) return norm(n.type);
    if ([ts.SyntaxKind.StringKeyword, ts.SyntaxKind.BooleanKeyword, ts.SyntaxKind.NumberKeyword, ts.SyntaxKind.UndefinedKeyword].includes(n.kind)) return ts.tokenToString(n.kind);
    if (ts.isUnionTypeNode(n)) return {union: n.types.map(norm).sort((a,b) => JSON.stringify(a).localeCompare(JSON.stringify(b)))};
    if (ts.isLiteralTypeNode(n) && ts.isStringLiteral(n.literal)) return {literal: n.literal.text};
    if (ts.isArrayTypeNode(n)) return {array: norm(n.elementType)};
    if (ts.isTypeReferenceNode(n) && n.typeArguments?.length === 1) {
      if (n.typeName.getText(file) === 'Array') return {array: norm(n.typeArguments[0])};
      if (n.typeName.getText(file) === 'CustomEvent') return {event: norm(n.typeArguments[0])};
    }
    if (ts.isTypeLiteralNode(n)) {
      const fields = Object.create(null);
      for (const member of n.members) {
        if (!ts.isPropertySignature(member) || !member.type || !(ts.isIdentifier(member.name) || ts.isStringLiteral(member.name)) || Object.hasOwn(fields, member.name.text)) throw Error('Unsupported/duplicate record field');
        fields[member.name.text] = {type: norm(member.type), optional: !!member.questionToken};
      }
      return {record: Object.fromEntries(Object.entries(fields).sort(([a],[b]) => a.localeCompare(b)))};
    }
    throw Error('Unsupported type form: ' + ts.SyntaxKind[n.kind]);
  }
  return norm(file.statements[0].type);
}
try {
  const fields = Object.fromEntries((req.declaration.members || []).map(m => [m.name, m.type?.text]));
  const events = Object.fromEntries((req.declaration.events || []).map(e => [e.name, e.type?.text]));
  const checks = [];
  for (const [category, actual, expected] of [['members', fields, req.expected.members], ['events', events, req.expected.events]]) {
    for (const [name, text] of Object.entries(expected)) {
      const observed = parse(actual[name]), required = parse(text);
      checks.push({category, name, observed, required, passed: JSON.stringify(observed) === JSON.stringify(required)});
    }
  }
  process.stdout.write(JSON.stringify({typescript: ts.version, checks, passed: checks.every(c => c.passed)}));
} catch (error) {
  process.stdout.write(JSON.stringify({passed: false, error: String(error), code: String(error).includes('Unsupported type form:') ? 'TYPE_FORM_UNSUPPORTED' : 'TYPE_INVALID'}));
  process.exitCode = 2;
}
