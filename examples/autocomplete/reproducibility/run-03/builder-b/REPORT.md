# REPORT — Builder B, Lauf autocomplete-reproducibility-03

Kontext: Frisch aus der eingefrorenen Definition unter `components/` (Autocomplete inkl.
Overlay- und ScrollArea-Definitionen) erzeugt, ohne Kenntnis früherer Läufe.
Komponente: `ui-contracts:Autocomplete` 0.1.0 (aus `components/autocomplete/component.json`).
Werkzeuge: gepinnte Originalumgebung `tools/openpencil` (`@open-pencil/*` 0.16.0, Node v24.13.1).

## Ergebnis

`autocomplete.fig` ist eine echte, binäre OpenPencil-Design-Datei (ZIP-Container, ZIP-Signatur
`PK`, 31.065 Bytes beim letzten Lauf), kein umbenanntes JSON und keine Rasterkopie. Sie enthält
eine Seite („Autocomplete“) mit einem Seitentitel und **zehn benannten Fall-Frames** — je einer
pro Story aus `components/autocomplete/stories.json`: `Autocomplete/closed`,
`Autocomplete/opening`, `Autocomplete/loading`, `Autocomplete/ready`, `Autocomplete/active`,
`Autocomplete/scroll-end`, `Autocomplete/selected`, `Autocomplete/empty`, `Autocomplete/error`,
`Autocomplete/disabled`. Innerhalb jedes Falls sind die Teile getrennt und verständlich benannt
(`label`, `input` mit `input.query`, `overlay.surface`, `overlay.scroll.viewport`,
`overlay.scroll.content`, `list`, `option/<key>`, `status`; in loading/empty/error zusätzlich
`message`). Sämtliche Gestaltung (Fills, Strokes, Radien, Schatten, Texte, Maße) stammt als
strukturierte, editierbare Knoteneigenschaften aus den Definitionsdateien — keine eingebetteten
Bilder (Prüfung `reimport.no-images`: 0 `IMAGE`-Knoten).

**Schreib- und Verifizierungspfad (alles Originalwerkzeuge der Bibliothek):**

1. `generate.mjs` liest Tokens (`tokens.json`, DTCG-Referenzen wie `{base.gap}` aufgelöst),
   Stories, a11y-Regeln, `component.json` und die drei `layout.css`-Dateien direkt aus
   `components/` — es sind keine Definitionswerte im Skript hartkodiert.
2. Der Designgraph wird im Speicher mit `renderJSX` aus `@open-pencil/core/design-jsx`
   (Original-Renderer inkl. Yoga-Layout) aufgebaut: 121 Knoten (Seite + 120 Ebenen).
3. Die Datei wird mit `exportFigFile` (`@open-pencil/core/io`, Original-Writer) geschrieben.
4. Die geschriebene Datei wird mit `parseFigFile` (Original-Reader, `populate: 'all'`)
   vollständig wieder eingelesen: 121/121 Knoten, Struktur identisch.
5. `preview.png` und `preview.svg` werden **aus dem wiedereingelesenen Graphen** gerendert
   (`headlessRenderNodes`, Scale 2; `renderNodesToSVG`).
6. 109 Selbstprüfungen (erwartet vs. tatsächlich, konkrete Werte) laufen gegen den
   wiedereingelesenen Graphen → `checks.json`: **109 bestanden, 0 fehlgeschlagen**.

**Größen und Knoten (letzter Lauf):**

| Artefakt | Größe |
| --- | --- |
| `autocomplete.fig` | 31.065 Bytes |
| `preview.png` | 193.917 Bytes (3744 × 1408 px, Scale 2) |
| `preview.svg` | 13.997 Bytes (Zusatzformat, von der Umgebung bereitgestellt) |
| `checks.json` | 47.977 Bytes (109 Prüfungen) |

Knoten: 121 geschrieben / 121 wiedereingelesen, davon 65 `FRAME` und 55 `TEXT`, 0 `IMAGE`.

