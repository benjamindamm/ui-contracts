# Evidenz der gemeinsamen Prüfkette

Stand: 26. Oktober 2026. Hauptzugang: [Bedienung und Grenzen](../README.md).

## Aktueller maßgeblicher Stand

- [web-current.json](web-current.json): gemeinsamer aktueller Bericht für run03; alle sechs Stufen im festgelegten begrenzten Webumfang bestanden.
- [run03/request.json](browser-2026-10-26-run03/request.json): Paket-/Hostrevision, Prüferfingerprint, neue Laufkennung und Challenge.
- [run03/collection.json](browser-2026-10-26-run03/collection.json): 24 aktuelle Captures (20 BR-Fälle und vier AX-Zwischenaufnahmen), vier erfolgreiche Browseroperationen, Empfangszeiten und Hashes.
- [run03/results.json](browser-2026-10-26-run03/results.json): erneute Auswertung der bisherigen 20 Browserfälle; keine neue Zählung als Kandidatenmatrixbedingungen.
- [31 Browser-Gegenfälle](browser-countercases.json), [47 bisherige Gegenfälle](countercases.json), [zwei tatsächliche Collector-Ablehnungen](collector-negative-controls.json).
- [Statische Referenz](static-reference.json), [Standardaufruf ohne Browserresultat](web-blocked.json), [fehlende Pythonbibliothek](missing-python-checker.json).

Die Rohdateien liegen unter `run03/captures/BR-01.json` bis `BR-20.json` und `AX-{loading,error,closed,ready}.json`. Ihre vollständige Liste und Einzelhashes stehen in `collection.json` und im [Gesamtmanifest](../manifest.json). Der Laufordner enthält auch die tatsächlich ausgeführten vier Browser-SDK-Skripte, den vollständigen Host-Snapshot, die neu ausgeführte Originalschema-Vorprüfung und den statischen Vorlauf.

Der gespeicherte erfolgreiche Bericht bleibt ein datierter Nachweis. Ein späterer aktueller Aufruf darf die zweistündige Laufgültigkeit nicht umgehen; danach muss neu ausgeführt werden.

## Erhaltene Vorstufen

- [static-v1/](static-v1/): ursprünglicher statischer Prüfeinstieg, bei dem noch kein Browseradapter vorhanden war; damalige Ergebnisse bleiben erhalten.
- [countercases-initial.json](countercases-initial.json), [Laufprotokoll](countercases-initial.log): Im ersten erweiterten statischen Test war der zuerst erwartete Diagnosecode für doppelte Zustands-IDs falsch; das Original-XSD wies schon vorher zurück. Die geforderte Ablehnung wurde nicht abgeschwächt.
- [run01](browser-2026-10-26-run01/request.json), [web-initial.json](web-initial.json), [damaliger Adapter](browser-gate-initial.py): erster neuer Browserlauf vor verpflichtenden Operationsreceipts. Kein aktueller Freigabebeleg.
- [run02](browser-2026-10-26-run02/request.json), [damaliger Adapter](browser-gate-before-final-hardening.py): Wiederholung nach Ergänzung der Operationsreceipts, vor abschließender Prüfer-/Berichts-/Ausgabepfadhärtung. Der aktuelle Checkerfingerprint ist verschieden.
- run03: abschließender vollständiger neuer Lauf unter aktuellem Prüfer. Die vier Browseroperationen haben jeweils erfolgreich abgeschlossen. Wiederholungen derselben 20 Fälle werden nicht künstlich als neue Forschungsbedingungen gezählt.

Die ursprünglichen 702 Bedingungen/106 Gruppen und die AC-R01-Studie bleiben separat und unverändert. Hash-/Challengezuordnung ist lokale Run-Provenienz, keine unabhängige Attestation gegen einen Betreiber, der die Dateien absichtlich fälschen kann.
