# Vier getrennte Domänen: ausführbarer begrenzter Webnachweis

Stand: 25. Oktober 2026. **Endbedingung dieses Arbeitspakets erreicht:** vier getrennte Prüfarbeitsdateien in unveränderten Originalsprachen prüfen, ihre expliziten Bindungen für zwei Instanzen mit Gegenfällen prüfen und die verknüpften Visualregeln im Browser messen. Keine ausgewählte Produktarchitektur und keine vollständige interaktive Integration.

## 1. Was tatsächlich verbunden wurde

Die Dateien unter fixtures/ wurden für dieses Experiment selbst erstellt. Es sind keine unveränderten Komponentenbeispiele fremder Autoren. Ihre **Formate** wurden nicht erweitert: CEM-JSON, W3C-SCXML, CSS und HTML-Hostsemantik. Die zusätzliche Bindung steht außerhalb dieser vier Dateien in profile.json. Diese JSON-Schreibweise ist nur Forschungsinput des Prüfers und keine beschlossene zusätzliche Contractsprache.

| Domäne | Führende Datei | Inhalt und eigene Prüfung |
| --- | --- | --- |
| Technische Schnittstelle | interface.json | Öffentlicher Stringwert, Ereignistyp CustomEvent<{value:string}> und benannte Stylingteile; originales CEM-JSON-Schema |
| Verhalten | behavior.scxml | closed/open/selected, Ereignisübergänge und statisches send/param; originale SCXML-XSD-Kette |
| Visual | visual.css | Anker/Ziel, acht Pixel Abstand, 160 Pixel Maximalhöhe, overflow-y:auto und feste Zeilenhöhe; originale css-tree-Eigenschaftsgrammatiken sowie tatsächliche Browsermessung |
| Accessibility / Webhost | accessibility.html | Zwei benannte Comboboxen mit eigenen Listen-/Optionsbeziehungen; neun originale axe-Regeln auf realem Browser-DOM |

HTML enthält die nötige Hoststruktur und einen ausdrücklich statischen offenen Zustandsausschnitt. Es ist **kein neu erfundenes neutrales Accessibility-Schema**. Die tatsächlichen Zustandswechsel sind in SCXML definiert; in diesem Experiment wird noch kein Interpreter mit dem DOM verbunden. CSS enthält keine UX-Übergänge, SCXML keine CSS-/ARIA-Definitionen und CEM keine fremden Fachmodelle. Die Quellstücke lassen sich jeweils lesen und prüfen, ohne ein kombiniertes Originalformat zu erfinden.

Die Anatomie unterscheidet ausdrücklich Popup-/Scrollcontainer und semantische Listbox. aria-controls zeigt auf die Listbox; die Geometrie- und Overflowregeln betreffen das Popup. Die benannten CEM-cssParts werden über die zusätzliche Tabelle zugeordnet. Ein Stylingpart wird dadurch nicht automatisch zu einem Fokusziel: Die konkrete Zielbedeutung entsteht sichtbar in dieser zusätzlichen Bindung.

## 2. Originalprüfungen und zusätzliche Regeln trennen

Die Kontrollartefakte bestehen das CEM-Schema und die SCXML-XSD-Kette. Alle Kontroll-CSS-Deklarationen matchen den unveränderten css-tree-3.2.1-Grammatiken. Der statische HTML-Kontrollfall liefert unter neun explizit gewählten axe-4.14.0-Regeln keine violation oder incomplete; eine Regel ist inapplicable, die übrigen acht bestehen. Keine vollständige CSS-Draft-/WCAG-/Assistenzkonformität aus diesen Teilprüfungen ableiten.

Der **zusätzliche Forschungsprüfer** bindet Definition, Teil, Instanz, Zustand, CSS-Anker und öffentliche Ereignisroute. Er verwendet tatsächliche CEM- und SCXML-Felder, geparste CSS-Deklarationen und reale HTML-ID-Beziehungen. Die Payloadzuordnung verwendet wie der frühere begrenzte Referenzfall ausdrücklich einen zusätzlichen Web-/TypeScript-CustomEvent.detail-Pfad; kein SCXML-Hostdispatch wird behauptet.

| Beschädigter Fall | Tatsächlich gemeldete Zusatzregel |
| --- | --- |
| Quellenhash stimmt nicht | source-integrity |
| Teilname fehlt in CEM | declared-part |
| Andere Verhaltensdefinition | behavior-definition |
| Snapshot verweist auf fehlenden Zustand | state-reference |
| Kontrollierte Liste oder aktive Option stammt aus B | same-instance-relation |
| CSS-Popup bindet Anker von B | same-instance-anchor |
| Abstand verliert die Einheit | geometry-unit; zusätzlich originales CSS-Grammatikmatching negativ |
| SCXML send nennt anderes öffentliches Ereignis | public-event-route |
| Zahlenpayload widerspricht öffentlichem Stringtyp | public-payload-type durch tatsächlichen TypeScript-Check |
| Geometrie erhält falsche führende Domäne | leading-source |
| Zwei Instanzen beanspruchen dieselben Teile | unique-instance-part |

Ein Kontrollfall und zwölf beschädigte Fälle wurden gegen vorab gespeicherte Erwartungen ausgeführt: **13/13 erfüllt**. Die CEM-/SCXML-Schemata akzeptieren auch die fachlich falschen Bindungsfälle, weil diese zusätzliche Beziehung außerhalb ihrer jeweiligen Sprache liegt. Das zeigt den tatsächlichen Mehrwert und die Grenze des Zusatzprüfers. Bei Inhaltsmutationen wird der erwartete Hash bewusst aktualisiert; sonst würde nur die Integritätsprüfung alle fachlichen Gegenfälle verdecken. Nur der eigentliche Hashgegenfall besitzt absichtlich einen falschen Hash.

