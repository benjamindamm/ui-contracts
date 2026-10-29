# Reproduzierbarkeitsversuch 02

Zwei neue Agenten bauen unabhängig voneinander ein editierbares OpenPencil-Design aus derselben eingefrorenen Autocomplete-Definition. Ein dritter Agent ohne übernommenen Gesprächskontext leitet vorab Prüfkriterien aus der Definition ab und vergleicht anschließend beide Originaldateien mit der Definition und miteinander.

Dieser Lauf wurde bewusst ohne Kenntnis der Ergebnisse aus [run-01](../run-01/README.md) durchgeführt. Eingabe, Kriterien und Annahmen wurden frisch gebildet; run-01, frühere Designs und Research-Dokumente waren für Builder und Prüfer gesperrt.

## Gleiche Eingabe, getrennte Arbeit

[run.json](run.json) bindet alle 22 Definitionsdateien, die Definitionsrevision und den Werkzeug-Lock. Die Revision `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727` wurde beim Start unabhängig aus `components/` nachgerechnet (SHA-256 über das kompakte, sortierte Pfad→Hash-Objekt); Werkzeug-Lock `ebdba852…` und alle 22 Einzelhashes stimmen mit den Builder-Manifesten überein.

Die Builder haben denselben Auftrag, jeweils einen eigenen Ausgabeordner und keinen Zugriff auf frühere Designs oder die Ausgabe des anderen. Die Kontextübernahme ist bei allen drei Agenten deaktiviert. Die Dateigrenzen sind Auftragsvorgaben, keine zusätzliche Dateisystemsandbox.

## Ablauf

1. Eingabeversion unabhängig prüfen und Hashes einfrieren.
2. Der Prüfer leitet aus der Definition allein 101 Kriterien ab (67 explizit, 22 abgeleitet, 12 unterbestimmt) und speichert sie, bevor er eine Builder-Ausgabe sieht.
3. Kriterien hashen und [versiegeln](review/preregistration-seal.json).
4. Beide Builder erstellen echte editierbare Dateien, Vorschau und Bericht.
5. Der Prüfer misst zuerst die Originaldateien selbst, dann liest er die Builderberichte.
6. Vergleich auf Komponentenebene; Unterschiede werden als Verletzung, erlaubte Freiheit oder unzureichend bestimmte Regel eingeordnet.

## Unterbrechungen

Beide Builder wurden während des Laufs mehrfach vom Step-Limit des Agenten-Harness unterbrochen und in derselben Session fortgesetzt. Die Unterbrechungen sind vollständig in [run.json](run.json) (`interruptions`, `interruptionImpact`) und im [Prüfbericht](review/REVIEW.md#2-unterbrechungen-der-builder-provenienz-keine-builder-ausgabe) sowie in [results.json](review/results.json) (`interruptions.effectOnValidity`) dokumentiert.

| Akteur | Stopp | Stand beim Stopp | Fortsetzung |
| --- | --- | --- | --- |
| Builder A | 1 | nur `_probe.mjs`, keine Lieferung | alle Artefakte außer `REPORT.md` |
| Builder A | 2 | alle Artefakte außer `REPORT.md` | `REPORT.md` geschrieben, Probe entfernt |
| Builder B | 1 | nur Analyse, keine Dateien | 6 von 7 Lieferungen plus Zwischenartefakt |
| Builder B | 2 | 6 von 7 Lieferungen plus `render-report.json` | `REPORT.md`, Zwischenartefakt entfernt, Generator erneut ausgeführt |

Ursache war ausschließlich das Step-Limit, kein Zugriff auf verbotene Eingaben. Jede Fortsetzung nutzte den eigenen vorherigen Kontext derselben Session; kein Builder sah den anderen, run-01 oder frühere Ergebnisse. Der Prüfer war nicht betroffen.

**Auswirkung:** Die Unterbrechungen mindern die Aussagekraft für Prozess-Reproduzierbarkeit (Single-Shot, Anzahl der Schritte). Sie mindern nicht die Bewertung der gelieferten Artefakte und nicht die Kontexttrennung beider Builder. Der Lauf belegt keinen ununterbrochenen Ein-Schuss-Durchlauf; die Zwischenartefakte `_probe.mjs` und `render-report.json` sind nicht mehr vorhanden und daher nicht prüfbar.

## Ergebnis

| | Design A | Design B |
| --- | --- | --- |
| Gesamturteil | **PASS_MIT_ABWEICHUNGEN** | **PASS_MIT_ABWEICHUNGEN** |
| erfüllt / verletzt / nicht anwendbar | 96 / 4 / 1 | 96 / 4 / 1 |
| explizit verletzt | 0 | 0 |
| abgeleitet verletzt | 4 | 4 |

Alle expliziten Kriterien sind in beiden Designs erfüllt: die zehn Zustände, Texte, Maße, Farben, Typografie und Clipping-Regeln. Beide Designs verletzen dieselben vier abgeleiteten Accessibility-Kriterien (A11Y01, A11Y02, A11Y03, A11Y07: keine maschinenlesbaren ARIA-Annotationen im `.fig`-Format dieser Toolchain). Die gemessene Paarübereinstimmung beträgt **1,000 (Band „hoch“)** über 199 Merkmale; hohe Übereinstimmung bedeutet gleiche Lesart der Definition, nicht automatisch Korrektheit.

Vollständige Befunde, Messwerte und Grenzen: [Prüfbericht](review/REVIEW.md) · [Ergebnisdaten](review/results.json) · [Einzelbeobachtungen](review/native-checks.json) · [Hashes](review/hashes.json).

## Ablage

Die Struktur entspricht [run-01](../run-01/README.md). Zwei ergänzende Dateien kommen hinzu: `builder-b/source-sha256.json` (Eingabe-Provenienz, wie bei Builder A) und `review/render-meta.json` (Render-Metadaten, von den Prüfskripten referenziert). Eingabehashes, Kriterien und Ergebnisse bleiben getrennt; die Definition und die Builderdateien wurden nach der Erzeugung nicht verändert.
