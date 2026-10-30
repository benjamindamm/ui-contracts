# Einheitliches Layout für preview.png

Stand: 29. Oktober 2026. Ein gemeinsames Layout-Werkzeug setzt bereits erzeugte Komponenten in ein einheitliches natives OpenPencil-Dokument. **Zentrale Vorlage:** [presentation.json](../../tools/openpencil/templates/presentation.json) enthält Raster, Abstände, Kartenfarben und Typografie. Das ist eine interne, versionierte Konfiguration unseres Renderers und kein neuer Komponentenstandard. OpenPencil liest das JSON nicht selbst; das Werkzeug erzeugt daraus native `.fig`-Elemente. Die Komponenten-Contracts bleiben davon getrennt.

## Darstellung

- Standardvorlage: zweispaltiges Raster, Reihenfolge aus der `stories`-Datei der ausgewählten Komponente.
- Gleiche Kopfzeile, nummerierte Zustandsbeschriftungen und neutraler Hintergrund. Karten ohne Theme-Zuordnung bleiben hell; explizit zugeordnete Karten verwenden ihren Bibliotheks-Hintergrundtoken und passende helle/dunkle Beschriftungen.
- Komponentengruppen bleiben in Originalgröße. Die Spaltenbreite wächst für breite Komponenten; Karten einer Reihe erhalten dieselbe ausreichende Höhe.
- Sichtbare Überstände und Schatten werden über die vorhandene native Geometrie berücksichtigt. Das Werkzeug setzt kein zusätzliches Clipping. Bereits im Original definierte Viewport-Clips und unsichtbare Ebenen bleiben erhalten.
- Alte Seitentitel und freie Beschriftungen außerhalb der ausgewählten Gruppen werden nur in der **neuen Ausgabe** durch die gemeinsame Präsentation ersetzt.

## Aufruf

Vom Repository-Stamm mit installierter gepinnter OpenPencil-Toolchain:

```sh
node tools/openpencil/preview.mjs \
  --library example \
  --component Autocomplete \
  --input examples/autocomplete/reproducibility/run-04/builder-a/autocomplete.fig \
  --output /tmp/autocomplete-output-new
```

`--component` ist der Schlüssel im Index der ausdrücklich ausgewählten Bibliothek. Das Werkzeug liest deren `component.json` und den vorhandenen `stories`-Verweis; es kennt keine fest eingebauten Autocomplete-Zustände. Die Fallgruppen müssen eindeutig benannt und auf der einen Eingabeseite direkt enthalten sein: entweder exakt nach Fall-ID oder als `Name / Fall-ID`.

Optional übergibt `--definition-revision LABEL` eine bekannte Quellrevision für Kopfzeile/Receipt. Der Wert wird vom Aufrufer angegeben und nicht aus der FIG-Datei bewiesen. Ohne Angabe zeigt die Ausgabe ausdrücklich „nicht mitgeliefert“; keine aktuelle Libraryrevision still auf ein älteres FIG übertragen.

Die Bibliothek benötigt für diesen initialen PNG-Adapter ein prüfbares lokales `fonts.json`, einschließlich normaler 400-/700-Schnitte der Präsentationsschrift. Auch alle tatsächlich genutzten Komponentenschriften müssen exakt lokal vorliegen und den Text abdecken. Keine stillen Fontfallbacks oder Netzwerkauflösung. Eine separate Lizenzdatei ist entsprechend der [Fontpolicy](../fonts/README.md) keine technische Voraussetzung.

## Themeabhängige Karten

Für Light-/Darkmode-Darstellungen beim Aufruf zusätzlich `--case-themes /pfad/case-themes.json` übergeben. Die Datei ist eine interne Zuordnung für den Präsentationsrenderer, kein neuer Komponentenstandard und keine Datei, die OpenPencil selbst liest. Ihre Schlüssel sind exakt die IDs aus der ausgewählten stories-Datei:

```json
{
  "light": {"mode": "light", "backgroundToken": "theme.light.canvas"},
  "dark": {"mode": "dark", "backgroundToken": "theme.dark.canvas"}
}
```

