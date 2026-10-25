# uSpec: tatsächliche externe CEM→Fact→Outputbindung und Quellführung

Stand:25. Oktober2026. **X03 A/C536 und X08 A/C537**, jeweils eng begründet, dieselben14 Bedingungen nur einmal als P96 gezählt. Keine native neue uSpec-Fremdquellen-/Ownershipfunktion behauptet.

## Original und Zusatz

Vollständige unveränderte ursprüngliche cache-validation am Pin1e25e9b8bc2e694689ba0489594f38807a341f14, tatsächliche APIcache-/Obligation-Evidence-Dateien. Der Originalvalidator prüft seine lokalen Outputpointer, Zielart und representation.equals. Der eigene zusätzliche Binder löst einen tatsächlich vorhandenen externen CEM-Dateipfad und JSONPointer auf, prüft den ursprünglichen CEM-Fieldkind, Modul-/Klassendefinition, Propertyname, primitive Typbezeichnung und konkreten Dateihash. Eine Datei wird wirklich gelesen; gleichnamige Mitglieder in einem anderen Modul gelten nicht als dasselbe Ziel.

Die bestehende sourcePaths-Angabe des Originalfacts wird mit genau diesem externen Ziel verglichen. Fact.name/type/representation.equals und tatsächlicher lokaler APIoutput müssen dem gelesenen ursprünglichen CEM-Member entsprechen. Die Originaldateien werden nicht um ein selbst erfundenes uSpec-Referenzfeld erweitert; der Forschungsbinder und sein Änderungsjournal sind separate Zusatzartefakte.

Die führende Information ist hier ausdrücklich Name/Typbezeichnung eines CEM-Properties. Evidence-Fact und APIcache-Zeile sind Ableitungen. Die Hashbindung befindet sich im eigenen Binder: _meta.baseSourceHash des ursprünglichen Minimalfixtures wird nicht heimlich als fremder CEM-Revisionsmechanismus umgedeutet. Keine authentifizierte Bearbeitungsfreigabe oder atomare Mehrdateitransaktion zugesichert.

## Vierzehn vorab gespeicherte Bedingungen

[Erwartungen](cases.json), [vollständige Original-/Zusatzentscheidungen und Journale](results.json).

| Fall | Beobachtung |
| --- | --- |
| control | Tatsächliche CEM-Datei, tatsächlicher Fact und tatsächlicher lokaler Output stimmen überein; Original und Zusatzbinder nehmen an. |
| source-revision-stale-hash | Tatsächliche CEM-Typbezeichnung string→number; unveränderte Revision wird zusätzlich abgewiesen. Original nimmt unveränderte lokale Facts/Outputs weiter an. |
| source-revision-stale-facts | Neuer Quellhash allein genügt nicht; alter Fact kollidiert mit tatsächlich gelesenem number. Original nimmt weiter an. |
| source-revision-rederived | Regeneration liest die geänderte Datei tatsächlich erneut, übernimmt Name/Typ in Fact/equals/APIzeile; beide Prüfungen nehmen an. |
| coordinated-derived-edit | Fact/equals/Output gemeinsam auf number geändert, CEM bleibt string: Original nimmt an, zusätzlicher Mastervergleich weist ab. |
| wrong-external-target-kind | Tatsächliches CEM-Event statt Field wird zusätzlich abgewiesen. |
| same-name-wrong-definition | Gleichnamiger Field in zweitem Modul wird wegen falschem Definitionskontext abgewiesen. |
| missing-external-file | Original nimmt lokalen Cache weiter an; zusätzliche Datei-Auflösung scheitert ausdrücklich. |
| missing-external-pointer | Fehlendes tatsächliches Fremdziel wird zusätzlich abgewiesen. |
| evidence-sourcepath-conflict | FactsourcePaths verweist auf ein anderes Artefakt; zusätzliche eindeutige Zuordnung scheitert. |
| unsupported-semantic-type | Ein komplexer originalschemafähiger Typausdruck ist für den primitiven Adapter nicht unterstützt. Kein generell ungültiger CEM-/TypeScript-Typ behauptet. |
| fact-updated-output-stale | number-Fact gegenüber altem string-Output: Hier weist bereits der Originalvalidator representation.equals ab; Zusatzbinder erkennt ebenfalls den Konflikt. |
| property-renamed-without-rebind | Tatsächliche Propertyumbenennung verletzt den gebundenen Definitionskontext. Kein stiller neuer Namenstreffer. |
| property-renamed-explicit-rebind | Explizit erneuerte Namensbindung und aus tatsächlich gelesener Quelle abgeleitete Facts/Outputs stimmen wieder überein. |

13 tatsächlich vorhandene Fremd-CEM-Varianten bestehen unverändertes Original-CEM-Schema; die14. Datei fehlt absichtlich. Diese Shape-Preflights werden nicht als zusätzliche Bedingungen gezählt. Eine strukturell gültige CEM-Datei ist nicht automatisch ein passendes semantisches Ziel.

## Zwei getrennte Kriterien

**X03 A/C536:** Externe Originaldatei, expliziter Pointer, ursprünglicher Field-/Definitionskontext, Typbedeutung und Revision sind bis zum tatsächlichen Originalfact und lokalen Output verbunden. Zusätzlicher Resolver erforderlich und ausgeführt. Dies sind Definitionsreferenzen; ein nicht vorhandener konkreter UI-Instanzbezug wird nicht erfunden.

**X08 A/C537:** Derselbe konkrete Informationsinhalt hat eine ausdrücklich führende CEM-Quelle und abgeleitete Fact-/Outputwerte. Tatsächliche Quelldateiänderung, Konflikt, erneute Ableitung und erneute Originalvalidierung sind samt vorher/nachher-Hashes protokolliert. Der Binder führt eine selektive Konsistenzentscheidung aus, kein allgemeines uSpec-Governance-System.

initial-literal-derivation-run.cjs hält die erste eigene Setupfassung fest: Neue Kontrollwerte waren zunächst explizit gesetzt. Der positive Regenerationspfad wurde vor Übernahme auf ein tatsächliches erneutes Lesen der Fremdquellendatei und daraus berechnete Fact-/Outputwerte umgestellt. Dieselben14 Bedingungen, keine doppelte Zählung.

Keine ganze Canonical-/Figma-/LLM-Pipeline, kein beliebiger Fremdmodellresolver, kein neuer Produktstandard und keine konkrete Instanzruntime. Frühere unbekannte sourcePaths-/Alias-/Schema-Gegenbefunde bleiben Originalgrenzen. Reproduktion: prepare.py, run.cjs, unveränderte gebundene Geschwistermodule und Original-CEM-Schema; eigene Journale liegen bei jedem Fixture. Kein Commit/Push.
