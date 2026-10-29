# Reproduzierbarkeitsversuch 03

Zwei neue Agenten bauen unabhängig voneinander ein editierbares OpenPencil-Design aus derselben eingefrorenen Autocomplete-Definition. Ein dritter Agent ohne übernommenen Gesprächskontext leitet vorab Prüfkriterien aus der Definition ab und vergleicht anschließend beide Originaldateien mit der Definition und miteinander.

Dieser Lauf wurde bewusst ohne Kenntnis der Ergebnisse früherer Läufe durchgeführt. Eingabe, Kriterien und Annahmen wurden frisch gebildet; frühere Läufe, frühere Designs und Research-Dokumente waren für beide Builder und den Prüfer gesperrt. Alle Rollen liefen als getrennte, frische Subagent-Sessions.

## Gleiche Eingabe, getrennte Arbeit

[run.json](run.json) bindet alle 22 Definitionsdateien, die Definitionsrevision und den Werkzeug-Lock. Die Revision `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727` wurde beim Start unabhängig aus `components/` nachgerechnet (SHA-256 über das kompakte, sortierte Pfad→Hash-Objekt); Werkzeug-Lock `ebdba852…` und alle 22 Einzelhashes stimmen mit den Builder-Manifesten überein.

Die Builder haben denselben Auftrag, jeweils einen eigenen Ausgabeordner und keinen Zugriff auf frühere Designs oder die Ausgabe des anderen. Die Kontextübernahme ist bei allen drei Agenten deaktiviert. Die Dateigrenzen sind Auftragsvorgaben, keine zusätzliche Dateisystemsandbox. Gleiche Modelle können gemeinsame blinde Flecken haben; ein universeller statistischer Unabhängigkeitsnachweis wird nicht behauptet.

## Modellkonfiguration

Alle Rollen erben die Modell-/Reasoning-Konfiguration des aufrufenden Systems (OpenCode, `local:default`). Exakte Modellrevision, Samplingparameter und Seeds werden von der verwendeten Agentenschnittstelle nicht als verifizierbare Laufmetadaten zurückgegeben und bleiben deshalb unbestimmt. Keine Modellwahl wurde je Rolle vorgeschrieben; es wird keine unterschiedliche Modellkonfiguration und keine statistische Unabhängigkeit ihrer Fehler behauptet.

## Ablauf

1. Eingabeversion unabhängig prüfen und Hashes einfrieren (22 Dateien, Revision, Werkzeug-Lock).
2. Der Prüfer leitet aus der Definition allein 91 Kriterien ab (74 explizit, 10 abgeleitet, 7 unterbestimmt) und speichert sie, bevor er eine Builder-Ausgabe sieht.
3. Kriterien hashen und [versiegeln](review/preregistration-seal.json); Versiegelung von der Koordination unabhängig nachgeprüft.
4. Beide Builder erstellen echte editierbare Dateien, Vorschau und Bericht.
5. Der Prüfer misst zuerst die Originaldateien selbst, dann liest er die Builderberichte.
6. Vergleich auf Komponentenebene; Unterschiede werden als Verletzung, erlaubte Freiheit oder unzureichend bestimmte Regel eingeordnet.

## Unterbrechungen und Provenienz

Während des Laufs fiel der Modellanbieter mehrfach mit HTTP 413 (Anfrage zu groß) aus. Die Auswirkungen sind vollständig in [run.json](run.json) (`interruptions`, `interruptionImpact`) sowie im [Prüfbericht](review/REVIEW.md) und in [results.json](review/results.json) dokumentiert.

| Akteur | Stopp | Stand beim Stopp | Fortsetzung |
| --- | --- | --- | --- |
| Builder A | 1 | alle 6 Artefakte geschrieben, `REPORT.md` fehlt | `REPORT.md` von einer neuen Session mit Zugriff nur auf die vorhandenen Artefakte, `components/` und die gepinnte Werkzeugumgebung |
| Prüfer | 2 | Phase-2-Vorlauf: `inspect-original.mjs`/`render-original.mjs` geschrieben und ausgeführt | nächste Session |
| Prüfer | 3 | kurzer Vorlauf (Berichte gelesen, Skripte erneut ausgeführt) | nächste Session |
| Prüfer | 4 | komplette Messkette ausgeführt (`verify.py`-Vorlauf, Kriterienergebnisse), Bericht nicht fertig | finale Session: Vorlauf-`verify.py` gegen das versiegelte Kriterienset auditiert (3 dokumentierte, judgments-neutrale Anpassungen, Altfassung als `verify.py.prev-1216` erhalten), gesamte Messkette neu ausgeführt (Status identisch, 182/182), Bericht geschrieben |

