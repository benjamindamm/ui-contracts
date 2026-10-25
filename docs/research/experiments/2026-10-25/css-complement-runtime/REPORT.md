# CSS, Interface, Behavior und Accessibility: zehn getrennte Ergänzungsnachweise

Stand:25. Oktober2026. **Neun CSS-Zellen und WAI-ARIA V06 jeweils A/C526–C535**, ausschließlich mit den hier ausgeführten zusätzlichen Bindungen. **27 unterschiedliche Bedingungen in10 Gruppen erfüllt.** Insgesamt603 Bedingungen/95 Gruppen;10 offene Nachweise verbleiben (6 Integration,4 Layout). Die vollständige Integration bleibt unbelegt.

## Endlicher Gegenstand und führende Quellen

Keine Produktionskomponente oder neue Contractsprache: Eigene minimale Forschungsfixtures in unveränderten ursprünglichen Syntaxen, tatsächliche ursprüngliche SCXML-Laufzeit, tatsächlicher Browser und ausdrücklich zusätzlicher Hostbinder. Die früheren generischen Hash-/Teilreferenzfälle werden nicht erneut gezählt. uSpecs Normalisierer und UXSpecs ausgeschöpfte Layoutmapper werden nicht erneut ausgeführt.

| Führende Quelle | Konkreter Inhalt | Abgeleitet durch Zusatzbindung |
| --- | --- | --- |
| CEM interface.json | maxHeight:number, enabled:boolean, query:string; value-change mit value/query jeweils string; Anatomie | Typ-/Einheitsprüfung am Hostinput und Prüfung tatsächlicher ursprünglicher parent-Eventdaten vor CustomEvent. |
| SCXML behavior.scxml | ready/closed/open/selected, enabled-Guard, QUERY/COMMIT-Assign und tatsächliches send an #_parent | Sichtbarer Maschinenzustandsmarker und öffentliche Eventroute je A/B-Instanz. |
| CSS visual.css | Pixel-Maximalhöhe mit CSS-Variablenoverride, Overflow auto, Display abhängig vom Zustandsmarker | Tatsächlich berechnete Geometrie/Overflow/Display. Der Binder besitzt keine zweite Displayregel. |
| HTML/ARIA accessibility.html | Rollen/Namen/Beziehungen, aktive Option, status/polite/atomic und Meldungspräfix | Abgeleitete expanded-/active-Nachführung, Bindung an kontrollierten Scrollcontainer und Meldungsinhalt aus tatsächlichem Event. |
| profile.json, eigener Binder | Konkrete semantische Zuordnungen und das ausgewählte endliche Key-/Stateprofil | Brücke zwischen getrennten ursprünglichen Artefakten; keine behauptete ursprüngliche Zusatzfunktion. |

Die gezeichnete CSS-Position top28 ist ein Testlayout; damit wird hier keine neue allgemeine Anchor-Semantik bewiesen. Pixelwerte und7 Optionen sind Testdaten, keine Produktvorgaben. Die Quellen bleiben getrennt; normale Laufzeiteingaben werden nicht als Änderungen ihrer Masterdateien ausgegeben. Gezielte Negativfälle mutieren ausdrücklich einen Parameter, eine abgeleitete Metadatenansicht, eine Originaleventroute oder einen DOM-Zustand.

## Tatsächliche Originalausführung

Unveränderte @scion-scxml/scxml4.3.28 und @babel/polyfill7.12.1 aus dem bereits gepinnten Werkzeugbestand. Der vollständige ursprüngliche Browsercompiler und Statechart laufen, keine nachgebaute Maschine und kein fingierter send-Callback. Ein ursprüngliches kompiliertes Modell wird vor **jeder** Kind-/Parentinstanz separat über die ursprüngliche prepare-API vorbereitet; der früher festgestellte gemeinsame-Ausführungskontext-Gegenbefund bleibt erhalten und wird nicht ignoriert.

Zwei echte Kindinstanzen A/B und zwei echte Parent-Statecharts. Tatsächliches ursprüngliches send target=#_parent liefert Daten und invokeid in den Parent; erst dort prüft der zusätzliche Interfacebinder Name, zwei Pflichtstrings und Instanz. Die erwarteten falschen Payload-/Parentfälle zeigen somit eine echte ursprüngliche Lieferung, keine simulierte Fehlerantwort. Auf diese Lieferung wird ereignisbasiert gewartet, kein pauschales Zeitdrain als Erfolgskriterium.

CEM und SCXML der exakten neuen Fixtures bestehen ihre unveränderten Originalschemas. [Preflight-Ergebnisse](schema-results.json) sind dokumentiert, aber nicht zusätzlich zu den27 Bedingungen gezählt. Tatsächlicher TypeScript5.9.3-AST liest die eigene CEM-Signatur CustomEvent mit zwei Pflichtfeldern; die zusätzliche Laufzeitprüfung ist bewusst auf diese primitiven Typen begrenzt, kein vollständiger TypeScriptwertvalidator und keine native CEM-Eventroute.

