# REPORT · run-04 · Builder A — Autocomplete als editierbares OpenPencil-Design

Auftrag `ac-run04-builder-a` (Revision 1, Rolle builder) · Definitionsrevision `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727` (Referenz `autocomplete-openpencil-0.1.0`) · Definitionsmanifest `74aa9eabcfe7301a0845d230cc1ff4acd6ce14cf0435ec1ed0e6cba0b6e25eb2` (22 Originaldateien, Root `components/`).

## 1. Lieferung (eigener Ausgabeordner)

| Datei | Bytes | SHA-256 |
|---|---|---|
| `autocomplete.fig` | 31635 | `974ecd154e27b816a0410c354e5d655eb4ca27d22a02f3b3de9d88a6e1eaf6dc` |
| `readback.json` | 154571 | `01c729a2f24fbe0953aeb49532eabd8175718bc92944c4c2938c2ccb58cef6c3` |
| `build-fig.mjs` | 14821 | `d463c18b26699e36276dcac9c08c049799a85026345c0959821515d3b3dd7680` |
| `readback.mjs` | 14632 | `cc770f5fd8e49873421da10a80af645efa83687b863820e86f98a073377a27be` |
| `check-receipt.json` | — | entsteht erst durch den Integritätslauf in Abschnitt 8 (referenziert das Handoff und ist daher kein deklarierbares Artefakt) |

Alle Werte des Designs stammen ausschließlich aus den hashgebundenen Originalquellen des Auftrags; es wurden keine Definitionen, Profile oder Werkzeuge geändert, keine früheren Läufe/`output`/`review`/`docs-research` gelesen, keine Webrecherche betrieben, kein Commit/Push ausgeführt.

## 2. Erzeugungspfad