## Ausführen

Exakter Befehl vom Repositorystamm aus:

```sh
node examples/autocomplete/reproducibility/run-03/builder-b/generate.mjs
```

Das Skript löst seine Pfade relativ zu seiner eigenen Position auf und verwendet ausschließlich
die gepinnte Umgebung `tools/openpencil/node_modules` (via `createRequire`-Anker an
`tools/openpencil/package.json`). Ein erneuter Lauf überschreibt exakt die fünf Ausgaben
`autocomplete.fig`, `preview.png`, `preview.svg`, `checks.json`, `source-sha256.json` im selben
Ordner und ändert nichts außerhalb (zweimal ausgeführt und verglichen, siehe „Tatsächliche
Prüfung“).

## Tatsächliche Prüfung

Was tatsächlich geprüft wurde — alles **nach** dem Schreib-/Reimport-Zyklus, also an der
Dateiinhaltsebene, nicht am Speichergraphen:

- **Dateiintegrität:** `autocomplete.fig` beginnt mit `PK` (ZIP-Container); 31.065 Bytes > 0
  (Prüfungen `fig.magic`, `fig.bytes`).
- **Reimport-Vollständigkeit:** 1 Seite („Autocomplete“), 121 Knoten geschrieben = 121
  wiedereingelesen; 0 `IMAGE`-Knoten; 65 `FRAME` + 55 `TEXT` (Prüfungen `reimport.*`).
- **Pro Fall (× 10):**
  - Fall-Frame: Name, x/y (Rasterposition), Breite 320, Fallhöhe (100 px ohne Popup, 140 px mit
    Meldungszeile, 268 px mit Ergebnisliste).
  - `label`: Text „Stadt auswählen“, Position (0, 0), Höhe 20, Inter 14, Farbe text
    (23,43,77,255).
  - `input`: Box (0, 28, 320 × 44), Radius 8, Randstärke 1, Randfarbe je Zustand — focus
    (37,99,235,255) in opening/loading/ready/active/scroll-end/empty/error, sonst border
    (203,213,225,255); Füllung surface.
  - `input.query`: exakter Text (Query oder Placeholder „Stadt suchen …“) und Farbe (text bzw.
    muted 100,116,139,255), Position (12, 12).
  - Bei sichtbarem Popup (6 Fälle): `overlay.surface` (0, 80, 320 × Viewporthöhe), Radius 8,
    Füllung surface, Drop-Shadow offset (0, 2), radius 8, Farbe (0,0,0,51);
    `overlay.scroll.viewport` mit `clipsContent = true` (160 px bei 7 Ergebnissen, 32 px bei
    Meldung); `overlay.scroll.content` mit Versatz y = 0 bzw. **y = −64** in `scroll-end`
    (Liste 224 px hoch, letzte Option Zürich sichtbar).
  - `list` (3 Fälle): Höhe 224 px = 7 × 32, alle 7 Optionen vorhanden — inkl. der geclippten
    `option/wien` (y = 160) und `option/zuerich` (y = 192) in `ready`.
  - Aktive Option: `option/hamburg` in `active` und `option/zuerich` in `scroll-end` tragen den
    highlight-Fill (234,242,255,255); alle anderen Optionen ohne Fill.
  - Deaktivierte Option: `option/muenchen` in allen drei Listenfällen mit Textfarbe disabled
    (148,163,184,255).
  - Meldungszustände: `message`-Zeile (32 px) mit exaktem Meldetext; Status-Text und -Farbe
    (muted, in `error` error 185,28,28,255), Status-Position unter dem jeweiligen sichtbaren
    Element (z. B. y = 120 in loading/empty/error, y = 248 in ready/active/scroll-end,
    y = 80 in closed/opening/selected/disabled).
  - `status`: exakter Meldetext aus `accessibility.rules.json` („7 Städte verfügbar.“,
    „Ausgewählt: Berlin.“, „Suche wird geöffnet.“ …), in closed/disabled leer, Inter 12,
    Zeilenhöhe 20.
  - closed/selected/disabled: keine `overlay.surface`-Kinder (Prüfung `no-popup`).
  - `scroll-end`-Sonderprüfung: Zürich-Absolute-Y (208–240) liegt vollständig innerhalb der
    sichtbaren Overlayfläche (80–240).
