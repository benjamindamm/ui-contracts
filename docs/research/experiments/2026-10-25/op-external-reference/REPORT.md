# OpenPencil: tatsächliche Propertyauflösung mit externem CEM-Ziel

Stand: 25. Oktober 2026. **OpenPencil X03 A/C505** ausschließlich für den expliziten Booleanbeitrag. **38 U:23 Integration,15 weitere. 478 Bedingungen/62 Gruppen.**

## Fehlende Aussage und Endbedingung

Der vorherige Befund C306 belegte nur interne Properties/Slots desselben Scenegraphs. X03 verlangt ein eindeutig adressiertes, semantisch zugeordnetes Ziel einer separat beschriebenen Domäne. Die Endbedingung hier lautet: tatsächliche ursprüngliche Switch-Booleanbindung an ein eigenständiges CEM-Interfacefeld binden; falsche Zielart, Typ, Owner und Quellenrevision abweisen; ID-Erhalt beim ursprünglichen Propertyrename und getrennte Instanzwerte prüfen. Kein bloßer Austausch des Frameworknamens im bisherigen Prüfer.

## Kandidatenspezifischer Originalpfad

Unveränderte veröffentlichte @open-pencil/scene-graph0.16.0 und @open-pencil/dom-css0.16.0 aus S100s eingefrorener Installation. Vollständige ursprüngliche behaviourFromSpec/behaviourProperties/behaviourToSpec/missingBindings-, SceneGraph.createNode/updateNode/createInstance- und behaviourControls-APIs ausgeführt; keine ausgeschnittene Ersatzfunktion, kein eigener Scenegraph. Der ursprüngliche Switchkind definiert value als erforderlichen Booleanwert. Originalspec values.value=Selected löst den tatsächlichen Propertynamen auf selected-id einer BOOLEAN-Definition auf.

Eigenständiges interface.json verwendet das unveränderte CEM-Originalmodell: ResearchSwitch, öffentliches Feld checked, Typtext boolean. Diese Forschungsfixture ist kein neues Komponentenprodukt und kein ausgewähltes Produktionsformat. Der ursprüngliche Graphpropertyname Selected ist ausdrücklich nicht gleich dem öffentlichen CEM-Feldnamen checked; die semantische Zuordnung ist zusätzlich und sichtbar.

## Zusätzliche präzise Referenz

Der zusätzliche Binder adressiert CEM per Dateihash und JSON Pointer auf den tatsächlichen field-Knoten; er prüft name/kind und die eingeschränkte primitive Booleansemantik. Auf OpenPencil-Seite verwendet er den tatsächlichen Owner, die ursprüngliche Behaviour-Property-ID und ihre ursprüngliche BOOLEAN-Definition. Owner plus Property-ID ist erforderlich: Eine zweite Komponente besitzt im Versuch absichtlich dieselbe lokale ID und denselben Namen. Referenzhashes binden CEM-Datei und den explizit gespeicherten ursprünglichen Owner-/Property-/Behaviourausschnitt. Dieser Ausschnittshash ist eigene Forschungsmetadatenbindung, keine vollständige .fig-/Libraryrevision und keine native OpenPencil-Versionsfunktion.

Beide angenommenen Fälle erzeugen ursprüngliche Instanzen A und B; ursprüngliche behaviourControls liefert designed=true für A und false für B. Nach Umbenennung Selected→Is Selected bei gleicher ID liefert behaviourToSpec den neuen Namen. Der externe CEM-Pointer und sein checked-Boolean bleiben unverändert. Kein Livehost, Editor-, Export- oder AT-Nachweis.

## Elf vorab benannte Referenzbedingungen P61

[Erwartungen](cases.json), [Resultate](results.json), [Runner](run.mjs).

