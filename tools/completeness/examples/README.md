# Nachvollziehbare Coveragefälle

Eigene synthetische Bibliothek unter `libraries/demo/`, ausschließlich für den Vollständigkeitscheck. Die Quellen sind absichtlich klein und kein ausgereifter Select: Beispielsweise fehlt eine vollständige Membership-/Fokuslogik. Auch `mapped.json` ist nur ein durchgehend belegter Record, kein korrekter vollständiger Vertrag.

Die Rohbeispiele unter `inputs/` sind ein künstlicher Designbeobachtungsauszug und eine kleine TypeScript-Quelle. Ihre Übertragung in Contracts ist manuell vorbereitete Testeingabe, kein bewiesener automatischer Import. Auch die abgeleiteten Contracts vereinfachen und ergänzen Aspekte; die Coverage kann deren semantische Gleichwertigkeit nicht bestätigen.

1. **Designimport:** `design-import.json` ordnet nur die beiden visuellen Fragen zu. Ergebnis: neun offene Fragen, darunter BEH-002 (Bestätigung), BEH-003 (Escape) und A11Y-002 (zugänglicher Name). Vorhandene andere Quelldateien schließen die ausdrücklich offenen Fragen nicht automatisch.
2. **Konflikt:** `conflict.json` weist Escape als widersprüchlich aus. Ergebnis: eine blockierende Frage BEH-003, keine automatische Wahl zwischen Aussagen.
3. **Durchgehend zugeordnet:** `mapped.json` bindet alle elf Kriterien. Ergebnis: `COVERAGE_RECORDED`; Komponente bleibt Draft, fachliche und Zielprüfung bleiben erforderlich.
4. **Echter Teil-Draft:** `components/design-only/component.json` hat keine Interface-/Verhaltens-/Semantikdateien. `design-only.json` ist strukturell ein gültiger all-open Coverage-Record mit elf offenen Fragen. Keine Dummy-SCXML wurde angelegt.

Vom Repository-Stamm beispielsweise:

```sh
tools/validation/.venv/bin/python tools/completeness/check.py \
  --repo tools/completeness/examples --library demo \
  --component components/choice/component.json \
  --record tools/completeness/examples/design-import.json --details
```

Exit 1 ist hier das erwartete Ergebnis. Für die anderen Fälle `--record` wechseln; beim Teil-Draft zusätzlich `--component components/design-only/component.json`. Alle Eingaben bleiben unverändert.

5. **Codeimport:** `code-import.json` ordnet nur API und grundlegende Verhaltensfragen zu; sechs Fragen zu Gestaltung, Semantik, Fokus/Tastatur und UX bleiben offen. Die vorhandene Funktionslogik wird nicht als Nachweis von Browserbedienung ausgegeben.

## So nutzt der Agent den Bericht

Aus BEH-002/003 könnte er diese zusammengehörige Rückfrage formulieren:

> „Wann soll eine Auswahl verbindlich werden: direkt beim Auswählen oder erst nach Bestätigung? Und soll Escape eine noch nicht bestätigte Auswahl verwerfen oder den bisherigen Wert unverändert lassen?“

Aus IF-001 und A11Y-002 folgen getrennte Fragen nach dem Wertevertrag und der Benennung. Der Agent darf Antworten nicht aus der Darstellung raten. Die Fragen sind keine vorgetestete Aussage über das Verhalten eines bestimmten Modells.

Nach einer Antwort: Contract ändern, neue Revision festhalten, genau betroffene Locators samt aktuellen Quellenhashes ergänzen und erneut prüfen. Die Regression `test_resolving_one_question_does_not_close_others` zeigt: Wird nur BEH-003 belegt, sinkt die offene Liste von neun auf acht; die anderen IDs bleiben offen.