- **Render:** `preview.png` mit PNG-Magic, 193.917 Bytes; `preview.svg` erzeugt (13.997 Bytes).
- **renderJSX-Warnungen:** keine (Prüfung `render.warnings`).
- **Unabhängige CLI-Verifikation** (Original-CLI der gepinnten Umgebung, `openpencil` 0.16.0):
  - `openpencil info autocomplete.fig` → „1 pages, 120 nodes — 55 TEXT, 65 FRAME — Fonts: Inter“.
  - `openpencil tree` → benannte Hierarchie wie oben (Seite „Autocomplete“, 10 Fall-Frames).
  - `openpencil query "//FRAME[@name='overlay.scroll.content']" --json` → fünf Content-Knoten:
    y = 0 (ready/active, h = 224), **y = −64 (scroll-end, h = 224)**, h = 32 (Meldungsfälle).
  - `openpencil node --id 0:58` (active → `option/hamburg`) → `fill: #EAF2FF`;
    `--id 0:35` (ready → `option/hamburg`) → kein Fill.
- **Reproduzierbarkeit:** das Skript wurde mehrfach nacheinander ausgeführt; jeder Lauf
  überschreibt dieselben fünf Dateien, und alle 109 Prüfungen bestehen in jedem Lauf.

## Quellenzuordnung

| Ergebnis in der Datei | Definitionsdatei (Quelle) |
| --- | --- |
| Maße: Breite 320, Input 44, Zeile 32, Max 160, Lücken 8, Radius 8, Padding 12, Zeilenhöhe 20, Schriften 14/12; Farben surface/text/muted/border/focus/highlight/disabled/error; Schriftfamilie Inter | `components/tokens.json` (inkl. `base.*`-Referenzen) |
| Grundgeometrie: Label → Input (labelGap), Popup am Inputende + gap mit gleicher Breite/Kante, Viewport `min(n × rowHeight, maxHeight)`, Status nach statusGap unter sichtbarem Popup sonst unter Input, verborgenes Popup belegt keinen Platz | `components/autocomplete/layout.css` + `components/autocomplete/README.md` („Sichtbare Geometrie“) |
| Zustandsregeln: Fokusrand in opening/loading/ready/empty/error; `:disabled` (Textfarbe, Randfarbe); Placeholder-Farbe; aktive Option mit highlight-Hintergrund; deaktivierte Option mit disabled-Farbe; Status-Farbe in error | `components/autocomplete/layout.css` |
| Overlayfläche: margin-top = gap, Hintergrund surface, kein Rand, Radius, `box-shadow: 0 2px 8px #0003` (roher Wert an die JSX-Prop `shadow`, Original-Parser `parseCSSShadows`) | `components/overlay/layout.css` |
| Viewport-Clipping: `max-height`, `overflow-y`; Liste ohne Margin/Padding | `components/scroll-area/layout.css` |
| Die zehn Fälle, Labels, Placeholders, Queries, Ergebnisrecords (key/label/disabled), `activeKey`, `value`, `enabled`, Phasen | `components/autocomplete/stories.json` |
| Status-/Meldungstexte (Vorlagen `{count}`/`{label}`), Popup-Sichtbarkeit je Phase (`projections.popupVisible`), Auswahlsemantik (aktiv ≠ bestätigt, disabled nicht aktivierbar) | `components/autocomplete/accessibility.rules.json` |
| Teilnamen `label`, `input`, `overlay.surface`, `overlay.scroll.viewport`, `list`, `option`, `status` | `components/autocomplete/component.json` (Anatomie-Keys) |
| Zustandsmodell, nach dem die Fälle gedeutet werden (closed/opening/active→loading/ready/empty/error; „selected = closed + value“, „active/scroll-end = ready + activeKey“, „disabled = closed + enabled=false“) | `components/autocomplete/behavior.scxml` + `components/autocomplete/README.md` |
| Scroll-Endanforderung: letzte aktive Option im sichtbaren Viewport, Inhalt des geclippten Viewports versetzt, alle Ergebnislayer bleiben erhalten | `components/autocomplete/README.md` („Sichtbare Geometrie“) |
| Identität `ui-contracts:Autocomplete` 0.1.0, Domänenzuordnung, targetScope (editierbare Zustände, keine Interaktivität im Canvas) | `components/autocomplete/component.json` |

