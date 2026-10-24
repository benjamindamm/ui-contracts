# uSpec: Folgeprüfung zweier offener Layoutfelder

Stand: 24. Oktober 2026. [Quellen S60](SOURCES.md#s60), [C400/C401](CLAIMS.md#c400). Manuelle Dokument-/Quellprüfung, keine ausgeführten Figma-, Contract- oder Laufzeittests.

| Feld | Ergebnis | Konkret geprüfte Grenze |
| --- | --- | --- |
| V04 Formale relative Geometrie | Bleibt U | section._anchor bezeichnet das Figma-Messziel. Variantenrelative bbox-Werte beschreiben Messkoordinaten, keine dynamische Bindung eines Overlays an eine Eingabe |
| V06 Overflow und Scrollen | Bleibt U | Die konkrete Baselineextraktion speichert clipsContent. Scrollrichtung und eine Auswahl auto/scroll sind in extractDims nicht enthalten; andere Pfade bleiben gesondert zu prüfen |

Die Folgeprüfung macht die bestehende Lücke genauer überprüfbar. Sie wertet vorhandene Clippinginformationen nicht zu einem vollständigen Scrollmodell auf. Umgekehrt wird aus dem begrenzten Exportpfad nicht auf die Unmöglichkeit von Scrollen im gesamten Projekt geschlossen.

**Gemeinsamer Stand nach dieser Runde:** Fünf Layoutfelder gezielt nachgeprüft (drei UXSpec, zwei uSpec); UXSpec V05 U→A, vier weiterhin U. Insgesamt verbleiben 72 U-Zellen. Unterkomponenten, Layoutwrapper und Messanker dürfen in der Integration nicht als dieselbe Zielart behandelt werden.
