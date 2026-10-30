# SELECTION-02 · Select mit Suche

**Abgeschlossen im begrenzten Studienumfang:** Zwei frische Builder wählen **Select bei drei** und **SelectWithSearch bei 30** vorgegebenen Ländervorwahlen. Tatsächliche Formulare wurden zentral im Browser geprüft. Ein Fokusfehler der B-Erstlieferung ist erhalten und separat repariert. Keine allgemeine UX-/Produktfreigabe.

[Prüfbericht](review/REVIEW.md) · [Ergebnisdaten](review/results.json) · [Vorabprotokoll](PROTOCOL.md) · [Studienregister](study.json) · [Kriterien](review/criteria.json) · [Freeze](freeze.json) · [Errata](ERRATA.md)

Der Versuch folgt auf die Nutzerkritik an SELECTION-01: Eine freie Schreibhilfe ist etwas anderes als eine feste Auswahl, und ein Select mit Suche fehlte im damaligen Angebot. Die [UX-Leitlinie](../../../../../ux/AUTOCOMPLETE.md) dokumentiert Zweck, Eignung, Gegenbeispiele und offene freie Variante.

## Ergebnis lesen

- **Neue Definition:** [SelectWithSearch](candidate-library/libraries/example/components/select-with-search/README.md), [vier Domänen](candidate-library/libraries/example/components/select-with-search/component.json), [Fähigkeitsprofil](candidate-library/libraries/example/components/select-with-search/ux.json), [Auswahlpolicy](candidate-library/libraries/example/selection-policy.json).
- **Erstlieferungen:** [A / Select](outputs/a/REPORT.md), [B / Select mit Suche](outputs/b/REPORT.md); Quellen/Entscheidungen bleiben unverändert.
- **Browserprüfung:** 36/37 begrenzte Erstchecks erfüllt, Fokusfehler SEL2-B01. Separate [B-Reparatur](outputs/b-repair-01/REPORT.md) erfüllt 10/10 betroffene Regressionen. Zählwerte sind keine Erfolgswahrscheinlichkeit oder UX-Qualitätsnote.
- **Vorprüfungen:** vier native DMN-Fälle, vier Fähigkeits-/Quellenprofile, 13 tatsächliche SCION-Verhaltensprüfungen; Originalformatprüfung akzeptiert Syntax/Originalschemas, bleibt insgesamt BLOCKED wegen fehlendem allgemeinem Semantikprofil.

Die Bibliothek ist eine **eigene Forschungsrevision** unter candidate-library/libraries/example. Keine Änderung an der vorherigen Live-example-Revision oder an SELECTION-01. Ein späteres Übernehmen in eine aktive Bibliothek braucht eine neue ausdrückliche Revision und deren Bindungen; freie Adress-Autovervollständigung ist noch nicht gebaut.

## Tatsächliche Browseransichten

A: natives Select. B: reparierte Ausgabe mit separater Suche „+1“ und unverändert bestätigtem Indien. Die Bilder wurden zentral aus den tatsächlichen Seiten aufgenommen, nicht von den Buildern oder einem Designexport erzeugt.

[Formular A](review/screenshots/a.png) · [Formular B, separate Reparatur](review/screenshots/b.png)

Eine Beobachtung pro Bedingung, geänderte Policy und geändertes Angebot erlauben keine isolierte Kausalaussage. Modellidentität, vollständige Zugriffsisolation, vollständige Accessibility und Plattformübertragbarkeit bleiben unbelegt.
