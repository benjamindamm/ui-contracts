# REPORT · run-03/builder-a · Autocomplete

Dieser Bericht wurde nachträglich von einer frischen Session geschrieben, nachdem die
Erzeugungssession durch einen Providerfehler abgebrochen wurde, bevor ein Bericht entstand.
Er stützt sich ausschließlich auf: (1) die Definitionen unter `components/`, (2) die gepinnte
Werkzeugumgebung `tools/openpencil/` (nur Lesezugriff), (3) die sechs vorhandenen Artefakte in
diesem Ordner (nur Lesezugriff, inklusive Wiedereinlesen von `autocomplete.fig` mit dem
Original-Reader der gepinnten Umgebung). `generate.mjs` wurde **nicht** neu ausgeführt; kein
Artefakt wurde verändert.

---

## Ergebnis

**`autocomplete.fig` ist eine echte binäre OpenPencil-Datei**, keine umbenannte JSON-Datei:

- 42.176 Byte, ZIP-Container (Kompression: store) mit genau drei Einträgen:
  - `canvas.fig` — 41.720 Byte, Binärformat mit Magie-Präfix `fig-kiwie` (OpenPencil-Kiwi-Format)
  - `thumbnail.png` — 70 Byte, 1×1-Bild, offensichtlich ein Writer-Platzhalter (nicht die Preview)
  - `meta.json` — 71 Byte: `{"version":1,"app":"OpenPencil","createdAt":"2026-10-29T10:07:39.106Z"}`
- Das `createdAt` (UTC) passt zur Modifikationszeit der Artefakte (29.10.2026, 11:07 lokal, UTC+1).
- Die Datei lässt sich mit dem Original-Reader der gepinnten Umgebung
  (`@open-pencil/core` 0.16.0, `io.parseFigFile`, `populate: 'all'`) vollständig einlesen.

**Entstehung** (aus `generate.mjs` belegt): Der Generator liest zur Laufzeit die Definitionen
unter `components/` (21 Dateien, keine hartkodierten Definitionswerte), löst DTCG-Tokens auf,
parsiert die drei `layout.css`-Dateien mit einem Mini-CSS-Parser, validiert SCXML-Phasen und
Teile-Struktur, baut den Szenengraphen über die Figma-Plugin-API-Kompatibilität
(`@open-pencil/core/figma-api`) und schreibt ihn mit `io.exportFigFile` aus. Textbreiten werden
echte Textmetriken aus CanvasKit/SkiaRenderer (gepinnt) gemessen. Danach liest der Generator die
Datei wieder ein, rendert daraus `preview.png` (Skala 2) und `preview.svg`, führt 178
Selbstprüfungen durch, macht einen kompletten zweiten Lauf in ein temporäres Artefakt zur
Determinismuskontrolle und schreibt `checks.json` plus `source-sha256.json`.

**Verifizierung**: `checks.json` meldet 178/178 bestanden (Details und Einschränkungen unter
„Tatsächliche Prüfung“). Meine eigenständige, unabhängige Read-back-Prüfung mit dem Original-Reader
ergab **keine Abweichung** von den aus `components/` abgeleiteten erwarteten Werten (siehe unten).

**Dokumentstruktur** (wiedereingelesener Graph, 136 Knoten):

- 1× `Document` (Root-Frame), 1× Seite `Autocomplete` (CANVAS), dann 22 Top-Knoten:
  - 2 Seitentexte: `Titel` = „Autocomplete · 10 Zustände“ (Inter 24/32), `Quelle` = Quellenzeile (Inter 12)
  - 10 Fall-Frames: `closed`, `opening`, `loading`, `ready`, `active`, `scroll-end`, `selected`, `empty`, `error`, `disabled`
  - 10 Captions `Hinweis <id>` mit Phase, SCXML-Pfad und Zusatzdaten (z. B. „active — Phase ready · SCXML active/ready · aktiv: hamburg · 7 Ergebnisse“)
