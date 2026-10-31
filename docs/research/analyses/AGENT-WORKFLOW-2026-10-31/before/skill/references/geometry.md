# Geometriehilfe für Designausgaben

## Wann brauche ich das Werkzeug?

Entscheide nach der Geometrie, nicht allein nach dem Namen der Komponente:

| Aufgabe | Vorgehen |
| --- | --- |
| Rechtecke, abgerundete Buttons, Pillen, Kreise, Ellipsen, gerade Linien | Native OpenPencil-Primitive bzw. passende SVG-Grundformen. Gleiche Breite/Höhe für einen Kreis; Pillenradius aus der Höhe ableiten. Kein D3 nötig. |
| Balkenchart | Meist Rechtecke und berechnete Positionen; keine Kurvenbibliothek nötig. |
| Pie-/Donut-Segmente, datenabhängige Bögen | Gepinnte Geometriehilfe `tools/charts/pie.mjs` nutzen. Winkel und Pfade aus Werten berechnen, nicht zeichnerisch erraten. |
| Linien-/Flächencharts oder weitere komplexe Kurven | D3-Shape ist als Abhängigkeit vorhanden; ein passender lokaler Adapter und repräsentative Import-/Readback-Prüfungen müssen noch ergänzt werden. Nicht als bereits unterstützt ausgeben. |
| Sonderformen außerhalb von Charts | Dieselbe Hilfe erwägen, wenn berechnete Kurven nötig sind. Kein Zwang, jede Form als Chart zu modellieren. |

Ein Kreis pro Datenwert ist kein Pie-Segment. Ein optisch ähnliches Bild ersetzt weder korrekte Anteile noch echte editierbare Sektoren. Fehler bei einfachen Rundungen zuerst über Maße, Radius und Transformationen korrigieren; dafür keinen Chartgenerator einführen.

## Werkzeug gezielt nutzen

Im gefundenen UI-Contracts-Repository liegt [tools/charts/README.md](../../../tools/charts/README.md). Nur diese Anleitung und die benötigte API laden; Beispielresultate und Forschungsläufe sind keine notwendigen Eingaben. In unabhängigen Läufen gelten weiterhin deren Zugriffsgrenzen. `d3-shape` ist die isolierte Rechenbibliothek; sie liefert Geometrie ohne vorgegebenes Chartlayout, Achsen oder Legende. Kein zusätzliches Komponenten-Beschreibungsformat wird eingeführt.

1. Führende Definition/Daten und Einheiten bestimmen. Fehlende Werte oder visuelle Regeln als offene Entscheidungen behandeln. Eingabedaten und Generator beim neuen Ergebnis nachvollziehbar ablegen.
2. Pie-Geometrie mit `pieGeometry(data, {radius, innerRadius})` erzeugen; `sectorsSvg(...)` liefert eine Gruppe einzelner SVG-Pfade. Eingabe-IDs sind eindeutig und XML-sicher, Werte endlich und nicht negativ, Gesamtsumme positiv, Farben sechsstellige HEX-Werte in Großbuchstaben. Nullwerte erzeugen keine sichtbaren Segmente. Die Reihenfolge bleibt erhalten, Werte werden zur Gesamtsumme normalisiert.
3. Titel, Typografie, Farben, Legende und Layout separat nach Definition gestalten. Eine selbst gewählte Normalisierung oder Rundungsregel offenlegen. Keine screenshotbasierten Beispieldaten als neue normative Vorgaben übernehmen.
4. SVG über den vorhandenen OpenPencil-Import in native Elemente überführen, FIG exportieren und erneut einlesen. Reguläre Ausgaben: `<komponente>.fig` und `preview.png` im Ergebnisordner; kein zusätzlicher presentation-Ordner. Die gemeinsame Zustandsübersicht nur bei entsprechendem Auftrag verwenden.
5. Tatsächliches Artefakt prüfen: einzelne editierbare Vektoren, Farben, Anteile, Grenzen, Beschriftungen und Rendering. Winkel-/Pfadberechnung, Import und sichtbares Ergebnis sind getrennte Prüfungen. Für neue Geometriefamilien passende Gegenfälle ergänzen.

## Beleg und Grenze

Der dreiteilige Pie-Proof unter `examples/charts/pie-chart/` belegt D3 → SVG → native FIG → PNG für genau diesen Fall; er ist bei erlaubtem Beispielzugriff erreichbar. 15 Regressionen decken zusätzlich Eingabefehler und einzelne Geometriefälle ab. Donut und Vollkreis haben Geometrietests, aber noch keinen vollständigen nativen End-to-End-Nachweis. `proof.mjs` ist der konkrete Demonstrationsadapter, kein universeller Renderer: seine Mittelpunktprüfung gilt nicht unverändert für Donuts/Vollkreise.

Die SVG-Importstrecke ist kein Versprechen, beliebiges SVG zu unterstützen. Editierbare Vektoren bedeuten keine eingebaute Chart-Datenbindung oder Runtime-Interaktion. Geänderte Daten erfordern erneute Generierung. Historische Ergebnisse nicht überschreiben. Erfolgreiche Geometrieprüfungen als begrenzten Nachweis berichten; keine Accessibility- oder Plattformfreigabe daraus ableiten.
