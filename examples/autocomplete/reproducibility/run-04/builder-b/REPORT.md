# Builder-B-Report · Autocomplete run-04

**Auftrag:** `ac-run04-builder-b` (Revision 1, Rolle builder, Phase normal) — editierbares OpenPencil-Design mit den zehn benannten Fall-Frames aus der eingefrobenen Autocomplete-Definition, exportiert als `autocomplete.fig`, zurückgelesen mit der gepinnten Toolchain.
**Definitionsrevision:** `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`
**Ergebnis:** 5/5 Readback-Checks `pass`; Handoff `handoff-v1.json` mit Status `ready`.

## 1. Erzeugungsweg

Alle Dateien liegen in diesem Ausgabeordner. Verwendet wurde nur die gepinnte Toolchain unter `tools/openpencil/` (`@open-pencil/core` 0.16.0; `package-lock.json`-SHA-256 `ebdba8523251984285705a8b03bc15220d41773131b72c66e7a05706837749e6` = Wert im Laufblatt). `bootstrap.json` und `task.json` wurden nicht verändert.

```bash
# 1) Generator: liest die 22 Originalquellen, verifiziert jeden Manifest-Hash,
#    rechnet das Revisionslabel nach (kompaktes JSON über pfad-sortierte
#    relPath→sha256-Map, siehe Laufblatt), baut die SceneGraph, exportiert .fig
node generate-fig.mjs     # → autocomplete.fig (31.501 B, 1 Seite, 163 Nodes)

# 2) Readback: parseFigFile(bytes, {populate:"all"}) → native Observations
#    (Typ, Name, Maße, Fills/Strokes, Texte, Editierbarkeit) + 5 eigenständige Checks
node readback.mjs         # → readback.json; exit 0 (readback/cases/parts/fidelity/scrollend = pass)

# 3) Unabhängige CLI-Inspektion des Exports
cd tools/openpencil
npm run openpencil -- info ../examples/autocomplete/reproducibility/run-04/builder-b/autocomplete.fig
npm run openpencil -- tree ../examples/autocomplete/reproducibility/run-04/builder-b/autocomplete.fig
# → 1 Page "Autocomplete", 163 Nodes (101 FRAME, 62 TEXT), Font: Inter
```

Beide Skripte verifizieren zusätzlich selbstständig alle 22 Manifest-Hashes und das Revisionslabel; bei Abweichung brechen sie ab (beide Läufe erfolgten ohne Abweichung).

## 2. Quellen (Manifest `input-manifest.json`, Root `components/`, 22 Einträge)

Manifest: `examples/autocomplete/reproducibility/run-04/input-manifest.json`, SHA-256 `74aa9eabcfe7301a0845d230cc1ff4acd6ce14cf0435ec1ed0e6cba0b6e25eb2` (identisch zu `task.json` → `definition.manifest`). Alle Pfade sind repo-intern, keine URL-Ableitung.

| relativer Pfad (unter `components/`) | SHA-256 |
|---|---|
| `README.md` | `b87d16ec9caba56e9f1e1da9b7f93492fda7a2447802214f22747aeca5fa5894` |
| `autocomplete/README.md` | `1f3e8de5630ee2393f3a081afd5c7c710234249ebadea08724899d8e028897d3` |
| `autocomplete/accessibility.html` | `dc00e567ffb0d463350451a9a0d938c9e6a068916e40054133613cca4694e470` |
| `autocomplete/accessibility.rules.json` | `f018316c156e3525a9f66cde07bc987bb68ee88fd698a11a469a799e89cb6ae2` |
| `autocomplete/behavior.scxml` | `a87176827ba56e383e6f1517cc7810fb900b6f6f02eb14c29f8df618cc2fd1ef` |
| `autocomplete/component.json` | `feb6ffda90a142869e39bffdedfa67807b5fc60e50617adf3c7333812cb00d63` |
| `autocomplete/error-relay.scxml` | `a9cd35123a7deeed043162145ad1e456600ebda5ffac43a19e61c10f163bb312` |
| `autocomplete/interface.json` | `d5db745ebf8e305093bc7bb11b396943a1bbdbc2790c2cd462e6f4152a113222` |
| `autocomplete/layout.css` | `1f5a72dd6e5523c8aea78f87ae2888c7b980234c3c6b0a4f30558b6a77567d42` |
| `autocomplete/stories.json` | `eb69c4a1ce65098612d82849d1dd62e22986e88ba65a4d3374991a9fe8d79f3d` |
| `library.json` | `23619a328ab3586163ac03152b80c56c34f09c23703973c1d6371c0d9dfdaa29` |
| `overlay/accessibility.html` | `b0acf5f55f72102a7a70f7128d896fc755d9c400b56b1c3cfd6bd3fb7118b037` |
| `overlay/behavior.scxml` | `e6de18363938212f25e7cfac2ad7104f20639d37cb5a4d0c2ac332a0e902baa8` |
| `overlay/component.json` | `43772ab7aad26dc45c06aed8782908d0030914a4a734b9e7b00521b38fdac70a` |
| `overlay/interface.json` | `bedd0eee49aaeb81c9ff186c4bf3c7f5ae91c394d967eb4b3dbaf6621fc699f0` |
| `overlay/layout.css` | `3c64e9cd819ed459bf0a7278eb9f032af378d147f8462bc845b4154e002f31f6` |
| `scroll-area/accessibility.html` | `b4b29c9d59e8acc5c908dc23fe68d8aec39237547a0f3f06f04b1c14ab800bd3` |
| `scroll-area/behavior.scxml` | `aa6b7ed43ec3f43e7eccfebf992e82f6d9b66922306ec58c7019123ba90ae8b8` |
| `scroll-area/component.json` | `ac416fc44418d2abf3904b495432027dd4bd76608526459d53d8d14178c7fe01` |
| `scroll-area/interface.json` | `6a6f74bcfecb346b8242c5acadd5badf6aa5b75940b256d608d125c5d164280d` |
| `scroll-area/layout.css` | `a9b58668e5a4fdb1ce52eeb594102e394a336a87cf8aa01692607ab4312bd4b7` |
| `tokens.json` | `828c8296d729c7b6313123c2566f9bea29b4f6817dd1637845cfd6d70d9d37f4` |

