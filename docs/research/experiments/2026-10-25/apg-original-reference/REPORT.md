# APG: tatsächliche Originalklasse, externe Feldtypen und Instanzkontexte

Stand:25. Oktober2026. **APG X03 A/C513 und X04 A/C514**, ausschließlich für das folgende ursprüngliche Referenzbeispiel mit ausdrücklicher zusätzlicher Bindung. **30 U:15 Integration,15 weitere.537 Bedingungen/73 Gruppen.** Acht native Beobachtungsbedingungen und zwei CEM-Schemabedingungen erfüllt; uSpec X03 bleibt gesondert U/C512.

## Endbedingungen und Rollen

X03: Ein sichtbares tatsächliches Feld der ursprünglichen Behavior-Beispielklasse auf einen separat beschriebenen Interfaceknoten mit explizitem Typ und Instanzkontext beziehen; falsche Zielart/Typ/Instanz abweisen. Nicht bloß Links auf die Patternwebseite oder gleichnamige DOM-IDs zählen.

X04: Die ursprüngliche Definition mit zwei tatsächlichen Konstruktorverwendungen, unterschiedlichen vorhandenen Parametern und eigenem Zustand wiederverwenden. Das Kriterium verlangt hier keine neue neutrale APG-Kompositionsdateisprache; allgemeine Neutralität, Versionierung und Lifecycle sind separate stärkere Fragen.

APG bleibt informativer Patternguide mit illustrativem Beispielcode, kein normativer Gesamtcontract und keine zugesicherte Produktionsbibliothek. Die eigene CEM-Datei beschreibt den tatsächlich sichtbaren Runtime-Feldbeitrag; sie ist kein von APG publizierter Interfacevertrag oder Anspruch auf eine stabile unterstützte öffentliche API.

## Unveränderte ursprüngliche Ausführung

Vollständiges ursprüngliches combobox-autocomplete.js am Pin `0f765e4dc33e966026114ac12a8380db1de3b787` über BrowserOS gelesen, unverändert in einem eigenen lokalen Host geladen. Vollständige Klasse samt Methoden und ursprünglichem load-Bootstrap vorhanden. Die eigenen Wrapper heißen bewusst nicht .combobox-list; daher findet der ursprüngliche Seitenscan null Wrapper. Der eigene Initialisierer erzeugt ausdrücklich genau zwei echte new ComboboxAutocomplete(input,button,listbox)-Objekte. Kein Proxy, keine nachgebaute Klasse, keine veränderte Originalmethode oder fingierter Callback.

Beide Objekte teilen tatsächlich dieselbe ursprüngliche Konstruktordefinition und sind verschiedene Instanzen. Ihre allOptions-Arrays und DOM-Optionen sind verschieden. A erhält per ursprünglichem aria-autocomplete-Parameter list mit Alabama/Alaska; B none mit Berlin/Bremen. Das sind eigene illustrative Parameterfälle, keine Produktwahl. Der Originalkonstruktor liest diese Attribute selbst.

## Zusätzliche externe Interfacebindung

interface.json ist eine eigene CEM-Beschreibung der tatsächlichen Klasse ComboboxAutocomplete im benannten JS-Modul. Der konkrete Zielknoten /modules/0/declarations/0/members/0 beschreibt das tatsächlich gespeicherte Klassenfeld comboboxNode als HTMLInputElement. CEM-Root und Feldtyptext verwenden unveränderte Originalsyntax.

Der eigene begrenzte Binder löst den CEM-Pointer, prüft class/field/Name, tatsächlichen Originalkonstruktornamen und den echten Native-DOM-Typ mittels instanceof. Er bindet außerdem den konkreten A/B-Kontext: Die ursprüngliche Feldreferenz muss auf input-a beziehungsweise input-b zeigen; deren aria-controls muss die tatsächlich im ursprünglichen Objekt gespeicherte listboxNode adressieren. Native Objektidentität/-typ, Originalfeld und fremder Interfacezielknoten werden so semantisch zugeordnet. Das ist mehr als ein bloßer gleicher DOM-ID-String, aber keine native CEM-Fähigkeit von APG.

Quell-CEM-/Variantenhash, ursprünglicher Klassenquellhash und Reporevision sind gespeichert. Die zusätzlich beschriebenen buttonNode/listboxNode-Feldtypen werden nicht als durch diese eine Bindung vollständig geprüft ausgegeben. Andere TypeScript-Typausdrücke, Realmwechsel, Modellmigrationen und andere Klassenfelder sind nicht unterstützt oder geprüft.

## Acht native Bedingungen P72

[Vorab gespeicherte Erwartungen](cases.json), [native Originalbeobachtungen und Referenznachweise](results.json).

