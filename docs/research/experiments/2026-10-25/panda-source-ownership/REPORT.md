# Panda: tatsächliche Quellenverfolgung eines Visualwerts

Stand:25. Oktober2026. **Panda CSS X08 A/C506**, nur für die beschriebene Tokenwert→Integrationsableitung. **37 U:22 Integration,15 weitere. 487 Bedingungen/63 Gruppen.**

## Endbedingung und Originalgegenstand

Für einen konkreten Wert feststellen, welche Konfiguration führt, wie dessen Herkunft im ursprünglichen Specindex erscheint und wie eine zusätzliche Integrationsableitung samt Änderung an diese Quelle gebunden wird. Kein bloßes neues Frameworklabel im bisherigen Booleanbinder.

Originalrevision `86f78a228204d63baa0b8bca2676d9f26190e449`. Vollständige Module packages/config/src/merge.ts, sources.ts, shared.ts und error.ts sowie packages/compiler-shared/src/design-system-spec/sources.ts mit TypeScript5.9.3 transpiliert und ausgeführt; keine Funktionen ersetzt. mergeConfigsWithSources, SourceTracker einschließlich ursprünglicher Pfad-/Token-Normalisierung und applySpecSources sind tatsächlich ausgeführt. Eigene geordnete Preset-/Configobjekte sind Eingaben in ursprünglicher Panda-Konfigurationsform.

Rust specs.rs erzeugt im gelesenen Originalpfad den Basisindex ohne die hier anschließend gesetzten Sourcefelder. Die TypeScriptfunktion applySpecSources ist die konkrete zusätzliche ursprüngliche Annotationsfunktion. **Die Rustengine, komplette Konfigurationsauflösung und Compileraufrufkette wurden nicht ausgeführt.** Der verwendete DesignSystemSpec-Grunddatensatz ist eine eigene passende Fixture mit einem Token und einem Wert aus dem tatsächlich gemergten Objekt, kein als Originalcompileroutput ausgegebener eigener Generator.

## Tatsächliche per-information Herkunft

Der Basispreset führt sizes.popup.value=120px. Eine nachfolgende eigene Konfiguration setzt160px; ursprüngliches Merge und Tracking wählen Configindex1. applySpecSources verwendet für den Token ausdrücklich den `.value`-Pfad und setzt dessen source-Index auf den tatsächlichen Configeintrag.

Der wichtige Gegenfall ergänzt nur description über theme.extend. Der übergeordnete Tokenpfad hat dann mehrere beitragende Quellen, value bleibt jedoch bei Presetindex0. Der Index wird nicht pauschal der zuletzt berührenden Datei des ganzen Objekts zugeschlagen. Ein anderer Fall mit zusätzlichem untergeordnetem Token verschiebt den eigenen Wert nach DEFAULT; ursprüngliches Tracking verschiebt den Wertpfad mit, und die Annotation normalisiert DEFAULT wieder zum Spec-Tokennamen.

## Ausdrücklich zusätzliche Integrationsbindung

Ein eigener begrenzter Zusatzschritt bindet den tatsächlich annotierten Tokenwert sizes.popup an research-vars.css/--popup-max-height. Er prüft vorhandenen gültigen Quellenindex, den benannten Config-/Presetdateieintrag, dessen eigenen Eingabehash und konkreten Valuepointer sowie Übereinstimmung zwischen ursprünglichem Mergewert, tatsächlichem Quellwert und eigener Spec-Wertzeile. Nur positive endliche px-Werte dieser Fixture werden übersetzt; keine generelle Token-/Alias-/Einheitenimplementierung.

Der [Änderungsnachweis](change-record.json) hält ursprünglichen Sourceeintrag/-index, Quellpointer und Quellhash sowie die abgeleitete CSS-Eigenschaft/-Hash vor und nach160→192px fest. Der Presethash bleibt gleich. CEM-/SCXML-/HTML-Quellen des bestehenden Vier-Domänen-Falls werden nicht geändert und sind gehasht. Das führt keine zweite Behavior-/Accessibilitydefinition ein. Es ist eigener Forschungsnachweis für genau die Ableitung, kein natives Panda-Journal und keine authentifizierte oder atomare Änderungstransaktion.

