# SCXML-Originalschema und getrennte öffentliche Ereignissignatur

Stand: 24. Oktober 2026. **Sechs Original-XSD-Proben und vier zusätzliche statische Bindungsfälle ausgeführt.** Keine SCXML-Engine, kein UI-Host und kein öffentliches Ereignis wurden zur Laufzeit ausgeführt. Das hier beschriebene begrenzte Referenzprofil ist eine zusätzliche Adapterentscheidung für die Forschung, keine Auswahl eines produktiven Formatstapels.

## Vollständige Original-XSD-Kette

Acht offizielle XML-Dateien wurden über BrowserOS neo aus W3C-Quellen als XML-Quelltext gelesen. Die Browserdarstellung einzelner XML-Dateien wird durch XSL verändert; deshalb wurde für die tatsächlich zu validierenden Daten die Originalantwort im Browserkontext gelesen. Adressen und SHA-256 der UTF-8-Texte stehen in source-manifest.json. Kein Schema wurde geändert.

Die lokale Prüfung verwendet lxml 6.1.1.0 / libxml2 2.14.6 / Python 3.12.14. Ein ausschließlich lokaler Resolver bindet alle Includes/Imports; Netzwerk und Entitätsauflösung sind während der Prüfung deaktiviert. Der permissive offizielle SCXML-XSD-1.0-Driver wurde erfolgreich kompiliert. Das strengere XSD-1.1-Set wurde nicht ausgeführt.

| Fall | Vorab erwartete Prüfung | Tatsächliches Ergebnis |
| --- | --- | --- |
| Zweizustandsmaschine aus dem Vergleich | akzeptiert | akzeptiert |
| version fehlt | abgewiesen | abgewiesen |
| Zustands-ID doppelt | abgewiesen | abgewiesen |
| Zielzustand fehlt | abgewiesen | **akzeptiert** |
| Ungültiger ECMAScript-Ausdruck | strukturell akzeptiert | akzeptiert |
| Statisches send mit benanntem param | akzeptiert | akzeptiert |

Der Lauf endet wegen der unerwarteten Zielakzeptanz mit Exitstatus 1; Erwartung und tatsächliches Ergebnis bleiben unverändert gespeichert. Dies ist ein Befund über genau diese Originalschema-/Validator-Kombination. Daraus folgt keine Aussage, dass jede XSD-Implementierung oder jeder SCXML-Interpreter denselben Fehler übersieht. XSD-Erfolg ist insbesondere kein Beleg gültiger ECMAScript-Ausdrücke oder eines ausführbaren Hosts.

## Die noch offene öffentliche Signaturfrage konkret beantworten

SCXML stellt send/param bereit; eine unabhängige öffentliche Komponenten-Signatur muss zusätzlich geführt werden. Der begrenzte Forschungsfall verwendet dafür die bereits geprüfte **separate CEM-Datei** und deren TypeScript-Typtext. CEM bleibt unverändert; SCXML bekommt keine erfundenen API-Pflichtfelder.

| Information | Originalort | Zusätzliche Bindungsregel im Forschungsprofil |
| --- | --- | --- |
| Öffentlicher Ereignisname | CEM events[].name = value-change | Genau dieses öffentliche Ereignis ist das Ziel der betrachteten statischen Ausgabe |
| Öffentlicher Payloadtyp | CEM events[].type.text = CustomEvent<{value:string}> | Gewählter Web-/TypeScript-Adapter projiziert auf detail |
| Zeitpunkt der Ausgabe | SCXML onentry/send | Wird durch Behavior bestimmt; nicht im öffentlichen Typvertrag dupliziert |
| Ausgehender Ereignisname | SCXML send@event | Muss im betrachteten statischen Fall mit der zugeordneten öffentlichen Signatur übereinstimmen |
| Ausgehende Felder | SCXML send/param@name, @expr | Parameternamen und Werte müssen zur Payload passen |
| Transport | SCXML send target=#_parent | Ein späterer Host müsste diese SCXML-Ausgabe ausdrücklich in den öffentlichen CustomEvent übersetzen; diese Laufzeitroute ist **nicht getestet** |

