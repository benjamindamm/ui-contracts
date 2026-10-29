# Pilotprotokoll · Gestufte Autocomplete-Erzeugung

**Planungsstand: 29. Oktober 2026 · Richtung beschlossen durch [RD-001](../decisions/RD-001-STAGED-GENERATION.md). Kein neuer Lauf gestartet.**

## Frage und Hypothese

Verbessern persistierte Teilübergaben und begrenzte, unabhängig geprüfte Reparaturrunden die Zuverlässigkeit eines weniger leistungsfähigen Modells bei gleicher Definition, Toolchain und Prüfpolicy?

Hypothese: Eine kompakte Quellenzuordnung mit Checkpoints senkt Kontext-/Übertragungsprobleme und erleichtert regelkonforme Korrekturen. Gegenhypothese: Die Übergaben kosten zusätzlichen Aufwand oder übertragen falsche Annahmen. Ergebnisqualität und Prozessstabilität werden deshalb getrennt bewertet.

Evaluationsgegenstand sind die [aktualisierten Skills und ihr Übergabevertrag](../../../skills/ui-contracts/references/workflow.md). Es geht nicht darum, schwächere Modelle lediglich mit mehr Agenten oder mehr Budget zu versorgen. Der Rollen-/Kontext-Helper ist implementiert und separat funktional geprüft; seine Version und Rollenaufträge müssen für beide Versuchsarme als zugängliche technische Grundlage festgehalten werden. Nur die kontrolliert variierte Nutzung der Zwischenübergaben gehört zur Prozessvariation.

## Feste und veränderliche Bedingungen

| Gemeinsam festzuhalten | Versuchsvariation |
| --- | --- |
| Dieselben 22 Definitionsdateien, SHA-256-Map und Revision `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`; gepinnter Werkzeug-Lock | Kontrollarm: zusammenhängender Builderauftrag; gestufter Arm: explizite Zwischenlieferungen und definierte Wiederaufnahmegrenzen. |
| Editierbares statisches OpenPencil, dieselben zehn Fälle | Die Strukturierung des Arbeitsablaufs, nicht der fachliche Umfang. |
| Modellrevision/Reasoning, Gesamtbudget, Werkzeughilfen, erlaubte Quellen und Reparaturfeedback | Prozessaufwand und Qualität als gemessene Ergebnisse. |
| Dieselbe unabhängig geprüfte Abnahmepolicy und dieselben Gegenfälle | Optional später ein anderes Modell, als gesonderter Block. |

Änderungen an Hilfsfunktionen, Eingabe oder Kriterien mitten im Vergleich erzeugen eine neue Versuchsbedingung. Keine nachträgliche Anpassung, um ein bestimmtes Modell bestehen zu lassen. Modelle erhalten in beiden Armen dieselbe aktuelle technische Dokumentation; historische Ausgaben und diese Auswertungen bleiben für die Builder gesperrt. Bekannte Regelbeispiele dürfen nur dann als neue Hilfe eingesetzt werden, wenn beide Arme sie identisch erhalten und das protokolliert ist.

## Mindestdesign des Pilots

Ein vorab festgelegtes Modell, **zwei unabhängige Erzeugungen je Arm**: vier Erstlieferungen. Reihenfolge der Arme vorab auslosen und speichern; jede Erzeugung startet mit leerem Gesprächskontext. Die Stichprobe ist explorativ, kein Signifikanz- oder allgemeiner Modellleistungsnachweis.

Der gestufte Arm verwendet die Stufen unten in einem Builderkontext mit expliziten Checkpoints. Ein notwendiger Sessionwechsel erhält nur freigegebene Originalquellen, eigenes Artefakt/Checkpoint und den unveränderten Auftrag; er wird als solcher dokumentiert. So werden nicht automatisch zusätzliches Modellwissen oder mehrere unabhängige Builder in eine einzelne Lieferung hineingemischt. Die Prüfung beider Arme wird getrennt vom Builder und mit derselben Policy durchgeführt.

