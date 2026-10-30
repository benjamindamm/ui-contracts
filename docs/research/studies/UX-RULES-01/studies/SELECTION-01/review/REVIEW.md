# SELECTION-01 · Ergebnis und Grenzen

Die beiden frischen Builder folgen der eingefrorenen Projektpolicy: **A wählt Select bei drei Optionen, B Autocomplete bei 30 Optionen.** Das belegt deren begrenzte Anwendung bei diesem Kandidatenangebot, keine optimale UX-Auswahl. Select mit Suche war nicht definiert. Die nachfolgende fachliche Kritik ist berechtigt und führt zu [SELECTION-02](../../SELECTION-02/README.md), ohne Erstlieferungen oder Kriterien umzuschreiben.

| Befund | Ergebnis / Beleg |
| --- | --- |
| Primäre Wahl | Beide policykonform. Bei drei Optionen waren beide Kandidaten hart zulässig; Select war die gesetzte Präferenz. Bei 30 schloss der geforderte Suchbedarf das einfache Select aus. |
| Browser-Erstprüfung | 32 begrenzte Checks, 30 erfüllt; zwei ursprüngliche Fehler bleiben als Fehler gezählt. [Strukturiertes Ergebnis](results.json), [Rohbeobachtungen](browser-first.json). |
| B · SEL-B01 | Die vier generischen Input-Felder emittierten keine definierten value-change-Ereignisse. |
| B · SEL-B02 | Die lokale Erfolgsmeldung blieb nach einer Eingabeänderung veraltet sichtbar. |
| Separate Reparatur | Derselbe B-Builder korrigierte nur die neue Ausgabe [b-repair-01](../outputs/b-repair-01/REPORT.md). Die betroffenen Browserregressionen sind erfüllt; die Erstlieferung bleibt unverändert. [Reparaturbeleg](browser-repair.json), [Hashes](repair-delivery.json). |

## Tatsächlich ausgeführte Prüfung

Der Koordinator hat die lokalen Formulare in BrowserOS neo geöffnet und mit synthetischen Personendaten bedient. Native Select-Optionen, tatsächliche Filterung nach „Indien“, feste Schlüsselübernahme, unbekannte Eingabe, Tastaturnavigation, Fokus, ARIA-Zustände und Scrollsichtbarkeit der letzten Option wurden beobachtet. Kanada und USA bleiben trotz identischer Vorwahl +1 getrennte Schlüssel. Die Telefonnummer bleibt eine Zeichenkette mit führender Null; eine internationale Telefonnummernvalidierung ist damit nicht nachgewiesen. Die beobachteten Ressourcen blieben lokal; das ist kein vollständiger Sicherheitsnachweis.

Nach der Reparatur wurden die Input-Ereignisse, Auswahl, Stringerhalt und das Löschen alter Erfolgsmeldungen erneut geprüft. Der zusätzliche disabled/readOnly-Gegenfall löste synthetische DOM-Ereignisse aus; das war keine reale Bedienung eines deaktivierten Felds.

Alle drei TypeScript-Ausgaben wurden mit ES2020, DOM und DOM.Iterable unabhängig kompiliert; die erzeugten JS-Bytes stimmen mit den gelieferten überein ([Compilerbeleg](compiler-declared-checks.json)). Eine frühere Koordinatorprüfung ohne DOM.Iterable meldete bei der Reparatur TS2488. Dieser unvollständige Prüfumfang bleibt in compiler-checks.json erhalten und wird nicht als falscher Builderbericht gewertet.

## Herkunft und Unabhängigkeit

Zwei neue Subagent-Kontexte ohne Elternhistorie wurden angefordert. Quellen, Policy und Kriterien waren vorher eingefroren. decision.json lag laut Dateizeiten jeweils vor der ersten UI-Datei; diese Metadaten beweisen weder den Inhalt zum damaligen Zeitpunkt noch vollständige Prozessisolation. [Erstlieferungsbindung](first-deliveries.json) und [Studienregister](../study.json) führen die tatsächlich vorhandenen Belege. Modellidentität und ein vollständiges unabhängiges Pfadaudit liegen nicht vor. Der Reviewer war der Koordinator, kein zusätzlicher blinder Prüfer.

Der zuvor unveränderte 28-Datei-Bibliotheksstand wird unter prior-library bewahrt. Der ältere AC-UX-01-Pilot reproduziert dagegen weiterhin seine drei Regeln; die erweiterte Live-Bibliothek wird korrekt als andere Revision abgewiesen ([Nachweis](previous-pilot-reproduction.json)). Ältere Ergebnisse werden nicht aktualisiert.

## Was wir daraus verbessern

1. **Eignung ist relativ zum Angebot.** Die Wahl des einzigen suchfähigen Kandidaten rechtfertigt kein Urteil „bestes Control“. Die neue UX-Dokumentation trennt [Schreibhilfe und feste Auswahl](../../../../../../ux/AUTOCOMPLETE.md).
2. **Autocomplete ist kein eindeutiger Wertevertrag.** Die vorhandene Variante erlaubt eine freie Query, aber keine neuen bestätigten Ergebniskeys. Ein freier Adressmodus, der unbekannten Text akzeptiert, ist damit nicht definiert.
3. **Feste Werte und Suche getrennt modellieren.** Der neue Kandidat SelectWithSearch führt Suchtext separat vom nicht editierbaren Auswahlwert. Mitgliedschaft wird bei der Übernahme durchgesetzt, nicht ausschließlich durch Formularvalidierung.
4. **Hostanforderungen festhalten.** Pflichtfelder und die gemeinsame Anordnung von Vorwahl/Rufnummer waren nicht vollständig spezifiziert. A machte alle Felder erforderlich, B nur die Länderwahl; diese Unterschiede werden nicht nachträglich zu eingefrorenen Fehlerkriterien erklärt. Der Folgelauf präzisiert die Pflichtfelder.
5. **Tatsächliche Ereignisse und veraltete Meldungen prüfen.** Sichtbar ähnliche Formulare können diese Vertragsdetails unterschiedlich implementieren. Bericht und Erscheinungsbild allein reichen nicht.

Ein Builder je Bedingung, keine Ablation und keine randomisierte Zuordnung erlauben keine Kausalaussage, dass allein UX-Metadaten die Wahl verursacht haben. Die Suchgrenze >15 ist gesetzte Policy. Vollständige CEM-/SCXML-Vertragstreue, Screenreader, reale IME und native Plattformen sind nicht abgenommen. **release:false.**
