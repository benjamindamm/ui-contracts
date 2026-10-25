# OpenPencil: Variablenschema und CSS-Ausgabeprüfung ausgeführt

Stand 24. Oktober 2026. Originalrevision ab2875cc761ee6cff17d389ff1c85fedae50aeab. Fortsetzung der Visualprüfung, kein neuer Produktadapter.

## Ergebnis

Die pauschale Gesprächsaussage „der Prüfer übernimmt übergebene Werte nicht“ ist durch diese Prüfung widerlegt. Das originale Variablenschema übernimmt Werte; der originale Headless-CSS-Prüfer akzeptiert auch var(--other). Beide prüfen unterschiedliche Gegenstände. Eine neu gefundene, spezifikationskonforme Alternative ist hiermit ausdrücklich nicht behauptet.

15 Fälle gegen originale Valibot-Schemata und 16 Fälle gegen den originalen CSSOM-Tokenvalidator sind ausgeführt. Vorab gespeicherte Erwartungen stehen unverändert in cases.json. 30 von 31 Erwartungen treffen zu; der Lauf endet deshalb mit Status 1. Das bedeutet keine pauschale Produktfehlerrate: viele erwartete Annahmen dokumentieren bewusst die begrenzte Rolle des Prüfers.

## Datenschema

Fehlende ID und numerischer Name werden abgewiesen. Beliebige Typzeichenfolge, falscher COLOR-Wert, unbekannte Einheit, leere Wertetabelle, nicht auflösbarer Alias und inkonsistente Modus-/Variablen-IDs werden vom untersuchten Hüllschema angenommen. Das Schema ist ausdrücklich loose und validiert Werte als unknown; stärkere Auflösung und Exportprüfung können später stattfinden. Diese Ergebnisse dürfen nicht auf den vollständigen Import-/Editorpfad verallgemeinert werden.

Unerwartet wird auch ein Array für valuesByMode akzeptiert und in ein Objekt mit Schlüssel "0" umgewandelt. Der originale Valibot-1.5.0-Recordpfad prüft auf nicht-null object und iteriert dessen Schlüssel; die Ausgabe ist in results.json erhalten. Kein eigener Array-Filter ergänzt, keine Erwartung nachträglich geändert.

Das separate COMPOSE_COLOR-Schema weist einen Farbstring statt des Farbobjekts und eine textuelle Opacity ab. Es akzeptiert hingegen die endliche Opacity 2 und einen Alias ohne aufgelöstes Ziel. Strukturprüfung, Wertebereich und Referenzintegrität bleiben getrennte Prüfschritte.

## CSS-Ausgabeprüfung

Das originale cssom-validator-Modul ruft createTokenValidator mit dem originalen @acemir/cssom-Parser auf. Gültige einfache Werte, var(), ein Selektor, Media-/Container-/Supports-Bedingungen und eine zusammengesetzte Mediaquery werden angenommen. Zusätzliche Deklarationen, mehrere erzeugte Regeln, ungültige Namen und ein nicht erlaubtes @import werden abgewiesen.

Ein Custom Property mit dem Text banana oder 16bananas bleibt zulässiger Tokenstrom für diesen Formprüfer. Ihm fehlt die fachliche Information, dass die spätere Verwendung beispielsweise color oder width erwartet. Auch ein unbekannter Wert des Mediafeatures wird strukturell angenommen. Das beweist keine vollständige Farb-/Dimensions-/Featurevalidierung. Anders als der vorher geprüfte Einzel-Featurehelfer verarbeitet dieser Pfad auch Selektoren, zusammengesetzte Bedingungen und @supports. Die Helfer dürfen nicht gleichgesetzt werden.

## Reproduktion

Originalquellen laut source-manifest.json beschaffen; SHA-256 bezieht sich auf UTF-8-Lesefassungen. Originalquellen werden nicht mitverteilt. tool/package-lock.json bindet valibot 1.5.0, postcss-value-parser 4.2.0 und @acemir/cssom 0.9.31; deren Versionen entsprechen den im Original angegebenen Bereichen. Mit npm ci --ignore-scripts im tool-Ordner wiederherstellen. run.cjs erwartet Sources unter sources/ und TypeScript 5.9.3 über PROBE_TYPESCRIPT oder den dokumentierten lokalen Vorläuferpfad. NODE_PATH auf tool/node_modules setzen. Ausgeführt mit Node 24.22.1; Originalprojekt nennt ~5.8.3 als TypeScript-Entwicklungsversion. Nur Transpilation, kein kompletter Projekt-Typecheck, Browserlauf oder Rendering.

Keine Vier-Domänen-Integration, keine Assistenztechnikprüfung, kein Commit oder Push. V01/V03 behalten ihren dokumentarisch belegten D-Beitrag; vollständige Original-/Paketvalidierung wird daraus nicht abgeleitet.