| Fall | Tatsächliche Beobachtung |
| --- | --- |
| different-original-parameters | A list/B none, verschiedene Instanzen und Optionsarrays, dieselbe tatsächliche Originaldefinition. |
| typed-external-field-references | Beide tatsächlichen comboboxNode-Felder sind HTMLInputElement und binden auf denselben CEM-Feldknoten mit eigenem A/B-Ziel/Listenkontext. |
| original-A-value-and-filter | Ursprüngliches A.setValue('Al')/A.open(): A-Wert Al, B leer, A-Optionen Alabama/Alaska. |
| original-B-value-with-own-mode | Ursprüngliches B.setValue('Br')/B.open(): A bleibt Al; B-Wert Br, eigener none-Modus behält Berlin/Bremen und setzt seinen Filter auf leer. |
| original-A-option-click | Tatsächliches LI.click() löst ursprünglichen onOptionClick aus: A-Wert Alaska, A geschlossen; B-Wert Br und offen unverändert. Das ist ein synthetisch ausgelöster nativer Klick, kein physischer Pointertest. |
| wrong-external-field-type | Externe Beschreibung HTMLDivElement passt nicht zum tatsächlichen Originalfeldobjekt HTMLInputElement; Zusatzbinder weist ab. |
| foreign-instance-reference | B-Objekt als A-Referenz zugeordnet; Zusatzbinder weist den falschen Instanzkontext ab. |
| missing-external-field-target | Nicht vorhandener CEM-Memberpointer wird vom Zusatzbinder abgewiesen. |

Die ergänzende reine Strukturbeobachtung sharedDefinition/distinctInstances wurde nach Speicherung dieser Erwartungen ohne neue Eventsequenz gelesen und dem vorhandenen Parameterfall zugeordnet; kein zusätzlicher Fall gezählt. Alle acht Beobachtungserwartungen erfüllt. Tatsächliche Methoden und ursprüngliche native Eventhandler ausgeführt; kein Keyboard-, AT- oder vollständiger Accessibility-Konformitätsnachweis.

## Zwei Originalschemabedingungen P73

[Schemaergebnis](schema-results.json). Unverändertes gepinntes Original-CEM-Schema akzeptiert sowohl die eigene korrekte als auch die gezielt falsche HTMLDivElement-Typmetadatei. Beide sind strukturell gültiges CEM. Erst der zusätzliche Native-Objektvergleich stellt die fachliche Diskrepanz fest. Kein eigener Binder als Originalschemafunktion ausgegeben.

## Bewertungen und Begrenzungen

**X03 A/C513:** ursprüngliche Klasse besitzt reale Objektverweise und native DOM-/Inputsemantik; zusätzlicher konkreter CEM-Pointer-/Feldtyp-/Instanzbinder ist erforderlich und ausgeführt. Kein allgemeiner Fremdmodellresolver und keine neue APG-Contractdateisprache.

**X04 A/C514:** eine tatsächliche unveränderte Definition wird mit eigenen Parametern und Kontexten zweifach verwendet; zusätzlicher Host-/Konstruktorbezug konkret. Das ist nicht schon ein neutrales Overlay/ScrollArea-Paket, keine vollständige Unterkomponentenvertragsarchitektur oder allgemeine Lifecycleverwaltung. Ursprüngliche Objekte registrieren gemeinsame document.body-Listener; Isolation aller globalen Pointerereignisse, dynamisches Entfernen und Listenerabbau wurden nicht geprüft. Die Daten-/Operationsisolation in der gespeicherten Folge wird nicht auf alle Interaktionen übertragen.

X01/X08 bleiben offen. Das zusätzliche Interface beschreibt einen Beispielimplementierungsbeitrag, keinen stabilen publizierten APG-APIstandard. Die Werte-/Parametervarianten und die zwei Instanzen sind Forschungshosts; keine Produktionskomponente wurde entwickelt. Keine Produktkopplung, Veröffentlichung, Commit oder Push.

## Reproduktion

Originalquelle am exakten Manifest-URL bereitstellen, gegen Lesekopie-Hash prüfen und als host/original-combobox.js bereitstellen. prepare.py erzeugt eigene CEM-/Host-/Erwartungsdateien; host/harness.js erzeugt zwei tatsächliche Originalinstanzen und führt die vorbereitete native Folge aus. Einen eigenen lokalen Server für host/ starten; Browserbereitschaft ist body[data-ready=true]. browser-capture.json/structural-capture.json enthalten die tatsächlichen Beobachtungen. check_schema.py nutzt das vorher gepinnte Original-CEM-Schema mit jsonschema4.25.1. Originalcode und Fremdbibliotheken werden nicht als eigene Implementierung ausgegeben. Source-/Input-/Methodenhashes im Manifest.

**Eigene Hostkorrektur und Ergebnisaufzeichnung:** Die eigenen Listboxen erhielten zusätzlich explizite Label-IDs/aria-labelledby, damit der Forschungshost keine vermeidbar unbenannten Listen enthält. Die ursprüngliche APG-Klasse blieb unverändert; dieselben acht Fälle wurden nach Reload erneut geprüft und nicht neu gezählt. Ein eigener Capture-Schreibfehler wurde vor der erfolgreichen Wiederholung/Aufzeichnung als own-capture-write-error.json gespeichert. Frühere eigene Host-/Capturestände bleiben als initial-host.html/initial-unlabelled-host-capture.json erhalten. Keine ursprüngliche APG-Fehlerdiagnose daraus abgeleitet.