- 112 Fall-Knoten, pro Fall einheitlich:
  - `Label` (Text „Stadt auswählen“, Inter 14/20), `Input` (Frame 320×44, y=28, Radius 8, geclippt, weiße Füllung, 1 px INSIDE-Rand) mit Kind `Query` oder `Placeholder` (x=12),
  - bei Popup-Fällen zusätzlich `Overlay Surface` (y=80, geclippt, weiße Füllung, Radius 8, DROP_SHADOW offset (0,2), blur 8, schwarz, Alpha 0.2) → `Overlay Scroll Viewport` (geclippt) → `Overlay Scroll Content` → `Listbox` → entweder 7× `Option: <key>` (jeweils mit `Label`) oder `Message Row` → `Message`,
  - `Status` (Text, Inter 12/20).

**Bytegrößen der Artefakte** (auf Disk): `autocomplete.fig` 42.176 · `preview.png` 327.145 ·
`preview.svg` 18.398 (18.309 Zeichen, UTF-8) · `checks.json` 189.686 · `source-sha256.json` 2.210 ·
`generate.mjs` 43.461.

**Previews**: `preview.png` ist ein RGBA-PNG 3816×1528 px (Inhaltsbereich 1908×764 × Skala 2),
gerendert aus dem wiedereingelesenen Graphen. Visueller Abgleich: die zehn Fälle erscheinen
exakt wie die Datenlage (Fokusborder in opening/loading/ready/active/scroll-end/empty/error,
Popup mit 5 sichtbaren Zeilen in ready/active, scroll-end mit versetztem Inhalt und sichtbarer
letzter Zeile „Zürich“ hervorgehoben, gedimmtes „München“, rote Statuszeile bei error,
keine Popupteile bei closed/opening/selected/disabled). `preview.svg` ist ein
`<?xml …><svg … width="1908" height="764">`-Dokument (Schatten als `feDropShadow`).

---

## Ausführen

Exakter Befehl **vom Repositorystamm** (laut Kopfkommentar von `generate.mjs`, Zeile 25):

```sh
node examples/autocomplete/reproducibility/run-03/builder-a/generate.mjs
```

Voraussetzung: die gepinnte Umgebung `tools/openpencil/node_modules`
(OpenPencil 0.16.0; hier geprüft mit Node v24.13.1). Der Skript schreibt ausschließlich in den
eigenen Ausgabeordner `run-03/builder-a/` und **überschreibt dabei** (bei erneutem Lauf):

- `autocomplete.fig` (byte-identisch garantiert **nicht** — `meta.json` erhält ein neues `createdAt`,
  ZIP-Dateinamen/Zeiten wechseln; nur die eingelesene Struktur und das PNG sind deterministisch,
  siehe x01/x02)
- `preview.png`, `preview.svg`
- `checks.json`, `source-sha256.json`
- zusätzlich kurzzeitig `autocomplete.rerun.fig` und `preview.rerun.png` für den zweiten
  Lauf; diese werden nach Erfolg wieder gelöscht (`rm … { force: true }`) und blieben bei einem
  abgebrochenen Lauf sonst zurück.

Da die vorhandenen Artefakte final und extern gehasht sind, ist dieser Befehl im Rahmen des
Reproduzierbarkeitslaufs **nicht** zu wiederholen; er ist hier nur als dokumentierte
Wiedergewinnungsmethode festgehalten.

---

## Tatsächliche Prüfung

### 1. Was `checks.json` tatsächlich prüft

Kopf: `component: "ui-contracts:Autocomplete v0.1.0"`, `run: "autocomplete/reproducibility/run-03/builder-a"`,
`nodeCount: 136`, `artifacts: {autocomplete.fig: 42176, preview.png: 327145, preview.svg: 18309}`,
`summary: {total: 178, passed: 178, failed: 0}`. Keine einzelne Prüfung ist fehlgeschlagen.