Nicht in die Darstellung eingegangen: `components/autocomplete/error-relay.scxml` (wurde gelesen;
beschreibt den `init.failed`-Fehlerpfad, für den es in `stories.json` keinen Fall gibt) und die
`accessibility.html`-Dateien (Semantik-Vorlage; die sichtbare Geometrie folgt layout.css).

## Fehlende oder mehrdeutige Angaben / Adaptergrenzen

Ehrliche Dokumentation aller Annahmen und Grenzen — die Definition legt die folgende Punkte
nicht eindeutig fest oder der Canvas-Adapter kann sie nicht abbilden:

1. **`#0003` im box-shadow (Mehdeutigkeit).** Strenge CSS-Lesart eines 4-stelligen Hexwerts
   (`#RGBA`, Ziffern verdoppelt) würde `rgba(0, 0, 51, 51)` ergeben; der Original-Parser der
   gepinnten Umgebung (`parseColor`/`parseCSSShadows`) liest `#0003` als `{r:0, g:0, b:0,
   a:51/255}`. Entscheidung: Der **Rohwert aus der Definition** wird unverändert an die
   JSX-Prop `shadow` übergeben und vom Original-Parser gelesen — das Ergebnis folgt also der
   Lesart der Werkzeugumgebung (Schwarz, α ≈ 20 %). Kein eigener Parse des Werts.
2. **Farbe der Meldungszeile im Popup (loading/empty/error).** Die Definition sagt nur „eine
   Zeile mit der entsprechenden Meldung“, ohne eigene Farbe. Annahme: Wurzelfarbe
   `--ac-text` (Vererbung wie bei normalen Optionen), Zeile mit Options-Padding (6 px / 12 px)
   und Zeilenhöhe 32.
3. **Status bei leerer Meldung.** „Ohne Meldung ist sein Text leer“ — impliziert, dass der
   Status-Teil weiterhin existiert. Entscheidung: Der `status`-Textknoten ist in **allen**
   zehn Fällen vorhanden (in closed/disabled mit leerem Text), damit das Teil editierbar und
   benannt bleibt.
4. **disabled-Input: Placeholder-Farbe.** Die CSS-Regel `:disabled` ändert nur Textfarbe und
   Randfarbe; `::placeholder` bleibt `--ac-muted`. Streng gelesen bleibt der Placeholder auch im
   disabled-Fall muted. Der Label-Text hat keine disabled-Regel und bleibt `--ac-text`.
5. **Fontgewicht.** Nichts in der Definition gibt ein Gewicht vor. Annahme: 400 (normal) für
   alle Komponententexte.
6. **Namen abgeleiteter Teile.** Die Anatomie liefert nur sieben Teilnamen. Die zusätzlichen,
   frei vergebenen Namen: `overlay.scroll.content` (aus dem ScrollArea-Teil `content`),
   `input.query` (Text im Input), `message` (Meldungszeile), `option/<key>` (Option nach
   fachlichem Key, gemäß „wird über den fachlichen Key identifiziert“), Textkinder der Optionen
   und der Meldung heißen `label` (Namensquelle `result.label`).