## 3. Ableitungsregeln (mit Quellen)

Zielwerte der `--ac-*`-CSS-Variablen kommen aus `tokens.json` `autocomplete.*` (dort `autocomplete.gap/{base.gap}`, `autocomplete.maxHeight/{base.max}`, `autocomplete.rowHeight/{base.row}` referenzieren die `base`-Dimensionen 8/160/32 px).

| Regel im Export | Quelle |
|---|---|
| 10 Frame-Namen und Reihenfolge `closed, opening, loading, ready, active, scroll-end, selected, empty, error, disabled` | `stories.json` → `stories[].id` (in genau dieser Datei-Reihenfolge) |
| Typografie: Inter, 14 px, lineHeight 20; Status 12 px | `autocomplete/layout.css` `[data-component="Autocomplete"]` (font-family/size/line-height/color) + `[data-part="status"]` (status-font-size); Tokens `autocomplete.fontFamily/fontSize/lineHeight/statusFontSize` |
| Label: Höhe = lineHeight (20), Abstand unten = labelGap (8) | `autocomplete/layout.css` `[data-part="label"]` + Token `autocomplete.labelGap` |
| Input: 320×44, Radius 8, Border 1 px solid inside, Innenabstand 12, Flächengrund, `font: inherit` | `autocomplete/layout.css` `[data-part="input"]` + Tokens `autocomplete.width/inputHeight/radius/borderWidth/paddingInline` |
| Fokus-Border (Farbe focus) in den Phasen opening, loading, ready, empty, error | `autocomplete/layout.css` `[data-state="…"] [data-part="input"]` (Zeilen 25–31) |
| Platzhalter in muted; deaktivierter Input: Text disabled, Border border | `autocomplete/layout.css` `::placeholder`-Regel und `[data-part="input"]:disabled` |
| Popup-Fläche: Oberkante = Input-Unterseite + gap (→ y = 20+8+44+8 = 80), gleiche Breite (320), Radius 8, `border: 0`, Schatten `0 2px 8px #0003`, Z-index 10 | `overlay/layout.css` `[data-part="surface"]` (anchor bottom/left, `margin-top: var(--ac-gap)`) + Tokens `autocomplete.gap/radius` |
| Viewport: `max-height: 160`, `overflow-y: auto`; Content/Listen ohne Padding | `scroll-area/layout.css` `[data-part="viewport"]/[data-part="content"]/[data-part="list"]` + Token `autocomplete.maxHeight` |
| Option: Höhe = rowHeight (32), Padding 6 px vertikal + 12 px horizontal, `flex-shrink: 0`; aktive Option: Hintergrund highlight; deaktivierte Option: Text disabled | `autocomplete/layout.css` `[data-part="option"]`, `[aria-selected="true"]`, `[aria-disabled="true"]` |
| Status: unter sichtbarem Popup, sonst unter Input (statusGap 8); Farbe muted; in error: Farbe error | `accessibility.rules.json` → `statusPlacement` + `autocomplete/layout.css` `[data-part="status"]` (inkl. `[data-state="error"]`-Regel) |
| Meldetexte (de): opening „Suche wird geöffnet.", loading „Städte werden geladen.", empty „Keine Städte gefunden.", error „Städte konnten nicht geladen werden.", selected „Ausgewählt: {label}.", closed/disabled leer | `accessibility.rules.json` → `messages` |
| Status in ready/active/scroll-end: „7 Städte verfügbar." (Template `results` mit `count = 7` Ergebnisrecords) | `accessibility.rules.json` → `messages.results` + `stories.json` (7 Ergebnisrecords in diesen Fällen) |
| Popup sichtbar/verborgen je Phase (loading/ready/empty/error sichtbar; closed/opening/selected/disabled verborgen) | `accessibility.rules.json` → `projections[].popupVisible` (active/scroll-end = ready, selected/disabled = closed gemäß `stories.json` `phase`) |
| Aktive Option: `active` → `hamburg` (2. Option), `scroll-end` → `zuerich` (7. Option); Highlight nur bei aktiver Option | `stories.json` → `activeKey` + `accessibility.rules.json` → `selection.ariaSelected` + CSS-Regel `[aria-selected="true"]` |
| `selected`: Label des `value` („Berlin") im Input, Status aus `selected`-Vorlage, Popup verborgen | `stories.json` → `value: "berlin"` + `autocomplete/README.md` „Sichtbare Geometrie" („Bei selected steht das zu value gehörige Label im Input …") |
| `disabled`: keine Popupteile sichtbar | `autocomplete/README.md` („Bei disabled sind keine Popupteile sichtbar.") + `stories.json` → `enabled: false` |
| loading/empty/error: eine Meldungszeile im Popupinhalt (Höhe rowHeight 32), Status wiederholt den Text darunter | `autocomplete/README.md` „Sichtbare Geometrie" („zeigt der Popupinhalt eine Zeile mit der entsprechenden Meldung …") |
| Viewporthöhe bei Ergebnislisten: `min(Anzahl × rowHeight, maxHeight)` = `min(7×32, 160)` = 160; bei Meldungszeilen 32; verborgener Popup belegt keinen Platz | `autocomplete/README.md` „Sichtbare Geometrie" + Tokens `autocomplete.rowHeight/maxHeight` |
| `scroll-end`: Content in geclipptem Viewport um −64 px versetzt (224 px Content − 160 px Viewport), sodass die aktive letzte Option sichtbar ist; alle 7 Ergebnislayer bleiben erhalten; statische Darstellung | `autocomplete/README.md` „Sichtbare Geometrie" (scroll-end-Absatz) + `stories.json` → `activeKey: "zuerich"` |
| Anordnung: Autocomplete = label + input + overlay(Overlay-Komponente, anchorPart `input`) mit scroll(ScrollArea-Komponente, contentPart `list`) | `component.json` → `composition`/`anatomy` |
| Äußere Anordnung (2×5-Raster, Seitentitel, Abstand 40 px) frei; Fall als benannte Frame-Gruppe | `autocomplete/README.md` „Exportrahmen" |

Farbwerte (srgb-Komponenten aus `tokens.json`, im Export als Hex): surface `#ffffff`, text `#172b4d`, muted `#64748b`, border `#cbd5e1`, focus `#2563eb`, highlight `#eaf2ff`, disabled `#94a3b8`, error `#b91c1c`. Schatten-Effekt: `0 2px 8px #0003` → Drop-Shadow (0, 2), Radius 8, `#00000033` 1:1.

## 4. Gaps und dokumentierte Abweichungen

1. **Keine CSS-Regel für die Meldungszeile.** In keiner der drei `layout.css`-Dateien existiert eine `[data-part="message-row"]`-Regel; die Zeile wird nur im README („eine Zeile … rowHeight hoch") beschrieben. → Höhe 32 aus `rowHeight`; Textposition (12, 6) und Textfarbe (geerbter `text`-Token über die Wurzel-Regel `color: var(--ac-text)`) sind eine **Ableitung** aus der Option-Zeilen-Metrik bzw. der CSS-Kaskade, nicht ein expliziter Quellwert.
2. **Kein Font-weight in den Quellen.** → Renderer-Default **400** in allen Text-Layern (im Readback verifiziert: `fontWeight: 400` nach Export und Import).
3. **Keine Scrollbar-Definition.** `overflow-y: auto` ist die einzige Quellenregel; ein Scrollbar-Visual existiert in den Quellen nicht. → Kein Scrollbar-Layer eingefügt; der Clipping-Viewport (320×160, Content 320×224) trägt die Semantik.
4. **Verborgene Popup-Bäume behalten Ausdehnung.** Für `closed/opening/selected/disabled` bleibt der vollständige 160-px-Popup-Subbaum im Layerbaum, mit `visible: false` an `overlay/surface`. Begründung: Abnahme verlangt alle Teile „getrennt editierbar"; Sichtbarkeit ist Zustandsdatum (`popupVisible`). Frame-Höhen werden ohne den verborgenen Popup berechnet („belegt keinen Platz"), wachsen also nicht.
5. **Leere Status-Texte.** `messages.closed` und `messages.disabled` sind leer → die `status`-Layer existieren editierbar mit leeren String.
6. **Deaktivierter Input zeigt Platzhalter.** `disabled`-Fall mit leerem Query: der sichtbare Text ist der Platzhalter → muted-Regel (`::placeholder`), nicht die `:disabled`-Textfarbe; die `:disabled`-Regel gilt für eingegebenen Text. (Abbildregel in `readback.mjs`, Zeile 146.)
7. **Page-Node exportiert als 100×100.** Der OpenPencil-Page-Knoten selbst trägt im Readback 100×100; die tatsächliche Ausdehnung des Blattes ergibt sich aus den Frame-Positionen (2 Spalten × 5 Zeilen ab 40 px). Beobachtung am Export, keine Regel der Definition.

## 5. Grenzen (keine Freigabe darüber hinaus)

- **Kein Runtime, keine Interaktion.** Der Export stellt die benannten Designzustände dar; Tastatursteuerung, Fokusfluss, Live-Regionen und SCXML-Verhalten werden nicht ausgeführt. Die Quellen sagen dies selbst voraus: `component.json` → `targetScope.openpencil` („No interactive combobox behaviour or ARIA execution claimed"), `accessibility.rules.json` → `designTarget` (semantische Annotationen), `README.md` („interaktive Canvas-Preview wird nicht gefordert").
- **Statisches Scroll-Bild.** `scroll-end` ist der Endzustand mit festem Content-Offset; dynamisches Scrollen ist nicht versprochen (README scroll-end-Absatz).
- **Font-Metriken viewer-abhängig.** „Inter" wird als Schriftname referenziert; exakte Glyphen-/Breitenmetriken hängen vom viewerseitigen Font-Fallback ab. Namen, Größen, Gewichte und Zeilenhöhen sind im Readback verifiziert.
- **Exporter-Kopplung.** Die Node-IDs in `readback.json` gehören zur Serialisierung von `@open-pencil/core` 0.16.0; andere Exporter/Versionen erzeugen andere IDs. Werte, Namen, Typen und Hierarchie sind checkbar identisch (5 Checks).
- **Kein Komponenten-Release.** Die Fälle sind editierbare `FRAME`-Gruppen (von der Abnahme ausdrücklich erlaubt); es wird keine Bibliotheksfreigabe erklärt (durchgehend `release: false`).

## 6. Hilfsausgaben

- **Handoff-Prüfung:** `handoffs.py check` (Skill-Hilfswerkzeug) wurde auf `handoff-v1.json` ausgeführt und liefert `HANDOFF_READY`. Der Tool-Output lag im Temp-Verzeichnis außerhalb des Repositories; die empfangene JSON-Ausgabe wurde als `handoff-check-receipt.json` in diesen Ausgabeordner kopiert. Dort sind u. a. `overall: "HANDOFF_READY"`, `handoffSha256` und `taskSha256` hashgebunden.
- **Bootstrap/Übriges:** Das Bootstrap-Receipt (`bootstrap.json`) wurde vor Arbeitsbeginn vorgefunden und nicht verändert. Weitere Helfer-Outputs wurden nicht erzeugt.

## 7. Verifizierte Artefakte

| Datei | Größe | SHA-256 |
|---|---|---|
| `autocomplete.fig` | 31.501 B | `4972198fe30b878f6e16733450c45acd9fbe4362235c590fce8016b40e6e47df` |
| `readback.json` | (siehe Datei) | in `handoff-v1.json` hashgebunden |
| `generate-fig.mjs`, `readback.mjs` | (siehe Dateien) | in `handoff-v1.json` hashgebunden |

Die fig-Datei-Referenz in `readback.json` (`file.sha256`) stimmt mit dem auf Datenebene gemessenen Wert überein. Node-Zählung: 163 (101 FRAME, 62 TEXT) auf 1 Seite; pro Fall: closed 10, opening 10, loading 12, ready 24, active 24, scroll-end 24, selected 24, empty 12, error 12, disabled 10 Layer (inkl. Titel-Text auf Seitenebene +1).
