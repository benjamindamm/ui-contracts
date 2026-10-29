# REPORT · run-04 · report-check — Builder-Handoffs gegen die eingefrorene Erstbewertung

Auftrag `ac-run04-reviewer-report` (Revision 1, Rolle reviewer, Phase report-check) · Definitionsrevision `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727` (Referenz `autocomplete-openpencil-0.1.0`) · Datum 2026-10-29.

## 1. Aufgabe und Methode

**Aufgabe:** Die Handoffs und Reports der beiden Builder als Daten gegen die eingefrorene Erstbewertung (`first-review.json`), die Originalquellen und die Policy prüfen; Widersprüche und unbelegte Pässe dokumentieren. Prüfgegenstand sind die vom Auftrag ausgewählten Claims (Builder A: 7, Builder B: 14, `claimIds` in `task-report.json`) plus sämtliche deklarierten Gaps, Einschränkungen und Fragen.

**Methode und Grenzen:**

1. Hashverifikation aller fünf Auftragseingaben, beider Producer-Tasks und der eingefrorenen Review-Dateien (Tabelle unten).
2. Abgleich jedes Claim-Werts gegen (a) die eingefrorenen Messwerte: `first-review.json` (`verdicts.{a,b}.cases`: 364 Soll/Ist-Zeilen je Design, 0 Failures; 449/449 unabhängige Readback-Prüfungen je FIG; Countercheck PASS_LIMITED, Exit 0, 562 Checks/FIG; Paar 572/572 exakt gleiche semantische Keys) und das Reviewer-Readback `readback-reviewer.json`; (b) die Originalquellen (relevante Dateien zeilenweise neu gelesen: `components/autocomplete/{layout.css,README.md,stories.json,accessibility.rules.json,component.json,interface.json}`, `components/tokens.json`, `components/overlay/layout.css`, `components/scroll-area/layout.css`, Laufblatt).
3. **Keine neuen nativen Messungen an den FIG-Dateien** (Blindphasen-Aufgabe, Auftragsscope); alle Ist-Belege sind die eingefrorenen Messwerte.

**Input-Verifikation (erwartet = `task-report.json`, gemessen = `shasum -a 256`):**

| Datei | SHA-256 (erwartet, Task) | Ergebnis |
|---|---|---|
| `review/first-review.json` | `99a6589c83663bb6d37ab455a0feddc4bd272be4274f99674d1d321d727f148b` | ✓ |
| `builder-a/handoff-v1.json` | `06c18fee9592256b345022d21246be51f63ed37915c1f8eae68cb3f106f0e5b3` | ✓ |
| `builder-a/REPORT.md` | `fa40a84f6ca21e22beec9a913ec0e3b337ab61f524cfb815f022ae79b963765a` | ✓ |
| `builder-b/handoff-v1.json` | `e519d69142cab7e4c90e5190e2bef92785b07b4abc7caf31b5614cd5ed1f325d` | ✓ |
| `builder-b/REPORT.md` | `9d611f8656bdd70fd84344a1afc9e085f2e4549fd0ae76566ef463f81de099aa` | ✓ |
| `builder-a/task.json` (Producer) | `051a14745998d9fffba819666860e7c0718108180d0718ca5bd2bab98b1d9356` | ✓ |
| `builder-b/task.json` (Producer) | `1dac121a371793add151e5126f6fc9b77b5f81eac7a67df7851d203b8f795f79` | ✓ |
| `review/handoff-blind-v1.json` (frozen) | `05cd0d2bd14a97f557524e0f7e583ba543cff378dd057abeabb74b2b949e22d1` | ✓ |
| `review/countercheck-receipt.json` (frozen) | `ca0b47ab5c6f02b82a76ae7318d3b159a8a9b6f75ec1c458ff95a609c95382d4` | ✓ |
| `review/readback-reviewer.json` (frozen) | `4b80cc36d48889e660b6ec7a67b630b14e9e9c00cd8366c1fafa02df33494f3b` | ✓ |

## 2. Ergebnis je Builder

### Builder A (`ac-run04-builder-a`) — keine Widersprüche

