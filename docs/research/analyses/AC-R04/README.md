# AC-R04 · Externe Ergebnisprüfung und nachträgliche PNGs

29. Oktober 2026. Prüfung von außen. [Originaler run-04](../../../../examples/autocomplete/reproducibility/run-04/README.md) unverändert; keine Neuerzeugung der FIGs, kein Commit/Push. Die PNGs und dieser Bericht sind spätere Ergänzungen und waren kein Teil der Erstlieferung.

## Urteil

**Brauchbares, im geprüften statischen Umfang sehr konsistentes Ergebnis.** Beide vorhandenen FIGs zeigen die zehn Fälle. Im extern erneut ausgeführten begrenzten Gegenprüfer: `PASS_LIMITED`, jeweils null Fehler/Warnungen; 572 von 572 verglichenen Beobachtungswerten stimmen überein. Beide setzen den disabled-Platzhalter auf den geforderten muted-Wert `#64748B`. Der bekannte Farbfehler ist in diesen Artefakten nicht vorhanden.

Auch die eigene Prüfkette des ursprünglichen Reviewers wurde erneut ausgeführt: 449/449 Checks je FIG; das gesamte JSON stimmt mit dem ursprünglichen Readback überein. Diese Wiederholung bestätigt die Reproduzierbarkeit dieses Prüfcodes, nicht unabhängig dessen vollständige fachliche Abdeckung. `check_process.py` liefert erneut `METADATA_COMPLETE`; das bedeutet vollständige Mindeststruktur und passende Hashes, keine bewiesene Prozessunabhängigkeit oder identifizierte Modelle.

## Sichtbare Ergebnisse

- [Builder A · PNG](previews/builder-a.png)
- [Builder B · PNG](previews/builder-b.png)

Direkt aus den gelieferten FIGs mit der gepinnten OpenPencil-Toolchain headless gerendert, Maßstab 1, transparenter Hintergrund. Die Originaldateien wurden nicht verändert. Die Seitengestaltung unterscheidet sich: A mit Zustandsbeschriftungen und anderer Anordnung, B mit gleichmäßigem Raster. Diese Freiheiten sind zulässig. Die Komponentenprojektionen wirken bei visueller Durchsicht konsistent; die letzten Optionen sind in scroll-end sichtbar. Das ist keine pixelgenaue Gleichheitsmessung, kein GUI-Speicher-Roundtrip und kein Nachweis echter Interaktion. Schriftdateien/Glyphmetriken wurden nicht zusätzlich qualifiziert.

## Was dieser Lauf zur Skillverbesserung belegt

| Beobachtung | Einordnung |
| --- | --- |
| Rollenkarten, hashgebundene Aufträge, Bootstraps und Handoffs vorhanden | Der organisatorische Einstieg und die Artefaktübergabe wurden genutzt. |
| Blindauftrag und spätere Reportphase getrennt dokumentiert; Erstbewertung an den Folgetask hashgebunden | Bessere nachvollziehbare Struktur. Zeit-/Zugriffsbehauptungen sind ohne unabhängige Sessionlogs nicht vollständig extern bewiesen. |
| Keine Unterbrechungen im Prozessmanifest | Positives dokumentiertes Prozessresultat; keine Ursache-Wirkungs-Aussage zur Kontextoptimierung. |
| Je Builder weiterhin eine Aufgabe für die gesamte Komponente, mit allen 22 Originaldateien plus technischem Laufblatt als Quellen | **Keine feinere fachliche Teilaufgabenzerlegung nachgewiesen.** Quellenzuordnung, minimale Lieferung und Verfeinerung sind nicht als eigene überprüfbare Zwischenlieferungen erhalten. |
| Zwei Erzeugungen, kein Kontrollarm mit gleichem Gesamtbudget | Explorative Wiederholung mit neuem Setup; kein abgeschlossener gestufter Pilot und kein kausaler Wirksamkeitsbeweis. |

Für diese Untersuchung sind weder mehr Agenten noch mehr Aufgaben an sich ein Erfolgskriterium. Entscheidend ist, ob benötigtes Wissen gezielt bereitsteht und einzelne Phasen an prüfbaren Lieferungen fortsetzen können. Das muss die nächste Untersuchung eigens erfassen.

## Befunde und Verbesserungen für die nächste Runde

