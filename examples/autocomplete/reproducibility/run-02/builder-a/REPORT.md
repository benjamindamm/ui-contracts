# Builder A — Autocomplete-Darstellungsfälle als editierbares OpenPencil-Dokument

Selbstauskunft des Exporteurs. Keine Bewertung des Ergebnisses, keine Aussage über andere Läufe.

## Ausführbefehl

Vom Repo-Root (`/Users/kcnpxcp/Dev/GitHub/ui-contracts`):

```sh
node examples/autocomplete/reproducibility/run-02/builder-a/generate.mjs
```

Das Skript schreibt ausschließlich in `examples/autocomplete/reproducibility/run-02/builder-a/` und benötigt kein Netzwerk. Es liest `components/**` und die gepinnten Pakete unter `tools/openpencil/node_modules/` (absolute Modulpfade über `pathToFileURL`, damit die Ausführung nicht von einer lokalen `node_modules` im Ausgabeordner abhängt).

## Informationsgrenze

Gelesen wurden ausschließlich die 22 Dateien unter `components/` (Autocomplete, Overlay, ScrollArea, `library.json`, `tokens.json`) sowie technische Dateien in `tools/openpencil/` (README, `package.json`, Typdefinitionen von `@open-pencil/core`, `scene-graph`, `cli`). Nicht gelesen: `examples/autocomplete/reproducibility/run-01/**`, `examples/autocomplete/output/**`, `examples/autocomplete/review/**`, `examples/autocomplete/reference.json`, `docs/**`, `scripts/**`, Root-`README.md`/`TASKS.md`, Git-Historie, `builder-b/`. Die GUI der OpenPencil-App wurde nicht geöffnet; es lief kein `openpencil eval` gegen die App, nur Node/headless über Dateien.

## Vorgehen

1. **Definition auswerten.** `tokens.json` wird mit Aliasauflösung (`{base.gap}`, `{base.max}`, `{base.row}`) gelesen. Die zehn Fälle stammen aus `stories.json` (IDs, `phase`, `inputs`, `results`, `activeKey`, `value`). Sichtbarkeit des Popups und Meldungstexte stammen aus `accessibility.rules.json` (`projections`, `messages`, `statusPlacement`). Anatomie und Teilebenen stammen aus `component.json` (`anatomy`), `interface.json` (`cssParts`), den drei `layout.css`-Dateien und den SCXML-Zuständen.
2. **Dokument bauen.** `new SceneGraph()`, `new FigmaAPI(graph)`; Knoten über die Figma-Plugin-API (`createFrame`, `createText`, `resize`, `fills`, `strokes`, `cornerRadius`, `clipsContent`, `effects`). Feste GUID-Session (`setIdSession(1618)`) für stabile Knoten-IDs.
3. **Export.** `initCanvasKit()` + `exportFigFile(graph, ck, undefined, pageId, true)` schreibt `autocomplete.fig` inkl. Thumbnail.
4. **Rückleseprüfung.** Die geschriebene Datei wird von der Platte gelesen und mit `parseFigFile(..., { populate: 'all' })` geöffnet. Alle Messwerte in `checks.json` stammen aus diesem zurückgelesenen Graphen.
5. **Vorschau.** `headlessRenderNodes(parsed, pageId, <alle Top-Level-Knoten>, { scale: 1 })` rendert `preview.png` aus dem zurückgelesenen Dokument.
6. **Prüfprotokolle.** `checks.json` (Bytes, Knoten-, Textknoten-, Fallmessungen) und `source-sha256.json` (SHA-256 der 22 gelesenen Definitionsdateien) werden im selben Lauf erzeugt.

### Aufbau pro Fall

Jeder Fall ist ein Frame `Autocomplete / <id>` mit den Kindknoten `label`, `input` (mit `input text`), optional `overlay surface` → `scroll viewport` → `list` → `option <key>` (mit `option label`) bzw. `message row` (mit `message text`), und `status`. Zusätzlich liegt außerhalb der Fallframes eine Seitenüberschrift und je eine Fallbeschriftung (`closed`, `opening`, …) auf der Seite.

