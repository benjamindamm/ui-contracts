# Prüfbericht run-02 — Autocomplete (Phase 2)

**Gegenstand:** zwei unabhängig erzeugte, editierbare OpenPencil-Designs (`builder-a/autocomplete.fig`, `builder-b/autocomplete.fig`)
**Definitionsrevision:** `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`
**Versiegelte Kriterien:** `preregistered.json` (101 Kriterien: 67 explicit, 22 derived, 12 underdetermined), `preregistration-seal.json`
**Prüfer:** unabhängige Messung an den Originaldateien; Builderberichte nur als Selbstauskunft (Abschnitt 8)

| | Design A | Design B |
| --- | --- | --- |
| **Gesamturteil** | **PASS_MIT_ABWEICHUNGEN** | **PASS_MIT_ABWEICHUNGEN** |
| erfüllt | 96 | 96 |
| verletzt | 4 | 4 |
| nicht anwendbar | 1 | 1 |
| explizit verletzt | 0 | 0 |
| abgeleitet verletzt | 4 | 4 |
| **Paarübereinstimmung** | **1,000 (Band „hoch“)** | |

Die vier Abweichungen je Design haben **eine gemeinsame Ursache**: fehlende maschinenlesbare ARIA-Annotationen (A11Y01, A11Y02, A11Y03, A11Y07). Alle expliziten Kriterien – einschließlich aller zehn Zustände, Texte, Maße, Farben, Typografie und Clipping-Regeln – sind erfüllt.

---

## 1. Auftrag, Informationsgrenze, Unabhängigkeit

Geprüft wurden ausschließlich:

- die 22 Dateien unter `components/**` (unverändert, siehe 4.1),
- `tools/openpencil/README.md`, `tools/openpencil/package.json` (gepinnte Toolchain 0.16.0),
- die versiegelten Kriterien unter `review/`,
- ab Phase 2 die Builder-Ausgaben `builder-a/**`, `builder-b/**`.

Nicht gelesen: `run-01/**`, `examples/autocomplete/output/**`, `examples/autocomplete/review/**`, `examples/autocomplete/reference.json`, `docs/**`, `scripts/**`, Root-`README.md`/`TASKS.md`, Git-Historie. Die Kriterien wurden vor Einsicht in die Builder-Ausgaben geschrieben und nicht geändert.

**Messreihenfolge (eingehalten):** `.fig` messen → `original-*.json` / `normalized-*.json` / Renders → `native-checks.json` → erst danach `REPORT.md`, `checks.json`, `source-sha256.json` lesen → bewerten.

---

## 2. Unterbrechungen der Builder (Provenienz, keine Builder-Ausgabe)

Beide Builder wurden während run-02 mehrfach vom **Step-Limit des Agenten-Harness** unterbrochen und in derselben Session fortgesetzt. Die Angaben stammen vom Koordinator; sie sind nicht aus den Artefakten rekonstruierbar.

| Builder | Stopp 1 | Stopp 2 | Stopp 3 |
| --- | --- | --- | --- |
| **A** | nach reiner Analyse; nur `_probe.mjs`, keine Lieferung | alle Artefakte außer `REPORT.md` | `REPORT.md` geschrieben, `_probe.mjs` entfernt |
| **B** | nach reiner Analyse; keine Dateien | 6 von 7 Lieferungen plus Zwischenartefakt `render-report.json` | `REPORT.md` geschrieben, Zwischenartefakt entfernt, `generate.mjs` erneut ausgeführt |

**Ursache:** ausschließlich Step-Limit, kein Zugriff auf verbotene Eingaben. Jede Fortsetzung nutzte den eigenen vorherigen Kontext derselben Session; kein Builder sah den anderen, run-01 oder frühere Ergebnisse. Der Prüfer (Phase 1) war nicht betroffen.

### Was daraus gilt und was nicht

**Gilt weiterhin:**

