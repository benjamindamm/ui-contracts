# Unabhängige Komponentenbibliotheken

Jedes Unterverzeichnis mit `library.json` ist eine eigene Bibliothek. Der Ordnername ist die Bibliotheks-ID. Es gibt keine implizit aktive Bibliothek und keinen automatischen Import aus anderen Bibliotheken.

- [example](example/README.md): bisherige Forschungs-/Beispielbibliothek mit Autocomplete, Overlay, ScrollArea, Select, Input und Select mit Suche. Als Orientierung gezielt lesbar; keine Vorlage für unabhängige Builds, sofern sie nicht selbst die vereinbarte Eingabe ist.
- Eigene Bibliotheken beginnen leer. Tokens und Komponenten gehören jeweils zur ausgewählten Bibliothek; generierte Ziele und Studien bleiben außerhalb ihrer Quellen.

## Nach einem Clone neu anfangen

Vom Repository-Stamm:

```sh
python3 tools/libraries/manage.py init meine-app --name "Meine App"
python3 tools/libraries/manage.py list
python3 tools/libraries/manage.py show meine-app
```

`init` legt `libraries/meine-app/library.json` mit leerem Komponentenindex und eine leere `tokens.json` sowie die leeren Ordner `components/` und `assets/` an. Es kopiert weder Beispiele noch Tokens. Bestehende Verzeichnisse werden niemals überschrieben. Ein Agentenauftrag benennt danach ausdrücklich `library: meine-app` und das gewünschte Ziel. Diese Angabe ist ein Arbeitsauftrag, keine neue Definition fachlicher Komponentenwerte.

Die Bibliothek enthält später beispielsweise `components/button/component.json` plus ihre führenden CEM-, DTCG/CSS-, SCXML- und HTML/ARIA-Dateien. Quellverweise bleiben relativ zum jeweiligen Bibliotheks-/Komponentenverzeichnis. Die vorhandene Bindungssyntax bleibt ein Arbeitsentwurf; `init` erstellt kein geprüftes Designsystem und keine Plattformimplementierung.

## Quellen einfrieren und prüfen

```sh
python3 tools/libraries/manage.py manifest meine-app --output /tmp/meine-app-input-manifest.json
python3 skills/ui-contracts/scripts/contracts.py inspect --library meine-app
```

Das Manifest nennt den ausgewählten Root und die SHA-256-Map; seine `revision` ist wie bisher der Hash der kompakten, nach Pfad sortierten Map. Ein neuer Rollenauftrag bindet dieses Manifest und nur benötigte Quellen. Der Helper kann sie integritätsprüfen. `inspect` führt vorhandene Syntax-/Originalschemaprüfungen aus und bleibt ohne passendes semantisches Profil `BLOCKED`; daraus folgt keine allgemeine Freigabe. Für eine leere Bibliothek gibt es noch keine Komponentenabnahme. `validate` und der Autocomplete-Gegenprüfer bleiben ausdrücklich begrenzte Forschungsprüfungen.

IDs gelten im Kontext der Bibliothek: Bei mehreren Bibliotheken immer Bibliotheks-ID, Komponenten-ID und Revision zusammen nennen. Es gibt noch keinen automatischen Resolver für bibliotheksübergreifende Abhängigkeiten. Ein solcher Import muss separat vereinbart und quellengebunden werden; keine Dateien heimlich aus example übernehmen.

## Migration und historische Nachweise

Die erste Migration am 29. Oktober 2026 verschob die 22 Forschungsquellen bytegleich von `components/` nach `libraries/example/`. Seit der Trennung vom 30. Oktober liegen aktuelle Komponenten unter `libraries/example/components/`; Tokens und optionale Fontbindung bleiben am Bibliotheksroot, gemeinsame Dateien unter `assets/`.

```text
libraries/<id>/
├── library.json
├── tokens.json
├── fonts.json        # optional
├── components/
│   └── <component>/
│       └── component.json
└── assets/
    ├── fonts/
    ├── icons/
    └── images/
```

`init` erstellt nur die beiden leeren Hauptordner; Asset-Unterordner und `fonts.json` entstehen nach Bedarf. Der Komponentenindex verwendet beispielsweise `components/button/component.json`. Tokens werden aus einer Komponente über `../../tokens.json` referenziert; Verweise auf benachbarte Komponenten bleiben `../<name>/component.json`. Assets werden relativ zu der Datei referenziert, die sie bindet (etwa `assets/fonts/...` in fonts.json am Root).

Historische Runs, Manifeste, Reports und Messdaten bleiben unverändert. Die ursprünglichen 22 Quelldateien sind bytegenau unter [frozen/example-v1](../docs/libraries/frozen/example-v1/README.md) erhalten; das ist ein Forschungsarchiv, keine zweite bearbeitbare Bibliothek. Ihre Definitionsrevision bleibt `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`. Der aktuelle Handoff-Resolver löst alte `components/...`-Locators in dieses Archiv auf, sofern kein alter Root existiert, und prüft weiterhin ihre Hashes. Auch der begrenzte historische Autocomplete-Gegenprüfer bleibt an das Archiv gebunden. Er prüft damit ausdrücklich nicht die aktuelle Bibliotheksrevision.

Die aktuelle Bibliothek hat durch neue relative Pfade eine neue Revision. Alte, direkt an `libraries/example/` gebundene Gesamtmanifeste müssen im ursprünglichen Checkout verwendet werden; sie werden nicht still auf neue Dateien oder Hashes umgebogen.

Diese Kompatibilität ersetzt keine alte Werkzeugversion: Hashgebundene historische Tasks erkennen geänderte Prüfer-/Skilldateien weiter als veraltet. Unveränderte historische Generatoren/Prüfscripte mit festem components-Pfad benötigen den ursprünglichen Checkout (z. B. den erhaltenen Stand `8ca5678` in einem separaten Worktree mit den gepinnten Abhängigkeiten). Alte Receipts werden durch eine aktuelle Wiederholung nicht nachträglich neu bestätigt.

[Migration und Tests](../docs/libraries/MIGRATION.md) · [Framework-Überblick](../README.md).

## Schriftdateien

Optional bindet `fonts.json` konkrete lokale Fontdateien an die Family-Tokens der ausgewählten Bibliothek. [Struktur, Inter-Beispiel und ausgeführte Fontprüfung](../docs/fonts/README.md). Die bestehenden 22 Beispieldateien bleiben erhalten; zusätzliche Fontassets bilden eine neue Gesamtbibliotheksrevision.

## Struktur und UX aktuell prüfen

`tools/validation/.venv/bin/python tools/libraries/check.py --library ID` prüft zusätzlich die ausgewählte Bibliothek auf fehlende/falsche Quellen, Identitäten, Zustandsziele, Kompositionszyklen und Token-Aliase. Das ist ein eigener begrenzter Mindestvertrag, keine allgemeine Komponentenfreigabe. [Operative UX-Prüfung und native DMN-Auswahl](../tools/ux/README.md). Eine leere eigene Bibliothek erbt keine UX-Policy aus example.

Vor der aktiven Revision 0.3.0 wurde die komplette 50-Datei-Eingabe von SELECTION-01 bytegleich unter docs/libraries/frozen/example-selection-01 bewahrt. Der [neue externe Replay](../docs/research/analyses/ACTIVE-UX-2026-10-31/replay_selection01.py) verwendet den unveränderten ursprünglichen Helper mit diesem Datenroot; alte Eingaben und Kriterien bleiben unverändert.
