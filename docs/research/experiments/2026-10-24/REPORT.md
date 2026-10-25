# Ausgeführte Nachweise: Originalschemata, Payload und Web-Mapper

Stand: 24. Oktober 2026. Dies ist die erste **E3-Runde** des Projekts. Sie ersetzt ausdrücklich die bisher nur dokumentarischen Vermutungen durch eng begrenzte Versuche. Keine UI-Komponente, kein Renderer und keine vollständige Vier-Domänen-Integration wurden implementiert. Es gab keinen Commit oder Push.

## Tatsächlich ausgeführt

| Prüfgruppe | Fälle | Gegenstand | Ergebnis |
| --- | ---: | --- | --- |
| Originalschemata | 15 | CEM Draft-07 und UXSpec Draft 2020-12 | 14 vorab erwartete Ergebnisse, eine unerwartete Akzeptanz im CEM-Gesamtschema |
| CEM-Gegenprüfung | 3 | Unveränderte Originaldefinitionen Event, CustomElementDeclaration, ClassDeclaration mit zusätzlichem Diagnosewrapper | Ursache der unerwarteten Akzeptanz eingegrenzt |
| UXSpec-Webmapper | 6 | Originalfunktionen mapContainerStyle/mapElementStyle | Größenkontrollen wirksam; vorgeschlagene Anker-/Overflowfelder in diesen Funktionen nicht umgesetzt |
| CEM-Payloadauflösung | 6 | TypeScript 5.9.3, tatsächlicher CEM-Typtext und explizite CustomEvent.detail-Projektion | Positive strukturierte Payloadfelder sowie Fehler-/Grenzfälle nachgewiesen |
| HTML-/ARIA-Checker | 5 | Nu Html Checker, gemeldeter Stand 26.10.18 | Ungültiger ARIA-Wert und doppelte ID erkannt; fehlendes controls-Ziel und falsche Instanz ohne zusätzliche Diagnose |
| CSS-Hostchecker | 4 | Derselbe Nu-Dienst im CSS-Modus | Basis-CSS geprüft; untersuchte Anchor-Syntax nicht unterstützt |
| **Gesamt** | **39** | **Getrennte Schema-, Funktions- und Adapterversuche** | **Kein gerenderter UI-/AT-Konformitätsnachweis** |

## 1. UXSpec: Originalschema und Fachsemantik

Der isolierte Behaviorfall ohne Visual wird akzeptiert. Fehlende `$machine` und ein nicht erlaubter primitiver Kontexttyp werden abgewiesen. Dagegen akzeptiert das Originalschema einen fehlenden Zielzustand, einen unbekannten Ausdrucksoperator und einen Default, der nicht zum daneben deklarierten Kontexttyp passt. Das beweist nicht, dass CLI oder Runtime dieselben Eingaben akzeptieren; diese Wege wurden hier nicht ausgeführt.

Der bisher manuell abgeleitete invoke-Befund ist nun bestätigt: Ein vollständiger Eintrag mit kind=machine, src und id wird wegen beider treffender oneOf-Zweige abgewiesen. Entfernt man die erforderliche id, akzeptiert der allgemeine Objektzweig den Eintrag. Das Originalschema wurde nicht repariert oder ersetzt. Fehlerpfade und tatsächliche Meldungen stehen in schema-results.json.

Freie Visual-Containerfelder für anchorTarget, placement und overflowY werden strukturell akzeptiert. Das ist keine bestätigte Interpretation dieser Felder. Genau diese Trennung wurde zusätzlich an den Originalmapperfunktionen geprüft.

## 2. CEM: unerwarteter Schema-Durchlass

Die ursprüngliche Erwartung war: Ein numerischer öffentlicher Eventname wird durch das Gesamtschema abgewiesen. Tatsächlich wird das Manifest akzeptiert. Diese Abweichung bleibt in schema-results-initial.json und schema-results.json erhalten; sie wurde nicht durch Umsetzen der Erwartung versteckt.

Drei Gegenfälle zeigen die Ursache: Die originale Event-Definition weist den numerischen Namen ab. Die originale CustomElementDeclaration weist dieselbe falsche Eventdeklaration ebenfalls ab. Die allgemeinere ClassDeclaration akzeptiert die Deklaration dagegen. Im Modul-`anyOf` kann damit der allgemeine Klassenzweig genügen. Die zusätzliche Diagnosehülle adressiert lediglich die unveränderten Originaldefinitionen; sie ist **keine Reparatur des Originalschemas**.

Auch syntaktisch unbrauchbarer TypeScript-Typtext, ein nicht existierendes Referenzziel und ein selbst erfundener zusätzlicher Payloadschlüssel passieren die Gesamtschemaform. Daraus folgt weder korrekte Typauflösung noch standardisierte Bedeutung des Zusatzschlüssels. X06 bleibt ein belegter Originalschema-Beitrag, aber keine Garantie vollständiger Eventfachprüfung.

