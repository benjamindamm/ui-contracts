# Bibliotheken · Migration und Grenzen

Aktuelle Ergänzung vom 30. Oktober 2026: [Trennung von components und assets](LAYOUT.md). Die folgenden Abschnitte dokumentieren die erste Migration vom 29. Oktober; deren damalige Receipts bleiben erhalten.

29. Oktober 2026. Auf Nutzerentscheid: Die bisherige Draftbibliothek wird eine gleichberechtigte **Beispielbibliothek**, eigene Projekte beginnen separat und leer. [Bedienung und Architektur](../../libraries/README.md).

## Umsetzung

- `components/` → `libraries/example/`, alle 22 Quelldateien bytegleich verschoben. Keine Root-Aliasdatei und kein components-Symlink.
- `tools/libraries/manage.py`: Bibliotheken entdecken (`list`), gezielt auswählen (`show ID`), leer anlegen (`init ID`) und einfrieren (`manifest ID --output ...`). Es gibt keine globale aktive Bibliothek, keine automatische Vererbung und kein Kopieren der Beispieldefinition.
- `library.json` bleibt ein eigener Draftindex. Bibliotheks-ID entspricht dem Ordnernamen; vorhandene Komponenten-IDs und das bestehende Indexformat wurden nicht nachträglich geändert.
- Autoren- und Rolleneinstiege verlangen eine ausdrücklich gewählte Bibliothek. Der Agent liest nur deren relevante Quellen. example kann bei einer normalen Aufgabe auf Wunsch als Orientierung dienen; bei Blind-/Reproduktionsaufträgen gelten weiterhin deren erlaubte Quellen.
- `contracts.py inspect --library ID`: begrenzte Originalformatprüfung der gewählten Bibliothek. Der Referenzpaketvalidator und Autocomplete-Gegenprüfer werden nicht zu allgemeinen Bibliotheksvalidatoren erklärt.
- Ausgaben/Receipts dürfen keine Libraryquellen überschreiben. Deklarierte Handoff-Ausgabeordner dürfen auch nicht in einer anderen Bibliothek liegen.

## Erhaltene Forschungsbindung

Definitionsrevision: `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`, weiterhin aus derselben relativen Pfad-/Hashmap abgeleitet. Der neue Manifestroot ist `libraries/example`, die alten Manifeste behalten `components`.

Der heutige Handoff-Resolver übersetzt ausdrücklich angegebene historische `components/...`-Verweise nach example, wenn kein alter components-Root vorhanden ist. Die Dateien müssen weiterhin ihre gebundenen Hashes erfüllen. Neue Aufträge schreiben den echten Bibliothekspfad. Der heutige Autocomplete-Gegenprüfer liest example und kennzeichnet die im eingefrorenen Profil erhaltenen historischen Quellenlocators.

Historische Runs und deren eingefrorene Werkzeug-/Skillhashes wurden nicht angepasst. Nach einer Werkzeugänderung darf ein historischer Auftrag mit altem Toolhash weiterhin blockieren; eine Pfadübersetzung ist keine Erlaubnis, die Hashbindung zu ignorieren. Für unveränderte historische JS-/Python-Scripte mit hartem components-Pfad den erhaltenen ursprünglichen Stand separat auschecken, etwa `8ca5678`, und die gepinnten Werkzeuge installieren. Aktuelle Wiederholungen separat dokumentieren.

## Dokumentation und Tests

Aktuelle Navigation angepasst: Haupt-README, AGENTS.md, Bibliotheksanleitung, Skill-Einstieg/Autoren-/Prüf-/Workflowreferenzen, Beispiel-Einstiegsseiten, TASKS und das geplante Pilotprotokoll. Historische Studien, Analysen, Experimente, Ergebnisse und Prozessreceipts bleiben Belege ihres damaligen Stands; sie sind keine gegenwärtigen Pfadvorgaben.

[Maschinenlesbare Migrationsverifikation](verification.json) enthält Quellhashes, ausgeführte Regressionen und Grenzen. [Librarytests](../../tools/libraries/test_libraries.py) prüfen insbesondere Leerstart, getrennte Tokens, keine Überschreibung, sichere Pfade, Auswahl, Quellschutz und bytegleichen Umzug. Bestehende Handoff-, Design- und Prozessregressionen wurden ebenfalls ausgeführt. Die begrenzte run-04-Gegenprüfung besteht weiterhin mit 572/572 gleichen Paarwerten und ohne Fehler/Warnungen.

Kein neuer Modelllauf, keine GUI-/Nativeprüfung und keine allgemeine semantische Freigabe neuer Bibliotheken. Bibliotheksübergreifende Abhängigkeiten haben noch keinen automatischen Resolver.

## Nachfolgende Font-Ergänzung

Die [Inter-Assets und Fontbindung](../fonts/README.md) ergänzen example, ohne die ursprünglichen 22 Dateien zu ändern. Der obige Migrationsbeleg dokumentiert den Stand vor dieser Ergänzung; neue vollständige Librarymanifeste enthalten auch die Fontdateien und haben eine andere Gesamtbibliotheksrevision. Historische Studien erhalten dadurch keine zusätzliche Fontprüfung.