Die Tokenpfade im Beispiel sind Platzhalter für die tatsächlichen Tokens in `libraries/<id>/tokens.json`. Keine Farben erfinden und keine Token ergänzen, nur damit eine Vorschau funktioniert. Der Hintergrund kommt aus der führenden Definition; er ist nicht die Oberfläche des Controls. Die Zuordnung anhand der Definition erstellen, nicht aus Gruppennamen oder aktuellen Füllfarben erraten. Falls die Definition Darkmode verlangt und der Hintergrund fehlt, diese offene Angabe melden, bevor eine finale Themevorschau erzeugt wird.

Unterstützt: sechsstellige HEX-Farben, deckende DTCG-sRGB-Farbwerte und Token-Aliase. Nicht unterstützt: transparente Hintergründe, andere Farbräume, automatische Modus-/Resolverauswahl und pauschales Durchsuchen von CSS nach möglichen Farben. Für solche Fälle einen passenden Adapter ergänzen; keine stille Näherung. Unbekannte Fall-IDs, fehlende Tokens, zyklische Aliase oder ein Themeeintrag ohne `mode` und `backgroundToken` blockieren den Aufruf.

Die zentrale `presentation.json` legt für dunkle Karten nur Rahmen- und Beschriftungsfarben fest (`darkCard`). Sie enthält absichtlich keinen universellen dunklen Hintergrund. Die äußere Übersichtsfläche bleibt neutral. Komponentengruppen und ihre eigenen Flächen werden unverändert übernommen. Der Renderer schaltet Komponenten nicht selbst in Darkmode; die Eingabe-FIG muss bereits die angeforderten Varianten enthalten.

Ohne Zuordnung bleibt die bisherige neutrale helle Karte erhalten und im Receipt steht `mode: unspecified`; das gilt nicht als Darkmode-Nachweis. Bei zugeordneten Fällen hält `preview-check.json` Mode, aufgelösten Hintergrundtoken und Farbwerte sowie Hashes der Zuordnungs- und Token-Datei fest. Kartengrund, Rahmen und Beschriftung werden nach FIG-Readback und Rendering zusätzlich geprüft. Ein korrekter Hintergrund ist kein Kontrast- oder Accessibility-Zertifikat.

[Theme-Regressionsnachweis](openpencil-theme-verification.json). Der synthetische Test nutzt eigene temporäre Quellen; die example-Definition und historische Vorschauen bleiben unverändert.

## Quellschutz und Nachweis

Das Layout gehört zur normalen OpenPencil-Ausgabe: `<komponente>.fig` und `preview.png` liegen im selben Ergebnisordner, ohne zusätzlichen presentation-Unterordner. Der Ausgabeordner darf bereits andere Arbeitsdateien enthalten; die drei Zieldateien müssen neu sein. Bestehende Zielartefakte, Libraries, historische Reproduktions-/Reviewordner und Forschungsordner werden nicht überschrieben. Auch über Symlinks aufgelöste Ausgabepfade unterliegen dieser Prüfung. Es entstehen:

- `<komponente>.fig`: native Komponente mit gemeinsamem Übersichtslayout (z. B. `autocomplete.fig`);
- `preview.png`: Rendering dieser erneut eingelesenen FIG;
- `preview-check.json`: Eingabe-/Ausgabehashes, Vorlagenhash, Quellverweise, Layout und Invarianten pro Fall.

Vor der Layoutänderung wird jeder Komponentenbaum rekursiv erfasst; nach Zusammensetzung, FIG-Readback und PNG-Rendering wird verglichen. Verglichen werden die eigenen nativen Eigenschaften einschließlich Texte, Styles, Maße, Farben, Effekte, Clips, Variablenbindungen, Layerreihenfolge und aller relativen Kindpositionen. Nur die äußere x/y-Position der Fallgruppe darf wechseln. Eltern-/Kind-IDs werden durch die rekursive Baumstruktur ersetzt; IDs, rohe Importmetadaten sowie die im Receipt explizit genannten Renderer-Caches werden nicht als unveränderte Wire-/Metadatenserialisierung ausgegeben.

Die tatsächliche Gruppenposition und Kartengeometrie werden zusätzlich gegen den Layoutplan geprüft. Der Eingabehash muss nach dem Vorgang identisch sein. Eine Abweichung blockiert den erfolgreichen Abschluss. Bereits erzeugte Teil-Ausgaben eines fehlgeschlagenen Aufrufs sind kein bestandener Nachweis und werden nicht über eine Wiederholung überschrieben.