Alle **7/7** ausgewählten Claims sind mit den eingefrorenen Messwerten und den Originalquellen konsistent. Keine unbelegten Pässe. Die zwei deklarierten Gaps/Einschränkungen (exportFigFile-Byteinstabilität, `enabled` unter `inputs.enabled`) sind quellenkonsistent und korrekt dokumentiert (§5.1). Die übrigen Limitations (statisches Design, keine ARIA-Attribute, Font nicht eingebettet, check-receipt nicht deklarierbar) stimmen mit den Originalquellen (`designTarget` in `accessibility.rules.json`, README:3, Exportrahmen README:32) und dem Übergabevertrag überein.

### Builder B (`ac-run04-builder-b`) — keine Widersprüche

Alle **14/14** ausgewählten Claims sind mit den eingefrorenen Messwerten und den Originalquellen konsistent. Keine unbelegten Pässe. Die sieben deklarierten Gaps (REPORT §4) sind jeweils verifiziert oder korrekt als Annahme/Ableitung klassifiziert (§5.2). Die offene Frage `q-msgrow-color` ist nicht blockierend; die Quellen normieren keine Muted-Farbe für die Meldungszeile (§5.2, Antwort).

## 3. Widerspruchstabelle (21 ausgewählte Claims)

Legende: **Soll** = Originalquelle mit Locator; **Ist** = eingefrorene Messung aus `first-review.json` (`verdicts.{a,b}.cases`) und/oder `readback-reviewer.json` (`designs.{a,b}`). Identische Messwerte in beiden FIGs werden gemeinsam zitiert.