## 3. Konkreter CEM-Payloadbeitrag mit zusätzlichem Adapter

Aus dem tatsächlich im synthetischen CEM gespeicherten öffentlichen Ereignis `value-change` wird der Typtext `CustomEvent<{value:string}>` genommen. TypeScript 5.9.3 löst mit seinem DOM-Typmodell `detail` auf; das Ergebnis enthält das Payloadfeld value mit Typ string. Ein zweiter Fall erhält zusätzlich eine optionale, verschachtelt typisierte metadata-Eigenschaft.

Die weiteren Fälle weisen ungültige Typausdrücke beziehungsweise fehlende Typdefinitionen ab. Ein bloßes Event ohne detail wird ausdrücklich als nicht passende Projektion erkannt. Ein numerischer Ereignisname wird durch eine zusätzliche Eingangsregel des Versuchsharness abgewiesen; diese Regel wird nicht dem CEM-Gesamtschema zugeschrieben.

**Folge für I02: U→A**, begrenzt auf ausdrücklich als TypeScript interpretierte Web-Typtexte und CustomEvent.detail. Der öffentliche Ereignisname und dessen strukturierte Payload sind damit unabhängig vom Auslösezeitpunkt erschließbar. Die Originaldaten bleiben unverändert; Typauflösung und die Web-Projektion sind die zusätzliche Bindung. Keine generelle Auflösung beliebiger JSDoc-/Closure-Syntax, externer npm-Pakete, nativer Ereignistypen oder kompletter rekursiver Typgraphen wird daraus abgeleitet.

## 4. UXSpec-Webmapper: konkrete Ausführung

Die Originalfunktion erzeugt bei maxHeight=160 den CSS-Wert 160px; ein Objekt mit value=5 und unit=rem ergibt 5rem. Die Kontrolle bestätigt also einen tatsächlich funktionierenden Größenpfad.

Zusätzliche Ankerfelder am Container erzeugen dagegen keine Ankerpositionierung. overflowY am Container und entsprechende Angaben im Style-/Elementobjekt erzeugen im geprüften Mapper keine Overflowdeklaration. Eine nachträglich angenommene allgemeine CSS-Durchreichung wäre falsch. Die Versuche rendern nichts und schließen andere Renderer/Hostregeln nicht aus. Deshalb bleiben die vollständigen UXSpec-Anker-/Scrollfragen U, jetzt mit E3-Nachweis für diese konkrete Pfadgrenze.

Der erste Mapperlauf hatte in vier Erwartungen die Standardwerte display:flex beziehungsweise flexDirection:column übersehen. Die ursprünglichen Ergebnisse sind als mapper-results-initial.json erhalten. Nach Korrektur dieser Harness-Erwartungen stimmen alle sechs Fälle; der Kandidatenquelltext blieb unverändert.

## 5. HTML-/ARIA-Checker: konkrete Reichweite

Fünf synthetische vollständige HTML-Dokumente wurden über die Textprüfung des W3C Nu Html Checker eingereicht. Die Ergebnisansicht meldete vnu 26.10.18. Es wurden ausschließlich selbst erzeugte Beispieldaten übertragen; keine Projektgeheimnisse oder Benutzerinhalte.

Der Kontrollfall besitzt eine Combobox mit aria-controls zur Listbox und aria-activedescendant zu deren Option. Der Checker gibt bereits hier eine allgemeine Warnung zu descendant/aria-owns aus. Dieser Kontrollfall wird deshalb nicht als vollständig warnungsfrei oder allgemein barrierefrei ausgegeben. Die abweichenden Fälle werden gegen genau diesen Warnungsstand verglichen.

Ein ungültiger Wert banana für aria-expanded erzeugt einen Fehler. Eine doppelte ID erzeugt einen Fehler und einen Hinweis auf das erste Vorkommen. Ein nicht existierendes aria-controls-Ziel sowie eine aktive Option aus einer zweiten Listbox erzeugen dagegen keine zusätzliche Diagnose gegenüber dem Kontrollfall. Die tatsächlichen Meldungen und alle Eingaben stehen in nu-results.json.

Damit ist ein reales Web-Werkzeug mit Teilprüfungen nachgewiesen. **WAI-ARIA X06 bleibt U** für das geforderte vollständige unabhängige Originalartefakt-/Profilprüfen. Der Dienst ist veränderlich; eine gemeldete Versionsnummer ist kein lokal gepinnter Prüfer oder normativer ARIA-Versionsnachweis. Die Warnung darf nicht durch zusätzliche aria-owns-Angaben bloß zum Schweigen gebracht werden, ohne die Produkt-/Patternsemantik zu prüfen. Die Kandidatenbeispiele selbst wurden nicht gerendert oder mit assistiver Technik bedient.

## 6. Werkzeugstand, Eingaben und Reproduktion

