# Aufgaben und Fortschritt

Stand: 24. Oktober 2026. Diese Liste ist die zentrale Übergabe für die weitere Arbeit. Sie unterscheidet Forschungsfortschritt von der Übernahme ins Projekt. Maßgeblich für „erledigt“ sind gespeicherte Ergebnisse in [Matrix](docs/research/MATRIX.md), [Begründungen](docs/research/CLAIMS.md), [Quellen](docs/research/SOURCES.md) und [Prüfregister](docs/research/study.json).

## Aktueller Stand

**10 von 16 Kandidatenprüfungen sind übernommen und abgehakt; 6 sind noch offen.** Die Drei-Agenten-Runde für AgentsORG, UXSpec und Ark UI ist abgeschlossen und zentral in Matrix, Begründungen, Quellen und Prüfregister gespeichert. Eine übernommene Prüfung kann weiterhin einzelne U-Fragen enthalten; sie ist kein Nachweis vollständiger Integration oder produktiver Eignung.

| Status | Anzahl | Bedeutung |
| --- | ---: | --- |
| Übernommen | 10 | Vertiefung mit Quellen, Begründungen und konkreten offenen Fragen im Projekt gespeichert |
| Bericht vorhanden, Übernahme fehlt | 0 | Kein ausstehender Bericht dieser Runde |
| Begonnen, Abschluss fehlt | 0 | Keine verbleibende Kandidatenprüfung dieser Runde |
| Offen | 6 | Vertiefte Kandidatenprüfung steht noch aus |
| **Gesamt** | **16** | **6 Kandidaten benötigen noch Arbeit bis zur Übernahme** |

## Abgeschlossene Drei-Agenten-Runde

| Kandidat | Ergebnis | Verbleibende U-Fragen |
| --- | --- | --- |
| AgentsORG | 20 von 22 offenen Feldern geklärt | X01, X08 |
| UXSpec | 12 von 17 offenen Feldern geklärt | V04, V05, V06, X01, X03 |
| Ark UI | 21 von 24 offenen Feldern geklärt | X01, X03, X06 |

Die Zahl der erledigten Kandidaten wurde erst nach tatsächlicher zentraler Übernahme erhöht. Es läuft keine weitere Kandidatenprüfung als Teil dieser Runde. Schema-/Linter-/Compilerbefunde sind Dokumenten-/Quelltextnachweise, keine Praxisversuche.

## Kandidaten zum Abhaken

Die Reihenfolge entspricht der bestehenden Kandidatenliste. Ein Häkchen bedeutet ausschließlich „übernommen“.

| Erledigt | Kandidat | Status | Nächste konkrete Aktion |
| --- | --- | --- | --- |
| [x] | CEM | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [x] | OpenUI | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [x] | Google DESIGN.md | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [x] | AgentsORG | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [x] | DTCG | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [x] | UXSpec | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [x] | SCXML | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [x] | XState | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [x] | Zag | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [x] | Ark UI | Übernommen | Verbleibende U-Fragen nur bei gezieltem Folgeauftrag bearbeiten |
| [ ] | Panda CSS | Offen | Vertiefte Prüfung der offenen Matrixfelder gegen Primärquellen |
| [ ] | uSpec | Offen | Vertiefte Prüfung der offenen Matrixfelder gegen Primärquellen |
| [ ] | OpenPencil | Offen | Vertiefte Prüfung des benannten Behaviour-Beitrags gegen Primärquellen |
| [ ] | WAI-ARIA | Offen | Vertiefte Prüfung des Semantikbeitrags getrennt von APG |
| [ ] | APG | Offen | Vertiefte Prüfung der Patternanforderungen getrennt von WAI-ARIA |
| [ ] | CSS Layout | Offen | Anchor Positioning und Overflow als getrennte Beiträge vertieft prüfen |

### Zählhistorie und gesicherte Vorarbeit

Die frühere Meldung „zehn übernommen, sechs offen“ war damals verfrüht. Nach dem jetzigen Abschluss ist dieser Stand tatsächlich erreicht. AgentsORGs vorhandener Bericht wurde gezielt gegengeprüft; UXSpec-Vorarbeit gesichert und vervollständigt; für Ark UI war kein vorheriger vollständiger Webbericht belegt. Temporäre Berichtspfade sind keine Dauerablage: Primärquellen und Ergebnisse sind jetzt in den vorhandenen Forschungsdateien gesichert.

Bei UXSpec gilt der aktuelle 26-Zeilen-Katalog mit neun vorher bewerteten und siebzehn zuvor offenen Feldern. Die ältere Chatangabe „19/27“ wurde korrigiert, nicht weitergezählt.

## Nächste Arbeitsschritte

- [x] AgentsORG-Bericht gegen Kriterien und Primärquellen prüfen und in die vorhandenen Forschungsdateien übernehmen.
- [x] UXSpec-Vorarbeit wiederfinden, verbleibende Prüfung abschließen und übernehmen.
- [x] Ark-UI-Vorarbeit wiederfinden, verbleibende Prüfung abschließen und übernehmen.
- [ ] Danach die sechs noch offenen Kandidaten in der vorhandenen Reihenfolge bearbeiten.
- [ ] Den vorgemerkten Zusatzvergleich zu **Originalschema und tatsächlichem Validierungstooling**, **Beschreibungsformat und zusätzlich nötigem Code** sowie **Reifegrad und Kompatibilität** vervollständigen. Teilbefunde für OpenUI, Google DESIGN.md, AgentsORG, UXSpec und Ark UI liegen vor; dies ist noch kein abgeschlossener Vergleich aller Kandidaten.
- [ ] Die beiden bestätigten Detailvergleiche gezielt vervollständigen: DESIGN.md gegen deklarative Layoutmodelle und UXSpec gegen SCXML.
- [ ] Gemeinsame Referenzen, Komponentenkomposition und Ownership anhand der verbleibenden Integrationsfragen zusammenführen.

Diese Liste hält Aufgaben fest und startet keine Recherche, Implementierung, Tests oder Skill-Erstellung. Spätere praktische Versuche benötigen einen entsprechenden Arbeitsauftrag; bisherige Recherchebefunde sind keine Laufzeitnachweise. Weitere Einzelheiten stehen in der [Forschungsplanung](docs/research/RESEARCH-PLAN.md).

## Pflege bei jeder Fortsetzung

1. Vor Arbeitsbeginn Status und vorhandene Ergebnisse lesen; bereits vorhandene Berichte zuerst nutzen.
2. Bei tatsächlichem Beginn den Kandidaten von „Offen“ auf „Begonnen“ setzen und die überprüfbare Arbeitsreferenz ergänzen.
3. Erst nach Vorliegen eines vollständigen Berichts auf „Bericht vorhanden“ setzen. Eine laufende Recherche oder mündliche Zwischenmeldung genügt nicht.
4. Erst nach zentraler Gegenprüfung und tatsächlichem Speichern in Matrix, Begründungen, Quellen und Prüfregister auf „Übernommen“ setzen und abhaken.
5. Gleichzeitig die Statuszahlen oben und diese Arbeitsschritte aktualisieren. Nicht aus einer geplanten Übernahme auf eine erledigte Aufgabe schließen.
6. Commit und Push sind getrennte Aktionen; ein neuer Arbeitsfortschritt wird durch diese Liste nicht automatisch dafür freigegeben.
