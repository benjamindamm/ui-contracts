# Unabhängige Komponentenbibliotheken

Jedes Unterverzeichnis mit `library.json` ist eine eigene Bibliothek. Der Ordnername ist die Bibliotheks-ID. Es gibt keine implizit aktive Bibliothek und keinen automatischen Import aus anderen Bibliotheken.

- [example](example/README.md): bisherige Forschungs-/Beispielbibliothek mit Autocomplete, Overlay und ScrollArea. Als Orientierung gezielt lesbar; keine Vorlage für unabhängige Builds, sofern sie nicht selbst die vereinbarte Eingabe ist.
- Eigene Bibliotheken beginnen leer. Tokens und Komponenten gehören jeweils zur ausgewählten Bibliothek; generierte Ziele und Studien bleiben außerhalb ihrer Quellen.

## Nach einem Clone neu anfangen

Vom Repository-Stamm:

```sh
python3 tools/libraries/manage.py init meine-app --name "Meine App"
python3 tools/libraries/manage.py list
python3 tools/libraries/manage.py show meine-app
```

`init` legt `libraries/meine-app/library.json` mit leerem Komponentenindex und eine leere `tokens.json` an. Es kopiert weder Beispiele noch Tokens. Bestehende Verzeichnisse werden niemals überschrieben. Ein Agentenauftrag benennt danach ausdrücklich `library: meine-app` und das gewünschte Ziel. Diese Angabe ist ein Arbeitsauftrag, keine neue Definition fachlicher Komponentenwerte.

Die Bibliothek enthält später beispielsweise `button/component.json` plus ihre führenden CEM-, DTCG/CSS-, SCXML- und HTML/ARIA-Dateien. Quellverweise bleiben relativ zum jeweiligen Bibliotheks-/Komponentenverzeichnis. Die vorhandene Bindungssyntax bleibt ein Arbeitsentwurf; `init` erstellt kein geprüftes Designsystem und keine Plattformimplementierung.

## Quellen einfrieren und prüfen

```sh
python3 tools/libraries/manage.py manifest meine-app --output /tmp/meine-app-input-manifest.json
python3 skills/ui-contracts/scripts/contracts.py inspect --library meine-app
```

Das Manifest nennt den ausgewählten Root und die SHA-256-Map; seine `revision` ist wie bisher der Hash der kompakten, nach Pfad sortierten Map. Ein neuer Rollenauftrag bindet dieses Manifest und nur benötigte Quellen. Der Helper kann sie integritätsprüfen. `inspect` führt vorhandene Syntax-/Originalschemaprüfungen aus und bleibt ohne passendes semantisches Profil `BLOCKED`; daraus folgt keine allgemeine Freigabe. Für eine leere Bibliothek gibt es noch keine Komponentenabnahme. `validate` und der Autocomplete-Gegenprüfer bleiben ausdrücklich begrenzte Forschungsprüfungen.

IDs gelten im Kontext der Bibliothek: Bei mehreren Bibliotheken immer Bibliotheks-ID, Komponenten-ID und Revision zusammen nennen. Es gibt noch keinen automatischen Resolver für bibliotheksübergreifende Abhängigkeiten. Ein solcher Import muss separat vereinbart und quellengebunden werden; keine Dateien heimlich aus example übernehmen.

## Migration und historische Nachweise

Die bisherigen 22 Dateien wurden am 29. Oktober 2026 **bytegleich von `components/` nach `libraries/example/` verschoben**. Die damalige 22-Datei-Definitionsrevision ist `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`; neue zusätzliche Assets fließen dagegen in die aktuelle Gesamtbibliotheksrevision ein. Es gibt absichtlich keinen weiterhin sichtbaren components-Ordner oder Symlink.

Historische Runs, Manifeste, Reports und Messdaten werden nicht umgeschrieben. Ihre `components/...`-Locators meinen die damaligen Dateien, die jetzt unter `libraries/example/...` liegen. Der aktuelle Handoff-Resolver kann solche alten Referenzen auflösen und prüft weiterhin deren Dateihashes. Der aktuelle begrenzte Design-Gegenprüfer verwendet example, hält historische Quellenlocators aber ausdrücklich als solche kenntlich.

Diese Kompatibilität ersetzt keine alte Werkzeugversion: Hashgebundene historische Tasks erkennen geänderte Prüfer-/Skilldateien weiter als veraltet. Unveränderte historische Generatoren/Prüfscripte mit festem components-Pfad benötigen den ursprünglichen Checkout (z. B. den erhaltenen Stand `8ca5678` in einem separaten Worktree mit den gepinnten Abhängigkeiten). Alte Receipts werden durch eine aktuelle Wiederholung nicht nachträglich neu bestätigt.

[Migration und Tests](../docs/libraries/MIGRATION.md) · [Framework-Überblick](../README.md).

## Schriftdateien

Optional bindet `fonts.json` konkrete lokale Fontdateien an die Family-Tokens der ausgewählten Bibliothek. [Struktur, Inter-Beispiel und ausgeführte Fontprüfung](../docs/fonts/README.md). Die bestehenden 22 Beispieldateien bleiben erhalten; zusätzliche Fontassets bilden eine neue Gesamtbibliotheksrevision.
