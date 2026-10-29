# Builder B — Reproduzierbarkeit Autocomplete

Erzeugung eines editierbaren OpenPencil-Dokuments ausschließlich aus der eingefrorenen
Komponentendefinition unter `components/`. Kopf des Berichts ist eine Selbstauskunft, keine
Bewertung.

## Ausführbefehl

Vom Repo-Root (`/Users/kcnpxcp/Dev/GitHub/ui-contracts`):

```sh
node examples/autocomplete/reproducibility/run-02/builder-b/generate.mjs
```

Das Skript ist eigenständig, benötigt kein Netzwerk und verwendet ausschließlich die gepinnten
Pakete unter `tools/openpencil/node_modules` (`@open-pencil/core` 0.16.0). Es schreibt alle
Artefakte in seinen eigenen Ordner.

Zusätzlich ausgeführte Prüfkommandos:

```sh
node tools/openpencil/node_modules/@open-pencil/cli/bin/openpencil.js info  examples/autocomplete/reproducibility/run-02/builder-b/autocomplete.fig
node tools/openpencil/node_modules/@open-pencil/cli/bin/openpencil.js fonts examples/autocomplete/reproducibility/run-02/builder-b/autocomplete.fig
node tools/openpencil/node_modules/@open-pencil/cli/bin/openpencil.js diff files <lauf-a.fig> <lauf-b.fig>
```

## Vorgehen

1. **Definition gelesen** (22 Dateien, siehe `source-sha256.json`): `components/README.md`,
   `components/library.json`, `components/tokens.json`, alle Dateien von
   `components/autocomplete/`, `components/overlay/`, `components/scroll-area/`.
2. **Fälle ermittelt** aus `components/autocomplete/stories.json` (zehn Einträge) und der
   Zuordnung in `components/autocomplete/README.md` (active/scroll-end = ready mit `activeKey`;
   selected = closed mit `value`; disabled = closed mit `enabled=false`).
3. **Regeln übertragen**: Maße/Farben/Typografie aus `tokens.json`; Geometrie- und
   Zustandsregeln aus den drei `layout.css`; Meldungstexte aus
   `accessibility.rules.json`; Anatomie und Teilebenen aus `component.json`,
   `interface.json` und den `accessibility.html`-Vorlagen.
4. **Dokument gebaut** headless über `@open-pencil/core` (`SceneGraph` + `createNode`,
   `exportFigFile`), ohne Desktop-App, ohne GUI.
5. **Selbstprüfung**: `autocomplete.fig` mit dem Originalreader (`parseFigFile`, Modus `all`)
   zurückgelesen, alle Kennzahlen aus dem gelesenen Graphen gemessen, danach `preview.png`
   (`initCanvasKit` + `headlessRenderNodes`, Scale 2) und `preview.svg` (`renderNodesToSVG`)
   aus genau dieser Datei gerendert.

Aufbau des Dokuments: eine Seite `Autocomplete` mit dem Rahmen `Autocomplete · Übersicht`
(1968 × 750). Darin liegen die zehn Fälle als **Komponenten** `Autocomplete / <id>`; jede
enthält die separat benannten und editierbaren Teile `label`, `input` (mit
`input/placeholder` bzw. `input/value`), `overlay.surface`, `overlay.scroll.viewport`, `list`,
`option/<key>` inkl. `option/<key>/label` und `status`. Die Außenanordnung (Raster,
Seitentitel, Hinweiszeile) ist frei gewählt und nicht Teil der Komponente.

## Dargestellte Fälle

| Fall | Darstellung |
| --- | --- |
| `closed` | Label, Input mit Platzhalter, Statusknoten leer; kein Popup |
| `opening` | wie closed, Input mit Fokusrahmen, Status „Suche wird geöffnet.“; kein Popup (Projektion `popupVisible:false`) |
| `loading` | Query „Be“, Popup mit einer Meldungszeile „Städte werden geladen.“, Status darunter |
| `ready` | 7 Ergebnisse, Viewport 160 px, sichtbar `berlin…koeln`, `wien`/`zuerich` geclippt, Status „7 Städte verfügbar.“ |
| `active` | wie ready, `hamburg` aktiv (Highlight `#EAF2FF`), Status „7 Städte verfügbar.“ |
| `scroll-end` | wie ready, Inhalt um 64 px versetzt, sichtbar `muenchen…zuerich`, `zuerich` aktiv; alle 7 Optionsknoten bleiben erhalten |
| `selected` | Inputwert „Berlin“, Status „Ausgewählt: Berlin.“, kein Popup |
| `empty` | Query „Atlantis“, Popup mit „Keine Städte gefunden.“, Status darunter |
| `error` | Query „Be“, Popup mit „Städte konnten nicht geladen werden.“, Status in `#B91C1C` |
| `disabled` | kein Popup, Input `enabled=false` (Rahmen `#CBD5E2`, Textfarbe `#94A3B8`), Status leer |

## Gemessene Kennzahlen

Alle Werte aus `checks.json`, gemessen am zurückgelesenen `autocomplete.fig`.

- Writer: `@open-pencil/core` 0.16.0, `exportFigFile`
- Reader: `@open-pencil/core` 0.16.0, `parseFigFile`
- Datei: 31 306 Bytes, SHA-256 `fbd3b9934a3e4f28b665392f8fe053e1b896103f56e6cf2e355549b909459f0a`
  (Hash des ausgelieferten Laufs; siehe Grenze „Byte-Determinismus“)
