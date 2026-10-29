# Eingefrorene Aufgabe · Unabhängige Prüfung (Reportabgleich) · run-04

Vorgabe vor Einsicht in die Builder-Ausgaben. Die formale `task-report.json` wird nach der eingefrorenen Erstbewertung und den Builder-Handoffs aus dieser Vorgabe instanziiert (hashgebundene Eingaben); die eigentlichen Eingrenzungen ändern sich dabei nicht.

## Aufgabe

- `role`: `reviewer`, `phase`: `report-check`
- `taskId`: `ac-run04-reviewer-report`, `revision`: 1
- `goal`: Builder-Handoffs und -Reports der beiden Builder gegen die eingefrorene Erstbewertung prüfen; Widersprüche und unbelegte Pässe dokumentieren.
- `scope`: Nur die eingefrorene `first-review.json`, die Builder-Handoffs/-Reports (als Daten), die Originalquellen und die Policy. Die Erstbewertung wird nicht überschrieben; Korrekturen nur als begründeter Nachtrag.
- `definition`: Manifest `input-manifest.json`, Revision `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`.
- `sources`: wie Blindphase (22 Originaldateien, `policy.json`, `runsheet-technical.md`, technische Werkzeuge).
- `inputs`:
  - `first-review.json` (Art `first-review`),
  - Builder-A: `builder-a/handoff-v1.json` (Art `handoff`, mit `taskId`/`revision`/`producerRole`/`producerTask`) und `builder-a/REPORT.md` (Art `artifact`),
  - Builder-B: analog `builder-b/handoff-v1.json` + `builder-b/REPORT.md`.
  - Falls ein Builder-Handoff den Status `partial` oder `blocked` hat und damit kein formaler `handoff`-Input möglich ist, wird die Datei als Art `artifact` übergeben und der Status in der Bewertung separat ausgewiesen.
- `outputs`: `examples/autocomplete/reproducibility/run-04/review`
- `acceptance`:
  - `report-a` (required): Handoff/Report von Builder A gegen die Erstbewertung geprüft; Widersprüche mit Verweisen auf konkrete Stellen und gemessene Werte.
  - `report-b` (required): dito für Builder B.
  - `no-override` (required): `first-review.json` unverändert; Korrekturen nur als Nachtrag mit Begründung.
  - `handoff` (required): `handoff-report-v1.json` gemäß Übergabevertrag.
- `context`: Standardbudgets.

## Kontextregel

Gleiche Prüfer-Session wie die Blindphase (Fortsetzung), neue formale Aufgabe; die Blindbewertung ist hashgebundene Voraussetzung. Fortsetzungstext ist der in `prompts/reviewer-report.txt` abgelegte Wortlaut; keine semantische Nachsteuerung.