Beide Arme erhalten nach eingefrorener Erstbewertung **höchstens zwei Reparaturrunden** mit demselben Diagnoseformat. Die Wirkung der Stufung wird an Erstlieferung und Prozess gemessen; Verbesserungen durch Reparaturen werden separat ausgewiesen. Ein stärkeres Modell ist im Primärvergleich nicht vorgesehen. Wird danach fachliche Eskalation gewünscht, gilt deren Ergebnis als „mit zusätzlicher Modellhilfe“, nicht als Primärerfolg des Ausgangsmodells.

Alte run-01/02/03 sind Kontext für die Forschung, keine gleichwertigen Kontrollarme: Prüfpolicy, Protokolle und Unterstützung unterscheiden sich.

## Vorbereitung: Gate P0

- [ ] Modell-ID/-Revision und Reasoning je Rolle sowie Harnessversion bestätigen. Unbekannte Angaben sichtbar lassen; keinen kontrollierten Modellvergleich behaupten, solange wesentliche Konfiguration fehlt.
- [ ] Vergleichspolicy versionieren und hashen. Der vorhandene [Zusatzchecker](../../../tools/design-review/README.md) ist eine Teilprüfung, keine vollständige Abnahme aller unten genannten Eigenschaften.
- [ ] Prüfabdeckung für Fallvollständigkeit, native Editierbarkeit, alle Teil-/Text-/Farb-/Geometriewerte, Popup-/Clipprojektion und statisches Scroll-Ende inventarisieren. Nichtautomatisierte Pflichten brauchen ein vorab vereinbartes manuelles Evidenzverfahren; ungeprüfte notwendige Felder blockieren den entsprechenden Konformitätsanspruch.
- [ ] Positive/negative Kontrollen aus R02-001 bis R02-006 bestehen lassen; neue Checktypen mit eigenen Gegenfällen abnehmen. Insbesondere richtiger/falscher Platzhalter, alle Optionsschriften, Konturstärke und Reports gegen Readback prüfen.
- [ ] Rolle statischer Accessibility festlegen: bereits explizit verlangte sichtbare Projektionen prüfen; zusätzliche native Semantik nur mit vereinbartem, tatsächlich roundtrip-geprüftem Kanal. Andernfalls keine pauschalen ARIA-Pass-/Failzählungen daraus erzeugen.
- [ ] Technische Helper dokumentieren und in beiden Armen identisch bereitstellen. Sie dürfen Token auflösen, native Elemente/Export/Readback bedienen und Messungen liefern; keine fertig gestaltete Autocomplete-Lösung oder frühere Generatoren als versteckte Vorlage enthalten.
- [ ] Quellenkarte- und Checkpointvorlage, Auftragswortlaut, erlaubte Dateipfade, Reviewerzugang und Budgetpolicy einfrieren.

Ohne dieses Gate bleibt der Pilot **vorbereitet, nicht gestartet**. Das Dokument ist noch keine vollständig numerisch präregistrierte Abnahme, weil Teile der Messabdeckung und tatsächliche Providerlimits erst bereitgestellt werden müssen.

## Gemeinsamer Datenrahmen

Eine neue Lauf-ID erst bei tatsächlichem Start vergeben; `run-04` wird nicht durch dieses Planungsdokument als ausgeführt markiert. Bestehende Top-Level-Struktur erhalten: `run.json`, `README.md`, `builder-a/`, `builder-b/`, `review/`. Weitere Versuchsarme über eigene Laufordner und ein gemeinsames Experimentmanifest verbinden, statt alte Ergebnisse zu überschreiben.

Jeder Builder erhält eigene Unterordner für `handoffs/`, `checkpoints/`, `initial/` und `repairs/01`, `repairs/02`. Zusatzpfade im Laufmanifest erklären. Eine fehlgeschlagene oder partielle Erstlieferung bleibt als Ergebnis vorhanden, statt durch die letzte Datei ersetzt zu werden. Reviewdateien eindeutig an Artefakt-SHA-256, Policy- und Werkzeugstand binden.