[Vorab gespeicherte25 Erwartungen](cases.json), [zwei zusätzlich vorab definierte AX-Erwartungen](ax-expectations.json), [alle Ergebnisse](results.json), [Originalbezüge und eigenes Quellenreview](source-review.json).

## Zehn eigene kriteriumsbezogene Bewertungen

| Kandidat/Feld | Eigener konkreter Nachweis | Gegenfall/Grenze | Ergebnis |
| --- | --- | --- | --- |
| CSS I01 | Benanntes CEM-maxHeight:number → explizite px-Zuordnung → tatsächliches CSS-max-height; A192, B160, Inhaltshöhe224. | String statt Zahl, rem statt festgelegtem px und falsche abgeleitete Propertytypzuordnung abgewiesen. Kein native CSS-Komponenten-API-Typsystem behauptet. | A/C526, P86:4 |
| CSS I02 | Ursprüngliches parent-send liefert value-change/value/query; danach typgeprüftes öffentliches CustomEvent an den eigenen Forschungssection-Host, Maschine/CSS wieder closed/none. | Ursprünglich akzeptiertes query=42 wird erst zusätzlich abgewiesen; falscher tatsächlicher Parent B mit invokeid A erzeugt kein öffentliches B-Event. | A/C527, P87:3 |
| CSS B01 | Tatsächliche closed→open→closed-Originalzustandsfolge steuert CSS none→block→none; B bleibt closed. | CSS beschreibt weiterhin keine eigene UX-Zustandsmaschine. Keine pauschale Übertragung aus geometrischen Fallbacks. | A/C528, P88:1 |
| CSS B02 | Tatsächliches SET_ENABLED/assign und ursprünglicher cond=enabled blockieren OPEN bei false; nach true erreicht Originalmaschine open und CSS block. | Der Zusatzbinder führt den Guard nicht selbst aus. Keine allgemeine Guardbibliothek oder sichere beliebige ECMAScript-Ausführung zugesichert. | A/C529, P89:1 |
| CSS B03 | QUERY-Daten werden durch tatsächliches ursprüngliches assign im Kontext gespeichert und mit getrenntem ausgewähltem value per ursprünglichem send ausgegeben. | Falscher query-Inputtyp wird zusätzlich abgewiesen; query=42-Bypass im I02-Gegenfall bleibt als Originalgrenze sichtbar, nicht erneut gezählt. | A/C530, P90:2 |
| CSS B04 | Synthetische native ArrowDown-Events am Input passieren den zusätzlichen Keyrouter, öffnen tatsächliche Originalmaschine und CSS und bewegen aktive Option bei erhaltenem Inputfokus. Eigener B-Input öffnet nur B. | Router ist ausdrücklich eigene Verbindung, kein CSS- oder SCXML-eigener Keyboardstandard. Kein vertrauenswürdiger physischer Tastendruck. | A/C531, P91:2 |
| CSS A01 | Layoutpopup → richtiger kontrollierter HTML-listbox-Kontext; führende Namen/Rollen/Beziehungen werden geprüft. Tatsächlicher Browser-AX-Baum enthält Search A/Search B und Results A als passende Rollen. | Falscher führender Labeltext und fremdes aria-controls-Ziel abgewiesen. Kein automatischer Nachweis beliebiger Accname-Ausdrücke oder aller semantischen Beziehungen. | A/C532, P92:4 |
| CSS A02 | Eigener endlicher Combobox-Listbox-Keybezug nach gepinntem APG: Escape schließt und behält DOM-Fokus am Input; Enter übernimmt aktive zweite Option und schließt; aktive Option via aria-activedescendant. | Abweichende abgeleitete Enterroute wird gegenüber dem führenden Profil abgewiesen. Nicht alle optionalen APG-Tasten, Popuptypen oder AT-Pfade geprüft. | A/C533, P93:3 |
| CSS A03 | Tatsächliches bestätigtes öffentliches Event aktualisiert getrennte status/polite/atomic-Region mit Präfix aus der A11yquelle; B bleibt leer. Native AX-Region enthält Live-/Atomic-Eigenschaften und Text. | Reine CSS-Maximalhöhenänderung erzeugt keine Meldung; abweichendes aria-live abgewiesen. Native AX-Daten sind keine bestätigte Sprachausgabe. | A/C534, P94:4 |
| WAI-ARIA V06 | Der tatsächliche aria-controls-listbox-Kontext ist an genau seinen äußeren CSS-Scrollport gebunden;7×32px in160px, aktive7. Option sichtbar nach scrollTop64. Native AX-Relation adressiert dieselbe Option/Liste. | Fremde Liste wird abgewiesen. Bewusster clip-Override bleibt gültiges CSS, macht in diesem verlangten Sichtbarkeitsprofil die aktive Option unsichtbar: scrollTop0, erwarteter Bindungskonflikt. | A/C535, P95:3 |

