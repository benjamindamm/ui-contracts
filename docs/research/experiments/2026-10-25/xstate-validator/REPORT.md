# XState X06: Originalartefaktprüfung, SDK-Typen und Laufzeit getrennt

Stand: 25. Oktober 2026. **Konkrete X06-Folgefrage zum veröffentlichten xstate-Core 5.33.3 abgeschlossen. Sechs Original-API-Bedingungen und drei SDK-Typbedingungen ausgeführt; sämtliche vorher gespeicherten Erwartungen erfüllt.** Kein eigenes Ersatzschema gebaut.

## Gegenstand, Kriterium und Endbedingung

Bewerteter Originalgegenstand: eine separat gespeicherte Maschinenkonfiguration als Domänenartefakt, hier machine.json. Gesucht ist dessen im Core bereitgestellter Originalschema-/Artefaktvalidator gemäß der bereits verwendeten X06-Auslegung. **Ein TypeScript-Programm gegen SDK-Deklarationen zu prüfen, eine Maschine zu konstruieren, eine Definition zu exportieren und einen Snapshot wiederherzustellen sind andere Prüfgegenstände.** Diese Unterscheidung ist bereits Gegenstand von C405 und wird hier praktisch geprüft.

Endbedingung: genaue Originaldistribution binden, tatsächlich vorhandene Original-API-/Typprüfpfade unterscheiden und die schemas-/Restore-Grenze mit positiven und negativen Kontrollen prüfen. Wenn der abgegrenzte Core kein solches eigenständiges Artefaktschema anbietet, diese konkrete Grenze begründen; keine negative Aussage über sämtliche XState-/Stately-Werkzeuge oder fremde Erweiterungen aus einer fehlenden Suche ableiten.

## Originalidentität und untersuchter Umfang

Original-NPM-Distribution **xstate 5.33.3**. Exakte Registry-Metadaten am 25.10.2026 über BrowserOS gelesen; Paket isoliert mit festem Lock und ohne Installationsskripte installiert. RegistryfileCount und tatsächlicher Paketumfang stimmen überein: **132 Dateien**. source-audit.json enthält deren vollständige Liste und Hashes, öffentliche Packageexporte und schemas-Vorkommen. Die sieben JSON-Dateien sind Paket-/Entrypointmetadaten, keine Maschinenartefaktschemas. Diese Inventur ist kein vollständiger Audit der Semantik aller Bibliotheksfunktionen.

Gelesene relevante Originalpfade: default CommonJS-Entrypoint, setup/createMachine, StateMachine-Konstruktor, schemas-Feld, toJSON/definition, restoreSnapshot und zugehörige SDK-Typdeklarationen. Exportierte Core-API und die öffentlichen Packageentrypoints sind protokolliert. Der schemas-Wert wird durchgereicht und gespeichert; die originale Deklaration dafür ist unknown. StateMachine stellt Graph/Transitions zusammen. Restore ist eine Methode der schon vorhandenen Maschine und bindet vorhandene Zustands-/Actorlogik.

Node v24.22.1, tatsächlich geladener Default-CommonJS-Build; **kein development-Condition-Lauf**. TypeScript 5.9.3 für die getrennten SDK-Fälle. Die Registry liefert hier keinen gitHead. Der frühere Quellsnapshot S28/S62 nennt ebenfalls Paketversion 5.33.3; eine ungeprüfte Byteidentität der jetzigen Distribution mit Commit 8f25b68… wird nicht behauptet. Für diesen Versuch führen Paketlock, Integrity und Dateihashes.

## Sechs tatsächliche Core-API-Bedingungen

| Fall | Gespeicherte Beobachtung |
| --- | --- |
| JSON-Maschinenkontrolle | createMachine/getInitialSnapshot akzeptiert, initial closed |
| schemas=false | Akzeptiert, Wert unverändert auf machine.schemas erhalten |
| schemas mit absichtlich werfender parse-Funktion | Maschine akzeptiert, Funktion nullmal aufgerufen, Objektidentität erhalten |
| Kontextwert 42 trotz übergebenem schemas.context mit string-Vorgabe | Akzeptiert, Initialkontext führt tatsächlich Zahl 42 |
| Transition auf missing-state | Originaler Graphaufbau weist sie zurück: Ziel existiert nicht |
| Snapshotkontext auf 42 verändert | Originalrestore über eine vorhandene Maschine akzeptiert und liefert Zahl 42 |