| Gruppe | IDs | Inhalt (konkret) |
|---|---|---|
| Dokument | d01–d05 | fig nicht leer; Größe 42.176 B; genau eine Seite; Seitenname `Autocomplete`; 136 Knoten im wiedereingelesenen Graphen |
| Fälle | c01–c03 | alle zehn Fall-Frames benannt vorhanden (c01, c02); Fall-IDs decken sich mit der README-Zeile „Die zehn Fälle heißen …“ (c03) |
| Regelfeststellungen | r01–r03 | Fokusborder-States = {opening, loading, ready, empty, error} (aus `autocomplete/layout.css`); Overlay-Anker = `anchor(bottom)`/`anchor(left)`/`anchor-size(width)` (r02, echte Abgleichprüfung gegen `overlay/layout.css`); Viewport `overflow-y: auto` (r03) |
| Fälle (11–22 Prüfungen je nach Fall, gesamt 160) | f01a–f10w | je Fall: Label-Text/-Typografie (14/20, Inter, 400)/Position (0,0)/Farbe; Input 320×44 @ y=28, Radius 8, `clips=true`, Füllung weiß, Rand 1 px INSIDE mit korrekter Farbe (focus oder border); Input-Text Name/Inhalt/Farbe/x=12 (Query vs. Placeholder); Overlayfläche anwesend bzw. abwesend gemäß Zustandsprojektion; Popup 320×h @ y=80, Radius 8, geclippt, weiß, Schatten (0,2)/blur 8/schwarz/0.2; Viewport geclippt, korrekte Höhe; Scrollinhalt-Versatz y=−scrollOffset und Inhaltshöhe; Optionen Namen in Reihenfolge, Geometrie (y=k×32, 320×32), Texte, Hervorhebung nur bei aktiver Option, gedimmte Farbe bei `muenchen`; aktive Zeile im sichtbaren Viewport; Status-Text/-Position/-Größe/-Farbe; Fallrahmen 320×caseH |
| Previews | p01–p03 | PNG existiert; PNG-Abmessungen 3816×1528 = Inhaltsbereich × 2 (p02, echte Prüfung gegen PNG-Header); SVG beginnt mit `<?xml … <svg` |
| Determinismus | x01–x02 | zweiter, kompletter Lauf in temporäre Artefakte: identischer Struktur-Dump des wiedereingelesenen Graphen (x01, echt — Node-for-Node-Vergleich inkl. Geometrie, Füllungen, Texten); byteidentisches `preview.png` (x02 = true) |
| Quellen | s01–s02 | `source-sha256.json` deckt alle 21 gelesenen Definitionsdateien ab; `library.json` verlinkt exakt `autocomplete/`, `overlay/`, `scroll-area/component.json` |

Konkrete, aus `checks.json` entnommene Kernwerte (Auswahl):

- `f01d`: Input `{w:320, h:44, y:28, radius:8, clips:true}` · `f01f`: Randfarbe border
  (0.7961, 0.8353, 0.8824), weight 1, INSIDE · `f02f`: Randfarbe focus (0.1451, 0.3882, 0.9216)
- `f03i`/`f08i`/`f09i`: Popup `{w:320, h:32, y:80}` (loading/empty/error) ·
  `f04i`/`f05i`/`f06i`: Popup `{w:320, h:160, y:80}` (ready/active/scroll-end)
- `f04k`: Schatten `{offset:{x:0,y:2}, radius:8, color:{r:0,g:0,b:0,a:0.2}}` (0.2 = `#0003` → `#00000033`)
- `f04n`: Optionennamen `Option: berlin/hamburg/muenchen/dresden/koeln/wien/zuerich` ·
  `f04p`: Texte `Berlin, Hamburg, München, Dresden, Köln, Wien, Zürich`
- `f05q`: Hervorhebung `[false,true,false,…]` (hamburg) · `f06q`: `[…,true]` (zuerich) ·
  `f06m`: Scrollinhalt `{y:-64, h:224}` · `f05s`/`f06s`: aktive Zeile im Viewport = true
- `f04t`/`f05t`/`f06t`: „7 Städte verfügbar.“ @ y=248 · `f07t`: „Ausgewählt: Berlin.“ @ y=80 ·
  `f09v`: error-Status @ y=120, Farbe (0.7255, 0.1098, 0.1098)
- `f01t`/`f10t`: Status-Text leer (closed/disabled) · `f10g`: disabled-Input zeigt Placeholder
  in Platzhalterfarbe (0.3922, 0.4549, 0.5451)

**Befunde zu `checks.json` (nicht beschönigt):**