- Die beiden Designs sind **voneinander unabhängig** (getrennte Sessions und Kontexte).
- Die **Informationsgrenze** ist nicht verletzt; in Dateien und Berichten finden sich keine Hinweise auf verbotene Quellen.
- Beide Ergebnisse entstanden aus **derselben eingefrorenen Definition** und sind daher vergleichbar.
- Die Artefakte sind **vollständig und prüfbar**; die Bewertung stützt sich auf die Dateien, nicht auf den Entstehungsweg.

**Gilt nicht mehr:**

- **Keine Behauptung eines ununterbrochenen Single-Shot-Laufs.** Es handelt sich um mehrfach fortgesetzte Läufe.
- Keine Aussage über die Zahl tatsächlich ausgeführter Zwischenschritte.
- Keine Aussage, ob ein einmaliger Lauf ohne Stop dasselbe Ergebnis erzeugt hätte.
- A: `_probe.mjs` und B: `render-report.json` sind als Zwischenartefakte **nicht mehr vorhanden** und damit nicht prüfbar.

**Einschätzung:** Die Unterbrechungen mindern die Aussagekraft für **Prozess**-Reproduzierbarkeit (Single-Shot, Step-Zahl), **nicht** für die Bewertung der gelieferten Artefakte. Beide Läufe bleiben kontextgetrennt; die Ergebnisse sind gültige, aber nicht „in einem Zug“ entstandene Stichproben. Wer aus run-02 einen Nachweis für Ein-Schuss-Reproduzierbarkeit ableiten will, würde die Daten überdehnen.

---

## 3. Methode und Werkzeuge

| Schritt | Werkzeug | Ergebnis |
| --- | --- | --- |
| Original lesen | `@open-pencil/core` 0.16.0 `parseFigFile(..., {populate:'all'})` | `original-a.json` (129 Knoten), `original-b.json` (122 Knoten) |
| Normalisieren | `inspect-original.mjs` | `normalized-a.json`, `normalized-b.json` (Fall-, Teil-, Options-, Farb-, Textwerte) |
| Rendern | `render-original.mjs`, CanvasKit `headlessRenderNodes(scale:2)` | `render-a.png` (286 268 B), `render-b.png` (219 034 B) |
| Einzelbeobachtungen | `verify.py --native-only` | `native-checks.json` |
| Bewerten | `verify.py` | `results.json`, `hashes.json` |
| Gegenprüfung | `shasum`, eigene Hashrechnung über `components/**` | 22/22 Dateien unverändert |

Absolute Seitenkoordinaten der Fallgruppen wurden **nicht** bewertet. Gemessen wurden Werte **relativ zur Fallgruppe** (Label, Input, Surface, Viewport, Liste, Optionen, Status) sowie Farben, Fonts, Clipping und Texte. Toleranzen wie in `preregistered.json` 4.2: Maße ±1 px pro Kante, kumulierte Offsets ±2 px, Gesamthöhen ±4 px, Farben ≤3/255 pro Kanal, Schriftgröße ±0.5 px.

**Render-Evidenz:** `render-b.png` ist **byte-identisch** mit `builder-b/preview.png` (`b6d935ee…`), obwohl unabhängig aus der `.fig` erzeugt. `render-a.png` (`d26be652…`) unterscheidet sich von `builder-a/preview.png` (`36a216a4…`), weil A laut REPORT mit `scale:1` gerendert hat, der Prüfer mit `scale:2`; die Inhalte sind visuell deckungsgleich.

---

## 4. Befunde an den Originaldateien

### 4.1 Definitionsunverändertheit (A08)

Alle 22 Dateien unter `components/**` wurden mit `sha256` gehasht. Die Werte stimmen **mit beiden** Builder-Manifesten (`source-sha256.json`) und untereinander überein; es gibt keine Abweichung:

- `components/tokens.json` `828c8296…`, `components/autocomplete/stories.json` `eb69c4a1…`, `components/autocomplete/README.md` `1f3e8de5…` usw. (vollständig in `hashes.json` bzw. den Manifesten).
- Beide Manifeste enthalten exakt dieselben 22 Pfade und Hashes.