### Quellenkarte: Stufe 1

Pro Regel/Fall/Teil mindestens:

```json
{
  "source": {"path": "components/autocomplete/layout.css", "sha256": "HASH", "selector": "[data-part=\"input\"]::placeholder"},
  "target": {"component": "ui-contracts:Autocomplete", "instance": "disabled", "part": "input", "facet": "placeholder.color"},
  "valueFrom": "components/tokens.json#autocomplete.muted",
  "classification": "explicit",
  "openQuestion": null
}
```

Dies ist ein Vorschlag für ein **Arbeitsformat**, kein neuer Standard. Die Originalquellen bleiben führend. Koordination prüft Hashbezug, alle zehn Fälle und Teilzuständigkeiten; fachliche Unsicherheit wird als offene Frage weitergegeben. Eine Interpretation darf nicht allein durch wiederholtes Abschreiben verbindlich werden.

### Minimale vollständige Lieferung: Stufe 2

Anatomie und sämtliche geforderten Fälle mit einfachen nativen Elementen anlegen; dann Datei exportieren und erneut öffnen. Texte, Farben und Geometrie aus den Originalquellen übernehmen. Ein frühes Readback-Gate sichert Lesbarkeit und Vollständigkeit, **nicht** die Freigabe aller Details. Danach verfeinern, ohne schon erfüllte Regeln zu verlieren. Die Reihenfolge darf technische Abhängigkeiten berücksichtigen.

Technische Nachweise: Artefakthash, Reader-/Writerstand, vorhandene Fälle/Teile, Exportfehler und verbleibende Aufgaben. Keine bloße „alles erfüllt“-Selbstauskunft. Tokens als Werte referenzieren/auflösen oder kopierte Werte ausdrücklich gegen die führenden Tokens prüfen.

### Unabhängige Prüfung und Reportabgleich: Stufe 3

1. Die gelieferten Originaldateien erneut lesen und rendern; keine Messwerte ungeprüft aus Builderberichten übernehmen.
2. Jeden abgedeckten Pflichtwert mit Sollquelle und Toleranz prüfen. Native Werte, sichtbare Rasterung und erlaubte Gestaltung getrennt bewerten.
3. Erstbewertung einfrieren, bevor Reparaturfeedback gegeben wird. Erfüllung, Abweichung, ungeprüft und unentscheidbar getrennt führen.
4. Anschließend jeden konkreten Reportclaim gegen Artefakt/Receipt abgleichen; ein Widerspruch bleibt unabhängig von der visuellen Qualität ein eigener Befund.
5. Paarvergleich auf demselben dokumentierten Merkmalsumfang berechnen. Keine frei gewählten Namen/Seitenpositionen als Konformitätsfehler und keine Übereinstimmung als Korrektheitsbeweis werten.

### Diagnose und Reparatur: Stufe 4

Jede Diagnose enthält `issueId`, Datei-/Artefakthash, Fall/Teil/Node, führende Quelle, Soll, Ist, Prüfmethode und betroffene Regressionen. Nur festgestellte Fehler und tatsächlich offene Fragen melden; nicht mit einem vollständig vorgegebenen Design nachcoachen.

Der Builder erzeugt eine neue Revision; Generator, Datei und Bericht bleiben konsistent. Anschließend Fehler und betroffene Regressionen erneut prüfen. Bei demselben ungeklärten Befund nach zwei Reparaturrunden, fehlender Fähigkeit des Zieladapters oder Widerspruch der Quellen endet der Primärlauf als **nicht vollständig erfüllt / blockiert im benannten Umfang**. Ein zusätzlicher Expertenentscheid wird außerhalb dieses Ergebnisses dokumentiert.

## Kontext-, Anfrage- und Wiederaufnahmepolicy