1. **Sich selbst erfüllende Prüfungen.** Bei d01, d02, d03, d05, r01, p01, p03 und x02 sind
   „erwartet“ und „tatsächlich“ derselbe Ausdruck im Code; diese Checks können nicht scheitern
   und dokumentieren nur den erreichten Wert. Konkret ist damit „genau eine sichtbare Seite“
   (d03) **nicht** als Assertion geprüft, sondern nur als Wert festgehalten (tatsächlich: 1 Seite).
   Die belastbaren Aussagen stammen aus den übrigen 170 Prüfungen, insbesondere den 160
   Fall-Prüfungen (f-Gruppe) sowie c01/c02/c03, r02/r03, p02, x01, s01/s02.
2. **`artifacts.preview.svg` ist eine Zeichenzahl, keine Bytezahl.** checks.json führt
   18.309, auf Disk sind es 18.398 Byte (UTF-8, 73 nicht-ASCII-Zeichen wie „…“, „·“, Umlaute).
   `autocomplete.fig` und `preview.png` sind dagegen als Bytezahlen korrekt (42.176 bzw. 327.145).
3. **Byte-Reproduzierbarkeit der `.fig` wird nicht behauptet.** x01 vergleicht nur den
   wiedereingelesenen Graph (gerundete Struktur), x02 nur das PNG. `meta.json` enthält pro
   Lauf ein frisches `createdAt`, die `.fig`-Bytes wären bei einem Wiederholungslauf also
   nicht byteidentisch.
4. Die Erwartungswerte der Checks sind von `generate.mjs` **aus derselben Definition** abgeleitet
   (Adapter-Eigencheck); sie belegen Konsistenz zwischen Definition, Adapter und Datei, aber nur
   insofern, als die Adapterinterpretation selbst stimmt. Deshalb existiert zusätzlich der
   unabhängige Read-back unten.

### 2. Unabhängige Read-back-Prüfung (dieser Bericht)

Methode: `autocomplete.fig` wurde mit dem Original-Reader der gepinnten Umgebung
(`tools/openpencil/node_modules/@open-pencil/core` 0.16.0, `parseFigFile`, `populate: 'all'`)
eingelesen; alle Werte wurden unabhängig aus `components/` neu abgeleitet und verglichen.
Außerdem: ZIP-Inhaltsverzeichnis, `meta.json`, PNG-Signatur/-Header, SVG-Kopf, SHA-256-Abgleich.

Ergebnis: **keine Abweichung**. Verifiziert wurde u. a.:

- 1 Seite `Autocomplete`, 136 Knoten (= 1 `Document` + 1 Seite + 22 Top-Knoten + 112
  Fall-Knoten), Top-Ebene wie oben beschrieben.
- Alle zehn Fall-Frames; Rahmenhöhen: closed/opening/selected/disabled 100 ·
  loading/empty/error 140 · ready/active/scroll-end 268 (alle Breite 320).
- Input in jedem Fall: 320×44 @ y=28, Radius 8, geclippt, Füllung weiß, 1 px INSIDE;
  Randfarbe focus (0.1451, 0.3882, 0.9216) in opening/loading/ready/active/scroll-end/empty/error,
  sonst border (0.7961, 0.8353, 0.8824).
- Input-Texte: `closed`/`opening`/`ready`/`active`/`scroll-end` → `Placeholder` „Stadt suchen …“
  in muted (0.3922, 0.4549, 0.5451); `loading`/`error` → `Query` „Be“, `empty` → `Query` „Atlantis“,
  `selected` → `Query` „Berlin“ (alle in Textfarbe (0.0902, 0.1686, 0.3020)); `disabled` →
  `Placeholder` in muted; alle bei x=12.
- Popup nur in loading/ready/active/scroll-end/empty/error (opening laut Projektion
  `popupVisible=false` → kein Popup); Oberfläche 320×160 bzw. 320×32 @ y=80, Radius 8, geclippt,
  weiß, Schatten (0,2)/blur 8/schwarz/Alpha 0.2; Viewport geclippt in gleicher Höhe;
  Listbox-Inhaltshöhe 224 (7×32) bzw. 32.
- scroll-end: `Overlay Scroll Content` bei y=−64 (statistischer Scroll-Versatz), sichtbare
  Zeilen München/Dresden/Köln/Wien/Zürich; aktive Zeile `zuerich` mit absoluter y=128,
  also vollständig im Viewport 0…160.