**Grenze:** Das in der Aufgabe genannte Revisionskürzel `1d83935f…` ließ sich mit den erlaubten Quellen nicht rekonstruieren (kein dokumentiertes Hash-Schema auffindbar). Geprüft ist damit die **Unverändertheit der Dateien** zwischen Build und Prüfung, nicht die formale Übereinstimmung mit einem Revisionslabel.

### 4.2 Dokumentkennzahlen

| Kennzahl | A | B |
| --- | --- | --- |
| Datei | 60 025 B, `f79ff07f…` | 31 306 B, `fbd3b993…` |
| Seiten | 1 (`Autocomplete`) | 2 (`Page 1` leer, `Autocomplete`) |
| Knoten im Graphen | 129 (inkl. Document-Root/Seite) | 122 (inkl. Document-Root/2 Seiten) |
| CLI `totalNodes` | 127 | 119 |
| Typen | 63 FRAME, 65 TEXT, 1 CANVAS | 54 FRAME, 56 TEXT, 10 COMPONENT, 2 CANVAS |
| Fallcontainer | 10 × FRAME `Autocomplete / <id>` | 10 × COMPONENT `Autocomplete / <id>` |
| Textknoten | 65, davon 2 leere Status | 56, davon 2 leere Status |
| Bitmap-Fills / Vektornetze | 0 / 0 | 0 / 0 |
| Fonts | Inter (400) | Inter (400) |
| Schriftgrößen | 12, 14 (24 nur Seitentitel) | 12, 14 (20 nur Sheet-Titel) |
| Optionen | 21 (7 × 3 Listenfälle) | 21 (7 × 3 Listenfälle) |

Beide Dokumente öffnen mit der gepinnten Toolchain fehlerfrei (A01). Beide enthalten ausschließlich echte TEXT-Knoten, keine Bitmaps, keine Outlines (A06/A07).

### 4.3 Anatomie und Zustände (Beispiele mit Knotenwerten)

**Design A, Fall `ready`** (`0:29`, FRAME, 320 × 268):

| Teil | Knoten | Messwert |
| --- | --- | --- |
| label | `0:30` TEXT | `Stadt auswählen`, 320 × 20 @ y=0, #172B4D, Inter 14/20 |
| input | `0:31` FRAME | 320 × 44 @ y=28, #FFFFFF, Stroke 1 px #2563EB, Radius 8 |
| surface | `0:33` FRAME | 320 × 160 @ y=80, #FFFFFF, 0 Strokes, Radius 8, DROP_SHADOW 0/2, r=8, α=0,2 |
| viewport | `0:34` FRAME | 320 × 160, `clipsContent=true` |
| list | `0:35` FRAME | 320 × 224 (7 × 32) |
| options | `0:36, 0:38, 0:40, 0:42, 0:44, 0:46, 0:48` | je 32 px, Text bei dx=12/dy=6, Highlight nur `hamburg` in `active` |
| status | `0:50` TEXT | y=248, 320 × 20, `7 Städte verfügbar.`, 12 px, #64748B |

**Design B, Fall `ready`** (`0:28`, COMPONENT, 320 × 268): label `0:29`, input `0:30`, surface `0:32` (320 × 160, `clipsContent=true`), viewport `0:33`, list `0:34` (320 × 224), Optionen `0:35, 0:37, …, 0:47`, Status `0:49` @ y=248. Werte wie bei A, mit zwei Unterschieden: Input-Rahmen `#CBD5E2` (Token `#CBD5E1`, Δ1) und Surface mit `clipsContent=true`.

**Zustandsmatrix (beide Designs identisch):**