Geometrie aus den Tokens: Breite 320, Labelhöhe 20 mit `labelGap` 8, Input 44 hoch bei y=28, Popup-Oberkante bei y=80 (`inputHeight + gap`), gleiche Breite und linke Kante wie der Input, Viewport `min(Zeilen × 32, 160)`, Zeilen 32 hoch mit Text bei y=6 und `paddingInline` 12, Status `statusGap` 8 unter Popup bzw. unter Input, Statuszeile 20 hoch mit Schriftgröße 12. Radius 8, Rahmen 1 px innen, Schatten `0 2px 8px #0003` als Drop Shadow (Offset 0/2, Radius 8, Deckkraft 0,2), Schrift Inter 14/20.

## Dargestellte Fälle

| Fall | Popup | Viewport | Zeilen/Content | Status | Input |
| --- | --- | --- | --- | --- | --- |
| closed | nein | – | – | `""` | Platzhalter „Stadt suchen …" (muted) |
| opening | nein (Projektion `popupVisible:false`) | – | – | „Suche wird geöffnet." | Platzhalter |
| loading | ja | 32 | Meldungszeile | „Städte werden geladen." | „Be" |
| ready | ja | 160 | 7 Optionen, Content 224 | „7 Städte verfügbar." | Platzhalter |
| active | ja | 160 | 7 Optionen, `hamburg` aktiv | „7 Städte verfügbar." | Platzhalter |
| scroll-end | ja | 160 | 7 Optionen, Content −64 versetzt, `zuerich` aktiv | „7 Städte verfügbar." | Platzhalter |
| selected | nein | – | – | „Ausgewählt: Berlin." | „Berlin" |
| empty | ja | 32 | Meldungszeile | „Keine Städte gefunden." | „Atlantis" |
| error | ja | 32 | Meldungszeile | „Städte konnten nicht geladen werden." (error-Farbe) | „Be" |
| disabled | nein | – | – | `""` | Platzhalter in `disabled`-Farbe, Rahmen `border` |

