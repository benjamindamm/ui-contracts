**Aktueller Stand – 25. Oktober 2026:** 41 offene Nachweise (26 Integration, 15 weitere), 435 benannte Prüfbedingungen in 56 Gruppen. Vollständige Integration, Produkt-UI und Assistenztechnik sind weiterhin nicht nachgewiesen; statische HTML-Host-Fixtures wurden inzwischen im Browser geprüft. Historische Zahlen und „nicht ausgeführt“-Aussagen unten beziehen sich auf die jeweils benannte frühere Runde. Maßgeblich ist das [aktuelle Register](OPEN-FIELDS.md).

# Originalschema und Werkzeug: drei gezielte Folgeprüfungen

Stand: 24. Oktober 2026. [Quellen S61](SOURCES.md#s61), [Befunde C402–C404](CLAIMS.md#c402). Prüfung der Zelle X06 für OpenUI, Google DESIGN.md und Panda CSS. Manuelle Quellprüfung, keine Installation oder ausgeführte Validierung.

| Kandidat | Positiv belegt | Grenze | Ergebnis |
| --- | --- | --- | --- |
| OpenUI | Feldkatalog, TS-Interface und HTML-Tabellenrenderer vorhanden | Abweichende Definitionsformen; Tabellenrenderer prüft kein Contractdokument. Kanonisches ausführbares Originalschema und Werkzeug weiterhin nicht belegt | X06 bleibt U |
| Google DESIGN.md | Öffentlich exportierte lint-Library mit Parser-, Modell- und Regelprüfung | Das Zod-Eingabeschema prüft den Textwrapper, nicht vollständig den fachlichen YAML-Vertrag. Rückkehr eines Berichts ist kein Konformitätsbeweis | X06 bleibt U |
| Panda CSS | parseDesignSystem liest den normalisierten Export und prüft ausgewählte Rootbedingungen | Tabellenformen und Zeilen werden nur teilweise beziehungsweise gar nicht geprüft; kein vollständiger fachlicher Validator daraus | X06 bleibt U |

## Nachvollziehbare Negativfälle für später

**OpenUI:** Ein künftiger offizieller Prüfer muss klären, welche Definition für license/group und enum/required maßgeblich ist. Ein selbst angeglichener Typ wäre bereits eine neue Projektentscheidung.

**Google:** Ein recoverable Parsefehler liefert im gelesenen Librarypfad einen Warnungsbericht mit leerem Modell. Die spätere Abnahme muss Findings und erwartete Inhalte auswerten. Daraus wird kein CLI-Exitcode abgeleitet.

**Panda:** Für das folgende absichtlich beschädigte Dokument ergibt der gelesene Kontrollfluss die Erwartung, dass der flache Reader es akzeptiert. **Damals nicht ausgeführt; inzwischen mit Originalfunktionen geprüft:** [18 Folgefälle](experiments/2026-10-25/panda-reader/REPORT.md). Die Werte categories/tokens sind vorhanden und nicht null, die geforderten Arrays und die numerische Version erfüllen die tatsächlich gelesenen Rootchecks:

```json
{"schemaVersion":1,"categories":7,"paths":[],"tokens":false,"values":[]}
```

Dieser Fall demonstriert auf Papier die Grenze des untersuchten Readers. Er beweist weder die Abwesenheit anderer Panda-Prüfungen noch eine erfolgreiche oder fehlgeschlagene Ausführung.

## Konsequenz für die Integration

Originalformat, Schema, offizielles Werkzeug, Codequalitätsprüfung und Ausgabereader werden einzeln erfasst. Vorhandene Teilprüfungen sollen erhalten bleiben. Ergänzungen erhalten eigene Herkunft und werden nicht als unverändertes Originalschema ausgegeben.

**Fortschritt:** Drei weitere offene Felder gezielt nachgeprüft und präzisiert, keine neue Abdeckungsumwertung. Es verbleiben 72 U-Zellen, darunter neun X06-Zellen. Als nächste Werkzeugfragen sind Ark UI, Zag und XState im Register geführt. Der Vergleich von Beschreibungssprache und Reifegrad bleibt zusätzlich offen.

## Ausgeführte Panda-Fortschreibung, 25.10.2026

[Originalreader und Index](experiments/2026-10-25/panda-reader/REPORT.md): 18 vorher festgelegte Fälle bestätigen die bewusst begrenzte Prüfung. Die alte Schlusszahl 72 beschreibt den damaligen Stand; aktuell 61 U. X06 bleibt U/C442.

## Ausgeführter Google-Folgeblock, 25.10.2026

[20 Original-Libraryfälle](experiments/2026-10-25/google-linter/REPORT.md) prüfen Warnungsreports, fachliche Modellregeln und tatsächlich erfasste Referenzen. Vier Hauptlauferwartungen widerlegt; Diagnosefälle bestätigen die begrenzte Komponentenpfadprüfung. X06 bleibt U/C443.