- Knoten: 120 inkl. Seitenknoten, 119 auf der Seite (CLI: 53 FRAME, 56 TEXT, 10 COMPONENT)
- Textknoten: 56, alle editierbar (`allTextNodesEditable: true`)
- Optionsknoten: 21 (7 × 3 Listenfälle), dazu 3 Meldungszeilen
- Statusabstand zum Anker (Popup-Unterkante bzw. Input-Unterkante) in allen Fällen: 8 px
- Viewport: `clipsContent = true`, Höhe `min(n × 32, 160)`; ready/active/scroll-end = 160,
  Meldungsfälle = 32
- Input: 320 × 44, Radius 8, Rahmen 1 px; Fokusrahmen `#2563EB` in opening/loading/ready/
  active/scroll-end/empty/error, sonst `#CBD5E2`
- Vorschauen: `preview.png` 219 034 Bytes (Scale 2),
  `preview.svg` 17 209 Bytes mit 56 `<text>`-Elementen

## Annahmen bei Mehrdeutigkeiten

1. **`opening` bei verborgenem Popup.** `accessibility.rules.json` projiziert
   `popupVisible:false`, liefert aber die Meldung „Suche wird geöffnet.“. Umgesetzt: kein
   Popup, Meldung als Status unter dem Input (Status steht laut README sonst unter dem Input).
2. **Farbe der Meldungszeile in loading/empty/error.** Für den Popupinhalt ist keine eigene
   Textfarbe definiert. Gewählt: `--ac-muted` (#64748B), konsistent zur Statusfarbe; der
   Fehlerfall färbt nur die Statusregion laut CSS auf `--ac-error`.
3. **Platzhalter im disabled-Fall.** `input::placeholder` setzt `--ac-muted`, `input:disabled`
   setzt `color: --ac-disabled`. Wörtlich gewinnt der Platzhalter (muted); zur
   unterscheidbaren Darstellung des Falls wurde `--ac-disabled` (#94A3B8) verwendet.
4. **Leerer Status.** In closed/disabled ist die Meldung laut Regeln `""`; der Statusknoten
   existiert mit leerem Text und den definierten Maßen (Höhe 20, Abstand 8).
5. **Label-/Statusfarbe.** Für `label` ist keine Farbe gesetzt (erbt `--ac-text`), für
   `status` gilt `--ac-muted` bzw. im Fehlerfall `--ac-error`. So umgesetzt.
6. **Textboxen in Input und Option.** `box-sizing: border-box` und Padding 12 px bedeutet
   Innenabstand ab Rahmeninnenseite: Inputtext bei x = 13, Optionstext bei x = 12. Vertikal
   wurde die 20-px-Zeilenbox in der 44-/32-px-Box zentriert.
7. **Status mit fontSize 12 und lineHeight 20.** Die Zeilenbox bleibt 20 px hoch; der Text
   wurde vertikal zentriert.
8. **Clipping-Radius.** Der Radius 8 liegt laut CSS auf `overlay.surface`; Viewport und
   Surface sind schließend (`clipsContent`), sodass die Rundung das Scrollen beschneidet.
9. **`scroll-end`-Versatz.** Inhalt 7 × 32 = 224, Viewport 160 → Versatz 64 px, damit die
   aktive letzte Option vollständig sichtbar ist. Kein dynamisches Scrollen, nur statische
   Darstellung.

## Grenzen

- **Kein interaktives Verhalten.** Das Dokument bildet die statischen Fälle ab; SCXML-Logik,
  Tastatursteuerung und ARIA-Ausführung werden nicht behauptet. Die ARIA-Semantik ist nur
  über Teilenamen und Texte abgebildet.
- **Renderer-Font.** Die Definition verlangt `Inter`; die Schrift ist lokal nicht installiert.
  Die Textknoten tragen `fontFamily: "Inter"` und die Token-Maße, der Headless-Renderer nutzt
  jedoch einen Fallback. Dadurch können Glyphenbreiten/Höhen in den Vorschauen minimal von
  einer Inter-Darstellung abweichen; die Dokumentwerte sind davon unberührt.
- **Byte-Determinismus.** Der Aufbau ist deterministisch: zwei Läufe ergeben laut
  `openpencil diff files` „Documents match“. Die .fig-Bytes unterscheiden sich jedoch in
  19 Bytes der ZIP-Zeitstempel (z. B. Offset 11 und Einträge `thumbnail`/`meta.json`), sodass
  der SHA-256 pro Lauf variiert. Der in `checks.json` genannte Hash gilt für die ausgelieferte
  Datei.
- **Keine GUI geöffnet.** Gearbeitet wurde ausschließlich headless über Dateien/Node; die
  OpenPencil-Desktop-App war nicht verbunden.
- **Keine Änderung der Definition.** `components/` und `tools/` blieben unangetastet; die
  Definition wurde nicht nachträglich angepasst.

## Lieferungen

`generate.mjs`, `autocomplete.fig`, `preview.png`, `preview.svg`, `checks.json`,
`source-sha256.json`, `REPORT.md` — alle in
`examples/autocomplete/reproducibility/run-02/builder-b/`.