Dies sind zehn einzeln begründete Adapterbeiträge, keine pauschale Übernahme der Fähigkeiten von CEM/SCXML/HTML in CSS oder einer CSS-Overflowpolitik in ARIA. CSS führt weiterhin ausschließlich Layout/Styles. ARIA definiert weiterhin zugängliche Semantik. Die zusätzlichen Laufzeitbezüge sind gerade der dokumentierte A-Bedarf.

## Originalfähigkeiten und Zusatzprüfer auseinanderhalten

- Original-CEM-Schema prüft die ursprüngliche Datenform, nicht alle realen Werte einer tatsächlichen CustomEvent-Lieferung. Die primitiven Payload-/Hostproperty-Checks sind zusätzlich.
- Ursprünglicher SCXML-Interpreter speichert und liefert auch query42; sein ECMAScriptdatamodel ist kein CEM-Payloadchecker. Der Gegenfall bleibt erhalten, obwohl die Zusatzprüfung ihn korrekt erkennt.
- Ursprüngliche CSS-Engine berechnet auto/clip und Display. clip ist kein genereller Fehler: Der Bindungskonflikt entsteht hier nur mit der konkret verlangten Sichtbarkeit der aktiven Option.
- HTML/ARIA liefert Rollen-/Namens-/Relations-/Livebegriffe; Meldungszeitpunkt und eigener Präfix werden konkret an das tatsächliche Event gebunden. Vollständige Browser-/AT-/Plattformkonformität wird nicht behauptet.
- Öffentliches Eventziel ist die eigene Forschungssection, kein implementiertes registriertes CEM-Custom-Element und keine neue Produktkomponente.

## Zusätzliche Gegenprüfung des eigenen Harnischs

initial-route-constants-harness.js hält die erste eigene Routerfassung fest: Die Standardtasten wurden korrekt geroutet, aber die Aktionswerte der geprüften Metadatenansicht wurden noch durch parallele Bedingungen verwendet. Der Router liest nun tatsächlich die abgeleitete Keymap; ihre Konfliktprüfung vergleicht diese mit dem führenden unveränderten Profil. Dieselben25 Fälle erneut ausgeführt, keine neuen Bedingungen hinzugezählt. Die erste Aufzeichnung bleibt getrennt erhalten.

Die kompakte BrowserOS-AX-Snapshotdarstellung zeigte status ohne seinen statischen Textinhalt. Daraus wurde kein ursprünglicher semantischer Fehlschlag gemacht. Der vollständige tatsächliche Chromium-AX-Baum über Accessibility.getFullAXTree zeigt den Status mit polite/atomic=true und einem StaticText-Nachfahren Selected Alpha A1. Der zweite Status bleibt ohne Text. [AX-Ergebnis](ax-results.json) und Rohbaumaufzeichnungen sind gesichert. Kein Screenreader wurde ausgeführt.

## Ergebnis und genau verbleibender Rest

**10 U:6 Integration und4 ursprüngliche Layoutfragen.** Die zehn fachfremden Ergänzungszellen sind ausschließlich im hier begrenzten Adapterumfang geschlossen. Offen bleiben UXSpec/uSpec V04/V06, uSpec X01/X03/X08, OpenPencil X01 sowie Google/OpenUI X06. Acht davon erlauben noch konkret benannte zusätzliche Bindungen beziehungsweise neue entscheidende Originalpfade; zwei sind ausdrückliche Originalklärungen. Dieser Block beweist weder das neutrale gemeinsame Contractpaket noch sämtliche Kandidaten-/Plattformkombinationen.

## Reproduktion

prepare.py schreibt eigene unveränderte Originalsyntaxfixtures und25 Erwartungen; Originalruntime und Polyfill werden bytegleich aus dem gepinnten lokalen Werkzeugbestand bereitgestellt. derive-interface.cjs erzeugt die zusätzliche primitive Signaturansicht mit dem tatsächlichen TypeScript-AST. schema_check.py nutzt gebundenes Python3.12 mit jsonschema/lxml gegen die ursprünglichen Schemas. Einen lokalen HTTP-Server für host starten; auf body[data-ready=true] warten, pro cases.json-ID complementResearch.runCase(id) ausführen. Für die zwei AX-Bedingungen die genannten vorbereitenden Fälle ausführen und den tatsächlichen AX-Baum lesen. check_results.py prüft25 Laufzeit- plus2 AX-Bedingungen und partitioniert die10 semantischen Gruppen. Erwartungs-/Quell-/Werkzeughashes im Manifest.

Originalruntime-/Polyfill-/Normtextkopien bleiben im lokalen Forschungsbereich und werden nicht als eigene Implementierung verteilt. Eigener Binder/Fixtures/Bericht sind Dokumentation und Forschung. Keine neuen Agenten/Chats, keine Commits oder Pushes.