- Optionen: 7 Frames `Option: <key>` bei y=0/32/64/96/128/160/192, je 320×32; Texte exakt
  `Berlin … Zürich` bei (12,6); `Option: muenchen` in disabled-Farbe (0.5804, 0.6392, 0.7216);
  Highlight-Füllung (0.9176, 0.9490, 1.0) exakt bei `hamburg` (active) bzw. `zuerich` (scroll-end),
  sonst keine Füllung.
- Status: `closed`/`disabled` leer (Knoten mit Breite 0) @ y=80; `opening` „Suche wird geöffnet.“
  @ y=80; `loading` „Städte werden geladen.“ @ y=120; `ready`/`active`/`scroll-end`
  „7 Städte verfügbar.“ @ y=248; `selected` „Ausgewählt: Berlin.“ @ y=80; `empty`
  „Keine Städte gefunden.“ @ y=120; `error` „Städte konnten nicht geladen werden.“ @ y=120
  in error-Farbe (0.7255, 0.1098, 0.1098); alle Inter 12/20, sonst muted.
- Meldungszeilen im Popup (loading/empty/error): `Message Row` 320×32 mit `Message` in Textfarbe,
  Text identisch zum jeweiligen Status.
- Captions `Hinweis <id>` mit Phase, SCXML-Pfad (`machine/closed` bzw. `active/<phase>`) und
  Zusatz (`aktiv: hamburg`, `value: berlin`, `enabled=false`, `7 Ergebnisse`).
- **SHA-256:** Alle 21 Einträge von `source-sha256.json` wurden gegen die aktuellen Dateien unter
  `components/` neu berechnet — **alle 21 stimmen überein**. Die Definition wurde seit dem Lauf
  nicht verändert.
- **Befund:** `components/autocomplete/error-relay.scxml` existiert, ist aber in
  `component.json` keiner Domäne zugeordnet, wird von `generate.mjs` nicht gelesen und fehlt in
  `source-sha256.json`. Er wurde in diesem Lauf damit nicht verwendet; ob er Teil der
  Definition sein soll, bleibt offen (außerhalb des erlaubten Zugriffs zu klären).
- Farbwerte liegen im Kiwi-Format als float32 vor (z. B. 0.39215686274509803 →
  0.3921568691730499); die Checks tolerieren deshalb ε=2·10⁻³.

---

## Quellenzuordnung

Welches Ergebnis aus dem Dokument aus welcher Definitionsdatei unter `components/` kommt:

| Element / Ergebnis in `autocomplete.fig` | Definitionsdatei | Ableitung |
|---|---|---|
| Die zehn Fälle, deren Reihenfolge, Namen und Phasen | `autocomplete/stories.json` | `stories[].id`, `phase`; Zählung zusätzlich gegen `autocomplete/README.md` abgeglichen (Check c03) |
| Fall-Inputs: Label „Stadt auswählen“, Placeholder „Stadt suchen …“, Queries („Be“, „Atlantis“), `enabled=false` | `autocomplete/stories.json` | `stories[].inputs` (übereinstimmend mit den Default-Werten in `autocomplete/interface.json`) |
| Ergebnisreihenfolge, Labels, `muenchen` deaktivierte, `activeKey` (hamburg/zuerich), `value` (berlin) | `autocomplete/stories.json` | `stories[].results`, `activeKey`, `value` |
| Komponentenbreite 320, Schrift Inter 14/20, Textfarbe, Status 12 px, Gaps 8 | `tokens.json` (+ `autocomplete/layout.css`) | `autocomplete.*`-Tokens, referenziert über `var(--ac-…)` in `layout.css` |
| Label-Geometrie (Höhe = Zeilenhöhe 20, Abstand 8) | `autocomplete/layout.css` | `[data-part="label"]` → `var(--ac-line-height)`, `var(--ac-label-gap)` |
| Input (44 hoch, Padding 0/12, Rand 1 solid, Radius 8, weiße Fläche) | `autocomplete/layout.css` + `tokens.json` | `[data-part="input"]` → `inputHeight`, `paddingInline`, `borderWidth`, `radius`, `surface` |
| Fokusborder in opening/loading/ready/empty/error | `autocomplete/layout.css` | `[data-state="…"] [data-part="input"]` → `var(--ac-focus)` |
| Platzhalterfarbe, deaktivierte Input-Farben | `autocomplete/layout.css` + `tokens.json` | `::placeholder` → `muted`, `:disabled` → `disabled`/`border` |
| Zeilenhöhe 32, Option-Padding 6/12 | `autocomplete/layout.css` + `tokens.json` | `[data-part="option"]` → `rowHeight` (`base.row`), `padding: 6px var(--ac-padding-inline)` |
| Hervorhebung der aktiven Option | `autocomplete/layout.css` + `tokens.json` | `[aria-selected="true"]` → `highlight` |
| Gedimmte deaktivierte Option | `autocomplete/layout.css` + `tokens.json` | `[aria-disabled="true"]` → `disabled` |
| Status (12 px, Abstand 8, muted; Rot bei error) | `autocomplete/layout.css` + `tokens.json` | `[data-part="status"]`, `[data-state="error"] [data-part="status"]` → `error` |
| Popup-Geometrie: Oberkante Input-Ende + 8, gleiche Breite/linke Kante, Radius 8, ohne Rand, Schatten 0 2px 8px #0003 | `overlay/layout.css` + `tokens.json` | `[data-part="surface"]`: `anchor(bottom)`, `anchor(left)`, `anchor-size(width)`, `margin-top: var(--ac-gap)`, `box-shadow` |
| Viewport: max-height 160, `overflow-y: auto` → Clipping, Höhe = min(Zeilen×32, 160) | `scroll-area/layout.css` + `tokens.json` + `autocomplete/README.md` | `[data-part="viewport"]` → `maxHeight` (`base.max`); die Formel min(n×rowHeight, maxHeight) steht in `autocomplete/README.md` („Sichtbare Geometrie“) |
| Verborgenes Popup belegt keinen Platz; Status unter sichtbarem Popup, sonst unter Input; Meldung = eine Zeile | `autocomplete/README.md` | Abschnitt „Sichtbare Geometrie“ |
| Popupsichtbarkeit je Phase (opening: **falsch**, sonst je Phase) | `autocomplete/accessibility.rules.json` | `projections[phase].popupVisible` |
| Status-Meldungstexte („7 Städte verfügbar.“, „Ausgewählt: Berlin.“, „Keine Städte gefunden.“, „Städte konnten nicht geladen werden.“, „Suche wird geöffnet.“, „Städte werden geladen.“; leer bei closed/disabled) | `autocomplete/accessibility.rules.json` + `autocomplete/stories.json` | `messages.*`-Vorlagen, `{count}`/`{label}` aus `results`/`value` |
| Schichtnamen `Listbox`, `Status` | `autocomplete/accessibility.html` | `role="listbox"`, `role="status"` (Kapitalisierung durch den Adapter) |
| Teilenamen/Teilestruktur (label, input, overlay.surface, overlay.scroll.viewport, list, option, status) | `autocomplete/component.json` (+ `overlay/component.json`, `scroll-area/component.json`) | `anatomy`, `composition`, `cssParts` in `interface.json` |
| Optionennamen `Option: <key>` (Key statt Index) | `autocomplete/component.json` + `autocomplete/stories.json` | `viewSemantics.repeatedPartIdentity`: „instance + option key, never row index“ |
| SCXML-Pfade in den Captions (`machine/closed`, `active/…`) | `autocomplete/behavior.scxml` + `autocomplete/stories.json` | Zustände `closed`, `active/{opening,loading,ready,empty,error}`; Phase→Zustand-Mapping durch den Adapter (validiert: jede Phase existiert als State) |
| Overlay- und ScrollArea-Teile als eigene Frames (Surface/Viewport/Content) | `overlay/component.json`, `scroll-area/component.json` | `cssParts` `surface`/`content`, `viewport`/`content`; „Listbox, Overlayfläche und Scrollviewport sind unterschiedliche Teile“ (`autocomplete/README.md`) |
| Kopfzeile/Komponentenidentität in `checks.json` (`ui-contracts:Autocomplete v0.1.0`) | `autocomplete/component.json` | `id`, `version` |
| Verlinkung der drei Komponenten (Check s02) | `library.json` | `components.*` |
| Seitenrahmen (Titel „Autocomplete · 10 Zustände“, Quellenzeile, Raster, Captions `Hinweis …`) | — (frei nach `autocomplete/README.md`, „Exportrahmen“) | Die Außenanordnung ist laut README frei; Textbausteine des Adapters (inkl. hartkodiertem Laufpfad „run-03/builder-a“) |
| Statistischer Scroll-Versatz in scroll-end (Content y=−64) | `autocomplete/README.md` | ausdrücklich erlaubt: „Für das Design darf dazu der Inhalt des geclippten Viewports entsprechend versetzt werden.“ |