| # | Claim (Builder·ID) | Aussage (Kurzfassung) | Soll (Quelle) | Ist (eingefrorene Messung) | Ergebnis |
|---|---|---|---|---|---|
| A1 | A·`c-cases` (explicit) | stories.json definiert genau die zehn Fälle mit inputs, Ergebnisrecords, activeKey, value | `src-autocomplete-stories.json` (stories: 10 Einträge) | stories.json enthält exakt diese zehn Fälle (inputs inkl. verschachteltem `enabled`, 0/7 Resultate, activeKey, value); `verdicts.a.caseFrames`: 10 Frames mit den Quellnamen | bestätigt |
| A2 | A·`c-cases-obs` (observation) | fig enthält auf der Seite „Autocomplete“ genau zehn benannte FRAMEs mit den Quellnamen | stories.json (Namen); README:32 (Exportrahmen) | `designs.a.frameNames`: 10×FRAME mit exakt den Quellnamen (beide FIGs); `caseFrames.count=10` | bestätigt |
| A3 | A·`c-fidelity` (derived) | Farben, Typografie, Maße, Ränder, Meldungen aus tokens + drei layout.css + a11y-rules; 0 Abweichungen | tokens `autocomplete.*`; autocomplete/layout.css 9–49; overlay/layout.css 2–13; scroll-area/layout.css 1–9; accessibility.rules.json (messages/statusPlacement) | alle claim-relevanten eingefrorenen Zeilen pass (449/449 Checks/FIG): 320×44, Radius 8, borderWidth 1, Gaps 8, row 32, max 160, Inter 14/20 (Status 12/20); alle acht Farben exakt (#FFFFFF, #172B4D, #64748B, #CBD5E1, #2563EB, #EAF2FF, #94A3B8, #B91C1C) | bestätigt (Anm. N3) |
| A4 | A·`c-scrollend` (derived) | Listbox y=−(7·32−160)=−64px; aktive letzte Option zuerich im sichtbaren 160-px-Viewport; alle sieben option/* editierbar | tokens `rowHeight`/`maxHeight`; stories scroll-end (7 Resultate, `activeKey=zuerich`); README (scroll-end-Regel) | beide FIGs: `options.count=7`, `highlight.options=[6]`, option6 „Zürich“ `inViewport=true`, Fill #EAF2FF; −64-px-Versatz in `first-review.json#interpretationNotes`; `scrollEnd.lastOptionInViewport=true` | bestätigt |
| A5 | A·`c-disabled-placeholder` (derived) | disabled (leerer Query): Platzhalter in muted #64748B; `:disabled` färbt nur eingegebenen Text | layout.css:32 (`::placeholder`→muted), :33 (`:disabled`→disabled-Textfarbe) | disabled: `inputText.text='Stadt suchen …'`, `inputText.color='#64748B'` (beide FIGs) | bestätigt |
| A6 | A·`c-hidden-popup` (assumption) | closed/opening/selected/disabled: Popupteile als visible=false-Layer erhalten (Designentscheid) | README („verborgener Popup belegt keinen Platz“); Definition legt Existenz verborgener Teile nicht fest | Annahme, korrekt gelabelt; eingefroren: `surface.visibleCount=0` in genau diesen vier Fällen; `statusGap.afterInput=8` (Status unter Input, keine Platzbelegung) | bestätigt (Annahme, quellenkonsistent) |
| A7 | A·`c-toolchain` (observation) | Ausschliesslich gepinnte Toolchain (core/scene-graph 0.16.0, Lock `ebdba852…`) | `src-runsheet` („Gepinnte Toolchain“, Zeilen 11, 13–19) | Lock-Hash = `ebdba8523251984285705a8b03bc15220d41773131b72c66e7a05706837749e6`; `node_modules`: core 0.16.0, scene-graph 0.16.0 | bestätigt (Anm. N2) |
| B1 | B·`c-cases` (explicit) | Zehn Frame-Namen in Stories-Reihenfolge, je FRAME 320px breit | stories[].id (Datei-Reihenfolge) | 10 Frames in exakt dieser Reihenfolge; `frame.width=320` in allen zehn Fällen (beide FIGs) | bestätigt |
| B2 | B·`c-geometry` (explicit) | Token-Werte: Input 320×44, Radius 8, Border 1, Padding 12, Gaps 8, row 32, max 160, acht Farben, Inter 14/12, lineHeight 20 | tokens `autocomplete.*` (inkl. Base-Referenzen 8/160/32); layout.css Part-Regeln | exakt in allen eingefrorenen Zeilen (449/449 Checks/FIG); Base-Dimensionen `base.gap/max/row` = 8/160/32 | bestätigt |
| B3 | B·`c-popup` (explicit) | Popup: Oberkante = Input-Unterseite + gap (y=80), Breite 320, linke Kante, Radius 8, border 0, surface, Schatten 0 2px 8px #0003 | overlay/layout.css 2–13 | `surface.width=320`, `leftAligned=0`, `topGap=8`, `fill=#FFFFFF`, `radius=8` (beide FIGs); Schatten als DROP_SHADOW beobachtet (`interpretationNotes`; Schatten nicht im Countercheck-Scope, policy `notChecked`) | bestätigt |
| B4 | B·c-viewport (explicit) | Viewport max-height 160, geclippt; Content/Liste ohne Margin/Padding | scroll-area/layout.css 1–9; tokens `maxHeight` | `viewport.clipsContent=true`; Höhe 160 (Listenfälle) / 32 (Meldungsfälle, README „Viewporthöhe … bei Meldungszeilen 32“) | bestätigt |
| B5 | B·`c-status` (explicit) | Status mit gap 8 unter sichtbarem Popup, sonst unter Input; Farbe muted, in error error-Farbe; de-Texte; closed/disabled leer | accessibility.rules.json (`statusPlacement`, `messages`); layout.css 43–49 (error :49) | `statusGap=8` in allen Fällen; Texte exakt je Fall: „“ (closed/disabled), „Suche wird geöffnet.“, „Städte werden geladen.“, „7 Städte verfügbar.“, „Ausgewählt: Berlin.“, „Keine Städte gefunden.“, „Städte konnten nicht geladen werden.“; error: #B91C1C, sonst #64748B | bestätigt |
| B6 | B·`c-focus` (explicit) | Input-Border focus in opening/loading/ready/empty/error, sonst border; Platzhalter muted; disabled-Input mit border-Farbe | layout.css 25–33 | `input.stroke.color=#2563EB` in opening/loading/ready/active/scroll-end/empty/error; `#CBD5E1` in closed/selected/disabled (beide FIGs); disabled-Text muted #64748B | bestätigt |
| B7 | B·`c-msgrow` (derived) | loading/empty/error: eine Meldungszeile im Popup (32px), Status wiederholt; Position/Farbe abgeleitet (keine CSS-Regel) | README „Sichtbare Geometrie“ (eine Zeile, rowHeight); keine `message-row`-Regel in den drei CSS | `popup.messageLine.count=1`, Text exakt, `visible=true`, Farbe #172B4D (geerbter text-Token), Zeile 32px (`viewport.height=32`) — in beiden FIGs; Ableitung korrekt gelabelt (Gap 1) | bestätigt |
| B8 | B·`c-visibility` (explicit) | popupVisible je Phase: loading/ready/empty/error sichtbar, closed/opening/selected/disabled verborgen | accessibility.rules.json `projections`; stories[].phase | `surface.visibleCount=1` (loading/ready/active/scroll-end/empty/error), `=0` (closed/opening/selected/disabled) — beide FIGs | bestätigt |
| B9 | B·`c-scrollend` (derived) | 224-px-Content um −64px im geclippten 160-px-Viewport; zuerich sichtbar und highlighted; 7 Layers; statisch | README (scroll-end-Absatz); stories `activeKey=zuerich` | wie A4: identische Messwerte in fig b (7 Optionen, Highlight [6], `inViewport=true`, Fill #EAF2FF) | bestätigt |
| B10 | B·`c-selected` (explicit) | selected: „Berlin“ im Input, „Ausgewählt: Berlin.“, Popup verborgen | stories selected (`value=berlin`, `query=Berlin`); README | `inputText.text='Berlin'` (#172B4D); Status-Text exakt; `surface.visibleCount=0`; Border #CBD5E1 (closed-Phase) | bestätigt |
| B11 | B·`c-hidden` (derived) | Verborgene Fälle behalten vollen Popup-Subbaum (visible:false); Frame-Höhen wachsen nicht | README (belegt keinen Platz; Teile separat editierbar); component.json `anatomy` | eingefroren: `visibleCount=0` in den vier Fällen; `statusGap.afterInput=8` (Status direkt unter Input → keine Platzbelegung) | bestätigt |
| B12 | B·`c-resultmsg` (derived) | ready/active/scroll-end: „7 Städte verfügbar.“ (results-Vorlage, count=7); kein „ready“-Schlüssel in messages | accessibility.rules.json `messages.results` = „{count} Städte verfügbar.“; stories (je 7 Records) | Status-Text exakt in allen drei Fällen (beide FIGs); `messages` enthält tatsächlich keinen `ready`-Key (Quellencheck) | bestätigt |
| B13 | B·`c-weight` (assumption) | Kein font-weight in den Quellen → Renderer-Default 400 | — (Annahme; Quellen definieren keinen Wert) | keine font-weight-Werte in tokens.json, keine font-weight-Regel in den drei CSS (Quellencheck); 400 im Builder-Readback | bestätigt (Annahme, kein Gegenbeleg) |
| B14 | B·`c-scrollbar` (assumption) | Kein Scrollbar-Visual in den Quellen → keiner eingefügt; Clipping trägt die Semantik | scroll-area/layout.css (nur `overflow-y: auto`) | kein Scrollbar-Layer in den eingefrorenen Messungen; Viewport geclippt (`clipsContent=true`) | bestätigt (Annahme, kein Gegenbeleg) |

**Ergebnis: 0 Widersprüche, 0 unbelegte Pässe — 21/21 Claims bestätigt.**

## 4. Anmerkungen (keine Widersprüche)

- **N1 (Builder B, Node-Zählung):** „163 Nodes“ ist die **CLI-Konvention** (die CLI zählt Document-Root und Canvas nicht); der eingefrorene Parse-Level lautet 165 (`verdicts.b.totalNodes`). Die Konvention ist in B-REPORT §1/§7 dokumentiert, die Pro-Fall-Aufschlüsselung (closed 10, opening 10, loading 12, ready 24, active 24, scroll-end 24, selected 24, empty 12, error 12, disabled 10 = 162) + 1 Seitentitel ergibt exakt 163. Präzisionsanmerkung, keine Abweichung.
- **N2 (Builder A, `c-toolchain`):** Die Teil-Aussage „die Skripte importieren nichts anderes“ ist in dieser Phase **nicht prüfbar**: `build-fig.mjs`/`readback.mjs` sind keine Eingaben dieses Auftrags. Die Toolchain-Bindung selbst (Lock-Hash, Core/Scene-Graph-Versionen) ist verifiziert (A7). Keine Abweichung.
- **N3 (Builder A, `c-fidelity`):** „197 Stichproben, 0 Abweichungen“ bezieht sich auf A's eigenes `readback.json` (Builder-Artefakt, keine Aufgabeingabe). Die Substanz (0 Abweichungen auf diesen Messgrössen) ist unabhängig durch die eingefrorenen 449/449 Checks je FIG bestätigt.
- **N4 (Builder A, `c-cases`):** „enabled unter `inputs.enabled`“ ist eine **Eigenschaft der Quelldaten**: `stories.json` verschachtelt `enabled` unter `inputs` (disabled: `inputs.enabled=false`); `interface.json` (CEM) führt `enabled` als Top-Level-Feld (Default `true`). Beide Builder lesen die Quelle konsistent; keine Abweichung, kein Definitionsfehler.
- **N5 (Builder B, Meldungszeilen-Namen):** Teilnamensgebung `message`/`message.text` (fig a) vs. `message-row`/`text` (fig b) ist nicht-normative Teilnamensgebung (`aVsB.nonNormativeDifferences`, README:32); Inhalte und Werte sind identisch.

## 5. Deklarierte Gaps, Einschränkungen und Fragen

### 5.1 Builder A

- **G-A1 — exportFigFile nicht bytestabil** (Handoff-Limitation 2, REPORT §5): Beobachtung mit konkretem Befund (ZIP-Zeitstempel, pro Lauf erzeugtes Dokument-Ids-Präfix, Bytegrösse 31632→31633→31635; nach Normalisierung identische Graphen über 156 Nodes). **Konsistent** mit Laufblatt Zeile 19 (Readback als Zuverlässigkeitsnachweis) und policy `notChecked` „process independence“. Korrekt als begrenzende Beobachtung, nicht als Abweichung vom Soll, dokumentiert. → kein Widerspruch.
- **G-A2 — `enabled` unter `inputs.enabled`** (Claim `c-cases`, REPORT §3): siehe N4. → kein Widerspruch.
- Übrige Limitations (statisches Design/keine Runtime, keine ARIA-Attribute — entspricht `designTarget`; Font Inter nicht eingebettet; check-receipt referenziert `handoffSha256` und ist daher kein deklarierbares Artefakt — stimmt mit Übergabevertrag überein). → keine Widersprüche.

### 5.2 Builder B

- **G-B1 — keine CSS-Regel für die Meldungszeile:** verifiziert — in keiner der drei `layout.css`-Dateien existiert eine `message-row`-Regel; README beschreibt „eine Zeile … rowHeight hoch“. Ableitungen (Höhe 32 aus rowHeight; Position (12,6) aus Option-Padding; Farbe #172B4D als geerbter text-Token) sind korrekt als `derived` gelabelt und im eingefrorenen Ist-Wert ablesbar. → kein Widerspruch.
- **G-B2 — kein Font-weight in den Quellen:** verifiziert (tokens.json und CSS enthalten keinen font-weight-Wert). Annahme (400) dokumentiert. → kein Widerspruch.
- **G-B3 — keine Scrollbar-Definition:** verifiziert (scroll-area/layout.css enthält nur `overflow-y: auto`). Annahme dokumentiert. → kein Widerspruch.
- **G-B4 — verborgene Popup-Bäume behalten Ausdehnung (visible:false an overlay/surface):** konsistent mit eingefrorenen Messungen (`surface.visibleCount=0`, keine Frame-Wachstum, `statusGap.afterInput=8`) und README „belegt keinen Platz“. → kein Widerspruch.
- **G-B5 — leere Status-Texte:** verifiziert — `messages.closed` = `messages.disabled` = „“; eingefroren `status.text=''` bei sichtbarem status-Layer. → kein Widerspruch.
- **G-B6 — deaktivierter Input zeigt Platzhalter:** dieselbe Cascade-Ableitung wie A5 (layout.css:32/33); eingefroren muted #64748B. → kein Widerspruch.
- **G-B7 — Page-Node exportiert 100×100:** Exporter-Beobachtung (OpenPencil-Page-Platzhalter); die Seiteneinrichtung ist frei (README:32 Exportrahmen; `aVsB.nonNormativeDifferences` „Seiteneinrichtung frei“). Ohne neue native Messung in dieser Phase nicht erneut überprüfbar (Auftragsgrenze). → konsistent, kein Widerspruch.
- **`q-msgrow-color` (offen, nicht blockierend) — Antwort:** Die Quellen normieren **keine** Farbe für die Meldungszeile: `accessibility.rules.json` `messages` enthält nur Textvorlagen, tokens.json definiert keinen message-spezifischen Farbtoken, und in den CSS greift für die Zeile nur die Wurzel-Regel `color: var(--ac-text)` (layout.css:7). Der gemessene Wert #172B4D ist damit der geerbte text-Token — B's Ableitung ist korrekt. Ein Muted-Anspruch existiert in der Definition nicht; die Frage bleibt offen und ist nicht blockierend. Eine Entscheidung für muted (oder einen neuen Token) wäre eine **neue Definitionsrevision** und liegt ausserhalb dieses Auftrags.

## 6. Erstbewertung: no-override, kein Nachtrag erforderlich

- **Unverändert:** gemessener SHA-256 von `first-review.json` = `99a6589c83663bb6d37ab455a0feddc4bd272be4274f99674d1d321d727f148b` = Task-Input (`in-first-review`) = eingefrorener Wert. Keine Schreiboperation auf die `review/`-Dateien (Schreibgrenze: nur `review/report-check/`).
- **Gegenprüfung der eingefrorenen Messwerte (Soll-Seite):** alle von der Erstbewertung zitierten Quell-Locators sind exakt (layout.css 25–31/32/33/34–42/43–49; overlay/layout.css 2–13; scroll-area/layout.css 1–9; README 24/26/28/32; accessibility.rules.json `messages`/`projections`/`statusPlacement`; tokens `autocomplete.*` inkl. Base 8/160/32).
- **Gegenprüfung der eingefrorenen Messwerte (Ist-Seite):** alle claim-relevanten Werte sind mit dem unabhängigen Reviewer-Readback (`readback-reviewer.json`) konsistent; keine internen Inkonsistenzen zwischen den 364 Zeilen je Design, `interpretationNotes` und `aVsB` (Fokus-Sets, Status-Texte, Highlights [ ]/[1]/[6], `surface.visibleCount` je Projektion sind in beiden Designs durchgehend konsistent).
- → **Kein Fehler in der Erstbewertung gefunden. Es ist daher kein Nachtrag erforderlich; eine `first-review-addendum.md` wird nicht erzeugt.**

## 7. Abnahmekriterien

| id | Ergebnis | Beleg |
|---|---|---|
| `report-a` | pass | §2, §3 (A1–A7), §4 (N2, N3, N4), §5.1 — alle 7 Claims mit Claim-IDs, Quellen-Locators und gemessenen Werten abgeglichen |
| `report-b` | pass | §2, §3 (B1–B14), §4 (N1, N5), §5.2 — alle 14 Claims inkl. Gaps und `q-msgrow-color` abgeglichen |
| `no-override` | pass | §6 — SHA-256 `99a6589c…` re-verifiziert, Datei unverändert, kein Nachtrag erforderlich |
| `handoff` | pass | `handoff-report-v1.json` gemäss `ui-contracts-handoff/1` (Input-Receipts inkl. Handoff-`taskId`/`revision`, Artefaktliste, Claims, Checks zu allen vier Abnahmekriterien, `ready` ohne blockierende Fragen); Integritätslauf `handoffs.py check` (Temp-Ausgabe) und empfangene JSON als `handoff-check-receipt.json` in diesem Ordner |

## 8. Grenzen

- **Keine neuen nativen Messungen** an den FIG-Dateien (Blindphasen-Aufgabe); alle Ist-Bezugnahmen sind die eingefrorenen Messwerte der Erstbewertung. Daher sind Exporter-Beobachtungen, die nur in den FIGs lesbar wären (z. B. G-B7 Page 100×100), in dieser Phase nicht erneut verifizierbar und bleiben als dokumentierte Beobachtungen bestehen.
- **Builder-Skripte/-Readbacks sind keine Aufgabeingaben:** deren Selbstchecks (A: 197 Stichproben, B: 5 Checks) wurden nicht neu ausgeführt; die Substanz ist über die eingefrorenen unabhängigen Messungen bestätigt (N2, N3).
- **Wertgleichheit ist kein Korrektheitsbeweis**; Originalquellen führen. PASS_LIMITED ist ein begrenzter statischer Nachweis ohne ARIA-/Runtime-Aussagen; `release` bleibt durchgehend `false`.
- Kein Commit, kein Push; alle run-04-Ausgaben bleiben unveröffentlichte Arbeitsdateien.