Ursache war ausschließlich der Providerfehler, kein Zugriff auf verbotene Eingaben. Keine Rolle sah frühere Läufe, fremde Ausgaben oder Research-Dokumente; die Sessionprotokolle wurden auf Pfadebene geprüft (siehe `accessAudit` in [run.json](run.json)).

**Provenienz-Limitationen (ausgewiesen im Prüfbericht):**
- Prüfer-Phase 1 (Kriterien) und Phase 2 (Vergleich) liefen in getrennten technischen Sessions; die finale Phase-2-Session arbeitete ausschließlich vom versiegelten Kriterienset. Die Kriterienableitung selbst ist dadurch nicht gegenprüfbar.
- `REPORT.md` von Builder A stammt aus einer zweiten Session (Rekonstruktion aus den Artefakten); alle Aussagen des Berichts wurden vom Prüfer eigenständig gegen die Artefakte verifiziert.
- Der Lauf belegt keinen ununterbrochenen Ein-Schuss-Durchlauf; die Aussagekraft für Prozess-Reproduzierbarkeit (Single-Shot, Schrittanzahl) ist dadurch begrenzt. Die Bewertung der gelieferten Artefakte und die Kontexttrennung sind davon nicht berührt.

## Ergebnis

| | Design A | Design B |
| --- | --- | --- |
| Gesamturteil | **Substanziell erfüllt** | **Substanziell erfüllt** |
| erfüllt / verletzt / nicht anwendbar | 79 / 5 / 7 | 78 / 6 / 7 |
| explizit verletzt | 5 | 6 |
| abgeleitet verletzt | 0 | 0 |

Beide Designs erfüllen alle geometrischen, typografischen, textlichen, farb- und strukturell relevanten Kriterien; die zehn Fälle, Maße, Texte, Clipping- und Editierbarkeitswerte stimmen in beiden Originaldateien überein.

Gemeinsame Verletzungen (beide): E-063, E-064, E-065, E-070, E-071 — die ARIA-Werte der Definition liegen in keinem Artefakt als lesbare Annotation vor (keine maschinenlesbare Annotation im `.fig`-Format dieser Toolchain; A führt 3/4 Rollenwerte als Layer-Namen, B 2/4).

Nur bei B: E-041 — im disabled-Fall zeigt B den Platzhalter in `#94A3B8` (Token „disabled“) statt muted `#64748B`; A zeigt `#64748B`. B-REPORT dokumentiert die gegenteilige Entscheidung — dokumentierter Report↔Artefakt-Widerspruch. Hintergrund ist das spannungsbehaftete CSS-Paar `::placeholder` vs. `:disabled` in der Definition, das in der Preregistrierung nicht als unterbestimmtes Kriterium erfasst wurde.

Die gemessene Paarübereinstimmung beträgt **1145/1208 Wertepaare = 94,78 % (Band 90–95 %)** über die normalisierten Komponentenwerte; auf kriterienrelevante Werte 100 % mit der einen Ausnahme (disabled-Platzhalterfarbe, nur bei B). Hohe Übereinstimmung bedeutet gleiche Lesart der Definition, nicht automatisch Korrektheit.

Vollständige Befunde, Messwerte und Grenzen: [Prüfbericht](review/REVIEW.md) · [Ergebnisdaten](review/results.json) · [Einzelbeobachtungen](review/native-checks.json) · [Kriterienergebnisse](review/criterion-results.json) · [Paarvergleich](review/pair-comparison.json) · [Hashes](review/hashes.json).

## Ablage

Die Struktur entspricht den vorherigen Läufen: `run.json`, `README.md`, `builder-a/`, `builder-b/`, `review/`. Alle vorherigen Pfade sind vorhanden; ergänzende Dateien sind hier dokumentiert: `builder-a/preview.svg` und `builder-b/source-sha256.json` (Eingabe-Provenienz) sowie `review/PHASE2-TASK.md` (Phase-2-Auftrag, da der Inline-Auftrag technisch nicht übermittelbar war), `review/criterion-results.json`, `review/definition-hash-check.json`, `review/pair-comparison.json` (Zwischenauswertungen) und `review/verify.py.prev-1216` (auditierte Vorlauf-Fassung des Prüfskripts). Eingabehashes, Kriterien und Ergebnisse bleiben getrennt; die Definition und die Builderdateien wurden nach der Erzeugung nicht verändert.