Ownership-Regeln in profile.json sind weiterhin ein **Vorschlag dieses Forschungsprofils**. Der Test belegt ihre technische Prüfbarkeit im Fall, keine bereits verabschiedete universelle Zuständigkeitsnorm und keinen Änderungs-/Roundtripprozess.

## 3. Browsermessung an zwei getrennten Instanzen

Die getrennte HTML-Datei und die getrennte CSS-Datei wurden tatsächlich zusammen im eigenen Browser-Prüftab gerendert. Kein Framework oder Produktwidget implementiert. Vorher definierte Erwartungen: acht Pixel Abstand, linke Kante am eigenen Input, 160 Pixel begrenzte Höhe, overflow-y:auto, sieben Zeilen zu je 32 Pixeln, Inhalt größer als sichtbarer Container. Toleranz maximal ein Pixel.

| Instanz | Gemessener Abstand | Popup-/Clienthöhe | Scrollinhalt | Zeilenhöhen | Ergebnis |
| --- | ---: | ---: | ---: | --- | --- |
| A | 8 px | 160 px | 224 px | 7 × 32 px | alle Erwartungen erfüllt |
| B | 8 px | 160 px | 224 px | 7 × 32 px | alle Erwartungen erfüllt |

CSS-Anchor-Support wird im tatsächlich verwendeten Chrome-155-Browser positiv gemeldet. Die unterschiedliche vertikale Lage der Inputs führt zu jeweils passenden eigenen Popupkoordinaten. Das belegt den gemessenen statischen Fall, nicht eine Zusage für andere Browser oder native Renderer.

## 4. Gegenprobe: unterschiedliche Zeilenhöhen

visual-variable.css ist eine **separate zusätzliche Visualvariante**, keine stille Änderung der vier Kontrollquellen. Beide Instanzen besitzen nun die Höhen 24/48/36/24/60/28/40 Pixel. Der Scrollinhalt beträgt 260 Pixel; das Popup bleibt 160 Pixel hoch und acht Pixel vom Input entfernt. Tatsächlich sind nur vier vollständige Zeilen sichtbar, die nächste ist angeschnitten. Beide vorher definierten Gegenproben sind erfüllt.

Damit sind geometrische Maximalhöhe und gewünschte Zahl vollständig sichtbarer Ergebnisse auch praktisch unterschieden. Ein pauschales „160px = fünf Einträge“ gilt nur unter den geprüften gleich hohen Zeilen. Eine Produktregel für variable Zeilenhöhen bleibt zusätzlich festzulegen.

## 5. X01-Neubewertung und verbleibende Grenzen

**X01 wird bei CEM, SCXML, CSS Layout und WAI-ARIA auf A eingeordnet**, ausschließlich für diesen begrenzten zusätzlichen Webreferenzfall: Vier eigenständige Fachbeiträge können getrennt geführt und mit expliziter Zusatzbindung auf denselben Fall bezogen werden. Die Bindung bleibt außerhalb der Originalsprachen. A kennzeichnet gerade die zusätzlich nötige Host-/Instanz-/Bedeutungszuordnung; es ist keine direkte universelle Paketfunktion eines Kandidaten.

Das ist ein Nachweis getrennter Beschreibbarkeit und zusätzlicher statischer Verbindung, **kein Nachweis der vollständigen interaktiven Vier-Domänen-Integration**. Nicht geschlossen werden dadurch die anderen Kandidaten-X01-Zellen, X03-/X06-Gesamtfragen, native Abbildungen, ScrollArea als eigenständige Unterkomponente, Actorisolation, Fokus/Tastatur, dynamische Ergebnisansagen, asynchrone Daten, Roundtrip oder Migration. Insbesondere bleiben Original-A11y-Dateischema und allgemeines neutrales Integrationsformat offen.

Die Abnahme des Arbeitspakets umfasst vier Originalformat-/Hostbedingungen, 13 zusätzliche Bindungsfälle und vier konkrete Layout-/Variantenfälle: **21 benannte Bedingungen in drei getrennten Gruppen**, sämtliche Voraberwartungen erfüllt. Nicht jede zusätzliche Typ-/Schemaaufrufwiederholung ist als neuer Fall gezählt.

## 6. Reproduktion und Quellen

Die Originalschema-/Werkzeugpins stammen aus den bereits protokollierten Nachweisen S66/S70/S73/S80. Keine Quellen als erneut vollständig recherchiert ausgegeben. Quellen-/Paketmanifeste und Hashes sind referenziert. Die eigentlichen Originalschemas oder Bibliotheken werden nicht mitverteilt; eigene Fixtures, Erwartungsdateien, Prüfer, Outputs und Reproduktionsangaben sind enthalten.

check.py erwartet die exakt gebundenen CEM-/SCXML-Quellen unter den dokumentierten Vorgängerpfaden in work/. Die separat installierten JSONschema-Abhängigkeiten werden über PYTHONPATH eingebunden; Python 3.12.14, lxml 6.1.1.0, libxml2 2.14.6. analyze.cjs nutzt TypeScript 5.9.3 und css-tree 3.2.1 aus den isolierten Vorgängerordnern. Pfade können explizit angepasst werden; Originalcode/Grammatiken bleiben unverändert. BrowserOS browser-run.js benötigt einen eigenen about:blank-Tab mit dem zuvor SRI-gebunden geladenen axe; danach browser-variable-run.js ausführen. Outputs enthalten konkrete Browserwerte und nicht bloß behauptete Testerfolge.

Keine Actor-/SCXML-Interpreterausführung, kein tatsächliches öffentliches Eventdispatch, keine Tastatur-/Fokus-/Assistenztechnikprüfung. Keine Produktkomponente, kein Commit oder Push.
