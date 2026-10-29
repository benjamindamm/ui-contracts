# Technisches Laufblatt · run-04

Nur technische Bindungen für Rollen dieses Laufs. Keine fachlichen Regeln, keine Vorlagen, keine früheren Ergebnisse.

## Definitionsrevision

- Root: `components/`
- Manifest: `input-manifest.json` in diesem Laufordner (22 Originaldateien, `relativer Pfad -> SHA-256`).
- Revisionslabel: SHA-256 über das UTF-8-kodierte, kompakte JSON-Objekt der nach Pfad sortierten `Pfad -> Datei-SHA-256`-Paare (`sort_keys=True`, `separators=(',', ':')`, `ensure_ascii=False`).
- Erwartetes Label für diesen Lauf: `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727` (Referenz `autocomplete-openpencil-0.1.0`).
- Toolchain-Lock: `tools/openpencil/package-lock.json`, SHA-256 `ebdba8523251984285705a8b03bc15220d41773131b72c66e7a05706837749e6`.

## Gepinnte Toolchain

- Ort: `tools/openpencil/` (Abhängigkeiten bereits installiert; Lock oben).
- CLI: `npm run openpencil -- --help` (Befehle u. a. `tree`, `info`, `find`, `query`, `export`).
- Core-API für Generierung und Readback: `tools/openpencil/node_modules/@open-pencil/core/dist/index.js` (u. a. `SceneGraph` aus `@open-pencil/scene-graph`, `exportFigFile(graph)`, `parseFigFile(buffer, {populate:'all'})`).
- Neues FIG erzeugen: eigenen Node-Skript erstellen, `SceneGraph` befüllen, mit `exportFigFile` als Bytes schreiben, Ergebnisdatei im eigenen Ausgabeordner ablegen.
- Readback: exportierte Datei erneut mit `parseFigFile` lesen und native Beobachtungen (Typ, Name, Maße, Fills/Strokes, Texte) als JSON-Receipt im eigenen Ausgabeordner speichern.

## Erlaubte Lesegrenzen je Rolle

- Builder: nur Originalquellen des Auftrags (`components/...` laut `task.json`), dieses Laufblatt, das Skill-Hilfswerkzeug (`skills/ui-contracts/scripts/handoffs.py`), die gepinnte Toolchain unter `tools/openpencil/` (inkl. `node_modules` der gepinnten Pakete) und die eigene Ausgabe.
- Prüfer: zusätzlich nur die eingefrorene Policy (`policy.json`), den gemeinsamen Gegenprüfer unter `tools/design-review/` (`check.py`, `read-fig.mjs`, `profile.json` laut `policy.json` hashgebunden) und die tatsächlich gelieferten Zielartefakte der Builder.
- Keine Rolle: frühere Laufordner (`run-01` bis `run-03`), `examples/autocomplete/output/`, `examples/autocomplete/review/`, `docs/research/` als Ergebnisvorlage.

## Hilfsausgaben

- Helfer- und Prüfausgaben (`bootstrap`, `check`, `check_process`, `check.py`) schreibt das jeweilige Werkzeug nur in ein Temp-Verzeichnis außerhalb des Repositories (Pflicht der Tools). Die empfangene JSON-Ausgabe wird anschließend als Receipt in den eigenen Ausgabeordner kopiert; der ursprüngliche Temp-Pfad wird in den Dokumenten genannt.
