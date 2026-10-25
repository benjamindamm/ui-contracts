# Panda: Originaler Exporttyp gegen tatsächlichen JSON-Reader

Stand: 25. Oktober 2026. **Neun vorab gespeicherte gepaarte Eingabebedingungen ausgeführt, alle Erwartungen erfüllt.** Dasselbe Eingabedatum wird jeweils am unveränderten Originalreader und über eine ausdrücklich zusätzliche Bindung am Originaltyp geprüft. Keine Wiederholung der 18 früheren Reader-/Indexfälle als neue Bedingungen gezählt.

## Gegenstand und Endbedingung

Das Originalartefakt ist Pandas design-system.json für Werkzeuge ohne Compiler am bereits gepinnten Commit 86f78a228204d63baa0b8bca2676d9f26190e449. Die originale DesignSystemSpec-Typdefinition beschreibt dieses JSON-Artefakt; parseDesignSystem ist der bereits isoliert ausführbar gemachte Originalreader. Frage: Welche Strukturregeln trägt der Originaltyp tatsächlich, welche trägt der Reader, und welche Referenz-/Wertebeziehungen trägt keiner von beiden?

Endbedingung: unveränderte Originalquellen/Hashes wiederverwenden, identische kontrollierte JSON-Daten in beiden Prüfrollen gegenübersetzen, Unterschiede und gemeinsame Grenzen konkret speichern. Kein neues Schema erfinden und den vorhandenen TypeScript-Typ nicht als originalen Runtime-JSON-Schemavalidator etikettieren.

## Originale und Zusatzbindung

Original read.ts/types.ts sind anhand des früheren source-manifest.json gebunden: Reader-SHA256 7b82843edd25a4794fdc0f9ba279b577d9eb82283e35b5f6be652bf4044bef63; Typdatei 05c7388cbdfc35eba9c9bf2eeb4b85269e8c0af4746b1669a72b794761a7613a. Vollständiges Originalreadermodul wurde früher mit TypeScript 5.9.3 transpiliert; genau dieser gehashte Output wird verwendet. Kein Funktionsersatz und keine neuen Readerregeln.

Zusätzliche Bindung: Jede eigene JSON-Fixture wird als TypeScript-Objektliteral einem importierten **Original-DesignSystemSpec** zugewiesen. TypeScript 5.9.3 prüft das mit strict/noEmit/skipLibCheck. Das ist eine statische Zusatzanbindung an den tatsächlichen Originalartefakttyp, kein neues semantisches Modell und kein Laufzeitchecker beliebiger JSON-Dateien. Die erzeugten Literale werden nicht ausgeführt. Die kleinen kontrollierten Eingaben enthalten keine Funktionen; keine allgemeine sichere Konversion fremder JSON-Daten in Programmcode behauptet.

## Neun gepaarte Bedingungen

| Eingabe | Originalreader | Originaltyp über Zusatzbindung |
| --- | --- | --- |
| Kleiner vollständiger Export | Akzeptiert | Akzeptiert |
| categories als Zahl | Akzeptiert | TS2322 |
| tokens als Boolean | Akzeptiert | TS2322 |
| null als values-Zeile | Akzeptiert | TS2322 |
| conditions und themes fehlen | Akzeptiert | TS2739 |
| values.value als Zahl statt String | Akzeptiert | TS2322 |
| refs nennt nicht vorhandenen Token | Akzeptiert | Akzeptiert |
| categories-Bereich über vorhandene paths hinaus | Akzeptiert | Akzeptiert |
| schemaVersion=-1 | Akzeptiert | Akzeptiert |

Alle neun Erwartungen treffen zu. Der Originaltyp hat also echte Shapeinformation, die der bewusst flache Reader nicht vollständig prüft. Das ist kein Beleg, dass der Reader typkonform validiert. Umgekehrt ist auch eine bestandene Originaltypzuweisung kein Nachweis referentieller Konsistenz: refs ist eine Stringliste, Kategoriegrenzen sind Zahlentupel und schemaVersion ist number. Semantische Ziel-/Bereichs-/Versionsbedingungen folgen nicht allein aus diesen Typen.

Der Rust-Generator oder ein regulärer Panda-Build wurde nicht ausgeführt. Die Gegenfälle behaupten ausdrücklich nicht, dass der reguläre Generator solche beschädigten Daten produziert. Ein Referenzfehler wird nicht zu einer Shapeverletzung umdefiniert und nicht durch künstlich strengere Originaltypen kaschiert.

## X06-Folge und verbleibender Nachweis

**Panda CSS X06 bleibt U/C469.** Es sind nun zwei konkrete vorhandene Originalgegenstände klarer belegt: die exportbezogene Shape-Typdefinition und der begrenzte Reader. Eine zusätzliche statische Typanbindung ist nachgewiesen; sie wird weder als vorhandenes neutrales Runtime-Schema noch als originale vollständige Contractvalidierung ausgegeben. Das Fehlen semantischer Referenzregeln allein wäre kein Grund, einem tatsächlich vorhandenen Originalschema sein D abzuerkennen; offen ist weiterhin dessen konkrete unabhängige Originalschema-/Validatoridentität im definierten Panda-Umfang, nicht die Forderung nach einem magisch vollständigen Prüfer.

Noch nötig: einen solchen Originalprüfgegenstand mit tatsächlichem Aufruf und abgegrenzter Regelabdeckung identifizieren oder eine abschließend belegte Modellgrenze des gesamten Kandidatenumfangs nachweisen. Der Befund ist kein globales N zu allen Panda-Paketen/Plugins oder späteren Veröffentlichungen. Ein eigener strengerer Export-/Referenzvalidator wäre eine Ergänzung und wurde hier nicht als Panda-Funktion gebaut.

Aktuell weiterhin **53 U-Zellen: 33 Integration und 20 weitere**; kein Matrixzähler durch Abschlussformulierung gesenkt. Gesamtumfang nun 330 benannte Bedingungen/42 Gruppen. Keine Produktionskomponente, Produktentscheidung, Commits oder Pushes.

## Reproduktion

prepare.py speichert Erwartungen und eigene .ts-Literalfixtures; run.cjs liest exakt diese JSON-Eingaben, führt den früher gehashten Originalreader aus und prüft die Originaltypzuweisung. TypeScript 5.9.3 und Node v24.22.1, keine neue Paketinstallation notwendig. Originalquellen anhand der im Manifest referenzierten gepinnten URLs und Hashes bereitstellen; der Ergebnisordner verteilt sie nicht als eigene Implementierung. results.json enthält Eingaben, beide Ergebnisse und sämtliche Compilerdiagnosen. Kein allgemeiner TypeScript-Projekttest oder Panda-Compilerbuild behauptet.