Das nominelle Kontextfenster des Modells ist kein sinnvoller Füllstand und kein Nachweis der erlaubten HTTP-Anfragegröße. Vor dem Pilot die tatsächliche Provider-/Gatewaykonfiguration und Fehlerdiagnostik aufnehmen. Die Grenzwerte können nicht aus „256K Kontext“ abgeleitet werden.

**Festgelegte lokale Pilotkonvention:** Werkzeugausgaben zunächst auf höchstens 8.000 Zeichen pro Rückgabe begrenzen; vollständige Dumps in Dateien ablegen und gezielte Ausschnitte nachladen. Das ist eine Arbeitskonvention, kein behauptetes Providerlimit. Bei Überschreitung nicht still abschneiden: Pfad, Gesamtgröße und Ausschnittsgrenze melden. Bilder einzeln und nur bei einer konkreten visuellen Frage laden.

Vor dem Lauf ein gleiches **Gesamtbudget** je Erzeugung und Reparaturphase festlegen; Stufung darf nicht durch unbegrenzt zusätzliche Sessions mehr Budget erhalten. Checkpoint möglichst bei 75 % des vereinbarten Schrittbudgets. Token-/Bytebudgets aus tatsächlichen Messungen und Providergrenzen ableiten und im Experimentmanifest eintragen, bevor Qualitätsdaten verglichen werden. Kein universeller Grenzwert wird hier erfunden.

Für jeden Fehler Ursache unterscheiden: Schrittlimit, HTTP 413, Kontextlimit laut konkreter Providerantwort, Timeout, Rate-Limit oder fachlicher Fehler. Bei 413 dieselbe Anfrage nicht blind wiederholen. Antwortcode, bereinigten Fehlertext, Requestbytes, geschätzte/gezählte Tokens, Zahl/Größe der Werkzeugausgaben und Bilder sowie Modell-/Gatewayroute erfassen. Keine Tokens, Schlüssel oder Zugangsdaten protokollieren. Fehlt eine Messgröße, bleibt sie unbekannt.

Ein verlorener Kontext wird durch persistierte eigene Übergaben wiederaufgenommen. Ein rekonstruierter Abschlussbericht wird ausdrücklich als Rekonstruktion ausgewiesen und am Artefakt geprüft. „Fortsetzung gleicher Session“ und „frische Session mit Checkpoint“ sind verschiedene Prozessereignisse.

## Messgrößen und Entscheidungsregeln

| Dimension | Zu speichern / auszuwerten |
| --- | --- |
| Erstleistung | Lieferung vollständig oder partiell; belegte explizite Regelverletzungen; ungeprüfte Pflichten; Reportwidersprüche. |
| Endleistung | Gleiche Größen nach maximal zwei Reparaturrunden; neu entstandene Regressionen; externe Hilfe separat. |
| Zuverlässigkeit | Anzahl und Ursache der Abbrüche, erhaltene Checkpoints, erfolgreiche Wiederaufnahme, verlorene/rekonstruierte Arbeit. |
| Aufwand | tatsächliche Schritte, Tokens/Requestbytes soweit verfügbar, Zeit und Reparaturrunden; unbekannte Werte nicht als null Aufwand. |
| Konsistenz | Unterschiede im gemeinsam definierten Eigenschaftssatz und erlaubte Freiheiten; gemeinsamer Fehler separat. |
| Nachvollziehbarkeit | Rollen-/Prompt-/Skill-/Quell-/Artefakthashes, Policy und Prozessereignisse vollständig oder konkrete Lücke. |

Ein gutes statisches Endergebnis erfordert keine beobachteten expliziten Verletzungen **im vollständig abgedeckten vereinbarten statischen Umfang**. Fehlende notwendige Prüfung verhindert diese Aussage. Allgemeine Produktions-, Runtime- oder Accessibilityfreigabe bleibt ausgeschlossen. Ein Modell kann brauchbare Ergebnisse liefern, ohne jedes Kriterium zu erfüllen; Nutzbarkeit und exakte Konformität werden weiterhin getrennt berichtet.

