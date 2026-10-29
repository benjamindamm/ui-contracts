# Eingefrorene Aufgabe · Unabhängige Prüfung (Blindphase) · run-04

Vorgabe vor Einsicht in die Builder-Ausgaben. Die formale `task-blind.json` wird nach Lieferung der Builder aus dieser Vorgabe instanziiert, weil die Auftragseingaben (beide `autocomplete.fig`) per Vertrag hashgebunden sind; die eigentlichen Eingrenzungen ändern sich dabei nicht. Abweichungen von dieser Vorgabe sind nicht erlaubt.

## Aufgabe

- `role`: `reviewer`, `phase`: `blind`
- `taskId`: `ac-run04-reviewer-blind`, `revision`: 1
- `goal`: Beide gelieferten `autocomplete.fig`-Dateien gegen die Originalquellen und die eingefrorene Policy unabhängig prüfen; Erstbewertung einfrieren.
- `scope`: Nur Originalquellen, `policy.json`, `runsheet-technical.md`, die hashgebundenen technischen Werkzeuge (`tools/design-review/check.py`, `read-fig.mjs`, `profile.json`) und die beiden gelieferten FIG-Artefakte. Keine Builder-Handoffs, -Reports oder -Erklärungen in der Blindphase. Keine früheren Läufe.
- `definition`: Manifest `input-manifest.json`, Revision `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`.
- `sources`: alle 22 Originaldateien des Manifests (Art `original`); `policy.json` (Art `policy`); `runsheet-technical.md` (Art `technical`); `check.py`, `read-fig.mjs`, `profile.json` (Art `technical`).
- `inputs`: `builder-a/autocomplete.fig` und `builder-b/autocomplete.fig` (beide Art `artifact`), Hashes aus den tatsächlich gelieferten Dateien.
- `outputs`: `examples/autocomplete/reproducibility/run-04/review`
- `acceptance`:
  - `blind-basis` (required): Erstbewertung basiert nur auf Originalquellen, Policy, technischen Werkzeugen und den zwei gelieferten FIGs; kein Builder-Handoff/-Report in der Blindphase gelesen.
  - `countercheck` (required): `tools/design-review/check.py --run …/run-04` wurde tatsächlich ausgeführt; Exitcode, Blockerliste und Receipt (Pfad + SHA-256) sind dokumentiert.
  - `soll-ist` (required): Pro FIG konkrete Soll-/Ist-Aussagen zu Fällen, Teilen, Maßen, Farben, Texten mit Quellenlocatoren; Wiederverwendung der gemessenen Werte statt Neubehauptung.
  - `freeze` (required): `first-review.json` enthält Artefakt-, Quell- und Policyhashes und ist vor jeglichem Reportabgleich geschrieben (eingefroren).
  - `handoff` (required): `handoff-blind-v1.json` mit Receipts, Artefaktlisten, Claims und Checks gemäß Übergabevertrag.
- `context`: Standardbudgets (Bootstrap 2000, Inline 8000, Handoff 16000).

## Kontextregel

Frische Kind-Session ohne übernahmene Elternhistorie (OpenCode-Subagenten-Start). Die Reportabgleichsphase läuft anschließend in derselben Prüfer-Session mit einer eigenen Aufgabe in Phase `report-check`; die Blindbewertung bleibt dabei unverändert.