## Neun vorab benannte Bedingungen P63

[Erwartungen](cases.json), [Resultate](results.json), [Prüfprogramm](run.cjs).

| Fall | Beobachtung |
| --- | --- |
| config-last | Ursprüngliches Merge160px, tatsächliche Originalherkunft Configindex1, zusätzliche CSS-Ableitung160px. |
| preset-alone | Ursprüngliches Merge120px und Presetindex0, zusätzliche Ableitung120px. |
| config-value-change | Geänderte Config192px bleibt Originalquelle, neue Quell-/Ableitungshashes nachvollziehbar. |
| description-extend | Nur Beschreibung von Config; Wert120px bleibt vom Presetindex0. |
| default-token-hoist | Ursprüngliche DEFAULT-Normalisierung erhält die Wertquelle und Annotation. |
| tracking-absent | Originalannotation liefert keinen Sourceindex; Zusatzbinder weist fehlende Herkunft zurück. Kein geratenes Ownership. |
| source-index-out-of-range | Originalannotation übernimmt den absichtlich beschädigten Trackerindex99; Zusatzbinder weist ihn zurück. Kein Original-Validatorversagen aus einer nicht normalen Trackerproduktion abgeleitet. |
| export-value-disagrees | Eigene Spec-Fixture enthält999px statt tatsächlichem Mergewert; Zusatzbinder weist die Ableitung zurück. Kein solcher Rustexport behauptet. |
| stale-source-file | Veralteter eigener Eingabehash verhindert die Ableitung. |

Neun Beobachtungserwartungen erfüllt. Eine rein redaktionelle Korrektur des eigenen Journalfeldnamens ist im initial-journal-key-results.json erhalten; Wiederholung zählt nicht als weitere Bedingung. Keine zusätzliche Regex-/Pointervalidierung wird dem Original zugeschrieben.

## Bewertung und Grenzen

X08 U→A/C506 für die konkrete originale Wertquellenführung mit zusätzlicher hashgebundener Änderung/Ableitung. Native Panda-Merge-/Source-Annotation ist vorhanden; Sourcehashes und Integrationsjournal ergänzt der Forschungsbinder. Kein allgemeines Vier-Domänen-Vorrangmodell, keine vollständige Compiler-/Rust-/CSS-Renderingprüfung, keine Token-DTCG-Konformität oder Browser-/AT-Zusage. Eingabereihenfolge wird bewusst presets-first/config-last vorgegeben; ein beliebiger Loader wird hier nicht geprüft.

Die anderen Panda-Zellen, besonders X01, werden nicht automatisch übertragen. Andere Informationstypen, ursprüngliche Aliasauflösung und semantische Themen-/Bedingungskontexte bleiben gesondert zu prüfen. Der benannte ursprüngliche Quellenpfad ist für diesen Wert ausgewertet; keine identischen Trackerproben zur bloßen Steigerung der Fallzahl.

## Reproduktion

Die Quell-URLs und Hashes aller gelesenen Originaldateien stehen im Manifest. prepare.cjs transpiliert die vollständigen benannten Originalmodule aus config/ und sources.ts mit dem vorhandenen isolierten TypeScript5.9.3-Werkzeug. run.cjs speichert neun Input-/Merge-/Tracking-/Annotations-/Ableitungsbeobachtungen. Die Originalquellen und erzeugter Originalmodulcode werden nicht als eigene Bibliothek verteilt; sie werden am angegebenen Snapshot bereitgestellt und gegen die Lesekopie-Hashes geprüft. Eigene Programme, Fixtures in den Ergebnisdateien, Änderungsnachweis und Resultate sind gespeichert. METHODS.md/REQUIREMENTS.md unverändert. Kein Commit/Push, keine Produktionskomponente oder ausgewählte Produktsprache.