Die Entscheidung über Weiterentwicklung folgt aus der Gegenüberstellung: weniger Verletzungen/Abbrüche bei vergleichbarem Budget und vertretbarem Reparaturaufwand stützen die Hypothese; bloße Verbesserung nach mehr Hilfe tut das nicht. Bei gemischten Ergebnissen keine allgemeine Modellrangfolge ziehen, sondern Fehlerklassen und Prozessengpässe benennen. Der kleine Pilot liefert deskriptive Evidenz, keine statistisch abgesicherte Überlegenheit.

## Übertragung auf die nächste komplexere Komponente

Erst nach dem Pilot eine Komponente mit zusätzlicher echter Komposition wählen. Auswahlkriterien: mindestens zwei Teilverträge, mehr als eine relevante Zustandsachse sowie Fehler-/Abbruch- oder asynchrone Übergänge. Die Wahl ist offen; hier wird keine neue Komponente erfunden oder implementiert.

Kompositionsfälle aus den Verbindungen ableiten: Wer besitzt Zustand und Wert? Welche Events überschreiten Teilgrenzen? Was passiert bei verzögerter Antwort, Schließen, erneutem Öffnen, Fokuswechsel und Scrollgrenze? Pro Verbindung normale Übergabe und relevanten Fehlerfall prüfen. Risikobasierte Auswahl und ausdrücklich ausgelassene Kombinationen dokumentieren; keine vollständige kartesische Zustandsabdeckung behaupten. Native Interaktionsnachweise bleiben ein eigener späterer Auftrag.

## Aufgabenstatus

- [x] Richtung beschließen und historisch abgrenzen.
- [x] Stufen, Übergaben, Kontrollbedingung, Reparaturrahmen und Messgrößen festlegen.
- [x] Fokussierte Rollen-Karten, Auftrags-/Übergabevertrag und Kontext-/Integritätshelper implementieren; Funktionstests bestehen. Wirkung auf echte Modellarbeit noch nicht bewertet.
- [ ] Gate P0: vollständigen gemeinsamen statischen Prüfumfang und neutrale technische Helper vorbereiten.
- [ ] Modell-/Rollen-/Budgetdaten und genaue Aufträge einfrieren; technische Anfragegrößenprobe durchführen.
- [ ] Pilot mit vier Erstlieferungen und begrenzten Reparaturen auf ausdrücklichen Ausführungsauftrag starten.
- [ ] Ergebnisse extern auswerten und Fehlerregister fortschreiben.
- [ ] Danach komplexere Komponente wählen und Übertragbarkeit separat prüfen.

## Ergänzung: Einstiegskontext messen

[Audit INITIAL-CONTEXT](../analyses/INITIAL-CONTEXT/README.md) ist Teil der Vorbereitung. Start- und Nachladestufen separat protokollieren: Historienübernahme, Plattform-/Toolvorgaben soweit verfügbar, aktiver Skill, Bootstrap, Auftrag/Rollenkarte, später gelesene Pfade und Werkzeugausgaben. Bootstrapgröße ist kein Gesamtrequestmaß. In beiden Armen dieselben gemeinsamen Mess-/Toolbedingungen wahren; die unterschiedliche Kontextaufteilung als Intervention dokumentieren. Fehlende Requestdaten als fehlend ausweisen.

Host-Einstiege zusätzlich nach [ENTRYPOINTS](../analyses/INITIAL-CONTEXT/ENTRYPOINTS.md) prüfen: Agentenprogramm/Version, geladene Regeldateien, globale Erinnerungen, Imports und tatsächliches Initialset separat vom Modellnamen dokumentieren. Die neuen Repositorywegweiser sind statisch geprüft; Host-Laufzeittests bleiben Vorbereitung für P0.
