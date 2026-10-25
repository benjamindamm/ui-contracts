# Vier verbleibende Layoutfragen: Originalbeitrag plus tatsächliche Zusatzbindung

Stand:25. Oktober2026. **UXSpec V04 A/C540, V06 A/C541; uSpec V04 A/C542, V06 A/C543.**16 unterschiedliche native Bedingungen in4 Gruppen, vollständig erfüllt nach offengelegter eigener Zeilenpolitik. Ein anfänglicher positiver Scrollbefund war nicht erfüllt und bleibt erhalten. Keine native Anker-/Scrollfähigkeit in die Originalformate hineingedeutet.

## Originale tatsächlich ausgeführt

**UXSpec:** Vollständiger unveränderter ursprünglicher Compiler am Pin20dfae0e7224d952e198afdf4ffed26d6fd67180 und vollständiges ursprüngliches style-map-Modul. Das genaue minimale Pflichtroot besteht unverändertes Originalschema. Tatsächlich kompiliertes slots.results und gemappte Containergröße160px werden verwendet. Ein akzeptiertes ursprüngliches container.overflow=scroll wird vom Originalmapper weiterhin nicht interpretiert; dies wird ausdrücklich gemessen und nicht durch den Zusatzadapter verschleiert. Kein UXSpec-Runner/React-Renderer oder ursprünglicher Timer ausgeführt.

**uSpec:** Vollständiger unveränderter ursprünglicher Canonical-Builder samt tatsächlicher Cachevalidierung/Identitätsnormalisierung am Pin1e25e9b8bc2e694689ba0489594f38807a341f14 auf eigenen minimalen Caches/Rendererevidence. Der tatsächlich normalisierte Section._anchor verweist auf die ursprüngliche Inputlayer-ID oder bleibt im Gegenfall unresolved. Er bleibt ein Messknotenanker; die Runtimebedeutung kommt ausdrücklich vom Zusatzbinder.

Für Clipping laufen die **vollständige unveränderte ursprüngliche extractDims-Funktion und ursprüngliches sg** auf eigenen clipping-only Minimalnodes. Sie erhalten ausschließlich clipsContent, keine numerischen/Paintfelder. Deshalb werden die entsprechenden anderen Figma-/Bindingbranches tatsächlich nicht ausgeführt; es wird kein figma-Objekt und kein resolveBinding-Stub bereitgestellt. Alle Originaldeklarationen sind unverändert, Quell-/Deklarationshashes gespeichert. Keine echte Figma-Sitzung oder gesamte Pluginpipeline behauptet. Der resultierende Original-Clippingbeleg wird durch den tatsächlichen Builder im sourceModel erhalten.

Originale _meta.baseSourceHash-Vergleiche bleiben nominale Originalmarker des Minimalfixtures, kein erfundener Beweis echter Figma-Extraktionsintegrität. Zusätzliche tatsächliche Input-/Outputdateihashes werden getrennt gebunden.

## Zusätzlicher semantischer Vertrag, kein stiller Schemaumbau

Separates ursprüngliches CEM beschreibt benannte input/popup-Teile. Der eigene Binder verbindet einen tatsächlich kompilierten UXSpec-Slot beziehungsweise einen tatsächlich normalisierten uSpec-Layer mit richtigen eigenen A/B-DOM-Kontexten und diesen Teilen. Laufzeitziel, Unterkante, Richtung und Abstand8px sind **zusätzliche** explizite Regeln. Native CSS-Anker implementieren sie; die ursprünglichen Domänendateien werden nicht um erfundene Ankereigenschaften erweitert.

Bei UXSpec kommt auto als ausdrückliche zusätzliche Overflowpolitik hinzu. Bei uSpec ist die enge Zuordnung original clipsContent=true→CSS clip und false→visible dokumentiert. Daraus wird weder natives auto/scroll in uSpec noch ein universeller Scrollvertrag abgeleitet. Die zusätzliche Viewportbegrenzung160 und feste Zeilengröße32 sind Testpolitik, keine extrahierten uSpec-Maße.

## Sechzehn Bedingungen

[Vorab-Erwartungen](cases.json), [alle native Ergebnisse](results.json).

