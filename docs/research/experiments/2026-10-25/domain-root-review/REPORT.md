# X01: Pflichtroot ist nicht automatisch eine zweite führende Fachquelle

Stand: 25. Oktober 2026. Begrenzter Quellenabgleich ohne neue Laufzeitbedingungen. **UXSpec X01 U/C200 und uSpec X01 U/C278 unverändert.** Nach dem getrennten XState-Versuch insgesamt40 U,443 Bedingungen/57 Gruppen.

[Originalstände und Hashes](source-review.json). UXSpec-Schema aus dem bisherigen gepinnten Originalbestand, uSpec component-contract.ts und types.ts erneut am unverändlichen Originalsnapshot über BrowserOS gelesen.

## UXSpec

Der Root verlangt $schema/$description/$machine. $visual ist optional: Behavior ohne Visual wird nicht durch eine gegenteilige Behauptung ausgeschlossen. Umgekehrt ist eine Visual-/Tokendatei ohne $machine kein selbständiges vollständiges UXSpec-Rootdokument. Das begrenzt den nativen Partialdokumentpfad, widerlegt aber nicht die Nutzung als eigenständigen Behaviorbeitrag neben anderen Originalsprachen. Der noch fehlende Nachweis ist eine solche konkrete kandidatenspezifische Bindung; das XState-Ergebnis wird nicht automatisch übertragen.

## uSpec

contractSchema verlangt api, structure, color, accessibility, dictionary und sourceModel neben Metadaten und Reconciliation. Die verschachtelten Confidence-/Coveragegruppen sind ebenfalls gemeinsam erforderlich. loadCanonicalComponentContract ruft validateCanonicalContract auf; ein fertiger Partialroot wird nicht durch einen alternativen dort sichtbaren Ladezweig akzeptiert.

Der Builder lädt dagegen ausdrücklich getrennte api-, dictionary-, structure-, color- und voice-Cachedateien sowie renderer evidence; anschließend erzeugt er aus deren semanticData einen gemeinsamen CanonicalComponentContract. sourceModel kommt aus Rendererbelegen, Quellenhash und Slug werden vor dem Aufbau verglichen. Getrennte Cachedateien sind real, ihre Fachgrenzen entsprechen jedoch nicht den gewünschten Interface/Visual/Behavior/Accessibility-Domänen. Ein eigenständiges Behaviorfachmodell ist in diesem Contractroot nicht definiert.

Die erforderlichen Felder können an vielen Stellen leere oder offene Werte enthalten. Aus bloßer Root-Optionalität oder ihrer Ablehnung folgt deshalb noch keine Aussage darüber, ob unabhängige führende Fachdefinitionen erhalten werden. Ebenso kann ein gemeinsam erzeugtes Ergebnis eine abgeleitete Sicht sein. Es wäre voreilig, allein aus required-Feldern eine globale Untrennbarkeit abzuleiten und X01 auf N zu setzen.

## Präziser Rest und nächste unabhängige Arbeit

UXSpec: den ursprünglichen Behaviorbeitrag mit eigenen Pflichtfeldern und tatsächlichem Compiler/Laufzeitgegenstand an drei unveränderte Fachbeiträge binden; XState-SDK-Typen oder eigene UXSpec-Reparaturfelder sind dafür kein Ersatz.

uSpec: die tatsächlich führende Cache-/Evidence-Quelle je fachlichem Inhalt sowie die Builderübernahme und zulässige Änderung bestimmen. Ein zusätzlicher Behaviorbeitrag müsste ausdrücklich extern bleiben. Diese Frage wird mit X08-Ownership behandelt, damit dieselben Rootdateien nicht wiederholt ohne neue Endbedingung gelesen werden. Keine endlose Suche nach hypothetischen Erweiterungen; die benannten ursprünglichen Pfade und ihre begrenzten Aussagen bleiben festgehalten.

Keine Umwertung, kein zusätzlicher Validator, keine neue Produktsprache und kein Commit/Push. Vollständiger Build und Cachevalidierung wurden in diesem Quellenabgleich nicht ausgeführt.
