# Unabhängige Prüfung des ersten Definitions-Proofs

Stand: 25. Oktober 2026. Der Bibliothekseintrag ist angelegt. Ein neuer Agent erhielt **keinen übernommenen Gesprächsverlauf** (`fork_turns: none`) und ausschließlich den Auftrag, aus components/ ein editierbares OpenPencil-Dokument zu bauen. Das Ergebnis ist ein erster Cold-Context-Autorenproof, kein bereits allgemeiner Compiler und noch kein Zwei-Ziel-Vergleich.

## Eingabegrenze

Der erlaubte fachliche Input war ausschließlich components/. Normale Original-OpenPencil-Dokumentation und die gepinnten Originalwerkzeuge unter tools/openpencil/ waren technische Hilfsmittel. Rechercheordner, frühere Bilder, Webharnesses, andere Beispiele und diese Reviewdateien waren im Auftrag ausdrücklich ausgeschlossen. Der Kontext wurde beim Agentenstart nicht übernommen. Die Dateizugriffsgrenze war eine Auftragsvorgabe, keine zusätzlich eingerichtete Dateisystemsandbox.

[definition-baseline.json](definition-baseline.json) enthält den vor Agentenstart eingefrorenen Hash aller 22 Definitionsdateien und sieben erfolgreiche Original-CEM-/SCXML-Schema-Vorläufe. Nach Abschluss sind sämtliche Dateien bytegleich geblieben. Der Ausgangsstand ist deshalb nicht nachträglich passend zum Ergebnis verändert worden.

## Tatsächlich unabhängige Ausgabekontrolle

Der Elternagent hat die erzeugte binäre [autocomplete.fig](../output/openpencil/autocomplete.fig) erneut mit dem Original-OpenPencil-Reader eingelesen, ohne die Aussagen des Generierungsskripts als Beweis zu übernehmen. [actual-graph.json](actual-graph.json) enthält die daraus gelesenen Knoten. [independent-results.json](independent-results.json) enthält die Prüfung gegen die eingefrorenen Tokens, Regeln und Stories.

Alle zehn Fälle sind vorhanden. Geprüft wurden unter anderem 320px Breite, 44px Inputhöhe, 8px Ankerabstand, Zeilen-/Viewportmaße, Statusposition und genaue Texte, erhaltene editierbare Optionen, deaktivierte/aktive Zuordnungen sowie die tatsächlich innerhalb des geclippten Viewports liegende aktive Option. Der scroll-end-Fall enthält alle sieben Optionen und zeigt Zürich durch einen Versatz von 64px. Aktive Füllfarbe stammt aus dem Token. Alle strukturellen Prüfaussagen sind erfüllt; 164 Knoten wurden aus der Originaldatei gelesen. Die gespeicherte PNG-Vorschau wurde zusätzlich visuell geprüft.

Der Exportagent hat außerdem eine Textänderung mit erneutem Original-Writer-/Reader-Roundtrip geprüft. Das ist von der unabhängigen strukturellen Nachprüfung getrennt im [Exportbericht](../output/openpencil/REPORT.md) dokumentiert.

## Was dieser Versuch aufgedeckt hat

Die Definition reicht für einen konkreten editierbaren Entwurf, ist aber noch nicht in jeder Einzelheit eindeutig:

1. Für Meldungstext innerhalb des Popups fehlt eine eigene Padding-/Ausrichtungsregel. Der Agent hat die Optionszeilenregel 12px/6px übernommen und diese Entscheidung offengelegt. Eine spätere Definitionsrevision muss die Regel ausdrücklich führen, bevor wir vollständige Gleichheit zweier Ziele beanspruchen.
2. Ein Satz nennt irrtümlich drei unsichtbare Datenzeilen; sieben Zeilen bei fünf sichtbaren ergeben zwei vollständig unsichtbare Zeilen. Der Export hat die präzisen Werte 7 × 32px / 160px befolgt und alle Daten erhalten. Der Fehler bleibt in der eingefrorenen ersten Revision sichtbar.
3. Die disabled-Placeholderfarbe folgt aktuell der eigenen CSS-Pseudoelementregel muted. Eine anders gewünschte Abbildung wäre eine ausdrückliche Visualänderung, keine Entscheidung des Exporteurs.

Diese Befunde sind ein Ergebnis des Tests. Die Definition wurde nicht still bereinigt und der Export nicht als vollständig interpretationsfrei ausgegeben. Vor einem strengen Zwei-Ziel-Vergleich werden Klarstellungen als neue Version angelegt und beide Ziele daraus erneut erzeugt.

## Grenzen

Die Datei ist tatsächlich mit OpenPencils Originalparser geöffnet und als editierbare Knoten gelesen worden; die Vorschau stammt aus der gespeicherten Datei. Eine sichtbare Öffnung in der Desktop-App konnte wegen gesperrtem Mac und nicht verfügbarer App-Verbindung nicht bestätigt werden. Es wurden keine weiteren Entsperrversuche unternommen.

Dies ist wie vereinbart ein **editierbares Design**, keine interaktive Autocomplete-Preview in OpenPencil. SCXML-Laufzeit, reale ARIA-Ausführung und HTML-/TypeScript-Ausgabe sind hier nicht als bestanden behauptet. Das zweite Ziel und der gemeinsame Änderungsnachweis stehen noch aus.

Die abgeschlossene Recherche und ihre 702 Bedingungen wurden nicht verändert oder um diesen neuen Anwendungsproof ergänzt. Keine Commits oder Pushes.