---

## Fehlende oder mehrdeutige Angaben / Adaptergrenzen

Vollständige Liste der Stellen, an denen die Definition etwas nicht eindeutig bestimmt und
`generate.mjs`/`checks.json` eine konkrete Annahme treffen. Nichts davon wurde still
ergänzt — alle Annahmen sind im Code nachvollziehbar, mehrere würden bei Abweichung der
Definition hart abbrechen.

**Adapterentscheidungen (Definition unbestimmt, Adapter entscheidet):**

1. **Gesamte Canvas-Übertragung.** Die Definitionen sind CEM-JSON, DTCG-Tokens, CSS, SCXML und
   HTML; die Abbildung auf Figma-Knoten (Frame/Text-Typen, Hierarchie, Koordinaten) ist
   rein Adapter-Logik. Die Definition schreibt vor, *was* sichtbar ist, nicht *wie* es
   als Design-Dokument gespeichert wird.
2. **Anker-Funktionen `anchor(bottom)` / `anchor(left)` / `anchor-size(width)`** sind kein
   Standards-CSS. Der Adapter prüft nur ihr Vorhandensein (sonst Abbruch) und setzt die
   Geometrie nach `autocomplete/README.md` um (Oberkante = Input-Unterkante + gap, gleiche
   Breite/linke Kante). Eine andere Anker-Interpretation wäre möglich, wurde nicht gewählt.
3. **Mini-CSS-Parser** versteht nur Regeln `Selektor { prop: wert; }`, nur `var(--ac-<key>)`
   (auflösbar auf `tokens.json → autocomplete.*`) und nur px-Literale. Reiche CSS-Strukturen
   (Nesting, andere Einheiten, `@media`) würden den Lauf abbrechen — sie werden nicht
   interpretiert.
4. **`box-shadow: 0 2px 8px #0003`** wird als einziger Schatten mit spread 0 gelesen (CSS kennt
   hier keinen Spread); 4-stelliges Hex wird auf 8-stellig erweitert (`#0003` → `#00000033`,
   also Schwarz mit Alpha 0.2). Andere Schatten-Formate würden abbrechen.
5. **Popupsichtbarkeit** wird aus `accessibility.rules.json → projections.popupVisible` genommen,
   nicht aus der SCXML-Variable `visible` oder dem Overlay-Reveal-Handshake. Die Zustandsmaschinen
   (`behavior.scxml` der drei Komponenten) werden **nicht simuliert**; sie dienen nur der
   Validierung (jede `phase` existiert als State) und dem Captions-Text.
6. **Priorität der Status-Meldung** (disabled → selected-Vorlage → Phase-Meldung) ist in der
   Definition nicht als Regel fixiert; der Adapter ableitet sie aus README-Formulierungen
   („Bei selected … der Status nutzt die selected-Vorlage“, „Bei disabled …“).
7. **Vertikale Position des Input-Textes** (y=12) ist eine berechnete Vertikalzentrierung
   aus `padding: 0 12px`, Höhe 44 und Zeilenhöhe 20; das CSS legt sie nicht fest.
8. **Schriftstyle „Regular“ / Weight 400** ist hartkodiert: `tokens.json` nennt nur die
   Familien „Inter“, keinen Style; die Checks erwarten 400.
9. **Schichtnamen** sind Adapter-Wahl (auf Basis von `anatomy` und Rollen): `Overlay Surface`,
   `Overlay Scroll Viewport`, `Overlay Scroll Content`, `Listbox`, `Option: <key>`, `Label`,
   `Query`/`Placeholder`, `Message Row`/`Message`, `Status`, `Hinweis <id>`. Eine andere,
   gleichberechtigte Benennung wäre möglich.
