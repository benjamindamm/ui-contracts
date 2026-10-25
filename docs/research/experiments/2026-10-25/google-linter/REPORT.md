# Google DESIGN.md: veröffentlichten Original-Linter ausgeführt

Stand 25. Oktober 2026. Zusätzlicher Untersuchungsgegenstand ist das veröffentlichte Paket @google/design.md 0.4.0, kein selbst angeglichener Validator. X06 bleibt offen; das tatsächlich vorhandene Tooling und seine Grenzen sind jetzt E3 belegt.

## Versionen sauber getrennt

Die bisherige Quellprüfung nutzte Commit 6e5da5382f41edbba9d73b2c62f33f32e9971f15. Die primären Registrymetadaten des Pakets 0.4.0 nennen dagegen 9bf8eae67128b6cc55ad9bf86665767deb4c11cd. Der tatsächliche Lauf nutzt den unveränderten veröffentlichten Linter samt Paketlock und Bundlehash. Parser-Spec und lint.ts wurden an beiden Commits vollständig gelesen; diese zwei UTF-8-Lesefassungen sind jeweils identisch. Daraus wird keine Identität des gesamten Repositorys abgeleitet. Parserhandler am Paketcommit und die mitgelieferte Spezifikation wurden ergänzend gelesen.

## 16 vorab definierte Hauptfälle

Die öffentliche lint-API wurde ohne eigene Regeln oder Funktionsersatz aufgerufen. Ein kleiner gültiger Farbfalldatensatz wird aufgelöst; ein falscher Farbwert und eine ungültige Rundungsdimension erzeugen Fehler. Auch ein unbekannter, tokenähnlicher Hauptschlüssel wird diagnostiziert.

Leerer Inhalt, fehlendes YAML, syntaktisch kaputtes YAML und doppelte YAML-Hauptabschnitte liefern hingegen einen Report mit leerem Modell, null Fehlern und einer Warnung. Ein zurückgegebener Report oder errors=0 ist deshalb kein Nachweis eines gültigen, vollständig verarbeiteten Dokuments. Das deklarierte ParserInputSchema mit min(1) ist kein Beleg, dass die öffentliche lint-API diesen Wrapperguard tatsächlich ausführt.

Ein Abstandswert 16bananas erzeugt in diesem Pfad keinen fachlichen Dimensionsfehler und fehlt in der aufgelösten spacing-Tabelle. Ein numerischer name-Wert wird nicht als formaler Schemafehler gemeldet; eine numerische colors-Sektion beziehungsweise eine YAML-Rootliste kann ein leeres Modell ohne Findings ergeben.

**Vier Voraberwartungen wurden widerlegt:** fehlender Tokenbezug und Tokenzyklus ohne Komponentenverwendung erzeugen keine erwarteten Fehler. Eine unbekannte Komponenteneigenschaft wird als Warnung statt des erwarteten Fehlers gemeldet. Ein Dokument nur mit name erzeugt nicht die erwartete Warnung. Alle ursprünglichen Erwartungen und Ausgaben bleiben erhalten; Hauptlauf Exitstatus 1, 12/16 Erwartungen bestätigt. Das ist keine pauschale Produktfehlerrate, da auch die Erwartungen selbst zu streng oder falsch sein können.

## Vier zusätzliche Diagnosefälle

Die Gegenprüfung trennt den unbenutzten Tokenpfad vom Komponentenpfad. Sobald eine Komponente den fehlenden oder zyklischen Farbtoken benutzt, meldet der unveränderte Linter jeweils einen unresolvedRef-Fehler. Ein gültiger Alias funktioniert als Kontrolle. Der fehlerhafte Abstand bleibt auch bei Verwendung als Component-Padding ohne fachlichen Dimensionsfehler. Die vier separat und vor ihrer Ausführung gespeicherten Diagnoseerwartungen treffen zu; Exitstatus 0.

Die Bundlequellprüfung erklärt die beobachtete Grenze: brokenRef traversiert Komponenten und deren unresolvedRefs. Ein Name der Regel oder eine allgemeine Beschreibung belegt daher nicht automatisch dieselbe Abdeckung für jeden Token im Dokument. Diese Aussage ist auf den gebundenen Paketstand und die geprüften Pfade begrenzt.

## Konsequenz für X06 und Integration

Reales originales Lintertooling ist belegt. Ein separates vollständiges Original-Dokumentschema wird dadurch nicht nachgewiesen: Textwrapperschema, Modellbildung, selektive Regeln und Spezifikationskonfiguration sind verschiedene Gegenstände. X06 bleibt U/C443. Der neue Nachweis schließt die Frage, ob überhaupt ein ausführbares Werkzeug existiert, aber nicht die engere Frage nach vollständiger Originalschema-/Fachabdeckung. Kein eigener fachlicher Validator als Original ausgegeben.

**Vorschlag für eine spätere Abnahme:** Warnungen zu nicht verarbeitetem YAML als Abnahmefehler behandeln; erwartete Modellinhalte prüfen; deklarierte, unbenutzte Token und Dimensionen separat kontrollieren; jede solche zusätzliche Regel als eigenes Prüfprofil kennzeichnen. Dieses Profil wurde hier nicht als Produktfunktion implementiert oder ausgewählt.

## Reproduktion und Artefakte

package.json/package-lock.json installieren das veröffentlichte Paket exakt, isoliert und ohne Lifecycle-Skripte. Ausgeführt mit Node 24.22.1. run.mjs importiert ausschließlich den öffentlichen Original-Linterexport mit Standardregeln. Hauptfälle: cases.json → results.json; Diagnose: PROBE_CASES=diagnosis-cases.json und PROBE_RESULTS=diagnosis-results.json. JSON enthält vollständige Reports, Maps als Objekte sowie Fall-/Bundlehashes. Parser-/Linter-/Schemaquellen werden nicht mitverteilt; gepinnte URLs und Hashes stehen im Manifest. Kein Produktcode, keine UI, kein Browser-/Assistenztest. Kein Commit oder Push.