Aktive Option: Hintergrund `highlight` (#EAF2FF). Deaktivierte Option (`muenchen`): Textfarbe `disabled` (#94A3B8), nicht aktiv. Fokusrahmen (`focus` #2563EB) auf dem Input in opening, loading, ready, active, scroll-end, empty, error; `border` in closed, selected, disabled.

## Annahmen bei Mehrdeutigkeiten

1. **opening zeigt kein Popup.** `stories.json` nennt `phase: opening`, `accessibility.rules.json` projiziert `popupVisible:false`, `expanded:false`. Die Meldung „Suche wird geöffnet." steht daher als Status unter dem Input, obwohl der Popupinhalt selbst nicht sichtbar ist.
2. **loading/empty/error: eine Meldungszeile.** Aus „Bei loading, empty und error zeigt der Popupinhalt eine Zeile mit der entsprechenden Meldung" folgt genau eine Zeile à `rowHeight` 32 als Popupinhalt; die Viewporthöhe ist damit 32. Die Zeile heißt `message row` und ist bewusst keine `option`, weil keine Ergebnisrecords existieren. Die `list` bleibt als Teil mit Höhe 0 erhalten.
3. **loading/empty/error: Meldungstext = Statusmeldung.** `accessibility.rules.json` liefert nur eine Meldungsvorlage je Zustand; Popupzeile und Statusregion verwenden denselben Text („die Statusregion wiederholt den Text").
4. **Statusfarbe bei error.** `layout.css` setzt `[data-state="error"] [data-part="status"]` auf `error`; die Popupzeile bleibt `muted`.
5. **active und scroll-end sind ready.** `layout.css` adressiert `[data-state="ready"]`; die beiden Fälle erben damit den Fokusrahmen und die ready-Statusvorlage. `active` hat `activeKey: hamburg` (Index 1) und benötigt kein Scrollen.
6. **scroll-end-Versatz.** Viewport 160 bei 7×32 = 224 Inhalt. Der Versatz wird aus der aktiven letzten Option berechnet: `6×32 − (160 − 32) = 64` px nach oben. Alle sieben Optionen bleiben als Knoten erhalten; der Viewport clippt. `muenchen` (deaktiviert) wird dadurch sichtbar.
7. **selected.** `phase: closed` mit `value: berlin`; im Input steht das Label des bestätigten Werts („Berlin") in normaler Textfarbe, kein Popup, Status aus der `selected`-Vorlage mit `{label}` = „Berlin".
8. **Leerer Status bleibt als Knoten.** „Ohne Meldung ist sein Text leer" — der Textknoten `status` bleibt mit leerem `characters` und Höhe 20 erhalten (closed, disabled), statt entfernt zu werden.
9. **Keine Scrollbalken-Darstellung.** Die Definition nennt keine Scrollbar-Regel; gezeichnet wird nur der geclippte Viewport.
10. **Seitliche Anordnung.** Zwei Spalten, Fallreihenfolge wie in `stories.json`, Fallbeschriftungen und Seitenüberschrift als freie Hinweise gemäß Exportrahmen.

## Grenzen

- Kein interaktives Verhalten: keine Tastatur-/Fokuslogik, keine SCXML-Ausführung, keine Behauptung von Screenreader-Verhalten. Die Datei bildet die zehn benannten statischen Zustände ab.
- `scroll-end` ist eine statische Momentaufnahme des Versatzes, kein lauffähiges Scrollen.
- Die Statusregionen sind sichtbare Textknoten; ARIA-Rollen/-Zustände (`expanded`, `busy`, `aria-selected`, `aria-disabled`) werden nur visuell und über die Knotennamen/Benennung abgebildet, nicht als Semantik ausgeführt.
- Reproduzierbarkeit: Designinhalte (`canvas.fig`, `thumbnail.png`) sind zwischen Läufen byte-identisch (gleiche CRC). `exportFigFile` schreibt jedoch einen `createdAt`-Zeitstempel in `meta.json` und aktuelle ZIP-mtimes; beides normalisiert `generate.mjs` auf einen festen Wert (`2026-01-01T00:00:00.000Z`), damit die gelieferte `.fig` byte-stabil ist. Die Designinhalte werden dabei nicht verändert.
- Für die Darstellung wird ausschließlich die mitgelieferte Inter-Schrift aus `@open-pencil/core/assets` verwendet.
- Die OpenPencil-Desktop-App war nicht verbunden; es wurde keine GUI geöffnet.

## Gemessene Kennzahlen (aus `checks.json`, zurückgelesene Datei)

- Writer: `@open-pencil/core 0.16.0 · exportFigFile`; Reader: `@open-pencil/core 0.16.0 · parseFigFile`
- Datei: `autocomplete.fig`, 60 025 Bytes
- Seiten: 1 (`Autocomplete`), Fallframes: 10
- Knoten gesamt (inkl. Root/Seite): 129
- Textknoten: 65, davon editierbar (Text, `fontName.family`, `fontSize > 0` über die Plugin-API lesbar): 65
- Alle zehn Fälle: gemessene Werte entsprechen den Erwartungen (`allCasesMatch: true`)
- SHA-256 der Lieferungen:
  - `autocomplete.fig` `f79ff07fd70d4775c344b0d8b0da8d33be1bc0c355751b1bc8de33c61a6d7da0`
  - `preview.png` `36a216a4e62b4ed2610109de6e70d204e6dd6fdccf36939855af9a9c76ebf003`
  - `checks.json` `f2834c1c844ba7f486f9815a0a13897ebffb8782eb1e11d5487aa801df74fca7`
  - `generate.mjs` `54d51ff7185634f24fcad825542f7f33d1cd750c32c4c967a1a5da38bcaceaad`
  - `source-sha256.json` `f9337147f57a8417d231828ceddde57b93a512b61b6cee275ae12f17df0cf27c`

Zwei aufeinanderfolgende Läufe erzeugten dieselben Hashes für `autocomplete.fig` und `preview.png`.

## Lieferungen

| Datei | Inhalt |
| --- | --- |
| `generate.mjs` | deterministischer Generator (Design + Export + Rückleseprüfung + Vorschau + Protokolle) |
| `autocomplete.fig` | editierbares OpenPencil-Dokument mit 10 benannten Fällen |
| `preview.png` | headless aus der geschriebenen `.fig` gerenderte Vorschau |
| `checks.json` | Writer/Reader, Bytes, Knoten, Textknoten, Messwerte je Fall |
| `source-sha256.json` | SHA-256 der 22 gelesenen Definitionsdateien |
| `REPORT.md` | diese Selbstauskunft |
