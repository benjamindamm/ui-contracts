# Integrationsabgleich und dokumentarischer Referenzfall

Stand: 24. Oktober 2026. **Dokumentarische Prüfung, keine Implementierung, keine ausgeführten Contract- oder Laufzeittests.** Dieser Abgleich bearbeitet die Referenz- und Kompositionsfragen aus dem [Integrationsentwurf](INTEGRATION.md). Er schließt weder sämtliche U-Felder noch die beiden vorgemerkten Detailvergleiche ab.

## 1. Ergebnis und Nachweisgrenze

Die vorhandenen Modelle bieten verwertbare Teilmechanismen. Daraus folgt bisher keine nachgewiesene gemeinsame Identität, semantische Bindung und Konfliktprüfung zwischen vier unveränderten Originalartefakten. Das ist eine Grenze der vorliegenden Nachweise, kein Beweis, dass eine Integration unmöglich wäre.

**Neu gegengeprüft:** Sechs gepinnte Quelltextdateien aus UXSpec, Ark UI und OpenPencil, siehe [S57](SOURCES.md#s57) und [C390–C393](CLAIMS.md#c390). Die Aussagen sind manuelle Quellbefunde mit begrenzten Ableitungen (E2), keine Ausführung (E3). Weitere Beiträge in der Tabelle beruhen ausdrücklich auf den bereits gespeicherten Kandidatenprüfungen.

## 2. Was vorhandene Mechanismen tatsächlich verbinden

| Beitrag | Belegter Bezug | Grenze für unser Paket | Weiterer Bedarf |
| --- | --- | --- | --- |
| CEM | Deklarationsbezüge und benannte Web-Komponententeile | Deklaration ist keine konkrete UI-Instanz; kein Vier-Domänen-Resolver nachgewiesen | Definition und Instanz auseinanderhalten; neutralen Typkern getrennt prüfen |
| DTCG Format/Resolver | Tokenwerte beziehungsweise Kontext-/Themeauflösung | Tokenziel ist kein Komponenten- oder Fokusziel | Tokenbindung mit Herkunft erhalten; UI-Zuordnung separat beschreiben |
| AgentsORG / DESIGN.md | Eigene visuelle Strukturen und teilweise Anatomie | Gemeinsame Vier-Domänen-Ownership nicht belegt | Bestehende visuelle Definitionen referenzieren; Priorität nicht aus Feldnamen ableiten |
| UXSpec | Eigene importierte Tokens, Elemente, Animationen und Maschinen; Elementparameter und Overrides | Fremde Originalformate benötigen eine explizite Abbildung; Instanzidentität entsteht nicht allein durch Expansion | Quellbindung, Instanzpfad, Typen und verschachtelte Referenzen gezielt prüfen |
| Ark UI / Zag | Konkrete Framework-Komposition, IDs, eigene Maschinenkontexte | Beleg gilt für die Web-/Frameworkrolle; Overlay mit ScrollArea und Vier-Dateien-Vertrag nicht praktisch geprüft | DOM-/Contract-Identität zuordnen und Fokus-/Scrollzuständigkeit prüfen |
| OpenPencil | Eigene Behaviourwerte und Parts auf Properties/Slots im Scenegraph | Scenegraph-Bindung ist keine externe Fachdatei-Referenz | Mapping ausdrücklich machen; heuristische und verlorene Bindungen sichtbar halten |
| uSpec | Interne Figma-/Dictionary-/Evidence-Bezüge | Kein hinreichender externer Vier-Domänen-Resolver belegt | Identitätsübersetzung samt Stabilität und Informationsverlust nachweisen |
| Panda CSS | Eigene Rezepte, Tokens und Paket-/Buildmechanismen | Kein eigenständiger Nachweis gemeinsamer UI-Instanzidentität | Visuelle Ableitungen von fachlichen Zuständen trennen |
| WAI-ARIA / APG | Web-Beziehungen beziehungsweise Bedienmuster | Keine allgemeine Originalformat-Komposition und kein vollständiger automatischer Konfliktprüfer | Gewähltes Pattern, Instanzziele und Produktregeln explizit binden |
| CSS Layout | Geometrische Beziehungen im Web | CSS-Zielbezug beweist keine neutrale Komponentenidentität | Geometrieziel und fachlichen Teil verbinden; native Übertragung offen |

Die Tabelle wählt keinen Kandidaten aus. Insbesondere werden CEM, UXSpec und DTCG dadurch nicht zu Pflichtformaten. Quellen für die übernommenen Befunde: [CLAIMS](CLAIMS.md), insbesondere X02–X08 der jeweiligen Kandidaten.

## 3. Konkrete Zusatzbefunde aus der Quellprüfung

### UXSpec: Auflösung ist mehr als ein passender String

Der Importresolver liest lokale JSON-Dateien und übernimmt ausdrücklich angeforderte UXSpec-Bereiche. Er enthält keine Auflösung externer Versionsbindungen. Ein angeforderter, aber fehlender Bereich erzeugt in dieser Funktion allein keine eigene Fehlermeldung; spätere Verwendung kann eine andere Diagnose auslösen. Das ist keine Behauptung, alle CLI-Pfade akzeptierten einen solchen Fall.

Bei importierten Elementen werden unqualifizierte **Tokenreferenzen** umgeschrieben. Verschachtelte unqualifizierte **Elementreferenzen** werden in dem gelesenen Expansionspfad dagegen mit dem lokalen Elementverzeichnis weiter aufgelöst. Daher ist die Bedeutung einer Unterreferenz beim Import gesondert zu prüfen. Die Prüfung wurde nicht ausgeführt. [C390–C391](CLAIMS.md#c390)

Der Bundler trägt Module unter ihrer Maschinen-ID ein; die gelesenen Zuweisungen weisen doppelte IDs nicht ausdrücklich zurück. Er löst Imports direkter Maschinenabhängigkeiten auf, bildet aber in dieser Funktion keinen allgemeinen rekursiven Modulabschluss. Die vorhandene Import-Zyklusdiagnose ist kein Beleg vollständiger Graphprüfung: Die gelesenen Bundler-Aufrufe teilen keine durchgehende Vorfahrenmenge. [C390](CLAIMS.md#c390)

### Ark: eigener Kontext, aber keine automatisch stabile Contract-Identität

Combobox und ScrollArea erzeugen jeweils einen eigenen Maschinenkontext. Explizite Props überschreiben die vorher gesetzten Defaults. In der Combobox kann damit auch das komplette vorgeschlagene `ids`-Objekt ersetzt werden; eine tiefe Zusammenführung mit Field-IDs findet in dieser Funktion nicht statt. Die Instanzisolierung des Zielsystems ist ein guter Ansatzpunkt, aber keine nachgewiesene stabile Identität über Umordnung, Sitzungen und Plattformen hinweg. [C392](CLAIMS.md#c392)

### OpenPencil: Teilprüfung und Rückkonvertierung unterscheiden

Die gelesene Auflösung kontrolliert bestimmte Namen, Propertytypen, Parts und doppelte Slotbelegung. Zustandszuordnungen enthalten heuristische Ableitungen; ausdrücklich gesetzte Statewerte werden im gelesenen Pfad zusammengeführt, ohne dort denselben vollständigen Optionsabgleich wie bei Boolean-Varianten zu zeigen. Die Rückkonvertierung lässt nicht auflösbare Bindungen aus. Für einen Contract dürfen deshalb weder vollständige Zustandsprüfung noch verlustfreier Roundtrip vorausgesetzt werden. [C393](CLAIMS.md#c393)

## 4. Referenzfall ohne neue Formatsprache

Die folgende Schreibweise ist **nur eine lesbare Dokumentationsnotation**, keine URI-Syntax, kein Schema und keine bereits kompatible Datei. Auch die vorgeschlagenen Rollen und Bindungen sind noch keine Formatentscheidung.

### Definitionen und Verwendungen

| Dokumentationsname | Bedeutung | Quellenstand |
| --- | --- | --- |
| Autocomplete-Definition | Schnittstelle, visuelle Regeln, Verhalten und Accessibility derselben wiederverwendbaren Komponente | Noch auszuwählende Originalartefakte mit festem Stand |
| ScrollArea-Definition | Eigenständige wiederverwendbare Unterkomponente | Ebenfalls separat zu binden |
| Suche A / Suche B | Zwei Verwendungen derselben Autocomplete-Definition | Jeweils dieselbe Definition, eigener Instanzkontext |
| Suche A / ScrollArea | Unterinstanz im Overlay von Suche A | ScrollArea-Definition |
| Suche B / ScrollArea | Unterinstanz im Overlay von Suche B | ScrollArea-Definition |

Jede Suche besitzt eigene fachliche Teile für Eingabe, Overlay, Liste und wiederholte Optionen. Ob die Liste unmittelbar der ScrollArea-Viewport ist oder ein Element darin, bleibt als konkrete Anatomieentscheidung offen. Ein übergebenes Kind wird nicht automatisch zum identischen fachlichen Teil.

**Zusätzliche Identitätsfrage:** Wiederholte Optionen benötigen eine nachvollziehbare Zuordnung zum Ergebnisdatensatz. Ein Listenindex allein ist bei Umordnung keine hinreichende Stabilitätsannahme. Vorschlag: einen im jeweiligen Ergebnisbestand eindeutigen fachlichen Schlüssel verwenden und sein Verhalten bei Aktualisierung festlegen. Das ist eine neue zu prüfende Anforderung, kein nachgewiesenes Feature aller Kandidaten.

### Erforderliche Beziehungen

| Nr. | Beziehung | Führende Information | Status |
| --- | --- | --- | --- |
| R1 | Jede Domäne meint dieselbe Definition, Instanz und denselben Teil | Fachliche Teildeklaration plus nachvollziehbares Mapping | Als Anforderung bestätigt; konkrete Syntax offen |
| R2 | Fokus auf Eingabe öffnet gemäß gewählter Produktregel das zugehörige Overlay | Behavior; Visual und Accessibility konsumieren denselben Zustand | Grundfall dokumentiert; Ablauf nicht ausgeführt |
| R3 | Aktive Option bindet Darstellung und zugängliche Vermittlung | Behaviorzustand, visuelle Variante, Accessibility-Regel | Mapping offen; nicht mit bestätigter Auswahl gleichsetzen |
| R4 | Auswahlbestätigung löst öffentliches Ereignis mit passendem Payload aus | Signatur im Interface, Auslöser im Behavior | Typabbildung und konkretes Ereignis noch zu bestimmen |
| R5 | Eingabe und Liste derselben Suche stehen in der gewählten Accessibility-Beziehung | Accessibility mit Instanzbezug | Webprofil zu konkretisieren; native Abbildung offen |
| R6 | Overlay verwendet eigene ScrollArea, ohne deren Definition zu kopieren | Komposition mit expliziter Parameter-/Ereignisbindung | Begrifflich ausgearbeitet; Originalformatkette unbewiesen |
| R7 | Navigation scrollt erforderlichenfalls die aktive Option sichtbar | Behavioranforderung und ScrollArea-Fähigkeit | Zuständigkeit und Aufrufbindung offen |
| R8 | Neue Ergebnisse aktualisieren Anzeige und zugängliche Rückmeldung derselben Suche | Behaviorauslöser; Accessibility-Inhalt und Vermittlung | Asynchronität, veraltete Antworten und Fokusverlust offen |
| R9 | Anker, Abstand, Größenbegrenzung und Theme beziehen sich auf korrekte Teile | Visual mit referenzierten Tokens und Geometriezielen | Formales Layoutmodell noch zu vergleichen |

### Vorschlag für Fokus- und Scrollzuständigkeit

Für einen ersten **Web-Prüffall** kann ein Pattern gewählt werden, bei dem DOM-Fokus auf der Eingabe bleibt und die aktive Option zugänglich referenziert wird. Das ist ein zu bestätigendes Zielprofil, keine universelle Produktpflicht. Der Autocomplete steuert aktive Option und Bestätigung. Die ScrollArea stellt ihre Scrollfunktion bereit; sie soll dieselben Navigationstasten nicht zusätzlich unabhängig als Auswahl verarbeiten. Overlay, Liste und Viewport müssen dabei ausdrücklich auseinandergehalten werden.

## 5. Positive und absichtlich beschädigte Dokumentationsfälle

| Fall | Erwartete fachliche Auswertung | Noch fehlender Nachweis |
| --- | --- | --- |
| Suche A und B verwenden dieselben Definitionen | Zwei getrennte Zustands-/Wertebereiche und zwei ScrollArea-Instanzen | Konkrete Instanziierungs- und Laufzeitprüfung |
| Suche A wird geöffnet und navigiert | Nur Beziehungen und aktive Option von A ändern sich | Konkrete Bindungen und Interaktion |
| Referenz von A zeigt versehentlich auf Liste B | Als fachlich falsche Instanzzuordnung melden, obwohl das Ziel existiert | Ownership-/Bereichsregel; reine Existenzprüfung genügt nicht |
| Teilname existiert nicht | Unauflösbares Ziel melden | Originalresolver oder ergänzende Prüfung identifizieren |
| Gleiche Instanzkennung zweimal | Identitätskollision melden | Kollisionsregel und tatsächlicher Prüfpfad |
| Payload widerspricht öffentlicher Signatur | Typkonflikt melden | Gemeinsame Typabbildung |
| Auswahl und aktive Navigation sind gleichgesetzt | Semantischen Widerspruch zur gewählten Produktregel melden | Explizites Mapping statt Namensvergleich |
| Lokaler Pfad zeigt auf anderen Bibliotheksstand | Fehlende Reproduzierbarkeit sichtbar machen | Snapshot-/Paketbindung bestimmen |
| Verschachtelter Import verweist auf lokalen Namensvetter | Falschen Geltungsbereich erkennen | UXSpec-Folgeprüfung aus C391 |
| Untermaschinen teilen dieselbe Maschinen-ID | Kollision vor möglichem Überschreiben melden | UXSpec-Folgeprüfung aus C390 |
| Verlorene Scenegraph-Bindung wird beim Export weggelassen | Verlust melden, keine Vollständigkeit behaupten | OpenPencil-Folgeprüfung aus C393 |

Dies sind erwartete Prüfergebnisse auf Papier. Keine Tabellenzeile bedeutet, dass ein Werkzeug den Fehler bereits erkannt hat.

## 6. Offene Punkte nach Priorität

| Priorität | Offener Punkt | Ergebnis dieser Runde | Nächster nachprüfbarer Schritt |
| --- | --- | --- | --- |
| 1 | Gemeinsame Definition-/Instanz-/Teilidentität | Erforderliche Zielarten und Instanzfälle konkretisiert | Für geeignete Originalartefakte genaue Fundstellen und Mappings zeigen |
| 1 | Verlustfreie Erhaltung der Originaldateien | Eigeninterne Referenzen reichen als Nachweis nicht aus | Je Domäne Originalartefakt, Validator und zusätzliche Bindung benennen |
| 1 | Typen, Ereignisse, Zustände und Ownership | R1–R9 trennen Signatur, Auslöser und Darstellung | Eine vollständige Bindungskette einschließlich Payload ausarbeiten |
| 1 | Unterkomponente und Fokus-/Scrollkonflikte | Getrennte Instanzen und Zuständigkeitsvorschlag dokumentiert | Gewähltes Pattern und echte Anatomie festlegen; später praktisch prüfen |
| 2 | Versionen, Kollisionen und Zyklen | Konkrete Grenzen der geprüften UXSpec-Pfade benannt | Snapshotstrategie und Graphprüfung an positiven/negativen Fällen prüfen |
| 2 | Native Zielprofile | Kein neuer Nachweis | Primärquellen für native Accessibility und Layout gezielt recherchieren |
| 2 | Formate und Reifegrad | Kandidatenbefunde bleiben getrennt | Vorgemerkten Gesamtvergleich abschließen |
| 3 | Eigenes Integrationsformat | Weiterhin keine Auswahl | Erst nach konkreter Originalformatkette über notwendigen Zusatz entscheiden |

**Zählweise:** Die acht Zeilen sind Arbeitsfragen, keine acht neuen Kandidaten und keine Zahl der verbleibenden U-Zellen. Alle sechzehn Kandidaten-Durchgänge bleiben abgeschlossen. Ihre Bewertungen werden durch diesen dokumentarischen Abgleich nicht automatisch geändert.


## Fortsetzung: Originalfelder und vollständiges offenes Register

Der [konkrete Feldabgleich](BINDINGS.md) präzisiert Typ-/Payloadabbildung, Einheiten und zugängliche Zielbeziehungen. Er unterscheidet aktive Option, zugänglich gemeldete Auswahl und bestätigten Produktwert. Das [offene Register](OPEN-FIELDS.md) zählt sämtliche U-Zellen: ursprünglich 73 insgesamt, nach der UXSpec-Layoutfolgeprüfung aktuell 72, davon unverändert 45 Integrationsfelder. Die acht priorisierten Arbeitsfragen oben sind damit keine alternative Matrixzählung.