Alle Erwartungen erfüllt. Die selbst beigefügte JSON-Schemaform im schemas.context-Versuch ist **keine vom Hersteller zugesagte Schema-API**. Sie ist ein kontrollierter Gegenfall zur Hypothese, das beliebige schemas-Feld löse einen solchen Prüfer aus. Der Callback-Gegenfall und der gelesene Originaldatenfluss grenzen dies zusätzlich ab. Daraus folgt nicht, dass XState generell keine Laufzeitprüfungen besitzt: Die ungültige Transition ist die ausdrückliche Gegenkontrolle.

Der Snapshotfall ist keine Originalquellmodellvalidierung und kein Nachweis, dass ein Snapshot allein die komplette Quellmaschine ersetzt. Er zeigt konkret, dass dieser Restorepfad den veränderten Kontext nicht gegen ein ursprüngliches String-Quellschema validiert.

## Drei getrennte SDK-Typbedingungen

Originale setup-/createMachine-/createActor-Deklarationen werden mit TypeScript strict, noEmit und skipLibCheck benutzt. skipLibCheck überspringt die interne Prüfung der Bibliotheksdeklarationskörper; die eigenen SDK-Aufrufe und deren Originalsignaturen bleiben Gegenstand der Typprüfung.

| Fall | Originaltyp-/Compilerergebnis |
| --- | --- |
| Stringkontext und String-Eventpayload | Keine Diagnose |
| Zahl 42 für deklarierten Stringkontext | TS2322: number nicht string |
| Zahl 42 für deklarierten String-Eventpayload | TS2322: number nicht string |

Alle Erwartungen erfüllt. Das ist ein realer vorhandener SDK-Typprüfpfad. Er wird weder als wertlos noch als unabhängiges neutrales JSON-Artefaktschema umgedeutet. Das TypeScript-Programm, die JSON-Konfiguration, die toJSON-Definition und der Snapshot bleiben unterschiedliche Originalgegenstände.

## X06-Einordnung und Reichweite

**XState X06: U → N/C464 für die ausdrücklich geprüfte veröffentlichte Core-Distribution 5.33.3 und die bisherige separate Artefaktschema-Auslegung.** Der dortige Originalgegenstand ist eine ausführbare SDK-Konfiguration mit Originaltypen und Graphaufbau, kein eigenständiger neutraler Maschinenartefakt-/Schema-/Validatorpfad. Dieses N stützt sich auf abgegrenzte Distribution/Exports, die konkrete Funktion des schemas-Feldes und tatsächlich ausgeführte Gegenkontrollen; nicht nur auf das erfolglose Finden einer Datei.

**N bedeutet hier nicht:** XState hat keine Typen, keine Validatoren beliebiger Art, keine internen Fehlerprüfungen oder kann in keinem größeren Werkzeugstapel validiert werden. Andere Stately-Produkte, Repository-Entwicklungswerkzeuge, externe Schemas und Zusatzadapter sind nicht derselbe geprüfte Coreumfang. Deren mögliche Fähigkeiten werden nicht negativ bewertet. Ein neuer neutraler Serializer/Validator wäre ein zusätzlicher Beitrag und wurde hier nicht erfunden. Bereits positive XState-Felder und seine Kompositionsfähigkeiten bleiben unverändert.

Die Frage, ob der schemas-Name oder Snapshotrestore diesen Originalartefaktnachweis liefert, ist damit für den Core **geklärt**. Die Suche nach einer geeigneten Gesamtpaketvalidierung bleibt separat. Aktuell **53 U-Zellen: 33 Integration und 20 weitere**. Bei X06 jetzt sieben D, ein begrenztes N und acht U. Keine neue Produkt-/Runtimeauswahl, Produktionskomponente, Commits oder Pushes.

## Reproduktion

Im tool-Ordner npm ci --ignore-scripts mit dem gespeicherten Lock; run.cjs führt die sechs gespeicherten API-Fälle aus. check-types.cjs nutzt den zuvor gepinnten TypeScript-5.9.3-Ordner; Fixtures und Erwartungen sind enthalten. Exakte Originaldateien, Registrycapture, SDK-Deklarationen-/Runtimehashes und Lock stehen im Manifest beziehungsweise source-audit.json. Originalpaketquellen werden nicht mitverteilt. Die Export-/Dateiinventur ist reproduzierbar; daraus wird kein ungelesener Vollcodeaudit behauptet.
