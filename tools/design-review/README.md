# Begrenzte Design-Gegenprüfung

Entstanden aus den belegten Prüflücken in [AC-R02](../../docs/research/analyses/AC-R02/README.md). **Keine Änderung oder Ersatzbewertung historischer Läufe, kein allgemeiner Komponentenvalidator.**

`profile.json` bindet die 22 Originaldateien und den Werkzeug-Lock. Die Zusatzprüfung liest tatsächliche FIG-Dateien erneut mit der gepinnten OpenPencil-Toolchain. Geänderte Definitionen oder Werkzeug-Locks enden mit `BLOCKED`; sie brauchen ein eigenes begründetes Profil.

```sh
python3 tools/design-review/check.py --run examples/autocomplete/reproducibility/run-02 --output /tmp/ac-r02-countercheck.json
python3 tools/design-review/test_review.py
python3 tools/design-review/test_process.py
```

Ausgaben nur außerhalb des untersuchten Laufordners und aller `libraries/`-Quellen. Der erste Befehl endet für die gelieferten Originale erwartungsgemäß mit Exitcode **1**, da ihre gemeinsame Platzhalterfarbe von der Quelle abweicht. Das ist kein Fehler der Ausführung. `0` bedeutet ausschließlich `PASS_LIMITED`, `2` bedeutet `BLOCKED`; `release:false` gilt immer.

## Abdeckung und Grenzen

Gemessen: Fall-/Teilevorhandensein, native Locks, Sichtbarkeit der wesentlichen Teile, Inputgröße/-radius/-kontur inklusive Stärke, Farben nach Einsatz, alle Textgrößen/Familien/Zeilenhöhen, Optionsdaten und Viewport-Clipflag/-höhe. Explizite Tokens werden verglichen; Kanalabweichungen bis 3 bleiben als Warnungen sichtbar. Eine Toleranz ist keine nachträgliche Quellfreiheit.

Nicht gemessen: vollständige Geometrie/Scroll-Offets, Schatten, echte Glyphmetriken, statische Semantikannotation, GUI-Editier-/Speicherrunde, Interaktion und Accessibility zur Laufzeit. Diese Felder stehen explizit in `notChecked`; sie werden weder pauschal als pass noch pauschal als Artefaktfehler gezählt.

Jeder Automatikeintrag enthält Soll, Ist, Status und Herkunft. Der Paarvergleich zählt alle vorhandenen semantischen Beobachtungsschlüssel; fehlende Werte werden nicht übersprungen. Er liefert Unterschiede statt eines allgemeinen Ähnlichkeits-Scores. Die Zuordnung von Textbeobachtungen folgt nativer Traversierungsreihenfolge innerhalb des Falls; bei anderer Reihenfolge können zusätzliche Unterschiede entstehen. Das ist kein pixelmetrischer oder vollständig namens-/strukturunabhängiger Vergleich.

Die zwölf Regressionstests verwenden frisch gelesene Originalknoten und verändern Kopien im Arbeitsspeicher. Sie prüfen die tatsächliche Erkennung der AC-R02-Gegenfälle, positive quellkonforme Eingaben, Sperren, Sichtbarkeit, Duplikate, fehlende Paarmerkmale sowie Profilbindungen. Sie sind keine End-to-End-Mutationsserie neu exportierter FIGs.

## Künftige Prozessprotokolle

[Protokollvertrag und Beispiel](../../docs/skills/REPRODUCIBILITY.md). Der separate Metadatenprüfer bewertet ausschließlich die Vergleichbarkeit der **aufgezeichneten** Angaben:

```sh
python3 tools/design-review/check_process.py --metadata PFAD/run-process.json --output /tmp/process-check.json
```

`METADATA_COMPLETE` / Exitcode 0 bestätigt vorhandene Angaben und Datei-Hashes, keine historische Authentizität oder Zugriffstrennung. Fehlende Angaben, nicht aufgelöste Stopps, falsche Hashes oder semantisches Nachcoaching ergeben `BLOCKED` / Exitcode 2 für den unveränderten Vergleichsanspruch. Artefakte bleiben separat prüfbar. Die sieben Regressionstests prüfen unter anderem diese Trennung.

Neue Fälle oder Fehler erhalten zuerst eine ID im [Fehlerregister](../../docs/skills/ISSUES.md), dann einen isolierten Gegenfall und einen Reparaturnachweis. Ein alter Beleg wird nicht geändert, um den neuen Test erfolgreich zu machen.

## Beispielbibliothek nach Migration

Der aktuelle Prüfer liest die bytegleich erhaltenen Quellen aus `docs/libraries/frozen/example-v1/` (historische Revision; keine Prüfung der aktuellen Library). Das eingefrorene Profil und historische `components/`-Quellenlocators bleiben erhalten und werden im Ergebnis durch `definitionRoot` erklärt. Andere Bibliotheken erhalten dadurch kein Autocomplete-Prüfprofil. Alte Tasks mit Hashes der früheren Werkzeugversion benötigen diese Version; siehe [Migration](../../docs/libraries/MIGRATION.md).