Beim neuen Build kann `tools/openpencil/layout.mjs` bereits vor dem Endexport auf den Graphen angewendet werden. Für vorhandene Dateien dient der CLI-Aufruf als Adapter: Ein eigener unfertiger `raw.fig` darf auch im selben Arbeitsordner liegen; sein Name darf nicht mit der finalen Zieldatei kollidieren. Eine vorhandene finale Komponente oder Vorschau wird nicht still ersetzt.

## Erprobter Umfang und Grenzen

[Beide run-04-Ergebnisse im selben Layout](../../examples/autocomplete/output/openpencil/run-04/README.md) · [Verifikation](openpencil-preview-verification.json).

Beide Original-FIGs und sämtliche historischen run-04-Dateien sind unverändert. Die neue Darstellung enthält weiterhin 142 Komponenten-Nodes für A bzw. 162 für B; nur die alte externe Präsentation wurde ersetzt. Beide Layoutpläne stimmen exakt überein. Eine zusätzliche begrenzte Autocomplete-Gegenprüfung besteht für beide, weiterhin 572/572 gleiche gemessene Paarwerte.

Das Werkzeug korrigiert keine Komponentenfehler und erzwingt keine Pixelgleichheit. Bereits vorhandene Unterschiede, etwa in nicht normierten Clip-/Eckenentscheidungen, bleiben erhalten. Neue Bibliotheks-Fontassets können anders rendern als frühere nicht gebundene Fonts; das ist kein nachträglicher Pixelnachweis für alte Studien.

Initial blockiert: mehrseitige Eingaben, gedrehte/gespiegelte Nodes, formatierte Text-Runs und Komponentenreferenzen außerhalb der ausgewählten Fallgruppen. Komplexere Kompositionen/Masken und beliebige Figma-Funktionen sind nicht allgemein qualifiziert. Runtime, Accessibility und Metadatenverlustfreiheit werden nicht aus der Präsentation abgeleitet. `PASS_LIMITED`, `release:false` bleibt sichtbar.

## Regressionen

```sh
node --test tools/openpencil/test_layout.mjs tools/openpencil/test_themes.mjs
```

Die Tests prüfen zusätzlich eine synthetische Disclosure-Komponente mit anderen Zustandsnamen. Sie decken Definitionreihenfolge, fehlende/doppelte Fälle, breite/überstehende/hohe Komponenten, Farb-/Clip-/Stroke-/Positions-/Reihenfolgemutationen, nativen Roundtrip und Eingabe-/Ausgabeschutz ab. Frisch erzeugte Graphen werden für den Roundtriptest erst als FIG serialisiert und eingelesen: Der echte Werkzeugeingang ist eine Datei, kein noch unnormalisierter In-Memory-Buildergraph. Die Invarianten selbst wurden dafür nicht abgeschwächt.

## Zentrale Vorlage, gewöhnliche Ergebnisdateien

Die Vorlage liegt beim Werkzeug, nicht in jedem Ergebnisordner. Bestehende Ausgangsdateien werden nicht neu als presentation.fig dupliziert. Neue Endausgaben heißen beispielsweise `autocomplete.fig` und `preview.png`. Die beiden nachträglichen run-04-Proben liegen nun innerhalb des vorhandenen Autocomplete-Ausgabebereichs; ihre FIG-/PNG-Bytes und die Forschungsoriginale wurden bei der Umordnung nicht verändert.

Qualifiziert ist die mitgelieferte Standardvorlage. Änderungen an Raster oder Typografie benötigen neue passende Vorschaunachweise; eine gültige JSON-Datei allein belegt keine überlappungsfreie Darstellung beliebiger Einstellungen.

## Sichtbares Beispiel

[Autocomplete der example-Bibliothek in Light und Dark](../../examples/autocomplete/output/openpencil/theme-preview/README.md): ready und disabled nebeneinander. Da example bisher keinen Darkmode definiert, bleiben die vorgeschlagenen Dark-Farben separat; die Bibliothek und historischen Artefakte sind unverändert.