| ID | Befund | Maßnahme / Status | Verbleibende Grenze |
| --- | --- | --- | --- |
| R04-001 | **Kein PNG geliefert.** Die Builderaufträge verlangen FIG, Readback, Report und Handoff, aber keine Bildvorschau. Beide erfüllten damit die dokumentierte Artefaktliste. | Zwei nachträgliche PNGs aus den Originalen erzeugt; Herkunft/Hashes in external-verification.json. Für zukünftige visuelle Ziele PNG oder vereinbartes alternatives Vorschauformat als ausdrückliches Abnahmekriterium aufnehmen. | Dies ist eine Lieferumfangslücke des Auftrags, kein nachgewiesenes fachliches Modellversagen. Die Vorschaupflicht muss im nächsten Auftrag vorab gelten. |
| R04-002 | Der Bootstrap ist klein, aber der tatsächlich gespeicherte Builderprompt hat 3.372 Zeichen, die anschließend gelesene Auftragsdatei 9.452 Zeichen und die Rollenkarte 1.550 Zeichen. Zusammen 14.374 Zeichen Text bei vollständiger Lesung, vor Fachquellen und Plattformvorgaben. | Größe hier separat erfasst. Künftig dünnere domänen-/schrittbezogene Aufträge mit nachladbarer Quellenkarte erproben; tatsächliche Read-Reihenfolge und Requestgrößen erfassen. | 986 Zeichen Bootstrap sind kein Anfangsbudget für den ganzen Modellrequest. Keine Tokenmessung und kein Beleg, dass 14.374 Zeichen ein Modell überfordern. |
| R04-003 | Originaler zusätzlicher Reviewer-Prüfcode blieb ausschließlich in einem Temp-Verzeichnis. Sein Ergebnis war gespeichert, die ausführbare Messkette im Run aber nicht dauerhaft enthalten. | Noch vorhandenen Code als reviewer-readback-preserved.mjs außerhalb des Runs gesichert und mit exakt gleichem Ergebnis wiederholt. Zukünftig Prüfscripte samt Inputs/Versionen dauerhaft referenzieren und hashen. | Die gesicherte Kopie ist ein nachträglicher Fund; ihre damalige Ausführung und damalige Codeidentität sind dadurch nicht unabhängig bewiesen. |
| R04-004 | „21/21 Claims bestätigt“ ist breiter als der ausgeführte Messumfang. Beispiel B3 enthält exakte Schattenparameter, der Readback vermerkt nur DROP_SHADOW und schließt Schatten ausdrücklich aus. B2 nennt paddingInline 12, ohne dass die eingefrorene Soll/Ist-Tabelle dessen Messung ausweist. | Aussagegenauigkeit im externen Bericht begrenzt: abgedeckte Teilbehauptungen bestätigt, weitere Teilwerte nicht durch diese Checks belegt. Für künftige Reportchecks Claims in atomare überprüfbare Teilbehauptungen teilen; checked/notChecked getrennt zählen. | Kein Beleg, dass diese Werte in den FIGs falsch sind. Es ist eine Grenze des dokumentierten Prüfbelegs, keine nachgewiesene Designabweichung. |
| R04-005 | Modellwerte sind bewusst nicht identifizierend; Kontext-/Werkzeugbudgets sind keine Token-/Gesamtschrittbudgets. Geladene globale Instruktionen und automatische Erinnerungen sind nicht separat nachgewiesen. | Vor nächstem Vergleich Modell-/Hostkonfiguration vom Betreiber festhalten, ohne Selbstrecherche des Modells zu verlangen. Konkrete Eingaben/Startladung getrennt von Dateiverweisen protokollieren. | Aus run-03s Nutzerangabe qwen3.8-27B FP8 darf run-04 nicht automatisch demselben Modell zugeschrieben werden. |

Die offene Meldungszeilenfarbe ist plausibel als nicht blockierende Definitionsfrage dokumentiert. Ein gewünschter muted-Wert wäre eine bewusste zukünftige Definitionsentscheidung, keine nachträgliche Reparatur dieses Runs.

## Nachweise und Erhalt der Originale

[Externe Gegenprüfung](external-countercheck.json) · [Externe Metadatenprüfung](external-process-check.json) · [Verifikation, Input- und PNG-Hashes](external-verification.json) · [Gesicherter ursprünglicher Reviewer-Code](reviewer-readback-preserved.mjs) · [PNG-Renderer](render-original.mjs).

Die ursprünglichen FIGs, Bewertungen, Handoffs und Reports wurden nicht überschrieben. Prüfergebnisse außerhalb dieses eng begrenzten statischen Umfangs bleiben offen: vollständige Geometrie/Scroll-Offsets, Schatten, Glyphmetriken, statische semantische Annotationen, GUI-Roundtrip, Runtime/ARIA sowie tatsächliche Zugriffstrennung. Kein allgemeines Komponentenrelease.