| Fall | Ergebnis und prüfende Rolle |
| --- | --- |
| external-boolean-reference | Tatsächliche ursprüngliche Booleanbindung und externe CEM-Zuordnung angenommen; A/B-Werte getrennt. |
| wrong-target-kind | CEM-Deklaration statt field als Ziel vom Zusatzbinder abgewiesen. |
| wrong-interface-type | CEM-string-Feld statt boolean vom Zusatzbinder abgewiesen. |
| stale-interface-revision | Veralteter CEM-Dateihash vom Zusatzbinder abgewiesen. |
| foreign-owner | Fremde Komponente mit gleichnamiger/lokal gleich-ID-Property vom Zusatzbinder abgewiesen. |
| wrong-original-property-type | TEXT statt BOOLEAN wird vom ursprünglichen behaviourFromSpec abgewiesen. |
| missing-original-property | Fehlendes Selected wird vom ursprünglichen Resolver abgewiesen. |
| ambiguous-original-property-name | Ursprünglicher Resolver wählt selected-id unter zwei gleichnamigen Properties; Zusatzbinder erkennt die Mehrdeutigkeit und verwirft den Fall. |
| removed-stored-binding | Entfernte Property bleibt im gespeicherten Behaviour referenziert; ursprüngliches missingBindings meldet value, Zusatzbinder verwirft. |
| renamed-original-property | Ursprüngliche IDbindung und externer CEM-Zielknoten bleiben erhalten, toSpec verwendet den neuen Originalnamen; A/B-Werte getrennt. |
| stale-graph-revision | Veralteter Hash des gebundenen Owner-/Property-/Behaviourausschnitts vom Zusatzbinder abgewiesen. |

Elf Beobachtungserwartungen erfüllt. Der gespeicherte erste Zehnerlauf wurde um die vorher festgelegte elfte Revisionsbedingung ergänzt; die wiederholten zehn zählen nicht erneut. Originaltrace des Mehrdeutigkeitsfalls bleibt erhalten: zwei Selected-Namen, ursprünglicher Treffer selected-id. Das zusätzliche Ablehnen ist keine ursprüngliche OpenPencil-Garantie.

## Zwei Originalschemabedingungen P62

[Schemaergebnisse](schema-results.json). Das bereits gepinnte unveränderte CEM-Schema akzeptiert sowohl die eigene boolean- als auch die gezielt geänderte string-Felddefinition. Beide sind strukturell gültiges CEM. Die fachliche Gleichsetzung mit OpenPencils Switchvalue wird allein vom zusätzlichen Booleanbinder beurteilt. Die zwei Ebenen werden nicht verwechselt.

## Bewertung und Grenzen

X03 U→A/C505: ursprünglicher Property-/Kindmechanismus vorhanden, zusätzliche externe Referenzbindung tatsächlich ausgeführt. Keine native CEM-Unterstützung von OpenPencil behauptet. Keine beliebigen TypeScript-Aliase/Unions, keine VARIANT-On/Off-Übersetzung, Text-/Zahlenwerte, Slots, externen SCXMLzustände, A11y-Ziele oder Librarymigrationen aus diesem Booleanfall ableiten. Die Referenzversion ist auf den benannten Ausschnitt beschränkt. X01 und X08 des Kandidaten bleiben offen; das Originalmodell erhält dadurch keine Vier-Domänen-Paketgovernance.

## Reproduktion und Quellenstand

prepare.py erzeugt eigene CEM-/Erwartungsdateien; run.mjs verwendet die unveränderten isolierten Originalpakete aus ../op-projection-origin/tool. check_schema.py verwendet das gespeicherte ursprüngliche CEM-Schema mit jsonschema4.25.1. tool-inventory.json aus S100 und die verwendeten Originalpfade sind im neuen Manifest gebunden; Lockdateien werden kopiert, node_modules nicht. Der veröffentlichte Paketstand wird nicht global bytegleich zum früheren Repo-Snapshot ab2875… erklärt. Eingaben, Prüfprogramme, Resultate und Hashes sind gespeichert; METHODS.md/REQUIREMENTS.md unverändert. Kein Commit/Push und keine Produktionskomponente.
