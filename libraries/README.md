# Unabhängige Komponentenbibliotheken

**Eine Bibliothek bündelt die Vorgaben für dein Projekt: Komponenten, Design-Tokens und Assets.** Hier wählst du eine bestehende Bibliothek oder beginnst unabhängig von unseren Beispielen.

## 1. Bibliothek wählen

- **Eigene Vorgaben:** Eine eigene Bibliothek anlegen oder eine vorhandene ausdrücklich auswählen.
- **Beispiel ausprobieren:** [example](example/README.md) enthält Autocomplete, Overlay, ScrollArea, Select, Input und Select mit Suche. Nur als ausdrücklich gewählte Eingabe oder Orientierung verwenden.

Der Ordnername unter `libraries/` ist die Bibliotheks-ID. Jeder Ordner mit `library.json` ist eine eigene Bibliothek; es gibt weder eine implizite Auswahl noch automatische Importe. Generierte Ergebnisse und Studien bleiben außerhalb der führenden Bibliotheksquellen.

## 2. Neue Bibliothek anlegen

Du kannst den [Agenten mit Skill](../docs/skills/README.md) damit beauftragen. Für die manuelle Einrichtung im Repository-Stamm:

```sh
python3 tools/libraries/manage.py init meine-app --name "Meine App"
python3 tools/libraries/manage.py list
python3 tools/libraries/manage.py show meine-app
```

`init` legt `libraries/meine-app/library.json` mit leerem Komponentenindex und eine leere `tokens.json` sowie die leeren Ordner `components/` und `assets/` an. Es kopiert weder Beispiele noch Tokens. Bestehende Verzeichnisse werden niemals überschrieben. Ein Agentenauftrag benennt danach ausdrücklich `library: meine-app` und das gewünschte Ziel. Diese Angabe ist ein Arbeitsauftrag, keine neue Definition fachlicher Komponentenwerte.

**Danach mit dem Agenten weiterarbeiten:** „Nutze die Bibliothek `meine-app`. Beschreibe eine Input-Komponente für ein Telefonnummernformular; kläre fehlende Gestaltungs- und Verhaltensregeln zuerst.“ Die neue Bibliothek enthält noch keine Komponenten und erbt keine Beispieldesigns.

Die Bibliothek enthält später beispielsweise `components/button/component.json` plus ihre führenden CEM-, DTCG/CSS-, SCXML- und HTML/ARIA-Dateien. Quellverweise bleiben relativ zum jeweiligen Bibliotheks-/Komponentenverzeichnis. Die vorhandene Bindungssyntax bleibt ein Arbeitsentwurf; `init` erstellt kein geprüftes Designsystem und keine Plattformimplementierung.

## 3. Quellenstand festhalten und prüfen

```sh
python3 tools/libraries/manage.py manifest meine-app --output /tmp/meine-app-input-manifest.json
python3 skills/ui-contracts/scripts/contracts.py inspect --library meine-app
```

Das Manifest nennt den ausgewählten Root und die SHA-256-Map; seine `revision` ist wie bisher der Hash der kompakten, nach Pfad sortierten Map. Ein neuer Rollenauftrag bindet dieses Manifest und nur benötigte Quellen. Der Helper kann sie integritätsprüfen. `inspect` führt vorhandene Syntax-/Originalschemaprüfungen aus und bleibt ohne passendes semantisches Profil `BLOCKED`; daraus folgt keine allgemeine Freigabe. Für eine leere Bibliothek gibt es noch keine Komponentenabnahme. `validate` und der Autocomplete-Gegenprüfer bleiben ausdrücklich begrenzte Forschungsprüfungen.

IDs gelten im Kontext der Bibliothek: Bei mehreren Bibliotheken immer Bibliotheks-ID, Komponenten-ID und Revision zusammen nennen. Es gibt noch keinen automatischen Resolver für bibliotheksübergreifende Abhängigkeiten. Ein solcher Import muss separat vereinbart und quellengebunden werden; keine Dateien heimlich aus example übernehmen.

## Dateiaufbau

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

## Schriftdateien

Optional bindet `fonts.json` konkrete lokale Fontdateien an die Family-Tokens der ausgewählten Bibliothek. [Struktur, Inter-Beispiel und ausgeführte Fontprüfung](../docs/fonts/README.md). Die bestehenden 22 Beispieldateien bleiben erhalten; zusätzliche Fontassets bilden eine neue Gesamtbibliotheksrevision.

## Struktur und UX aktuell prüfen

`tools/validation/.venv/bin/python tools/libraries/check.py --library ID` prüft zusätzlich die ausgewählte Bibliothek auf fehlende/falsche Quellen, Identitäten, Zustandsziele, Kompositionszyklen und Token-Aliase. Das ist ein eigener begrenzter Mindestvertrag, keine allgemeine Komponentenfreigabe. [Operative UX-Prüfung und native DMN-Auswahl](../tools/ux/README.md). Eine leere eigene Bibliothek erbt keine UX-Policy aus example.


## Frühere Quellen und Migration

Alte Studien bleiben an ihre eingefrorenen Dateien und Werkzeugversionen gebunden. Aktuelle Bibliotheken und historische Nachweise sind unterschiedliche Quellenstände. Nur für die Arbeit mit alten Läufen [Migration und Kompatibilität](HISTORY.md) nachladen.