7. **Seitenlayout.** Explizit frei laut Exportrahmen: Titel-Text („Autocomplete — 10 benannte
   Zustände …“, Inter 16, Gewicht 600, Textfarbe aus den Tokens), Raster 5 × 2, Rand 48 px,
   Spalten-/Zeilenabstand 64 px, Zeilenhöhe = größte Fallhöhe (268 px).
8. **Scroll-Offset in `scroll-end`.** „entsprechend versetzt“ ist nicht numerisch fixiert.
   Entscheidung: Volles Scroll-Ende, Offset = Listenhöhe − Viewporthöhe = 224 − 160 = **64 px**;
   damit ist Zürich (letzte aktive Option) vollständig im Viewport (Prüfung dokumentiert).
9. **Popup in `opening`.** Die Maschine ist in `opening` bereits im `active`-Zweig, aber die
   a11y-Projektion gibt `popupVisible: false`. Entscheidung: Projektionsregel folgt → kein
   Popup in `opening`, dafür Fokusrand (layout.css listet `opening` in der Fokusgruppe) und
   Status „Suche wird geöffnet.“
10. **Viewporthöhe in Meldungszuständen.** „Eine Zeile“ → Höhe = rowHeight (32 px), also
    `min(1 × 32, 160)`.
11. **Zeilenhöhe für alle Texte.** Die Wurzel-`line-height: 20px` wird auf label,
    Input-Text, Options-Text und Status angewendet (der Status-Frame ist laut CSS ebenfalls
    `--ac-line-height` hoch bei 12 px Schrift).
12. **Stroke-Align.** CSS-Border bei `border-box` → Stroke `INSIDE` (Bibliotheksdafüllwert);
    nicht explizit in der Definition genannt.
13. **Absolute Geometrie statt Auto-Layout.** Die CSS-Regeln beschreiben einfache Blockgeometrie
    mit expliziten Höhen und Margins; ich habe sie 1:1 in absolute Positionen (layoutMode NONE)
    übersetzt, weil das die Prüfbasis exakt macht. Ein Auto-Layout-Adapter wäre eine zulässige
    Alternative, würde aber die exakte Prüfbarkeit der Geometrie verschlechtern.
14. **Statisches Scrollen.** `scroll-end` ist eine statische Darstellung (Versatz des
    Viewportinhalts), kein dynamisches Scrollen im Canvas — von der README ausdrücklich erlaubt.
15. **Nicht-repräsentierte Zustände.** `error-relay.scxml` (`init.failed` → closed mit fault)
    und die Übergangszustände der Maschine selbst haben keine Stories und werden daher nicht
    als eigene Fälle gerendert; die zehn Stories sind der geforderte Prüfumfang.
16. **Keine Interaktivität/ARIA im Canvas.** Laut `targetScope` ist das OpenPencil-Ziel
    „editable named component states“; `aria-*`-Attribute und Verhalten sind semantische
    Annotationen der Definition und werden im Design nicht ausgeführt (nur ihre sichtbaren
    Folgen: Fokusrand, Hervorhebung, Meldungen).
17. **Nicht-Byte-identische Wiederholungen.** Der Original-Writer erzeugt pro Lauf eine zufällige
    ID-Sitzung (Knoten-GUIDs), daher können die `.fig`-Byte zwischen Läufen minimal abweichen
    (z. B. 31.065 vs. 31.066 Bytes); Namen, Struktur, Geometrie und alle geprüften Werte sind
    deterministisch, und jeder Lauf überschreibt exakt dieselben fünf Ausgabedateien.
18. **Schrift beim Render.** `Inter` ist in der Werkzeugumgebung nicht gebündelt; der
    Original-Renderer rendert die Vorschau mit einem Systemschrift-Fallback. Der Designknoten
    trägt korrekterweise `fontFamily: Inter` aus dem Token (CLI: „Fonts: Inter“).