Python 3.12.14 mit python-jsonschema 4.25.1; vollständige aufgelöste Abhängigkeiten stehen in schema-results.json. Node 24.22.1 führt den unveränderten Original-TypeScript-Mapper mit nativer Typentfernung aus. Der Payloadversuch verwendet TypeScript 5.9.3 und dessen DOM-Bibliothek; package-lock.json enthält den Paketpin und Integritätswert. Alle Werkzeuge wurden ausschließlich im isolierten Forschungsordner bereitgestellt.

Eingaben, Erwartungen, tatsächliche Ausgaben und Fehlermeldungen sind gespeichert. source-manifest.json bindet die gelesenen Quelltexte an Originaladresse und SHA-256 des extrahierten Texts. Das ist ein Hash der Browser-Lesefassung, kein behaupteter Hash der HTTP-Originalbytes. Die Originalquellen bleiben außerhalb der Dokumentationskopie; die Reproduktionsanleitung nennt ihre exakten Ziele. Es werden keine vollständigen Kandidatenpakete oder installierten Abhängigkeiten in die Dokumentation kopiert.

Die Skripte und Ergebnisse sind Forschungsnachweise, keine Produktvalidatoren. Ein solcher Harness darf insbesondere nicht als neue originale Contractsprache oder bereits fertige Integration ausgegeben werden.

## 7. Offene Konsequenzen

Die begrenzte CEM-I02-Frage kann als Adapterbeitrag eingeordnet werden. Die bekannten UXSpec-Schemagrenszen sind jetzt praktisch belegt. Gemeinsame Referenzziele, Instanzen, externe Revisionen, Ownership und die gesamte Vier-Domänen-Kette bleiben dadurch nicht automatisch geschlossen. Jede weitere Neubewertung braucht ihren eigenen Nachweis; die Zahl offener Zellen wird nicht um die Zahl ausgeführter Testfälle verringert.

## Ergänzung: CSS-Prüfwerkzeug konkret ausprobiert

Vier zusätzliche CSS-Eingaben wurden im selben Nu-Dienst mit ausdrücklich gesetztem „check as CSS“ geprüft. Der Kontrollfall mit max-height, overflow-y und prefers-color-scheme passiert ohne Meldung. Ungültiger Overflowwert und ungültige Längeneinheit werden beanstandet. Der Fall mit anchor-scope, anchor-name, position-anchor, anchor() und anchor-size() wird dagegen als unbekannte beziehungsweise unzulässige Syntax zurückgewiesen. Die zu den gespeicherten Spezifikationsständen gehörenden Eigenschaften werden damit von diesem Dienst nicht hinreichend unterstützt.

CSS X06 bleibt U: Der getestete Dienst ist kein positiver Nachweis eines Checkers für genau unsere Draftkombination. Das ist eine Toolgrenze, keine Aussage, dass die CSS-Eigenschaften selbst nicht existieren oder kein Browser sie unterstützt. Die vier Eingaben und vollständigen Meldungen stehen in css-checker-results.json.

## Folgearbeit: SCXML und getrennte Signaturbindung

Der [SCXML-Bericht](scxml/REPORT.md) ergänzt sechs Original-XSD-Proben und vier statische CEM-/SCXML-Bindungsfälle. Zusammen mit den 39 Fällen dieser ersten Phase sind jetzt 49 begrenzte Prüffälle gespeichert. SCXML I02 ist A für das ausdrückliche Zusatzprofil; eine öffentliche Hostroute ist nicht implementiert. Aktuell 65 U-Nachweise.

## Weitere Folgearbeit: Referenzen und Bündel

[14 explorative Originalpfad-Fälle](references/REPORT.md) ergänzen den Stand auf insgesamt 63 begrenzte Prüffälle. Schema-konforme Maschinen-ID-Kollisionen überschreiben Definitionen ohne Diagnose. Bei Referenz-/Invoke-Fällen ist die gesonderte Originalschema-Vorprüfung entscheidend; diese sind nicht pauschal gültige UI-Gegenfälle. Kein weiteres U wird allein wegen dieser negativen Befunde geschlossen; weiterhin 65.

## Weitere Folgearbeit: CSS-Grammatikstände

[Zwei gebundene CSS-Prüferstände](css-grammar/REPORT.md) ergänzen je 17 Fall-/Versionspaare; insgesamt sind nun 97 benannte Prüfbedingungen in elf Gruppen dokumentiert. Neuere Anchor-Unterstützung ist belegt, die komplette gespeicherte Draftkombination bleibt ungeklärt. Kein weiteres U geschlossen; weiterhin 65.

## OpenPencil: Datenhülle und CSS-Ausgabe getrennt

[31 Originalvalidatorfälle](openpencil-validation/REPORT.md) ergänzen die zehn Bedingungshelferfälle. Nun 138 benannte Bedingungen in 14 Gruppen, weiterhin 63 U. Die pauschale Behauptung fehlender Wertübernahme ist nicht belegt; eine unerwartete Arrayannahme bleibt mit fehlgeschlagener Voraberwartung erhalten.
