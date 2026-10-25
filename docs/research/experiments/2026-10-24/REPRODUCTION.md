# Reproduktion der begrenzten Forschungsproben

Die Skripte sind zusätzliche Forschungswerkzeuge, keine Originalvalidatoren der Kandidaten und keine Produktimplementierung. Quellen werden unverändert als Eingabe verwendet. Die vollständigen Originaldateien und installierten Pakete sind nicht Bestandteil dieser Dokumentationskopie.

1. Die drei exakten Adressen in `source-manifest.json` im Browser öffnen und die Quelltexte als UTF-8 unter den dort genannten `sources/`-Namen sichern. Die aufgezeichneten Hashes beziehen sich auf den aus dem gespeicherten vollständigen Browserauszug extrahierten Codeblock; zusätzliche abschließende Zeilenumbrüche können den Text-Hash ändern. Inhaltliche Abweichungen zuerst klären. `style-map.mts` ist eine Umbenennung des originalen style-map.ts für Nodes Modulmodus; der Inhalt ist unverändert.
2. Python 3.12.14, Node 24.22.1 und die festgehaltenen Pakete ausschließlich in einem isolierten Arbeitsordner verwenden. Vollständige Paketstände stehen in den Ergebnissen; `typescript-package-lock.json` bindet das TypeScript-Paket.
3. Aus diesem Ordner ausführen:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-probe.txt
.venv/bin/python run_schema.py
.venv/bin/python diagnose_cem.py
node run_mapper.mjs
npm ci --prefix ts-tool --ignore-scripts --no-audit --no-fund
node resolve_payload.cjs
```

Für npm ci zuvor `typescript-package.json` und `typescript-package-lock.json` als `ts-tool/package.json` und `ts-tool/package-lock.json` ablegen. Der Schemaaufruf endet beim aufgezeichneten CEM-Überraschungsfall mit Exitstatus 1, weil die vorab festgelegte Erwartung falsch war. Das ist ein gespeicherter Forschungsbefund; nicht durch Änderung der Erwartung verdecken. Die Gegenprüfung erklärt den Unterschied der Original-Schemazweige.

`mapper-results-initial.json` hält die vier zuerst unvollständigen Harness-Erwartungen fest. Nach Berücksichtigung der gelesenen Standardlayoutwerte stimmen die endgültigen sechs Erwartungen. Es gibt keine Änderung des Originalmappers.

Die fünf Nu-Prüfungen wurden im Browser über https://validator.w3.org/nu/ → „text input“ ausgeführt. Jeweils das input-Feld eines Eintrags aus `nu-results.json` einfügen, prüfen und vollständige Meldungen sowie gemeldete Dienstversion speichern. Ein späterer veränderter Dienst darf andere Ausgaben liefern; dies ist kein lokal gepinnter Nu-Release. Formulierung und Ergebnis jeder Eingabe wurden zum damaligen Zeitpunkt aufgezeichnet. Die HTML-Eingaben dienen der statischen Prüfung, nicht als fertige Autocomplete-Implementierung.

Die vier zusätzlichen CSS-Prüfungen stehen in css-checker-results.json. Beim selben Nu-Dienst ausdrücklich „check as CSS“ aktivieren, Eingabe einsetzen und die vollständige Ergebnisansicht speichern. HTML- und CSS-Modus sind getrennte Prüfgegenstände.
