# CSS-Grammatik: zwei gebundene Prüferstände

Stand: 24. Oktober 2026. **17 Deklarationsfälle je Version, insgesamt 34 Fall-/Versionspaare ausgeführt.** Geprüft wurden die unveränderten Wörterbücher und der Property-Lexer von css-tree 3.1.0 und 3.2.1; keine Grammatikergänzung, keine UI und keine Browserunterstützungsprüfung.

Die 3.1.0-Paketidentität wurde vor Bereitstellung anhand der offiziellen Registry geprüft. Der anschließende Abruf des latest-Eintrags zeigte 3.2.1; dieser Stand wurde getrennt und exakt gebunden untersucht. package-lock-3.1.0.json und package-lock-3.2.1.json binden auch Abhängigkeiten und Integrität. 3.1.0 verwendet mdn-data 2.12.2, 3.2.1 verwendet mdn-data 2.27.1. „Latest“ ist nur eine datierte Beobachtung, keine spätere Versionsgarantie.

## Was besser unterstützt wird und was offen bleibt

| Fall | css-tree 3.1.0 | css-tree 3.2.1 |
| --- | --- | --- |
| anchor-name und anchor-scope mit --input | akzeptiert | akzeptiert |
| position-anchor mit benanntem Anker | akzeptiert | akzeptiert |
| top: anchor(bottom) | abgewiesen | akzeptiert |
| width: anchor-size(width) | abgewiesen | akzeptiert |
| max-height: 160px und overflow-y: auto | akzeptiert | akzeptiert |
| Falsche Längeneinheit, Overflowwert, bloßer Ankername ohne -- | abgewiesen | abgewiesen |
| position-anchor: --missing | syntaktisch akzeptiert | syntaktisch akzeptiert |
| top: calc(anchor(bottom) + 8px) | akzeptiert | akzeptiert |
| top: calc(anchor(banana) + 8px) | **ebenfalls akzeptiert** | **ebenfalls akzeptiert** |
| position-anchor: normal / match-parent | abgewiesen | abgewiesen |
| max-height: var(--max-height) | Matching ausdrücklich nicht unterstützt | Matching ausdrücklich nicht unterstützt |

Die Propertywörterbücher und tatsächlichen Fehler stehen pro Fall in den Ergebnissen. Ein erfolgreicher äußerer calc-Match beweist hier keine Prüfung aller verschachtelten Anchorargumente. Ein fehlender Anker wird ohne DOM-/Instanzkontext nicht erkannt. Die var-Antwort ist **eine Unterstützungsgrenze des Matchers**, kein Nachweis ungültigen CSS.

## Abgleich mit dem gespeicherten Originalstandard

Der geprüfte Anchor-Working-Draft vom 27. März 2026 definiert für position-anchor ausdrücklich normal, none, auto, einen Ankernamen und match-parent. Die gespeicherten css-tree-Wörterbücher enthalten 3.1.0 nur auto/Ankername, 3.2.1 auto/none/Ankername. Ein neueres Paket deckt damit noch nicht automatisch den ausgewählten Draftstand ab.

Die negative verschachtelte Anchorprobe verwendet banana als anchor-side; dies gehört nicht zu den definierten Seitenwerten. Die beobachtete Akzeptanz darf nicht durch ein grünes Property-Matchergebnis als vollständige Draftkonformität ausgegeben werden.

Die originalen CSS-Formate wurden nicht erweitert. Es wurde auch kein eigenes ergänztes Grammatikpaket als Originalvalidator bezeichnet. Ein zusätzlicher, ausdrücklich gebundener Checker-/Profilaufbau könnte die Lücken später behandeln; er wäre zusätzliche Projektarbeit.

## Konsequenz

**CSS X06 bleibt U** für einen geeigneten vollständigen Prüfeinstieg der gespeicherten Modulstände. Gegenüber dem zuvor untersuchten Nu-Dienst existiert nun ein konkreter lokal gebundener Checker mit deutlich mehr Anchor-Unterstützung. Zugleich sind seine Versions-, Verschachtelungs-, Variablen- und Referenzgrenzen praktisch sichtbar. Das schließt weder DOM-/Instanzprüfung noch native Layoutübertragung ein.

## Reproduktion

Node 24.22.1 verwenden; die beiden package-Dateipaare in tool/ und tool-current/ ablegen und jeweils npm ci mit deaktivierten Installationsskripten ausführen. Die installierten Originalpakete sind nicht Teil der Dokumentationskopie.

```sh
npm ci --prefix tool --ignore-scripts --no-audit --no-fund
npm ci --prefix tool-current --ignore-scripts --no-audit --no-fund
PROBE_CSS_OUTPUT=results-3.1.0.json node run.cjs
PROBE_CSS_TOOL=./tool-current/node_modules PROBE_CSS_OUTPUT=results-3.2.1.json node run.cjs
```

Dies sind gezielte Lexermatches mit dokumentierten Erwartungen, keine allgemeine Stylelint-/Browser-Konformitätsprüfung. Die Versionspaare werden als unterschiedliche Prüfbedingungen gezählt; frühere Zwischenläufe mit weniger Fällen erhöhen die Fallzahl nicht zusätzlich.