| Fall | Popup | Viewport | sichtbare Zeilen | Highlight | Statustext |
| --- | --- | --- | --- | --- | --- |
| closed | nein | – | – | – | `""` |
| opening | nein | – | – | – | `Suche wird geöffnet.` |
| loading | ja, 1 Meldungszeile | 32 | 1 Meldung | – | `Städte werden geladen.` |
| ready | ja | 160 | 5 voll, 0 angeschnitten, 2 außerhalb | – | `7 Städte verfügbar.` |
| active | ja | 160 | 5 / 0 / 2 | `hamburg` | `7 Städte verfügbar.` |
| scroll-end | ja | 160 | 5 / 0 / 2 | `zuerich` | `7 Städte verfügbar.` |
| selected | nein | – | – | – | `Ausgewählt: Berlin.` |
| empty | ja, 1 Meldungszeile | 32 | 1 Meldung | – | `Keine Städte gefunden.` |
| error | ja, 1 Meldungszeile | 32 | 1 Meldung | – | `Städte konnten nicht geladen werden.` (Status #B91C1C) |
| disabled | nein | – | – | – | `""` |

**`scroll-end` im Detail (beide):** Liste um **64 px** nach oben versetzt (`list y = −64` relativ zum Viewport). Sichtbar sind `muenchen … zuerich`; `berlin`/`hamburg` liegen vollständig außerhalb. `zuerich` endet exakt bei 160 px (Viewport-Unterkante). Alle **7 Optionsknoten bleiben erhalten** – die zwei geclippten wurden nicht gelöscht (CLIP02/CLIP03). Das ist konsistent mit der Rechnung 7 × 32 = 224, Viewport 160 → 2 geclippte Zeilen; die Formulierung „drei unsichtbare Daten“ in `components/autocomplete/README.md` Z. 26 ist ein Redaktionsfehler (in der Prüfrichtlinie als Annahme AS1 festgehalten).

**Texte:** Label `Stadt auswählen` in 10/10 Fällen; Placeholder `Stadt suchen …` mit **U+2026** (Codepoints geprüft), nicht `...`; `München`, `Köln`, `Zürich` mit korrekten Umlauten; Query `Be` in `loading`/`error`, `Berlin` in `selected`, `Atlantis` in `empty`. Keine Zusatztexte innerhalb der Fallgruppen (TX07).

### 4.4 Geometrie, Farbe, Clipping (aggregiert)

- Komponentenbreite 320, Input 320 × 44 @ y=28, Labelhöhe 20 + 8 px Gap, Popup-Oberkante = Input-Unterkante + 8, gleiche linke Kante, gleiche Breite (6/6 Popup-Fälle).
- Optionszeilen 32 px, Text bei dx=12/dy=6; Statushöhe 20, Statusabstand 8; Fallhöhen 100 / 140 / 268 px.
- Input-Radius 8, 1 px Stroke; Surface-Radius 8, 0 Strokes, weiße Füllung; Schatten `0 2 8`, α 0,2.
- Farben ausschließlich aus den acht Tokens (±3). B weicht beim Input-Rahmen um **1/255** ab (`#CBD5E2`), innerhalb der Toleranz.
- Fokusrahmen `#2563EB` in opening/loading/ready/active/scroll-end/empty/error; `#CBD5E1`(A)/`#CBD5E2`(B) in closed/selected/disabled.
- Genau eine Highlight-Fläche je `active`/`scroll-end`, keine in `ready`; München `#94A3B8`.
- Viewport clippt in allen sechs Popup-Fällen; keine sichtbare Überlappung von Status und Surface; kein angeschnittener Zeilentext.

### 4.5 Accessibility (statisch)

| Prüfpunkt | A | B |
| --- | --- | --- |
| Statusknoten sichtbar, Text korrekt | ja | ja |
| benannte Teile (`label`, `input`, `list`, `option/<key>`, `status`) | ja | ja |
| `combobox`-Annotation/Name | **nein** | **nein** |
| `listbox`-Name + zugänglicher Name `Stadt auswählen` | **nein** | **nein** |
| `aria-selected`/`aria-disabled` maschinenlesbar | **nein** (nur visuell) | **nein** (nur visuell) |
| Input-Name aus Label verknüpft | **nein** | **nein** |
| expanded-Projektion | konventionsbasiert (Fallname) | konventionsbasiert (Fallname) |
| zusätzliche Rollen/Tabstops an Popup/Viewport | nein | nein |

Beide Berichte legen offen, dass ARIA-Rollen/-Zustände „nur visuell und über die Knotennamen“ abgebildet werden (A REPORT Z. 68, B REPORT Z. 117). Das `.fig`-Format dieser Toolchain hat kein Rollenfeld; die Builder hätten `pluginData` nutzen können, taten es aber nur für `layoutDirection`/`textDirection`.

---

## 5. Kriterienbewertung

101 Kriterien, für beide Designs vollständig ausgewertet (1 × `n/a`: A11Y09, nicht statisch prüfbar).

| Gruppe | Kriterien | A pass | A fail | B pass | B fail |
| --- | --- | --- | --- | --- | --- |
| A Artefakt/Editierbarkeit | 12 | 12 | 0 | 12 | 0 |
| ST Zustände | 12 | 12 | 0 | 12 | 0 |
| AN Anatomie | 10 | 10 | 0 | 10 | 0 |
| TX Texte | 9 | 9 | 0 | 9 | 0 |
| GEO Maße | 13 | 13 | 0 | 13 | 0 |
| CLIP Clipping | 8 | 8 | 0 | 8 | 0 |
| COL Farben | 11 | 11 | 0 | 11 | 0 |
| TY Typografie | 5 | 5 | 0 | 5 | 0 |
| A11Y Accessibility | 9 | 4 | 4 (+1 n/a) | 4 | 4 (+1 n/a) |
| FREE Freiheiten | 12 | 12 | 0 | 12 | 0 |

**Nach Klassifikation:** explicit 66/67 erfüllt (A und B), 1 × `n/a` (A11Y09, nicht statisch prüfbar), 0 verletzt; derived 18/22 erfüllt (4 verletzt); underdetermined 12/12 im zulässigen Raum.

### 5.1 Die vier Abweichungen (identisch für A und B)

| ID | Klasse | Befund |
| --- | --- | --- |
| A11Y01 | derived | Input heißt `input`, keine `combobox`-Annotation; `pluginData` enthält nur `layoutDirection`/`textDirection`. |
| A11Y02 | derived | Liste heißt `list` bzw. `overlay.scroll.viewport`, keine `listbox`-Annotation und kein zugänglicher Name `Stadt auswählen`. |
| A11Y03 | derived | `aria-selected`/`aria-disabled` nicht annotiert; die Semantik existiert nur als Füllfarbe `#EAF2FF` bzw. Textfarbe `#94A3B8`. |
| A11Y07 | derived | Label ist Geschwistertext; keine Namensannotation/-verknüpfung am Input. |

Diese vier teilen **eine** Ursache (keine ARIA-Metadaten) und sind keine visuellen oder strukturellen Fehler. Sie sind bewusst nicht als explizit gewertet: Die Definition verlangt in `accessibility.rules.json` `designTarget` ausdrücklich benannte Teile, Label, Statustext sowie aktive/deaktivierte Styles – und diese sind vorhanden. Die Annahme „Rollen sollten maschinenlesbar sein“ war eine frische Prüferannahme (derived), keine ausdrückliche Forderung.

**A11Y05 (explizit) – Auslegung offengelegt:** Beide Designs haben keine `expanded`-Annotation. Der Fallname (`Autocomplete / ready` usw.) plus die Projektionstabelle der Definition bilden den Zustand jedoch eindeutig ab, und beide Berichte legen diese Konvention offen. Das Kriterium erlaubt ausdrücklich eine „dokumentierte Namenskonvention“; ich habe diese weiche Auslegung gewählt und als Grenze dokumentiert. Bei strengerer Lesart (nur maschinenlesbare Annotation) würden beide Designs ein explizites Kriterium verletzen und damit **FAIL** erhalten – der Unterschied ist im Bericht sichtbar, nicht versteckt.

---

## 6. Gesamturteil je Design

Angewandt wurde die versiegelte Regel (`preregistered.json` › `overallJudgementRule`):

1. **Gates:** A01, A02, A04, A05, A06, A07, A08 – **alle erfüllt** (Dokument öffnet, 10 Fälle, getrennte Teile, echte Texte, keine Bitmaps, Definitionen unverändert).
2. **Explizite Verletzungen:** `E = 0` für A und B.
3. **Abgeleitete Verletzungen:** `D = 4` für A und B → Bereich 2–4.

| Bedingung | Ergebnis |
| --- | --- |
| Gate-Verstoß oder `E ≥ 1` oder `D ≥ 5` | nicht erfüllt |
| `E = 0` und `2 ≤ D ≤ 4` | **PASS_MIT_ABWEICHUNGEN** (A und B) |
| `E = 0` und `D ≤ 1` | nicht erfüllt |

**Design A: PASS_MIT_ABWEICHUNGEN** — alle zehn Zustände, Anatomie, Texte, Maße, Farben, Typografie und Clipping-Regeln entsprechen der Definition. Abweichungen ausschließlich bei maschinenlesbaren ARIA-Annotationen.

**Design B: PASS_MIT_ABWEICHUNGEN** — gleiches Bild. Zusätzlich: Input-Rahmen `#CBD5E2` statt `#CBD5E1` (Δ1, innerhalb Toleranz, im REPORT offengelegt), leere Seite `Page 1` (kosmetisch), Sheet 750 px hoch, während der `scroll-end`-Fall 24 px darüber hinausreicht (Seitenlayout, frei).

---

## 7. Paarübereinstimmung (Komponentenebene)

Berechnet nach dem versiegelten Protokoll (Gewichte 0,30 / 0,30 / 0,40; Seitenlayout, technische IDs und Byte-Gleichheit ausgeschlossen):

| Maß | Wert |
| --- | --- |
| `A_struct` (Fall-/Teilemengen, Optionslabels) | **1,000** |
| `A_state` (Popup, activeKey, Inputanzeige, Statustext) | **1,000** |
| `A_vis` (Geometrie, Farbe, Typografie; 199 Merkmale) | **1,000** |
| **Paarwert** | **1,000** |
| Band | **hoch** (≥ 0,90) |
| abweichende Merkmale über Toleranz | keine |
| einseitig erfüllte Kriterien | keine |
| gemeinsam verletzte Kriterien | A11Y01, A11Y02, A11Y03, A11Y07 |

**Unterhalb der Toleranz** gibt es sehr wohl Unterschiede (20 Einzelwerte, in `results.json` › `pairAgreement.subToleranceDifferences`):

- Fallcontainer: A = FRAME, B = COMPONENT (beide nach A04 zulässig).
- Seiten: A 1 Seite, B 2 Seiten (davon eine leer).
- Input-Rahmen: A `#CBD5E1`, B `#CBD5E2` (Δ1).
- Surface-Clipping: A `clipsContent=false`, B `true` (FREE06/AS12 ausdrücklich frei).
- Input-Text-Einsatz: A 12 px, B 13 px (1-px-Rahmen; GEO10 regelt nur Optionen).
- Vertikale Textausrichtung: A `TOP`, B `CENTER` – Bounding-Boxen identisch (FREE09).

**Interpretation:** Paarwert 1,000 heißt **gleiche Lesart der Definition**, nicht Korrektheit. Zwei identisch falsche Designs würden ebenfalls 1,000 erreichen; hier sind beide jedoch auch gegen die Definition geprüft und bestehen alle expliziten Kriterien. Die vier gemeinsam verletzten A11Y-Kriterien zeigen eine **systematische**, nicht zufällige Lücke: Beide Builder interpretierten „Semantik“ als sichtbare Namen und Styles, nicht als Metadaten. Genau dort liegt der einzige belastbare Unterschied zwischen „definitionskonform“ und „zugänglich annotiert“.

---

## 8. Selbstauskünfte der Builder (nur Einordnung)

| Behauptung | Prüfung |
| --- | --- |
| A: 60 025 B, 129 Knoten, 65 Textknoten, 10 Fälle | **bestätigt** |
| A: `allCasesMatch: true` | Selbstauskunft; unabhängig nachgemessen – alle Fallwerte stimmen |
| A: `preview.png` `36a216a4…` | bestätigt (Datei-Hash); eigener Render mit `scale:2` hat anderen Hash, Inhalt gleich |
| B: 31 306 B, 119 Knoten auf der Seite, 56 Textknoten, 21 Optionen | **bestätigt** |
| B: Input-Rahmen `#CBD5E2` | **bestätigt** (Δ1 zum Token) |
| B: `preview.png` 219 034 B | **bestätigt**, und byte-identisch mit `render-b.png` |
| B: „ARIA nur über Teilenamen/Texte“ | **bestätigt** – und der Grund für die vier Abweichungen |
| beide: Definition unverändert | **bestätigt** über 22/22 Hashes |

Die Berichte ersetzen keine Messung; sie erklären die gewählten Freiheiten (opening ohne Popup, Meldungszeile, disabled-Platzhalter, `scroll-end`-Offset) und sind insoweit für A09 relevant. Keiner der Berichte behauptet ein interaktives oder screenreader-fähiges Verhalten.

**Nicht offengelegt (aber auch nicht still erfunden):** Die 6/7-Alternative bei `{count} Städte verfügbar.` wird von keinem Builder erörtert; beide wählen 7 (= `results.length`), den in der Prüfrichtlinie bevorzugten Wert (AS2/FREE05). Das ist zulässig, aber eine kleine Dokumentationslücke.

---

## 9. Grenzen der Prüfung

1. **Revisionslabel nicht rekonstruierbar.** `1d83935f…` ließ sich mit den erlaubten Quellen nicht nachrechnen; geprüft ist die Unverändertheit der 22 Dateien gegen beide Manifeste und den aktuellen Stand.
2. **ARIA im Canvas-Format.** Rollen/Zustände haben im `.fig` dieser Toolchain kein eigenes Feld. Die Bewertung stützt sich auf Namen, Texte, `pluginData` und visuelle Zustände. Fehlende Annotationen sind als Abweichung ausgewiesen, nicht als Formatfehler.
3. **A11Y05 weich ausgelegt** (dokumentierte Namenskonvention statt Annotation). Bei strenger Lesart wären beide Designs FAIL; die Alternative ist im Bericht transparent.
4. **Schriftmetriken** (Glyphbreiten) wurden nicht nachgerechnet; TY05 stützt sich auf den Render. B weist selbst auf einen Renderer-Font-Fallback hin; die Dokumentwerte tragen `Inter`.
5. **Visuelle Urteile** (Schatten, Highlight, Clipping) sind am Render bei Scale 2 geprüft, nicht pixelmetrisch.
6. **Unterbrechungen** sind Koordinator-Angabe; die Zwischenartefakte (`_probe.mjs`, `render-report.json`) existieren nicht mehr und sind nicht prüfbar.
7. **Stichprobe.** Zwei Designs, ein Definitionstand, keine Aussage über Varianz über viele Läufe.

---

## 10. Artefakte und Hashes

| Datei | SHA-256 (gekürzt) |
| --- | --- |
| `builder-a/autocomplete.fig` | `f79ff07fd70d4775…` |
| `builder-b/autocomplete.fig` | `fbd3b9934a3e4f28…` |
| `review/render-a.png` | `d26be652f34c8913…` |
| `review/render-b.png` | `b6d935eedd663a35…` (= `builder-b/preview.png`) |
| `builder-a/preview.png` | `36a216a4e62b4ed2…` |
| `review/original-a.json` | `a1911c1f1ef823a1…` |
| `review/original-b.json` | `44a3fda4d590a6c7…` |
| `review/native-checks.json` | `6863cb97c4836e7c…` |

Vollständige Liste: `hashes.json` (review-Dateien und geprüfte Builder-Artefakte).

**Prüfskripte (vom Repo-Root ausführbar, ohne Netzwerk):**

```sh
node examples/autocomplete/reproducibility/run-02/review/inspect-original.mjs
node examples/autocomplete/reproducibility/run-02/review/render-original.mjs
python3 examples/autocomplete/reproducibility/run-02/review/verify.py --native-only
python3 examples/autocomplete/reproducibility/run-02/review/verify.py
```

`inspect-original.mjs` und `render-original.mjs` importieren die gepinnten Pakete über absolute Pfade aus `tools/openpencil/node_modules`; `verify.py` nutzt nur die Standardbibliothek.
