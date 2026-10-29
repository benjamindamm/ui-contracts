# Einheitliche native Komponentenpräsentation

Stand: 29. Oktober 2026. Ein gemeinsames Layout-Werkzeug setzt bereits erzeugte Komponenten in ein einheitliches natives OpenPencil-Dokument. **Kein presentation.json und kein neuer Beschreibungsstandard.** Layoutregeln liegen als versionierte Konstanten im Werkzeug, die Ausgabe bleibt eine editierbare `.fig`.

## Darstellung

- Zweispaltiges Raster, Reihenfolge aus der `stories`-Datei der ausgewählten Komponente.
- Gleiche Kopfzeile, nummerierte Zustandsbeschriftungen, helle Karten und neutraler Hintergrund.
- Komponentengruppen bleiben in Originalgröße. Die Spaltenbreite wächst für breite Komponenten; Karten einer Reihe erhalten dieselbe ausreichende Höhe.
- Sichtbare Überstände und Schatten werden über die vorhandene native Geometrie berücksichtigt. Das Werkzeug setzt kein zusätzliches Clipping. Bereits im Original definierte Viewport-Clips und unsichtbare Ebenen bleiben erhalten.
- Alte Seitentitel und freie Beschriftungen außerhalb der ausgewählten Gruppen werden nur in der **neuen Ausgabe** durch die gemeinsame Präsentation ersetzt.

## Aufruf

Vom Repository-Stamm mit installierter gepinnter OpenPencil-Toolchain:

```sh
node tools/presentation/present.mjs \
  --library example \
  --component Autocomplete \
  --input examples/autocomplete/reproducibility/run-04/builder-a/autocomplete.fig \
  --output /tmp/autocomplete-presentation-new
```

`--component` ist der Schlüssel im Index der ausdrücklich ausgewählten Bibliothek. Das Werkzeug liest deren `component.json` und den vorhandenen `stories`-Verweis; es kennt keine fest eingebauten Autocomplete-Zustände. Die Fallgruppen müssen eindeutig benannt und auf der einen Eingabeseite direkt enthalten sein: entweder exakt nach Fall-ID oder als `Name / Fall-ID`.

Optional übergibt `--definition-revision LABEL` eine bekannte Quellrevision für Kopfzeile/Receipt. Der Wert wird vom Aufrufer angegeben und nicht aus der FIG-Datei bewiesen. Ohne Angabe zeigt die Ausgabe ausdrücklich „nicht mitgeliefert“; keine aktuelle Libraryrevision still auf ein älteres FIG übertragen.

Die Bibliothek benötigt für diesen initialen PNG-Adapter ein prüfbares lokales `fonts.json`, einschließlich normaler 400-/700-Schnitte der Präsentationsschrift. Auch alle tatsächlich genutzten Komponentenschriften müssen exakt lokal vorliegen und den Text abdecken. Keine stillen Fontfallbacks oder Netzwerkauflösung. Eine separate Lizenzdatei ist entsprechend der [Fontpolicy](../fonts/README.md) keine technische Voraussetzung.

## Quellschutz und Nachweis

Das Werkzeug schreibt nur in einen neuen Ausgabeordner; bestehende Ausgaben, Libraries, historische Autocomplete-Ordner, Forschungsordner und Unterordner des Eingabeortes werden abgewiesen. Auch über Symlinks aufgelöste Ausgabepfade unterliegen dieser Prüfung. Es entstehen:

- `presentation.fig`: neue native Präsentation;
- `presentation.png`: Rendering dieser erneut eingelesenen FIG;
- `receipt.json`: Eingabe-/Ausgabehashes, Quellverweise, Layout und Invarianten pro Fall.

Vor der Layoutänderung wird jeder Komponentenbaum rekursiv erfasst; nach Zusammensetzung, FIG-Readback und PNG-Rendering wird verglichen. Verglichen werden die eigenen nativen Eigenschaften einschließlich Texte, Styles, Maße, Farben, Effekte, Clips, Variablenbindungen, Layerreihenfolge und aller relativen Kindpositionen. Nur die äußere x/y-Position der Fallgruppe darf wechseln. Eltern-/Kind-IDs werden durch die rekursive Baumstruktur ersetzt; IDs, rohe Importmetadaten sowie die im Receipt explizit genannten Renderer-Caches werden nicht als unveränderte Wire-/Metadatenserialisierung ausgegeben.

Die tatsächliche Gruppenposition und Kartengeometrie werden zusätzlich gegen den Layoutplan geprüft. Der Eingabehash muss nach dem Vorgang identisch sein. Eine Abweichung blockiert den erfolgreichen Abschluss. Bereits erzeugte Teil-Ausgaben eines fehlgeschlagenen Aufrufs sind kein bestandener Nachweis und werden nicht über eine Wiederholung überschrieben.

## Erprobter Umfang und Grenzen

[Beide run-04-Ergebnisse im selben Layout](../../examples/presentation/autocomplete-run04/README.md) · [Verifikation](verification.json).

Beide Original-FIGs und sämtliche historischen run-04-Dateien sind unverändert. Die neue Darstellung enthält weiterhin 142 Komponenten-Nodes für A bzw. 162 für B; nur die alte externe Präsentation wurde ersetzt. Beide Layoutpläne stimmen exakt überein. Eine zusätzliche begrenzte Autocomplete-Gegenprüfung besteht für beide, weiterhin 572/572 gleiche gemessene Paarwerte.

Das Werkzeug korrigiert keine Komponentenfehler und erzwingt keine Pixelgleichheit. Bereits vorhandene Unterschiede, etwa in nicht normierten Clip-/Eckenentscheidungen, bleiben erhalten. Neue Bibliotheks-Fontassets können anders rendern als frühere nicht gebundene Fonts; das ist kein nachträglicher Pixelnachweis für alte Studien.

Initial blockiert: mehrseitige Eingaben, gedrehte/gespiegelte Nodes, formatierte Text-Runs und Komponentenreferenzen außerhalb der ausgewählten Fallgruppen. Komplexere Kompositionen/Masken und beliebige Figma-Funktionen sind nicht allgemein qualifiziert. Runtime, Accessibility und Metadatenverlustfreiheit werden nicht aus der Präsentation abgeleitet. `PASS_LIMITED`, `release:false` bleibt sichtbar.

## Regressionen

```sh
node --test tools/presentation/test_presentation.mjs
```

Die Tests prüfen zusätzlich eine synthetische Disclosure-Komponente mit anderen Zustandsnamen. Sie decken Definitionreihenfolge, fehlende/doppelte Fälle, breite/überstehende/hohe Komponenten, Farb-/Clip-/Stroke-/Positions-/Reihenfolgemutationen, nativen Roundtrip und Eingabe-/Ausgabeschutz ab. Frisch erzeugte Graphen werden für den Roundtriptest erst als FIG serialisiert und eingelesen: Der echte Werkzeugeingang ist eine Datei, kein noch unnormalisierter In-Memory-Buildergraph. Die Invarianten selbst wurden dafür nicht abgeschwächt.
