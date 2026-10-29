# Reproduzierbarkeitsversuch 01

Zwei neue Agenten bauen unabhängig voneinander ein editierbares OpenPencil-Design aus derselben eingefrorenen Autocomplete-Definition. Ein dritter Agent ohne übernommenen Gesprächskontext leitet vorab Prüfkriterien aus der Definition ab und vergleicht anschließend beide Originaldateien mit der Definition und miteinander.

## Gleiche Eingabe, getrennte Arbeit

[run.json](run.json) bindet alle 22 Definitionsdateien, die Definitionsrevision und den Werkzeug-Lock. Die Builder haben denselben Auftrag, jeweils einen eigenen Ausgabeordner und keinen Zugriff auf frühere Designs oder die Ausgabe des anderen im erlaubten Arbeitsumfang. Die Kontextübernahme ist bei allen drei Agenten deaktiviert. Die Dateigrenzen sind Auftragsvorgaben, keine zusätzliche Dateisystemsandbox. Gleiche Modelle können gemeinsame blinde Flecken haben; ein universeller statistischer Unabhängigkeitsnachweis wird nicht behauptet.

## Modellkonfiguration

**GPT-6.1 Sol · Reasoning: Medium**, nachträglich vom Nutzer am 29. Oktober 2026 angegeben. Die historischen Laufzeitprotokolle wurden hierfür nicht verifiziert; eine eigene Modellzuordnung je Builder und Prüfer sowie genaue Modellrevision und Seeds sind nicht belegt. Diese Ergänzung verändert weder die eingefrorenen Eingaben noch die ursprünglichen Prüfergebnisse. Modellkonfiguration und Ergebnis sind auch im [Studienregister](../../../../docs/research/STUDIES.md) aufgeführt. Ein Vergleich mit anderen Modellen steht noch aus.

## Ablauf

1. Eingabeversion einfrieren und Hashes prüfen.
2. Beide Builder erstellen echte editierbare Dateien, Vorschau und Generierungs-/Ergebnisbericht.
3. Der Prüfer speichert seine Kriterien, bevor er irgendeine Builder-Ausgabe liest.
4. Nach Abschluss beider Builder prüft er die Originaldateien zunächst selbst; anschließend liest er deren Berichte.
5. Vergleich auf Komponentenebene: Zustände, Teile, Texte, Maße, visuelle Regeln, Clipping und Editierbarkeit. Die freie Anordnung auf der Designseite und technische IDs dürfen abweichen.
6. Unterschiede werden als Verletzung einer klaren Regel, erlaubte Freiheit oder unzureichend bestimmte Regel eingeordnet.

Die Auswertung ist abgeschlossen: Die erfassten normalisierten Komponentenwerte stimmen überein; beide Designs verletzen dieselbe Platzhalterfarbregel und erhalten insgesamt FAIL. [Studienbericht](../../../../docs/research/studies/AC-R01/README.md). Die ursprüngliche Definition und die Ausgaben bleiben unverändert.