- **Gepinnte Toolchain** (Laufblatt `runsheet-technical.md`): `tools/openpencil/`, `@open-pencil/core` 0.16.0 und `@open-pencil/scene-graph` 0.16.0, Lock `tools/openpencil/package-lock.json` = `ebdba8523251984285705a8b03bc15220d41773131b72c66e7a05706837749e6`.
- **Generierung** (`build-fig.mjs`, Core-API): importiert `SceneGraph` aus `…/@open-pencil/scene-graph/dist/index.js` und `exportFigFile` aus `…/@open-pencil/core/dist/index.js`. Liest `tokens.json`, `autocomplete/stories.json` und `autocomplete/accessibility.rules.json` zur Laufzeit ein und prüft jeden Dateihash gegen `input-manifest.json` (Manifest-Hash zusätzlich gegen den task.json-Wert); Abweichung ⇒ Abbruch.
- **Node-Struktur pro Fall**: `FRAME(<case>)` → `label` (TEXT), `input` (FRAME, radius 8, surface-Fill, 1px-Stroke) → `input.text` (TEXT), `overlay.surface` (FRAME, radius 8, DROP_SHADOW 0/2/8 #0003) → `overlay.scroll.viewport` (FRAME, `clipsContent`) → `listbox` (FRAME) → `option/<key>` (FRAME) → `option.text` (TEXT), bei loading/empty/error zusätzlich `message` (FRAME) → `message.text` (TEXT), sowie `status` (TEXT).
- **Seite**: ein Canvas „Autocomplete“ mit `page-title`, `page-subtitle`, zehn `case-caption/<id>` und den zehn Fäll-frames in zwei Spalten (Spalte 0: closed, opening, loading, ready, active; Spalte 1: scroll-end, selected, empty, error, disabled).
- **Node-Kontingenz** (endgültige Datei): `totalNodes` 156 = Dokument-Root „Document“ (1) + Seite (1) + 12 Seitentexte + 142 Nodes in den zehn Fäll-frames (closed/opening/disabled je 8, loading/empty/error je 10, ready/active/scroll-end/selected je 22).
- **Readback** (`readback.mjs`): `parseFigFile(buffer, { populate: "all" })` aus derselben gepinnten Core-API; speichert native Beobachtungen (Typ, Name, x/y/width/height, fills/strokes/effects, Texte/Fonts, `visible`, `clipsContent`, Editierbarkeit) plus Checks in `readback.json`.
- **CLI-Kreuzprüfung**: `npm run openpencil -- info …/autocomplete.fig` (aus `tools/openpencil/`): `1 pages, 154 nodes` (73 TEXT + 81 FRAME; Root und Canvas werden von der CLI nicht gezählt), Font Inter.

## 3. Verwendete Quellen (Originalquellen des Auftrags)

| id | Pfad | Entnommen |
|---|---|---|
| src-tokens | `components/tokens.json` | alle benannten Werte: width 320, inputHeight 44, rowHeight 32, maxHeight 160, gap/labelGap/statusGap 8, lineHeight 20, fontSize 14, statusFontSize 12, radius 8, borderWidth 1, paddingInline 12, font Inter; Farben surface #ffffff, text #172b4d, muted #64748b, border #cbd5e1, focus #2563eb, highlight #eaf2ff, disabled #94a3b8, error #b91c1c |
| src-stories | `components/autocomplete/stories.json` | die zehn Faelle, `inputs` (label „Stadt auswählen“, placeholder „Stadt suchen …“, query, `inputs.enabled`), Ergebnisrecords (7, inkl. `muenchen` `disabled: true`), `activeKey`, `value` |
| src-a11y-rules | `components/autocomplete/accessibility.rules.json` | Meldungsvorlagen (closed/opening/loading/results/empty/error/selected), `projections.*.popupVisible`, `statusPlacement`, `designTarget` |
| src-layout-ac | `components/autocomplete/layout.css` | Geometrie- und Zustandsregeln mit Zeilenbezug: label (9–13), input (14–24), Fokus-Rand (25–31), `::placeholder` (32), `:disabled` (33), option (34–42), status (43–49) |
| src-layout-ov | `components/overlay/layout.css` | Surface am Inputende plus gap, Breite/linke Kante gleich, surface, radius, `box-shadow 0 2px 8px #0003`, kein border (2–13) |
| src-layout-sa | `components/scroll-area/layout.css` | Viewport `max-height` maxHeight; Content/Liste ohne Margin/Padding (1–9) |
| src-readme-ac | `components/autocomplete/README.md` | Lesereihenfolge, Viewporthöhe = min(Ergebnisanzahl × rowHeight, maxHeight), Meldungsfälle eine Zeile, Statusplatzierung, scroll-end-Regel, `selected` = closed mit value, `disabled` = closed mit `enabled=false`, „verborgener Popup belegt keinen Platz“ |
| src-readme-lib / src-library / src-component / src-interface | Library-/Identitäts-/CEM-Quellen | Kontext: Bibliothekseintrag, Teile (`data-part`), CEM-Signatur (label, placeholder, query, value, results, enabled) |
| src-a11y / src-behavior / src-error-relay / src-ov-* / src-sa-* | Accessibility-/Verhaltensquellen | Kontext; ARIA-Rollen/-Namen und SCXML-Zustände sind in einem statischen Design nicht abbildbar (Abschnitt 7) |
| src-runsheet (technical) | `run-04/runsheet-technical.md` | Revisionsalgorithmus, Toolchain-Bindung, Lesegrenzen, Receipt-Regeln |

Abgeleitete Geometrie-Konstanten (im Build-Skript-Kopf mit Zeilenbezug dokumentiert): INPUT_Y 28, INPUT_BOTTOM 72, POPUP_TOP 80, Input-Text 13/12 (border 1 + paddingInline 12; (44−20)/2), Option-Text 12/6, Status unter sichtbarem Popup bzw. unter dem Input plus statusGap.

## 4. Designentscheidungen, Abweichungen und Definitionslücken (dokumentiert, nicht versteckt)

1. **Verborgene Popups bleiben als Layer erhalten.** In closed, opening, selected und disabled existieren alle Popupteile (`overlay.surface` → `viewport` → `listbox`, ohne Optionen) mit `visible=false`. Sie belegen keinen Platz (Status steht in allen FaelLEN unter dem Input bzw. sichtbaren Popup). Die Definition legt nicht fest, ob Teile verborgener Zustände existieren sollen (README: „verborgener Popup belegt keinen Platz“); die Abnahmekriterien verlangen editierbare Teile in jedem Fall.
2. **Placeholder-Farbe im disabled-Fall = muted #64748b.** Der disabled-Fall hat leeren Query; die explizite `::placeholder`-Regel (layout.css:32) legt muted als Platzhalterfarbe fest, die `:disabled`-Regel (layout.css:33) färbt den eingegebenen Text, der hier nicht existiert (CSS-Cascade). Ein möglicher eingegebener Text wäre in disabled #94a3b8.
3. **Deaktivierte Option `muenchen`:** Option-Text in #94a3b8 (Regel `[aria-disabled="true"]`, layout.css:42); sie bleibt als editierbarer Layer erhalten.
4. **scroll-end-Versatz:** `listbox.y = −(7 × 32 − 160) = −64` px, abgeleitet aus tokens (rowHeight, maxHeight) und den 7 Ergebnissen. Die aktive letzte Option `zuerich` liegt damit bei Viewport-y 128 (Zeilenband 128–160) im sichtbaren 160-px-Viewport; alle sieben `option/*`-Frames bleiben erhalten.
5. **Meldungsfälle loading/empty/error:** Popups = eine Zeile (rowHeight 32) mit `message`/`message.text` („Städte werden geladen.“ / „Keine Städte gefunden.“ / „Städte konnten nicht geladen werden.“); die Listbox bleibt als leerer Rahmen vorhanden.
6. **Status-Texte** folgen `accessibility.rules.json`: closed/disabled leer („“ / keine Meldung im closed-Zustand), ready „7 Städte verfügbar.“, selected „Ausgewählt: Berlin.“ (Template `{label}`), opening „Suche wird geöffnet.“; Status bei error in #b91c1c (layout.css:49).
7. **Seitenausstattung** (zwei Spalten, Kaptionen, Titel/Untertitel) ist freies Layout und verwendet ausschließlich Token-Farben/-Typografie.

## 5. Toolchain-Befund: nicht bytestabiler Export

- `exportFigFile` ist **nicht bytestabil**: aufeinanderfolgende Läufe von `build-fig.mjs` erzeugten Bytefolge und Größe verändernde Dateien (beobachtet 31632 → 31633 → 31635 Bytes).
- Geprüft: Die `.fig` ist ein ZIP-Archiv (`canvas.fig`, `thumbnail.png`, `meta.json`). Unterschiede zwischen zwei Läufen: ZIP-Eintragszeitstempel und ein **pro Lauf erzeugtes Dokument-IDs-Präfix** in der eingebetteten `source`-Record-Struktur jedes Nodes (beobachtet `992180101:3` bzw. `1777195598:3`).
- Nach Normalisierung genau dieses Dokument-Ids sind die beiden geparschten Graphen bei allen 156 Nodes in **allen** Node-Eigenschaften identisch.
- **Konsequenz:** Der SHA-256-Wert in Abschnitt 1 bindet die gelieferte Datei; ein erneuter Build erzeugt eine strukturell identische, aber nicht bytegleiche Datei. Zuverlässiger Reproduktionsnachweis ist der Readback (Abschnitt 6), nicht Bytegleichheit.

## 6. Nachweise (Readback + CLI)

`readback.json` (Format `ui-contracts-readback-receipt/1`, bindet die fig-Hashes aus Abschnitt 1) enthält die Checks — alle `pass`:

| Check | Detail (Auszug) |
|---|---|
| cases | genau zehn Top-level-Frames mit den Quellnamen; alle FRAME |
| parts | in jedem Fall label, input, overlay.surface, overlay.scroll.viewport, listbox, option/*, status als eigene benannte Nodes; Option-Anzahl = stories.json; Popupsichtbarkeit = `accessibility.rules.json` projections |
| fidelity | 197 Stichproben (Farben, Ränder, Größen, Texte, Fonts, Clipping, Listbox-Versatz), 0 Fehler |
| scrollend | Viewport 160, Listbox-Versatz −64, `option/zuerich` bei Viewport-y 128 sichtbar, `allSevenEditable: true`, `activeHighlight: true` |
| readback | `parseFigFile` erfolgreich, Seite „Autocomplete“, 156 Nodes |
| editability | nur native Nodes (CANVAS/FRAME/TEXT), kein Flattening/Bild |

CLI-Kreuzprüfung: `1 pages, 154 nodes` (73 TEXT + 81 FRAME), Font Inter (Abschnitt 2).

## 7. Grenzen und ungeprüfte Bereiche

- **Statisches Design:** Laufzeitverhalten (Fokus, Tastaturnavigation, SCXML-Zustandsübergänge, Error-Relay) ist im `.fig` nicht prüfbar; die formale Definition (`behavior.scxml`, `error-relay.scxml`, Overlay-/ScrollArea-Verhalten) wurde nur als Kontext gelesen.
- **ARIA:** Rollen, Namen, `expanded`/`busy` sind nur als Layer-Namen, Texte und Sichtbarkeit repräsentiert; die Toolchain trägt keine ARIA-Attribute. Dies entspricht dem `designTarget` in `accessibility.rules.json` („semantic annotations, not a claim of screenreader behaviour on a design canvas“).
- **Font:** Inter ist nicht in die `.fig` eingebettet; die Darstellung beim Öffnen setzt den Font voraus.
- **Kein interaktiver Check:** keine Vorschau, kein Screenshot-Vergleich gegen eine Browser-Renderung der CSS-Quellen.
- **Byte-Reproduzierbarkeit** des Exports ist begrenzt (Abschnitt 5).

## 8. Integritätsprüfung (`handoffs.py check`)

- Befehl: `python3 skills/ui-contracts/scripts/handoffs.py check --repo /Users/kcnpxcp/Dev/GitHub/ui-contracts --task /Users/kcnpxcp/Dev/GitHub/ui-contracts/examples/autocomplete/reproducibility/run-04/builder-a/task.json --handoff /Users/kcnpxcp/Dev/GitHub/ui-contracts/examples/autocomplete/reproducibility/run-04/builder-a/handoff-v1.json --output /private/var/folders/9x/61c_c41s5rvbz4bqchv5m8v40000gn/T/opencode/ac-run04-builder-a/handoff-check.json`
- Der Helfer schreibt nur in ein Temp-Verzeichnis außerhalb des Repositories (Laufblatt „Hilfsausgaben“); der für den finalen Lauf festgelegte Temp-Pfad ist oben angegeben. Eventuelle Fehlläufe nutzen abweichende Pfade im selben Verzeichnis und werden nicht als Receipt übernommen.
- Die vom Helfer empfangene JSON-Ausgabe wird anschließend als `check-receipt.json` in diesen Ausgabeordner kopiert. Der Receipt referenziert das Handoff (`handoffSha256`) und die Aufgabe (`taskSha256`) und ist daher kein Artefakt des eigenen Handoffs.