Die Zuordnung verwendet bewusst dieselben Namen als **explizite zusätzliche Regel**. Gleichnamigkeit wird nicht als allgemeine semantische Gleichheit beliebiger Ereignisse ausgegeben. Andere Routen, dynamische eventexpr, content, namelist, alternative I/O-Prozessoren und native Ereignisse sind nicht Teil dieses Nachweises.

## Vier tatsächlich geprüfte Bindungsfälle

Die vier SCXML-Eingaben bestehen zunächst alle die unveränderte Original-XSD-Prüfung. Die zusätzliche statische Prüfung vergleicht den angegebenen Ausgabenamen mit dem separaten CEM-Event und erzeugt für die Parametertypprüfung einen TypeScript-noEmit-Prüfeingang gegen den originalen CEM-Typtext.

Dabei wird nur eine enge gemeinsame ECMAScript-/TypeScript-Teilmenge verwendet: benannte Daten mit literalem Initialwert und direkte param-Ausdrücke. TypeScript prüft diese Eingabe, es führt sie nicht aus. Das ist kein neuer allgemeiner SCXML-Ausdrucksinterpreter.

| Fall | Original-XSD | Zusätzliche Bindungsprüfung |
| --- | --- | --- |
| value-change, param value, Stringwert | akzeptiert | kompatibel |
| Anderer Ausgabenname | akzeptiert | Ereigniszuordnung abgewiesen |
| Falscher Parameternamen | akzeptiert | Payloadtypfehler |
| Numerischer Wert bei value:string | akzeptiert | Payloadtypfehler |

Eingaben, erzeugte TypeScript-Prüftexte und tatsächliche Diagnostik stehen in binding-results.json. Der Harness ist zusätzliche Forschungslogik; er wird nicht als Original-SCXML- oder CEM-Validator bezeichnet. Es gibt keine stille Erweiterung der Originalschemata.

## Konsequenz für die Matrix

**SCXML I02 wird U→A** für diesen ausdrücklich begrenzten Beitrag: statisches benanntes send/param plus separat geführte öffentliche CEM-Signatur und zusätzliche Typ-/Transportbindung. Damit ist die bisherige Frage beantwortet, ob send selbst einen unabhängigen öffentlichen Signaturkatalog bereitstellt: Dies wurde nicht belegt; im konkreten geprüften Fall liefert ihn das eigene Interfaceartefakt.

A ist kein Nachweis eines fertig implementierten Webadapters. Der öffentliche Auslösezeitpunkt bleibt vom öffentlichen Payloadvertrag getrennt. Die tatsächliche SCXML-Kommunikation, Host-Dispatch, Abbruch-/Ereignisordnung, komplexe Ausdrücke, Instanzidentität und gemeinsame Vier-Domänen-Integration bleiben offen.

## Reproduktion

Die Originaldateien anhand source-manifest.json unter sources/ ablegen; vollständige Quellkopien sind nicht Teil der Dokumentation. Die gespeicherten Hashes an der UTF-8-Lesefassung prüfen. Im isolierten Werkzeugordner Python 3.12.14 mit lxml 6.1.1 und im übergeordneten Versuchsordner TypeScript 5.9.3 bereitstellen.

```sh
python run_xsd.py
node check_binding.cjs
python check_binding_schemas.py
```

Der erste Aufruf endet bei dem aufgezeichneten unerwarteten Zielakzeptanzfall mit Status 1. Die Bindungsprüfung erwartet TypeScript standardmäßig unter ../ts-tool/node_modules/typescript; ein anderer lokaler Werkzeugpfad kann durch PROBE_TYPESCRIPT explizit angegeben werden. Kein Interpreter wird installiert oder gestartet. Die gespeicherte lxml-Versionsausgabe 6.1.1.0 ist die interne Vierer-Versionsdarstellung des Pakets 6.1.1.
