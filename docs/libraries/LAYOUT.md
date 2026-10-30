# Bibliothekslayout · 30. Oktober 2026

Entscheidung: Jede Bibliothek trennt `components/` (führende Komponentendefinitionen) und `assets/` (gemeinsame Dateien). `library.json`, `tokens.json`, optionale `fonts.json` und README bleiben am Root. [Struktur und Beispiele](../../libraries/README.md).

## Umsetzung und historische Integrität

Die drei example-Komponenten wurden in `libraries/example/components/` verschoben. Indexpfade und Tokenverweise wurden angepasst; Inhalt, IDs, Zustände, Werte und benachbarte Komponentenbindungen bleiben erhalten. Fontdateien und fonts.json bleiben unverändert unter ihrem bestehenden Pfad. Neue Bibliotheken erhalten beide leeren Hauptordner; sie kopieren keine Beispielquellen.

Da Änderungen relativer Verweise die Quellhashes verändern, wurden die ursprünglichen 22 Dateien vor der Migration bytegleich nach `frozen/example-v1/` gesichert. Das Archiv bleibt eine eingefrorene historische Eingabe und wird nicht parallel gepflegt. Alle ursprünglichen Hashes und die 22-Datei-Revision werden gegen das unveränderte Design-Prüfprofil getestet. Historische Runs, Forschungsbelege und frühere Receipts wurden nicht umgeschrieben.

Der Handoff-Resolver für alte `components/...`-Locators und der profilgebundene historische Design-Gegenprüfer verwenden das Archiv. `definitionRoot` weist dies aus. Neue Aufträge wählen dagegen `libraries/<id>/` und ein aktuelles Manifest. Historische Gesamtmanifeste mit Root `libraries/example` aus der Zeit vor der Trennung brauchen ihren ursprünglichen Checkout; keine pauschale Aliasregel für gegenwärtige Bibliothekspfade.

Die aktuelle Revision wird separat ermittelt. Kein alter Lauf erhält dadurch eine neue Freigabe. Kein neuer Browser-/Modelllauf oder plattformübergreifender Nachweis wird behauptet.

[Prüfergebnisse und Hashes](layout-verification.json).
