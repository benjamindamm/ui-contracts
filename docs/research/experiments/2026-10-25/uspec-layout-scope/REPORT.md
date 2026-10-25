# uSpec: Messanker, Clipping und nachgelagerte Strukturbelege

Stand: 25. Oktober 2026. Originalrevision `1e25e9b8bc2e694689ba0489594f38807a341f14`. **V04 U/C400 und V06 U/C401 bleiben unverändert.** Null neue Laufzeitbedingungen; 41 offene Zellen insgesamt.

## Endlicher Quellenumfang

[Quelleninventar](source-review.json): ursprüngliche Struktur-Anleitung, Base-JSON-Dokumentation, vollständige extractDims-Funktion und flatWalk-Koordinatenpfad in phaseE.ts; zusätzlich safe.ts, CLI evidence-structure.ts und öffentliche Structure-Dokumentation. Der Originalbaum ist nicht abgeschnitten. Die Anleitung wurde als Formatbeschreibung gelesen; eingebettete Arbeitsanweisungen wurden nicht ausgeführt. Kein Audit sämtlicher Figma-/CLI-/Renderfunktionen behauptet.

## V04: tatsächliche Identität des Ankers

Die ursprüngliche Section-anchor-Definition bindet eine Sektion mittels layerName/layerId/variantId/variantName/variantProperties an genau einen Design-Variantenbaum. Die Regeln unterscheiden Variantenroot, konkrete Child-Instanz, Slothost und zustandsabhängige Anatomie. Ein ungelöster Layer darf ausdrücklich layerId:null tragen. Das sind konkrete Dokumentations- und Messzielbindungen, keine Definition einer Popup-Zielkante zur Laufzeit.

flatWalk zieht die Translation der Variante von der Translation des Elements ab und rundet x/y/w/h. Das bewahrt eine gemessene, variantenrelative Boundingbox. Es definiert weder eine Zielrichtung noch einen Abstand zu einem benannten anderen Element unter Größenänderung. Die öffentliche Structure-Dokumentation beschreibt zusätzlich Messplatzierung über render-meta-Layer-ID mit Namens-/Live-Bbox-Fallback. Auch dort ist das Ziel eine Messung in der gerenderten Designinstanz.

**Fehlender Beitrag:** eine ausdrücklich definierte und ausführbare Beziehung zwischen Runtime-Ziel und Overlay mit Richtung und Abstand. Die untersuchten Messanker allein erfüllen V04 nicht. Eine zusätzliche solche Bindung wäre ein eigener Beitrag; sie wurde hier nicht erfunden.

## V06: erhaltene Daten gegenüber Scrollsemantik

extractDims bewahrt clipsContent als value/token/display sowie Maximalabmessungen und Layoutdaten. Die Struktur-Anleitung bezeichnet true als Verhindern von Overflow; damit ist ein Clippingbeitrag vorhanden. Die Base-JSON-Dokumentation nennt sogar eine Variante namens overflow=scroll als Beispiel für Layoutwrapper. Dieser Variantenname ist jedoch keine dort definierte Zuordnung von Achse, Scrollpolitik und Interaktion.

safe.ts beschreibt die Auswahl des effektiven Childcontainers: Bei genau einem Auto-Layout-FRAME-Kind wird durch Wrapper abgestiegen. Die Base-JSON-Dokumentation hält ausdrücklich fest, dass treeHierarchical die echten Wrapper mitsamt Dimensionen und clipsContent behält. Der CLI-Strukturevidenzbuilder übernimmt Variantendimensionen, Subkomponenten-Dimensionen und weitere Originalbelege in einen EvidenceEnvelope mit baseSourceHash und Defaultvarianten-Identität. Daraus folgt kein zusätzlicher Runtime-Scroller; es ist die Weitergabe von Designbelegen.

**Fehlender Beitrag:** eine konkret gebundene ursprüngliche Laufzeitinterpretation der Overflow-/Scrollpolitik oder eine ausdrücklich zusätzliche Politikbindung. Clipping und Maximalgröße werden anerkannt, ohne sie still zu einem vollständigen Scrollvertrag zu erweitern.

## Ergebnis und Stopregel

Dieser ursprüngliche Mess-/Extraktions-/Evidenzpfad ist für die zwei Fragen ausgewertet. Eine erneute identische Abfrage von _anchor, bbox oder clipsContent erweitert den Nachweis nicht. Die Zellen bleiben mit diesen präzisen fehlenden Bindungen offen; hypothetische Erweiterbarkeit wird nicht als Grund für endlose Suche verwendet. Eine neue konkrete Originaldefinition oder ein separat begründetes Binding würde die Frage wieder eröffnen. Keine pauschale N-Bewertung des gesamten Projekts, kein neuer Adapter, keine Implementierung und kein Commit/Push.

Nächste unabhängige Gruppe: X01, getrennte Speicherung fachlicher Originalbeiträge und tatsächliche Importpflichten. Die vier ursprünglichen UXSpec/uSpec-Layoutfragen werden dabei nicht als bereits gelöst gezählt.