10. **Seitenraster und Seitentexte** (Rand 64, 5 Spalten, Spaltenabstand 48, Zeilenabstand 56,
    Titel 24/32, Captions 12 px, Quellenzeile, Laufpfad-String „run-03/builder-a“) sind freie
    Exportrahmen-Wahl laut README; der Laufpfad ist im Skript hartkodiert.
11. **ARIA/semantik wird nicht in die Datei geschrieben.** Rollen (combobox/listbox/option/status),
    `aria-expanded`, `aria-selected`, `aria-live` aus `accessibility.html` erscheinen nur als
    Schichtnamen und Caption-Text. Das ist mit `accessibility.rules.json → designTarget`
    vereinbar („semantic annotations, not a claim of screenreader behaviour on a design
    canvas“), bedeutet aber: die semantischen Attribute sind aus der Datei nicht maschinenlesbar
    zurückgewinnbar.
12. **Textbreiten** (z. B. „Berlin“ = 38 px) stammen aus echten Textmetriken (CanvasKit/Skia)
    der gepinnten Umgebung — abhängig von den dort verfügbaren Inter-Schriften.
13. **Determinismus-Garantie ist begrenzt:** Struktur (gerundet auf 4 Dezimalstellen) und PNG
    sind über Läufe stabil (x01/x02); die `.fig`-Bytes sind es nicht (frisches `createdAt` in
    `meta.json`), und das wird auch nicht behauptet.

**Mehdeutigkeiten/Stellen der Definition, die der Adapter auflösen musste:**

14. **`opening` ohne Popup.** Laut `projections.opening.popupVisible=false` ist im
    „opening“-Fall kein Popup sichtbar — trotz des Namens. Das README nennt für die
    Ein-Zeilen-Meldung nur „loading, empty und error“ und sagt, ein verborgenes Popup belege
    keinen Platz; die Sichtbarkeit in `opening` folgt ausschließlich der Projektion.
15. **Leerer, deaktivierter Input.** Das CSS hat sowohl `::placeholder { color: muted }` als
    auch `:disabled { color: disabled }`. Im `disabled`-Fall ist der Input leer (nur
    Placeholder sichtbar); der Adapter wendet die Platzhalter-Regel an (muted), die
    `:disabled`-Textfarbe würde hier nicht sichtbar werden. Der Rand folgt `:disabled`
    (normale border-Farbe, kein Fokusborder).
16. **`error-relay.scxml`** (`components/autocomplete/`) ist nicht an `component.json` gebunden
    und nicht Teil des Quell-Manifests; seine Rolle (offenbar Fehlersimulations-Komponente
    „ResearchErrorRelay“) bleibt aus den erlaubten Quellen unklar. Sie wurde im Lauf nicht
    gelesen (Befund, nicht aufgelöst).
17. **Farbpräzision:** sRGB-Doubles in den Tokens vs. float32 im Kiwi-Format; nur mit
    Toleranz ε=2·10⁻³ vergleichbar. `checks.json` führt erwartete (double) und tatsächliche
    (float32) Werte deshalb leicht unterschiedlich (z. B. 0.39215686274509803 vs.
    0.3921568691730499).
18. **`value` vs. `selectedView`**: Die SCXML kennt `value` (bestätigter Key) und das
    README leitet `selectedView` ab. Im Design ist `selected` der einzige Fall mit `value`;
    die Ableitungsregel wird nicht weiter ausgeführt (z. B. kein Fall, in dem `value` gesetzt
    ist, aber die Phase aktiv ist) — die Definition bietet dafür keine Story.
19. **`ariaActivedescendant`/`ariaSelected`-Semantik** wird ausschließlich visuell
    (Highlight-Füllung) und textuell (Caption „aktiv: …“) abgebildet; es gibt kein
    maschinenlesbares „selected“-Attribut im Dokument (s. Punkt 11).

---

*Quellen dieses Berichts: `autocomplete.fig` (via Original-Reader `@open-pencil/core` 0.16.0
gepinnt), `checks.json`, `generate.mjs`, `preview.png` (visuell), `preview.svg`,
`source-sha256.json`, `components/**` (21 gelesene Dateien), `tools/openpencil/`
(Paketversionen). Keine Git-Befehle, keine anderen Verzeichnisse, keine Artefaktänderungen.*
