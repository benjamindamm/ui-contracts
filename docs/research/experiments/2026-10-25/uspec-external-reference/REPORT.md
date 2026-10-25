# uSpec: externe Quellpfade gegenüber tatsächlichen Output-Pointern

Stand:25. Oktober2026. **X03 bleibt U/C512.** Acht neue Beobachtungsbedingungen P71 im vollständigen unveränderten Originalcachevalidator mit tatsächlich vorhandener Obligation-Evidence-Datei. Akzeptierte Quellhinweise sind kein Nachweis einer fremden Artefaktauflösung.

## Neuer benannter Originalpfad

Revision `1e25e9b8bc2e694689ba0489594f38807a341f14`. Derselbe vollständige ursprüngliche cache-validation.ts wie im vorigen Ownershipblock, diesmal ist research-evidence-api.json ausdrücklich vorhanden. Damit wird validateEvidenceObligations → validateObligationCoverage → validateRepresentationTarget tatsächlich ausgeführt. Der frühere Builderblock ohne diese Evidence wird nicht identisch wiederholt. Keine Originalfunktion ersetzt und kein externer Resolver hinzugefügt.

Die eigene API-Cachefixture enthält ein value/string-Property, eine emitted-Ledgerzuordnung und eine must-emit-Obligation mit api-property-Targettyp und Feldvergleich type=string. Eine separate tatsächliche CEM-Datei ist vorhanden. Eigenes sourcePaths/Facts-Snapshot zeigt auf ihren benannten Feldknoten; er wird nicht als publiziertes neutrales uSpec-CEM-Binding ausgegeben.

## Acht vorab benannte Bedingungen

[Erwartungen](cases.json), [Ergebnisse mit Originaldiagnosen und tatsächlicher Fremdquelle](results.json), [Runner](run.cjs).

| Fall | Tatsächliches Originalergebnis |
| --- | --- |
| local-output-control | Eigener vorhandener /data/mainTable/properties/0-Output wird aufgelöst, api-property und type=string akzeptiert. |
| missing-output-target | Fehlender lokaler Propertyknoten abgewiesen. |
| wrong-output-kind | Derselbe lokale Zielpfad als voice-record deklariert: abgewiesen. |
| external-output-uri | Tatsächlich vorhandene foreign-cem.json plus Fragmentpointer wird nicht geöffnet/aufgelöst, Outputtarget abgewiesen. |
| unknown-source-path | Nicht existierender sourcePaths-Eintrag wird akzeptiert. |
| missing-source-file-uri | sourcePaths mit nicht existierender fremder Datei wird akzeptiert. |
| changed-external-source | Fremdes tatsächliches CEM-Feld jetzt number; gespeicherte Evidencefacts und Output weiter string. Originalcacheprüfung akzeptiert. |
| output-semantic-type-conflict | Output selbst number gegen die representation.equals-Vorgabe string: Originalprüfung weist ab. |

Acht Beobachtungserwartungen erfüllt. Der lokale Typ-/Feldvergleich ist vorhanden und wird anerkannt. Er vergleicht Output gegen gelieferte Evidencevorgabe; er verifiziert nicht automatisch die tatsächliche Fremdquelle hinter einem beliebigen sourcePaths-String.

## Belegte Grenze und verbleibender Nachweis

Die gelesene und ausgeführte Originalfunktion verlangt bei sourcePaths nur eine nichtleere Liste. Die Output-Targets werden dagegen als JSON Pointer innerhalb des übergebenen Caches aufgelöst und anhand der vier ursprünglichen Zielart-Grammatiken geprüft. Strings mit fremdem Dateinamen/URI erhalten dadurch keine definierte externe Resolversemantik. sourcePaths ist kein alleiniger Beleg für Originaldatei-, Versions-, Typ- oder Instanzbindung.

**X03 bleibt U:** Ein tatsächlich zusätzlich gebundener fremder Originalgegenstand mit Domänenbedeutung und Quellen-/Revisionsprüfung fehlt. Ein eigener Adapter könnte diese Arbeit ergänzen; er wurde hier nicht zur bloßen Matrixschließung erfunden. Aus diesem lokalen vollständigen Validatorpfad wird keine globale Nichtexistenz anderer uSpec-Integrationen abgeleitet, deshalb keine pauschale N-Umwertung. Die präzise Grenze ist jetzt ausgeführt, statt dieselben Required-Felder erneut zu lesen.

Die API-/Figma-/Structure-/Voice-Evidenzmodelle behalten ihre eigenen Regeln. Dieser Test ist keine Behauptung, beliebige CEM-Dateien seien ursprüngliche zulässige Figma-Evidence oder die ursprüngliche Gesamtpipeline sei konträr zu ihrer Spezifikation. Keine Originalschema- oder Versionsmigrationsgarantie für Fremdartefakte aus der Snapshotakzeptanz ableiten.

## Reproduktion

run.cjs nutzt das vollständig unverändert transpilierte cache-validation.js des benachbarten uspec-ownership und legt eigene acht Cache-/Evidence-/CEM-Dateisätze an. Das Modul benötigt nur seine ursprünglichen Node-Datei-/Pfadfunktionen. Quelle und kompilierte Datei am Hash gebunden; keine neue Abhängigkeit oder Schemaerweiterung. Inputs/Outputs/Originaldiagnosen gespeichert. Kein Commit/Push, keine Produktsprache oder Produktionskomponente.