| Originalbeitrag/Feld | Fälle und tatsächliche Entscheidung |
| --- | --- |
| UXSpec V04, P99:5 | Slot/Teil/Kontext korrekt: Abstand8. Inputhöhe20→40: Abstand bleibt8. Fremdes Inputziel, fehlender nativer Input und nicht unterstützte Gap-Einheit werden zusätzlich abgewiesen. Andere Einheiten sind nicht global ungültig. |
| UXSpec V06, P100:3 | Originalmapper interpretiert overflow nicht. Mit ausdrücklichem Zusatz-auto und fester Zeilenpolitik: Client160, Inhalt224, scrollTop64. Fehlende zusätzliche Politik und fremder Popupkontext werden abgewiesen. |
| uSpec V04, P101:4 | Tatsächlich normalisierter Inputlayer wird an richtiges Runtimeziel gebunden; Abstand8 bleibt bei Input20→40. Fremde Instanz scheitert. Tatsächlich vom Originalbuilder als unresolved ausgegebener Anker wird nicht in ein gültiges Runtimeziel umgedeutet. |
| uSpec V06, P102:4 | Tatsächlicher Original-Clippingwert true erzeugt zusätzlichen CSS-clip-Port: letzte Zeile nicht gemalt, scrollTop0. false erzeugt visible: letzte Zeile außerhalb der Box gemalt. Fehlender oder absichtlich untypisierter Originalbeleg wird vom Zusatzbinder abgewiesen. |

Gemaltheit wird mit tatsächlichen Browserrechtecken und elementFromPoint an der letzten Zeile geprüft, nicht aus bloßem CSS-String geraten. Fremdkontext-/Zielprobleme werden nicht als ungültige Original-CSS-Syntax ausgegeben. Native Browserunterstützung für CSS-Anker wird ausdrücklich geprüft; ein nicht unterstützter Browser würde als solcher auffallen. Der eingesetzte Browser unterstützt den konkreten Pfad.

Der absichtliche clipsContent=auto-Minimalnode ist ein negativer Eingabeversuch der breiten ursprünglichen any-Funktion, kein behaupteter realer Figma-Ausgabewert. Dass die Originalfunktion einen String erhalten kann, ist keine neu behauptete Figma-Fähigkeit oder generelle Originalschemaverletzung. Fehlender Beleg wird nicht still zu false/default umgedeutet.

## Erhaltene erste Erwartung und Korrektur

initial-native-capture.json bewahrt einen nicht erfüllten ursprünglichen eigenen Scroll-Expectationsstand: Der tatsächliche Originalmapper liefert standardmäßig column-flex. Die eigene erste Zeilenfixture hatte zwar height32, erlaubte aber Schrumpfen;7 Zeilen wurden in160 eingepasst, scrollHeight160/scrollTop0. Daraus durfte kein Overflowbeweis entstehen.

Die zusätzliche Forschungsprämisse fester32px-Zeilen ist nun durch flex-shrink:0 ausdrücklich gesetzt und in additional-row-policy.json offengelegt. Der Originalmapper/Compiler wurde nicht verändert. Dieselben16 Bedingungen erneut geprüft, keine Wiederholung hinzugezählt. initial-flex-shrink-host.html erhält den ersten Host. Zusätzlich bewahrt own-preflight-syntax-error.json einen eigenen fehlenden Objektklammerfehler vor jeglicher Originalausführung; keine Originalstörung daraus abgeleitet.

## Reichweite und Reproduktion

A jeweils nur für die ausgeführte Originalquelle plus konkret erforderlichen zusätzlichen CEM-/Kontext-/CSS-Adapter. Die früher unerfüllte OpenPencil-Popup/Inputrelation, UXSpec-Unitverluste, uSpec-Aliase, lokale Evidencegrenzen und SSR-Gegenbefunde bleiben erhalten. Kein ursprünglicher neutraler gemeinsamer Layoutstandard, keine gesamte native Plattform-/Accessibility-/Editorabnahme.

prepare.cjs erzeugt die tatsächlichen ursprünglichen Modelle und zusätzliche Profile, Originalmapper wird ausschließlich transpiliert; Originalcode wird nicht als eigene Implementierung verteilt. Eigener HTTP-Host für host, body[data-ready=true], layoutResearch.runCase(id), check_results.py. Rohcaptures, ursprüngliche Modellausgaben und Quellenhashes sind gespeichert. Keine neue Produktsprache, Produktionseinheit, Commit oder Push.
