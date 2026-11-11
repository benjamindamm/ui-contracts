# Autocomplete 0.3.0 · gemeinsame Abnahme

## Primärer visueller Vergleich

Verwende die Story `active` aus `sources/components/autocomplete/stories.json` mit ihren exakten Texten, Schlüsseln, der Originalreihenfolge, der deaktivierten Zeile und der aktiven Zeile. Lade die Story reproduzierbar in einer eigenen Vorschau der tatsächlich gebauten nativen Komponente. Nimm den Screenshot im hellen Modus bei Standardschriftgrösse ohne Bildschirmtastatur auf. Die Story-Vorschau darf den normalen Bedienpfad ergänzen. Im Komponentenausschnitt keine Testelemente zeigen.

Sollwerte und Zustandsregeln ausschliesslich aus den gebundenen CSS-Dateien und aufgelösten Tokens entnehmen. Prüfe die eingerahmte Komponente am realen Gerät in logischen Einheiten. Bei der verfügbaren Breite des Testgeräts soll die Komponente 320 pt/dp breit sein. CSS-px für diesen Pilot als pt/dp abbilden. Melde mindestens Breite, Eingabehöhe, Abstände zwischen Label, Feld, Overlay und Status, Zeilenhöhe, Viewport-Höhe, Radien, verwendete Schrift, Eingaberand, aktive und deaktivierte Zeile, Oberflächen- und Textfarben sowie Schatten. Der Viewport schneidet nach fünf vollständigen Zeilen ab und ist scrollbar. Messbare Sollmasse mit höchstens 1 pt/dp Rundungsabweichung. Farben als sRGB-Sollwerte und gerenderte Stichproben dokumentieren, Schriftglättung ausnehmen. Native Schattenabweichung kenntlich machen. Wenn eine Messung fehlt, als nicht geprüft ausweisen.

## Ergänzende Prüfung der vier Domänen

Die übrigen Zustände geschlossen, Laden, leer und Fehler separat gegen die Quellen prüfen. In einer bedienbaren Vorschau Suchtext, aktive Zeile und bestätigten Schlüssel getrennt halten. Mit deterministischen Testantworten alte Antworten, deaktivierte Treffer, einmaliges Bestätigungsereignis und Abbruch ohne Wertänderung prüfen. Zugänglichen Namen, Fokus und Status getrennt ausweisen. Hörbare Meldungen sind ein separater Screenreader-Nachweis. Für jede Prüfung das tatsächliche Vorgehen, Soll, Ist und offene Punkte festhalten. Visuelle Übereinstimmung und Funktionsprüfungen getrennt ausweisen.

Der unabhängige Prüfer verwendet ausschliesslich diese Kriterien, Quellen und die gelieferte Ausgabe. Der Builder legt vor Änderungen nach Erstlieferung eine separate Revision an.
