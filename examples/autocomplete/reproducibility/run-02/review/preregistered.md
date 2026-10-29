# Vorab registrierte Prüfkriterien — Autocomplete (run-02, Phase 1)

**Status:** eingefroren vor Einsicht in Builder-Ausgaben.
**Prüfgegenstand:** zwei unabhängig erzeugte, editierbare OpenPencil-Designs zum Autocomplete.
**Definitionsrevision:** `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`
**Erlaubte Lesequellen (eingehalten):** die 22 Dateien unter `components/` (rekursiv) sowie `tools/openpencil/README.md` und `tools/openpencil/package.json`. Keine Einsicht in frühere Läufe, Ergebnisse, Reviews, `reference.json`, `docs/`, `scripts/`, Root-README/TASKS oder Git-Historie.

---

## 1. Quelleninventar und Rollen

| Quelle | Rolle im Prüfverfahren |
| --- | --- |
| `components/library.json` | Bibliotheksindex; bestätigt Autocomplete, Overlay, ScrollArea als Definitionsbestand |
| `components/tokens.json` | alle benannten Designwerte (DTCG), autoritativ für Maße, Farben, Typografie |
| `components/autocomplete/component.json` | Identität, Anatomie, Komposition, viewSemantics |
| `components/autocomplete/interface.json` | CEM-Signatur: `label`, `placeholder`, `query`, `value`, `results`, `enabled`; CSS-Parts |
| `components/autocomplete/layout.css` | Geometrie- und Zustandsregeln des Autocomplete |
| `components/autocomplete/behavior.scxml` | Zustände/Übergänge; liefert u. a. `activeKey`-Semantik und Navigationsregeln |
| `components/autocomplete/stories.json` | die zehn Darstellungsfälle mit Eingaben, Ergebnissen, `activeKey`, `value` |
| `components/autocomplete/accessibility.html` | statische Grundstruktur und Rollen |
| `components/autocomplete/accessibility.rules.json` | Meldungstexte, Sichtbarkeitsprojektion, Auswahlprojektion, Statusplatzierung |
| `components/autocomplete/error-relay.scxml` | nur Beleg für `init.failed`-Weiterleitung; kein eigener Darstellungsfall |
| `components/overlay/*` | Popupfläche: Ankerung, Breite, Radius, Schatten, `border: 0`; keine zweite Auswahlmaschine |
| `components/scroll-area/*` | Viewport mit `max-height` und `overflow-y: auto`; Liste als Spalte; kein eigener Auswahlzustand |
| `components/README.md`, `components/autocomplete/README.md` | führende fachliche und geometrische Regeln, Exportrahmen |
| `tools/openpencil/README.md`, `package.json` | technische Randbedingungen: gepinnte Pakete `@open-pencil/*` 0.16.0, CLI `openpencil` |

**Nicht als Anforderungquelle verwendet:** Beispieldateien, frühere Ausgaben, Screenshots, Git-Historie.

---

## 2. Abgeleitete Sollwerte (vor der Bewertung festgeschrieben)

### 2.1 Tokenwerte

| Token | Wert | Verwendung |
| --- | --- | --- |
| `autocomplete.width` | 320 px | Komponentenbreite, Input- und Popup-Breite |
| `autocomplete.inputHeight` | 44 px | Input |
| `autocomplete.fontSize` | 14 px | Label, Input, Optionen |
| `autocomplete.statusFontSize` | 12 px | Status |
| `autocomplete.lineHeight` | 20 px | Labelhöhe, Statuszeile, Textzeile in Zeilen |
| `autocomplete.labelGap` | 8 px | Label → Input |
| `autocomplete.gap` | 8 px (→ `base.gap`) | Input → Popup-Oberkante |
| `autocomplete.statusGap` | 8 px | Popup/Input → Status |
| `autocomplete.rowHeight` | 32 px (→ `base.row`) | jede Optionszeile |
| `autocomplete.maxHeight` | 160 px (→ `base.max`) | Viewport-Maximum |
| `autocomplete.radius` | 8 px | Input und Popupfläche |
| `autocomplete.borderWidth` | 1 px | Input-Rahmen |
| `autocomplete.paddingInline` | 12 px | Input horizontal, Option horizontal |
| `autocomplete.fontFamily` | Inter | gesamte Komponente |

### 2.2 Farben (Token → sRGB-8-Bit, zur Prüferleichterung, aus `tokens.json` berechnet)

| Token | Komponenten | Hex |
| --- | --- | --- |
| `surface` | 1.0 / 1.0 / 1.0 | `#FFFFFF` |
| `text` | 0.0902 / 0.1686 / 0.3020 | `#172B4D` |
| `muted` | 0.3922 / 0.4549 / 0.5451 | `#64748B` |
| `border` | 0.7961 / 0.8353 / 0.8824 | `#CBD5E1` |
| `focus` | 0.1451 / 0.3882 / 0.9216 | `#2563EB` |
| `highlight` | 0.9176 / 0.9490 / 1.0 | `#EAF2FF` |
| `disabled` | 0.5804 / 0.6392 / 0.7216 | `#94A3B8` |
| `error` | 0.7255 / 0.1098 / 0.1098 | `#B91C1C` |

Overlay-Schatten: `0 2px 8px #0003` (Schwarz, Alpha ≈ 0.20), `border: 0`, `margin-top: 8px`, Breite = Ankerbreite, linke Kante = Ankerkante.

### 2.3 Fallmatrix (Sollzustand je Story)

| Fall | Phase | Query-Anzeige | Popup | Zeilen im Viewport | aktive Option | Status (Text) | Input-Rahmen | Statusfarbe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `closed` | closed | Placeholder | nein | – | keine | `""` (leer) | `#CBD5E1` | `#64748B` |
| `opening` | opening | Placeholder | nein | – | keine | `Suche wird geöffnet.` | `#2563EB` | `#64748B` |
| `loading` | loading | `Be` | ja, 1 Meldungszeile | 1 Meldungszeile | keine | `Städte werden geladen.` | `#2563EB` | `#64748B` |
| `ready` | ready | Placeholder | ja | 5 von 7 (160/32), oben beginnend | keine | `7 Städte verfügbar.` (auch `6 …` zulässig, s. AS5) | `#2563EB` | `#64748B` |
| `active` | ready | Placeholder | ja | 5 von 7 | `hamburg` / „Hamburg“ | `7 Städte verfügbar.` | `#2563EB` | `#64748B` |
| `scroll-end` | ready | Placeholder | ja | 5 von 7, Ende sichtbar | `zuerich` / „Zürich“ | `7 Städte verfügbar.` | `#2563EB` | `#64748B` |
| `selected` | closed | `Berlin` | nein | – | keine | `Ausgewählt: Berlin.` | `#CBD5E1` | `#64748B` |
| `empty` | empty | `Atlantis` | ja, 1 Meldungszeile | 1 Meldungszeile | keine | `Keine Städte gefunden.` | `#2563EB` | `#64748B` |
| `error` | error | `Be` | ja, 1 Meldungszeile | 1 Meldungszeile | keine | `Städte konnten nicht geladen werden.` | `#2563EB` | `#B91C1C` |
| `disabled` | closed | Placeholder | nein | – | keine | `""` (leer) | `#CBD5E1` | `#64748B` |

Ergebnisliste (identisch in `ready`, `active`, `scroll-end`, `selected`): `berlin`→„Berlin“, `hamburg`→„Hamburg“, `muenchen`→„München“ (disabled), `dresden`→„Dresden“, `koeln`→„Köln“, `wien`→„Wien“, `zuerich`→„Zürich“.

### 2.4 Rechenwerte, die sich zwingend aus den Tokens ergeben

- Ergebnisliste: 7 × 32 px = 224 px Inhalt; Viewport = min(224, 160) = **160 px** → genau **5 volle Zeilen** sichtbar, **0 angeschnittene**, **2 vollständig geclippte** (`Berlin`, `Hamburg` bei Ansicht am Listenende).
- `scroll-end`: maximaler Offset = 224 − 160 = **64 px** (= 2 Zeilen).
- Gesamthöhe ohne Popup: 20 (Label) + 8 + 44 + 8 + 20 (Status) = **100 px**.
- Gesamthöhe mit Ergebnispopup: 20 + 8 + 44 + 8 + 160 + 8 + 20 = **268 px**.
- Gesamthöhe mit Meldungszeile: 20 + 8 + 44 + 8 + H + 8 + 20, mit H = 32 → **140 px** (H = 20 → 128 px; Freiheit AS6).

---

## 3. Kriterien

Legende: **E** = explicit, **D** = derived, **U** = underdetermined (Definition lässt Freiheit; der zulässige Raum ist in der Erwartung genannt). Schwere: **K** = kritisch, **M** = major, **m** = minor.
Toleranzen (Details in Abschnitt 4): Maße ±1 px pro Kante, kumulierte Offsets ±2 px, Gesamthöhen ±4 px, Farben max. 3/255 pro Kanal, Schriftgröße ±0.5 px.

### 3.1 Artefakt, Export, Editierbarkeit

| ID | Quelle | Aussage | Erwartung | Kl. | Schwere |
| --- | --- | --- | --- | --- | --- |
| A01 | autocomplete/README.md „Exportrahmen“ | Das Ergebnis ist ein tatsächlich öffnbares OpenPencil-Dokument, keine umbenannte JSON-Datei und kein reiner Speichergraph. | Datei lässt sich mit der gepinnten Toolchain (`@open-pencil/core` 0.16.0) laden; Szenengraph mit ≥ 10 Frames wird ausgelesen; Loader-Fehler = Verstoß. | E | K |
| A02 | README Z. 28/32; stories.json | Genau die zehn benannten Fälle sind als Gruppen vorhanden: `closed`, `opening`, `loading`, `ready`, `active`, `scroll-end`, `selected`, `empty`, `error`, `disabled`. | 10 Fallgruppen; normalisierte Namen enthalten je Fall-ID; keine fehlt, keine zusätzliche elfte Zustandsgruppe. | E | K |
| A03 | README Z. 28 | `active`, `scroll-end`, `selected`, `disabled` sind keine zusätzlich unabhängig geführten SCXML-Zustände. | Keine Fallgruppe trägt einen eigenen, erfundenen Zustandsnamen außerhalb der zehn IDs; Zusatzgruppen nur als frei dekorative Seitenelemente, nicht als Zustand. | E | M |
| A04 | README Z. 32 | Jeder Fall ist als Komponenten-/Framelayergruppe benannt. | Pro Fall ein Container-Knoten (Frame/Component/Group), dessen Name die Fall-ID enthält; Fallinhalte liegen darin. | E | K |
| A05 | README Z. 32; component.json `anatomy`; interface.json `cssParts` | Label, Input, Overlayfläche, Scrollviewport, Listbox, jede Option und Status bleiben separat editierbar und benannt. | Für jeden sichtbaren Fall existieren getrennte Knoten für `label`, `input`, `surface` (nur Popup-Fälle), `viewport` (nur Popup-Fälle), `list` (nur Ergebnis-/Meldungsfälle), je eine Option pro Ergebnis und `status`; kein Zusammenfall zu einem Knoten. | E | K |
| A06 | README Z. 34; component.json `targetScope` | Sichtbare Texte sind echte, editierbare Textknoten. | Jeder geforderte Text ist als Textobjekt mit editierbarem String vorhanden; keine Vektorpfade, keine Outline-Konvertierung, kein eingebettetes Bild für Text. | E | K |
| A07 | README Z. 34 | Ein Bild oder eine bloße Bitmap genügt nicht. | Kein Fall ist als Rasterbild/Screenshot repräsentiert; Bitmap-Anteil der Komponente = 0 (Seitenhintergrund/Notizen ausgenommen). | E | K |
| A08 | README Z. 34 | Der Exporteur darf die Definitionsdateien nicht passend zum Ergebnis ändern. | SHA-256 über `components/**` entspricht der Revision `1d83935f…c727`; Abweichung = Verstoß (und Prüfung wird gegen die eingefrorene Revision fortgesetzt). | E | K |
| A09 | README Z. 34 | Fehlende Angaben werden als Lücke dokumentiert, nicht still ergänzt. | Für jede in Abschnitt 6 gelistete Unterbestimmtheit, die das Design betrifft, existiert eine kurze schriftliche Offenlegung (Notiz/README des Laufs); stilles Erfinden = Verstoß. | E | M |
| A10 | README Z. 32 | Teile sind „verständlich benannt“. | Normalisierter Knotenname enthält mindestens einen der Begriffe `label`, `input`, `surface`/`popup`, `viewport`/`scroll`, `list`/`listbox`, `option`, `status`; deutsche Synonyme zulässig. Stil/Großschreibung frei. | D | m |
| A11 | component.json `repeatedPartIdentity`; README Z. 20 | Optionen sind über den fachlichen Key identifiziert, nicht über den Zeilenindex. | Je Ergebnis genau ein Optionsknoten; Knotenname oder Metadatum enthält den Key (`berlin`, `hamburg`, `muenchen`, `dresden`, `koeln`, `wien`, `zuerich`) oder ist eindeutig dem Label zuordenbar; keine reine `row-1…7`-Benennung. | D | m |
| A12 | README Z. 32 | Die Fallgruppe enthält die Komponente des Falls, keine fremden Komponentenkopien. | Innerhalb einer Fallgruppe höchstens ein Label, ein Input, eine Popupfläche, eine Listbox, ein Status; freie Seitenhinweise außerhalb der Gruppe. | D | M |

### 3.2 Zustände und Fallprojektion

| ID | Quelle | Aussage | Erwartung | Kl. | Schwere |
| --- | --- | --- | --- | --- | --- |
| ST01 | stories.json `closed`; rules `projections.closed`; README Z. 28 | `closed`: Popup nicht sichtbar, kein Platzverbrauch, Status ohne Meldung, Placeholder sichtbar. | Keine sichtbare Popupfläche/Liste/Option; Statusabstand direkt nach Input (8 px); Statustext leer; Input zeigt Placeholder; Rahmen `#CBD5E1`. | E | K |
| ST02 | stories `opening`; rules `messages.opening`, `projections.opening`; README Z. 24 | `opening`: Popup geschlossen, aber Meldung „Suche wird geöffnet.“ im Status. | Kein sichtbares Popup; Status unter dem Input mit Text `Suche wird geöffnet.`; Placeholder sichtbar; Rahmen `#2563EB`. | D | M |
| ST03 | stories `loading`; rules `messages.loading`, `projections.loading`; README Z. 24 | `loading`: Popup sichtbar mit genau einer Meldungszeile, Status wiederholt den Text. | Popup mit einem Meldungstext `Städte werden geladen.`; keine Optionsknoten; Status darunter mit identischem Text; Input zeigt `Be`; Rahmen `#2563EB`. | E | K |
| ST04 | stories `ready`; rules `projections.ready`; tokens | `ready`: Popup mit 7 Ergebnissen, Viewport 160, keine aktive Option, Statusmeldung. | 7 Optionsknoten, Viewport 160 px, 5 volle Zeilen sichtbar, keine Highlight-Fläche, Status `… Städte verfügbar.`, München als disabled markiert. | E | K |
| ST05 | stories `active` (`activeKey: hamburg`); rules `selection.ariaSelected`; layout.css | `active`: genau Hamburg ist aktiv hervorgehoben. | Genau die Zeile „Hamburg“ besitzt `#EAF2FF`-Hintergrund (bzw. äquivalente Highlight-Füllung); alle anderen Optionszeilen ohne Highlight; Status wie `ready`. | E | K |
| ST06 | stories `scroll-end` (`activeKey: zuerich`); README Z. 26 | `scroll-end`: die aktive letzte Option ist tatsächlich im sichtbaren Viewport dargestellt. | „Zürich“ ist hervorgehoben und liegt vollständig innerhalb der Viewportgrenzen (Ober- und Unterkante); Inhalt darf um ≤ 64 px versetzt sein; alle 7 Optionen bleiben vorhanden. | E | K |
| ST07 | stories `selected` (`value: berlin`); README Z. 28 | `selected`: geschlossen, Input zeigt das Label des Werts, Status nutzt die selected-Vorlage. | Kein sichtbares Popup; Inputtext `Berlin` (kein Placeholder); Status `Ausgewählt: Berlin.`; Rahmen `#CBD5E1`. | E | K |
| ST08 | stories `empty`; rules `projections.empty`; README Z. 24 | `empty`: Popup mit Meldungszeile, Status wiederholt sie. | Input `Atlantis`; Popup mit genau `Keine Städte gefunden.`; keine Optionsknoten; Status identisch; Rahmen `#2563EB`. | E | K |
| ST09 | stories `error`; rules `messages.error`; layout.css | `error`: Popup mit Fehlermeldung, Status wiederholt sie in Fehlerfarbe. | Input `Be`; Popup mit `Städte konnten nicht geladen werden.`; Status identisch, Farbe `#B91C1C`; keine Optionsknoten; Rahmen `#2563EB`. | E | K |
| ST10 | stories `disabled` (`enabled:false`); rules `messages.disabled`, `projections.closed` | `disabled`: deaktiviert, keine Popupteile sichtbar, kein Statustext. | Keine sichtbare Popupfläche/Liste/Option; Input mit Disabled-Textfarbe und `#CBD5E1`-Rahmen; Statustext leer. | E | K |
| ST11 | README Z. 28 | Die Fall-Phasen sind festgelegt: `active`/`scroll-end` = ready, `selected`/`disabled` = closed, `closed`/`opening`/`loading`/`ready`/`empty`/`error` wie benannt. | Die beobachtete Zustandsprojektion jedes Falls entspricht seiner Phase (z. B. Fokusrahmen bei `active`/`scroll-end` wie `ready`, kein Popup bei `selected`). | E | M |
| ST12 | rules `projections` | Sichtbarkeit von Popup und Expanded-Zustand folgt der Projektionstabelle. | Für `closed`/`opening`: `popupVisible=false`; für `loading`/`ready`/`empty`/`error`: `popupVisible=true`. Abweichung = Verstoß. | E | K |

### 3.3 Anatomie und Komposition

| ID | Quelle | Aussage | Erwartung | Kl. | Schwere |
| --- | --- | --- | --- | --- | --- |
| AN01 | component.json `anatomy.label`; layout.css | Das Label steht sichtbar über dem Input. | Label-Oberkante < Input-Oberkante; horizontal linksbündig zum Input (±1 px). | E | M |
| AN02 | component.json `anatomy.input`; layout.css | Der Input gehört zum Autocomplete und nimmt die Komponentenbreite ein. | Input-Breite = 320 px (±1) und = Komponentenbreite; Input liegt unter dem Label. | E | M |
| AN03 | README Z. 20; overlay/interface.json `cssParts`; scroll-area/interface.json `cssParts` | Listbox, Overlayfläche und Scrollviewport sind unterschiedliche Teile. | Drei getrennte Knoten; keiner ist mit einem der anderen identisch oder darin aufgegangen. | E | K |
| AN04 | README Z. 20; component.json `composition`; scroll-area/layout.css | Das Popup enthält die ScrollArea; die Listbox liegt im Scrollinhalt. | Hierarchie `surface` ⊃ `viewport` ⊃ (`content`) ⊃ `list` ⊃ `option`; Optionen nicht direkt an der Surface ohne Viewport/Liste. | D | K |
| AN05 | component.json `anatomy.status`; rules `statusPlacement` | Der Status steht außerhalb des Popups. | Statusknoten ist kein Nachfahre von `surface`/`viewport`. | E | M |
| AN06 | README Z. 20; overlay/component.json `responsibility` | Ein Overlay besitzt keine zweite Auswahlmaschine. | Pro Fall höchstens eine Listbox und ein Optionssatz; keine parallele, versteckte zweite Liste mit denselben Optionen. | E | K |
| AN07 | component.json `composition.overlay.scroll` | Die ScrollArea ist im Overlay verortet. | `viewport` liegt innerhalb der Popupfläche; `list` innerhalb des Viewports. | D | M |
| AN08 | scroll-area/layout.css `[data-part="list"]` | Die Optionen bilden eine vertikale Liste innerhalb der Listbox. | Alle Optionsknoten sind Kinder desselben Listencontainers, in Ergebnisreihenfolge, ohne Zwischengruppe pro Zeile mit abweichender Semantik. | D | m |
| AN09 | README Z. 20 | Kein doppelter Optionssatz durch die Komposition. | Anzahl Optionsknoten im gesamten Fall = Anzahl Ergebnisse (7 bzw. 0), nicht 14. | E | M |
| AN10 | layout.css `[data-part="status"]`; README Z. 24 | Eine Statusregion existiert auch ohne Meldung. | Statusknoten in jedem Fall vorhanden (Text ggf. leer); Fehlen bei `closed`/`disabled` = Verstoß (Freiheit AS7 betrifft nur Sichtbarkeit/Existenz bei leerem Text, s. Abschnitt 6). | D | m |

### 3.4 Sichtbare Texte

| ID | Quelle | Aussage | Erwartung | Kl. | Schwere |
| --- | --- | --- | --- | --- | --- |
| TX01 | interface.json `label.default`; stories; accessibility.html | Jeder Fall zeigt das Label „Stadt auswählen“. | Textinhalt des Labelknotens == `Stadt auswählen` (NFC, exakt). | E | K |
| TX02 | interface.json `placeholder.default`; layout.css `::placeholder` | Der Placeholder lautet exakt „Stadt suchen …“ und erscheint nur bei leerer Query. | Bei `query == ""` ist `Stadt suchen …` sichtbar (U+2026, Leerzeichen davor); bei nicht-leerer Query kein Placeholder. | E | M |
| TX03 | stories `inputs.query` | Die Query-Anzeige entspricht den Story-Eingaben. | `closed`/`opening`/`ready`/`active`/`scroll-end`/`disabled`: Placeholder; `loading`/`error`: `Be`; `selected`: `Berlin`; `empty`: `Atlantis`. | E | K |
| TX04 | stories `results[].label` | Die sieben Optionslabels lauten exakt wie definiert. | `Berlin`, `Hamburg`, `München`, `Dresden`, `Köln`, `Wien`, `Zürich`; Reihenfolge wie in stories; keine Zusätze. | E | K |
| TX05 | rules `messages` | Die Statustexte folgen den Meldungsvorlagen. | `closed`/`disabled`: leer; `opening`: `Suche wird geöffnet.`; `loading`: `Städte werden geladen.`; `ready`/`active`/`scroll-end`: `{count} Städte verfügbar.`; `selected`: `Ausgewählt: Berlin.`; `empty`: `Keine Städte gefunden.`; `error`: `Städte konnten nicht geladen werden.` | E | K |
| TX06 | README Z. 24 | Bei `loading`, `empty`, `error` wiederholt die Statusregion den Text der Popupzeile. | Statustext == Meldungstext der Popupzeile (zeichengleich). | E | M |
| TX07 | README Z. 28 | Sichtbare Texte stammen nur aus Inputs, Ergebnislabels und `accessibility.rules.json`. | Innerhalb der Fallgruppe kein zusätzlicher erfundener Text (z. B. „Ergebnisse“, „Tippen Sie…“, Zähler) außer den geforderten; Seitenhinweise außerhalb sind frei. | D | M |
| TX08 | interface.json defaults; stories | Umlaute und Ellipse bleiben unverändert. | Kein `Munchen`/`Koeln`/`Zuerich`/`...` als Ersatz für `München`/`Köln`/`Zürich`/`…`; keine Umschrift, keine Capitalization-Änderung. | E | M |
| TX09 | README Z. 28; behavior.scxml `SET_VALUE`/`ENTER` | Bei `selected` steht das Ergebnislabel zum Wert im Input. | Inputtext == `Berlin` (Label zu `value: berlin`), nicht der Key. | E | K |

### 3.5 Maße, Abstände, Radius

| ID | Quelle | Aussage | Erwartung | Kl. | Schwere |
| --- | --- | --- | --- | --- | --- |
| GEO01 | tokens `autocomplete.width`; layout.css | Die Komponente ist 320 px breit. | Rahmenbreite des Fallcontainers = Komponentenbreite = 320 px (±1). | E | M |
| GEO02 | tokens `inputHeight` | Der Input ist 44 px hoch. | Inputhöhe 44 px (±1). | E | M |
| GEO03 | layout.css Label; tokens `lineHeight`, `labelGap` | Labelzeile 20 px hoch, darunter 8 px bis zum Input. | Labelhöhe 20 (±1); Abstand Label-Unterkante → Input-Oberkante 8 (±1). | E | M |
| GEO04 | layout.css Option; tokens `rowHeight` | Jede Optionszeile ist 32 px hoch und schrumpft nicht. | Jede Optionszeile 32 px (±1); keine Zeile mit abweichender Höhe. | E | M |
| GEO05 | scroll-area/layout.css; tokens `maxHeight`; README Z. 24 | Die Viewporthöhe ist min(Ergebnisanzahl × 32, 160). | Ergebnislisten: 160 px (±1); Meldungsfälle: eine Zeile, Höhe ≤ 40 px; `closed`-Fälle: kein Viewport sichtbar. | E | M |
| GEO06 | overlay/layout.css; README Z. 24 | Das Popup sitzt mit Oberkante am Inputende + 8 px, gleicher Breite und linker Kante. | `surface.top − input.bottom = 8` (±2); `surface.left = input.left` (±1); `surface.width = 320` (±1). | E | M |
| GEO07 | layout.css Status; tokens `statusGap`, `lineHeight` | Status: 8 px Abstand nach oben, Höhe 20 px. | `status.top − (popup.bottom oder input.bottom) = 8` (±2); Statushöhe 20 (±1). | E | M |
| GEO08 | layout.css; overlay/layout.css; tokens `borderWidth`, `radius` | Input: 1 px Rahmen, Radius 8; Popup: kein Rahmen, Radius 8. | Input-Rahmenstärke 1 (±0.5), Eckenradius 8 (±1); Surface-Rahmen 0, Radius 8 (±1). | E | M |
| GEO09 | README Z. 24; rules `statusPlacement` | Der Status steht unter dem tatsächlich sichtbaren Popup, sonst unter dem Input. | Popup-Fälle: Status unter Popup; popup-lose Fälle: Status unter Input; keine Überlappung. | E | K |
| GEO10 | layout.css Option | Options-Innenabstand: 12 px horizontal, 6 px vertikal. | Texteinsatz ≥ 12 px (±1) von links, Textblock innerhalb der 32-px-Zeile mit ca. 6 px oben/unten (±2), kein Anschneiden. | E | m |
| GEO11 | Rechnung aus 2.4 (frisch abgeleitet) | Die Gesamthöhen folgen aus den Einzelmaßen. | Popup-lose Fälle ≈ 100 px; Ergebnisfälle ≈ 268 px; Meldungsfälle 124–144 px; Toleranz ±4 px. | D | m |
| GEO12 | README Z. 24 | Ein verborgener Popup belegt keinen Platz und überlappt den Input nicht. | Sichtbare Surface beginnt nicht über `input.bottom`; in popup-losen Fällen kein Reserveabstand > 8 px zwischen Input und Status. | E | M |
| GEO13 | overlay/layout.css | Die Popupfläche trägt den definierten Schatten. | Schatten vorhanden, Versatz ≈ (0, 2), Weichzeichnung ≈ 8 px, Schwarz mit Alpha 0.15–0.25; Näherungen der Engine zulässig. | E | m |

### 3.6 Clipping und Overflow

| ID | Quelle | Aussage | Erwartung | Kl. | Schwere |
| --- | --- | --- | --- | --- | --- |
| CLIP01 | tokens `maxHeight`, `rowHeight`; scroll-area/layout.css | Ergebnis-Viewports clippen bei 160 px. | In `ready`/`active`/`scroll-end`: genau 5 volle Optionszeilen innerhalb der Viewportgrenzen, 0 angeschnittene Zeilen, 2 Zeilen vollständig außerhalb. | D | K |
| CLIP02 | README Z. 26 | Geclippte Ergebnislayer bleiben erhalten. | Alle 7 Optionen sind als Knoten vorhanden; `Berlin` und `Hamburg` dürfen außerhalb des Clips liegen, dürfen aber nicht gelöscht sein. | E | K |
| CLIP03 | README Z. 26 | In `scroll-end` ist die aktive letzte Option tatsächlich sichtbar. | Rechteck von „Zürich“ vollständig innerhalb der Viewportgrenzen (±1 px). | E | K |
| CLIP04 | Rechnung 2.4; scroll-area/layout.css | Kein Overscroll/Leerraum unter der letzten Zeile. | In `scroll-end` endet der sichtbare Inhalt spätestens an der Viewport-Unterkante; kein leerer Streifen > 2 px unter „Zürich“ innerhalb des Viewports. | D | M |
| CLIP05 | scroll-area/layout.css `overflow-y`; overlay/layout.css | Optionsinhalt ragt nicht sichtbar über Surface/Viewport hinaus. | Kein Optionsknoten (bzw. dessen Füllung/Text) ist außerhalb der Surface-Grenzen sichtbar; Überstand nur innerhalb des Clips. | E | K |
| CLIP06 | layout.css Option (feste Höhe) | Kein Label wird innerhalb einer Zeile abgeschnitten. | Jeder Options- und Meldungstext liegt vollständig in seiner Zeile; keine horizontale oder vertikale Textclipping-Kante. | D | M |
| CLIP07 | scroll-area/layout.css | Das Popup wächst nicht über die maximale Höhe. | Surface-Innenhöhe (Viewport) ≤ 160 px in Ergebnisfällen; Gesamtpopup ≤ 160 px + etwaige Meldungszeile. | E | K |
| CLIP08 | rules `statusPlacement` | Der Status wird nicht vom Popup überdeckt. | Statusrechteck schneidet das Surface-Rechteck nicht (Toleranz 0 px). | E | M |

### 3.7 Farben

| ID | Quelle | Aussage | Erwartung | Kl. | Schwere |
| --- | --- | --- | --- | --- | --- |
| COL01 | layout.css Input/Surface; overlay/layout.css | Input- und Popupfläche sind weiß. | Füllung `#FFFFFF` (±3/Kanal) in allen Fällen. | E | M |
| COL02 | layout.css Root; tokens `text` | Label, Inputtext und Optionslabels nutzen die Textfarbe. | `#172B4D` (±3/Kanal). | E | M |
| COL03 | layout.css `::placeholder`; tokens `muted` | Der Placeholder ist gedämpft. | `#64748B` (±3/Kanal), sofern Placeholder sichtbar. | E | M |
| COL04 | layout.css Input-Border; tokens `border` | Ohne Fokuszustand ist der Input-Rahmen `#CBD5E1`. | In `closed`/`selected`: `#CBD5E1` (±3); `disabled`: ebenfalls `#CBD5E1`. | E | M |
| COL05 | layout.css Fokusregeln; tokens `focus` | In `opening`, `loading`, `ready`, `empty`, `error` (inkl. `active`, `scroll-end`) ist der Input-Rahmen fokussiert. | Rahmen `#2563EB` (±3) in genau diesen Fällen; nicht in `closed`/`selected`/`disabled`. | E | M |
| COL06 | layout.css `[aria-selected="true"]`; tokens `highlight` | Nur die aktive Option ist hervorgehoben. | Genau eine Optionszeile mit Füllung `#EAF2FF` (±3) in `active`/`scroll-end`; keine in `ready`. | E | K |
| COL07 | layout.css `[aria-disabled="true"]`; tokens `disabled` | Deaktivierte Optionen sind farblich deaktiviert. | „München“ in `ready`/`active`/`scroll-end` mit Textfarbe `#94A3B8` (±3); andere Optionen nicht. | E | M |
| COL08 | layout.css `:disabled` | Ein deaktivierter Input nutzt Disabled-Text und normalen Rahmen. | In `disabled`: Textfarbe `#94A3B8` (±3), Rahmen `#CBD5E1` (±3). | E | M |
| COL09 | layout.css Status; tokens `muted`, `error` | Statusfarbe ist gedämpft, im Fehlerfall rot. | `#64748B` in allen Statusfällen außer `error`; `#B91C1C` (±3) in `error`. | E | M |
| COL10 | overlay/layout.css | Die Popupfläche hat keine zusätzliche Kontur und keine abweichende Füllung. | Kein sichtbarer Rand/Stroke an der Surface; Füllung weiß (siehe COL01); kein Farbverlauf. | E | M |
| COL11 | tokens (abschließende Liste) | Es werden keine weiteren Farben still erfunden. | Alle sichtbaren Füllungen/Konturen der Komponententeile stammen aus den acht Tokens; zusätzliche Farben = Verstoß (Schatten und Seitenhintergrund ausgenommen). | D | M |

### 3.8 Typografie

| ID | Quelle | Aussage | Erwartung | Kl. | Schwere |
| --- | --- | --- | --- | --- | --- |
| TY01 | tokens `fontFamily` | Die Komponente nutzt Inter. | Font-Familie der Textknoten == `Inter` (case-insensitiv); eine dokumentierte Ersatzschrift ist Abweichung, keine stillschweigende. | E | M |
| TY02 | tokens `fontSize`; layout.css | Label, Input und Optionen sind 14 px groß. | Schriftgröße 14 px (±0.5) für diese Textknoten. | E | M |
| TY03 | tokens `statusFontSize` | Der Status ist 12 px groß. | Schriftgröße 12 px (±0.5). | E | M |
| TY04 | tokens `lineHeight` | Die Zeilenhöhe beträgt 20 px. | Zeilenhöhe 20 px (±1) für Label, Optionen, Status. | E | m |
| TY05 | abgeleitet aus fester Breite/Höhe | Kein Text wird durch zu große Schrift abgeschnitten oder umgebrochen. | Jeder geforderte Text einzeilig; „Stadt auswählen“, „Stadt suchen …“, „Städte konnten nicht geladen werden.“ passen ohne Truncation in 320 px bei 14/12 px Inter. | D | M |

### 3.9 Accessibility (nur statisch prüfbare Struktur)

| ID | Quelle | Aussage | Erwartung | Kl. | Schwere |
| --- | --- | --- | --- | --- | --- |
| A11Y01 | accessibility.html `role="combobox"`; rules `designTarget` | Der Input ist als Combobox ausgezeichnet. | Rollen-/Semantikannotation `combobox` am Inputknoten oder – falls das Format keine Rollen trägt – Name enthält `combobox`; fehlend = Abweichung. | D | m |
| A11Y02 | accessibility.html; rules `listNameSource` | Die Listbox ist als solche benannt und trägt den Labelnamen. | Listenknoten mit `listbox`-Annotation/Name und zugänglichem Namen `Stadt auswählen`. | D | m |
| A11Y03 | rules `selection` | Optionen sind Optionen; `aria-selected` gilt nur der aktiven, `aria-disabled` folgt `result.disabled`. | Annotationen `option`, `selected` nur bei `hamburg`/`zuerich`, `disabled` bei `muenchen`; keine Selected-Markierung in `ready`. | D | M |
| A11Y04 | accessibility.html `role="status" aria-live="polite" aria-atomic="true"` | Der Status ist eine benannte Live-Region. | Statusknoten mit `status`/`live`-Annotation oder Name `status`; nicht als reiner Text ohne Region. | D | m |
| A11Y05 | rules `projections.*.expanded` | Expanded folgt der Projektion. | `closed`/`opening`: `expanded=false`; `loading`/`ready`/`empty`/`error`: `expanded=true` (Annotation oder dokumentierte Namenskonvention). | E | M |
| A11Y06 | rules `focus`; overlay/scroll-area interface | Popup und Viewport erhalten keine zusätzliche Rolle und keinen Tabstopp. | Keine `listbox`-Rolle am Viewport, keine zweite Combobox, keine fokussierbaren Zusatzknoten. | D | m |
| A11Y07 | rules `labelSource`; component.json `anatomy.label` | Der zugängliche Name des Inputs stammt aus dem Label. | Input-Name == `Stadt auswählen` (Annotation) oder eindeutige Label-Verknüpfung im Dokument. | D | m |
| A11Y08 | README Z. 24; rules `designTarget` | Der Statustext ist sichtbar und nicht dekorativ versteckt. | Statusknoten sichtbar (nicht 0 % opacity/off-canvas), Text entspricht TX05. | D | M |
| A11Y09 | rules `focus` | Der Input behält den DOM-Fokus während der Tastaturnavigation. | Statisch nicht prüfbar → wird als `n/a` geführt und fließt nicht in die Quote ein; nur der Fokusrahmen (COL05) wird geprüft. | E | – |

### 3.10 Zulässige Freiheiten (underdetermined)

Diese Kriterien können nicht „verletzt“ werden, solange das Design im genannten Raum bleibt. Verlässt es ihn, zählt das als Verstoß gegen die zugeordnete Oberkategorie.

| ID | Quelle | Aussage | Zulässiger Raum | Kl. |
| --- | --- | --- | --- | --- |
| FREE01 | README Z. 32 | Außenanordnung der Fälle, Seitentitel und beschreibende Hinweise sind frei. | Beliebige Position/Reihenfolge/Raster auf einer oder mehreren Seiten; Titel/Notizen außerhalb der Fallgruppen; Hintergrund frei. | U |
| FREE02 | README Z. 32 | Namensstil der Ebenen ist frei. | Jede verständliche Benennung, die A10/A11 erfüllt (deutsch/englisch, Präfixe, Nummerierung). | U |
| FREE03 | scroll-area/layout.css `overflow-y:auto` | Die Darstellung einer Scrollbar ist nicht festgelegt. | Scrollbar gezeichnet oder nicht; wenn gezeichnet, darf sie keine Optionslabels überdecken und max. 12 px breit sein. | U |
| FREE04 | README Z. 24 | Die Geometrie der Meldungszeile ist nicht im Detail festgelegt. | Höhe zwischen 20 und 40 px, Text linksbündig mit ≥12 px Einsatz, vertikal zentriert oder mit ≤6 px Innenabstand; keine Option-Semantik nötig. | U |
| FREE05 | rules `messages.results` | `{count}` ist nicht definiert (Ergebnisanzahl vs. auswählbare Anzahl). | `7 Städte verfügbar.` oder `6 Städte verfügbar.`; jede andere Zahl = Verstoß. Bevorzugt 7 (= `results.length`). | U |
| FREE06 | overlay/layout.css (kein `overflow:hidden`) | Ob der Radius die Optionszeilen an den Ecken beschneidet, ist offen. | Ecken der Zeilen scharf oder durch Radius 8 geclippt. | U |
| FREE07 | README Z. 24 | Ein verborgener Popup kann als fehlender oder als unsichtbarer Knoten umgesetzt sein. | Knoten fehlt, ist `visible=false`, 0×0 oder vollständig transparent – solange kein Platz belegt und nichts sichtbar ist. | U |
| FREE08 | layout.css Status; README Z. 24 | Bei leerer Meldung ist der Statusinhalt leer; die Darstellung des leeren Knotens ist offen. | Leerer Textknoten, leerer Container oder fehlender Statusknoten, solange keine sichtbare Höhe > 0 und kein Text erscheint. (Kollidiert mit AN10 → AN10 wird nur als erfüllt gewertet, wenn ein Statusknoten existiert; fehlt er, gilt AN10 als minor-Abweichung, FREE08 aber als gewahrt.) | U |
| FREE09 | layout.css Input/Option | Vertikale Textausrichtung in Input und Zeile ist nicht explizit. | Zentriert oder mit symmetrischem Innenabstand; Text vollständig sichtbar, ≥2 px Abstand zu allen Kanten. | U |
| FREE10 | overlay/layout.css Schatten | Engine-Näherung des Schattens ist zulässig. | Versatz 0–3 px, Blur 6–10 px, Alpha 0.15–0.25, keine harte Kante. | U |
| FREE11 | README Z. 24; scroll-area/layout.css | Die Meldungszeile kann im Viewport oder anstelle der Liste liegen. | Ein Meldungstext innerhalb der Surface, im Viewport oder als dessen einziger Inhalt; keine zusätzliche Liste mit Optionen. | U |
| FREE12 | README Z. 32 | Fallinterne Zusatzabstände über die definierten Maße hinaus sind nicht vorgesehen, aber Seitenabstände zwischen Fällen sind frei. | Abstand zwischen Fallgruppen beliebig; innerhalb einer Fallgruppe nur die definierten 8/20/32/44/160-Werte. | U |

---

## 4. Vergleichsverfahren

### 4.1 Prüfwerkzeuge und Reihenfolge

1. **Datei-Gate:** Dokument mit der gepinnten Toolchain laden (A01); Szenengraph injizieren/auslesen; Definition-Hash prüfen (A08).
2. **Struktur:** Fallgruppen, Teile, Hierarchie, Optionsanzahl, Knotentypen (A02–A07, A10–A12, AN01–AN10).
3. **Texte:** alle Textknoten extrahieren, normalisieren, gegen Solltexte matchen (TX01–TX09).
4. **Geometrie:** Bounding-Boxen relativ zur Fallgruppe; Maße, Abstände, Ausrichtung, Clipping (GEO01–GEO13, CLIP01–CLIP08).
5. **Farbe/Typografie:** Füllungen/Konturen und Fontattribute der benannten Teile (COL01–COL11, TY01–TY05).
6. **A11y-Annotationen:** Rollen/Names/Metadaten (A11Y01–A11Y08).
7. **Render-Abgleich:** Screenshot je Fall bei 1× zur Sichtprüfung von Clipping, Überlappung, Highlight; Pixelwerte nur unterstützend, nie allein entscheidend.

### 4.2 Normalisierung

- **Einheiten:** alle Maße in px; Vergleich pro Kante ±1 px, kumulierte Offsets (Popup-Top, Status-Top, Fallhöhe) ±2 px, Gesamthöhen ±4 px, Radius ±1 px, Rahmenstärke ±0.5 px.
- **Farben:** sRGB, 8 Bit; max. absoluter Kanalunterschied ≤ 3; Alpha ±0.02. Hex-Angaben in Abschnitt 2.2 sind nur Lesefassung der Tokenwerte.
- **Typografie:** Familie case-insensitiv; Größe ±0.5 px; Zeilenhöhe ±1 px; Schriftschnitt normal (kein Faux-Bold).
- **Texte:** Unicode-NFC; führende/abschließende Whitespaces entfernt; innere Leerzeichen, Satzzeichen und U+2026 bleiben signifikant; Vergleich case-sensitiv.
- **Namen:** lowercase, Nicht-Alphanumerisches → Leerzeichen, Mehrfach-Leerzeichen kollabiert; Treffer über Token-Enthaltensein; Synonymliste in A10.
- **Knotentypen:** `text` muss editierbaren String tragen; `frame`/`group`/`rect`/`ellipse` zählen als Container/Fläche; `image`/`bitmap` zählen als Raster (A07).
- **Ignoriert:** absolute Position der Fallgruppen auf der Seite, Seitenanzahl/-format, Titel, Notizen, Ebenen-IDs, Reihenfolge der Fälle, Dateibytes, unsichtbare Hilfsknoten ohne Sichtwirkung.

### 4.3 Verletzungsarten

| Code | Bedeutung | Beispiel |
| --- | --- | --- |
| V-EXPORT | Dokument nicht ladbar / kein OpenPencil-Dokument | JSON-Umbenennung, korrupter Graph |
| V-STRUCT | fehlender/duplizierter/verschachtelter Pflichtteil, fehlender Fall | keine Listbox, Option außerhalb des Viewports, 11 Fallgruppen |
| V-STATE | Zustandsprojektion falsch | Popup in `closed`, Highlight in `ready`, `Zürich` nicht sichtbar |
| V-TEXT | Text fehlt/abweichend | `Munchen`, `...` statt `…`, falscher Statustext |
| V-GEO | Maß/Abstand/Ausrichtung außerhalb Toleranz | Input 40 px, Popup 12 px unter Input, Status überlappend |
| V-COLOR | Farbe außerhalb Toleranz / erfunden | Highlight `#DDEBFF` (Δ>3), zusätzliche Rahmenfarbe |
| V-TYPE | Familie/Größe/Zeilenhöhe falsch | 13 px Status, Arial |
| V-CLIP | Clipping/Overflow falsch | 7 Zeilen sichtbar bei 160 px, angeschnittene Zeile, gelöschte geclippte Optionen |
| V-EDIT | nicht editierbar | Text als Pfad, Fall als Bitmap, alles in einer Gruppe |
| V-A11Y | statische Semantik fehlt/falsch | Status ohne Region, `selected` auf falscher Option |
| V-FREE | zulässigen Freiheitsraum verlassen | Statustext „8 Städte verfügbar.“, erfundene Zusatzmeldung |

### 4.4 Keine Erfolgsbedingungen

Folgendes ist **ausdrücklich kein** Kriterium und darf weder zum Pass noch zum Fail führen:

- byteweise oder strukturelle Dateigleichheit zwischen den beiden Designs,
- identische technische IDs, UUIDs, Ebenennamen oder Reihenfolge,
- gleiche Seitenanordnung, gleicher Seitentitel, gleiche Notizen,
- gleiche Anzahl an Hilfsknoten/Gruppierungstiefe, sofern die Pflichtteile getrennt bleiben,
- identische Scrollbar-, Schatten- oder Anti-Aliasing-Darstellung,
- Rendering-Genauigkeit unterhalb der genannten Toleranzen.

### 4.5 Bewertung je Kriterium

Jedes Kriterium erhält pro Design genau einen von: `pass`, `fail`, `n/a`.
`n/a` nur, wenn der Fall im Design nicht anwendbar ist (z. B. Popup-Kriterium im Fall `closed`) oder das Kriterium explizit als nicht statisch prüfbar markiert ist (A11Y09). `n/a` zählt nicht in Quoten.

### 4.6 Gesamturteil je Design

**Gates (jedes einzelne ist bindend):** A01, A02, A04, A05, A06, A07, A08.
→ Schlägt ein Gate fehl: **FAIL** (unabhängig von allen anderen Werten).

Danach:
- `E` = Anzahl `fail` unter allen Kriterien der Klasse **E** (ohne `n/a`).
- `D` = Anzahl `fail` unter allen Kriterien der Klasse **D**.
- `U` = Anzahl der Freiheitskriterien, deren Raum verlassen wurde (jeweils zusätzlich als `E`-Verstoß der Oberkategorie gezählt).

| Bedingung | Urteil |
| --- | --- |
| Gate-Verstoß **oder** `E ≥ 1` **oder** `D ≥ 5` | **FAIL** |
| `E = 0` und `2 ≤ D ≤ 4` | **PASS_MIT_ABWEICHUNGEN** |
| `E = 0` und `D ≤ 1` | **PASS** |

Zusätzlich wird je Design ausgewiesen: Anzahl erfüllter/verfehlter Kriterien pro Gruppe, Liste aller `fail`-IDs mit Evidenz (Knotenpfad, gemessener Wert, Sollwert, Screenshot-Referenz) und die Liste der in Anspruch genommenen Freiheiten (FREE-IDs). Ein Design, das eine Unterbestimmtheit nicht offenlegt (A09), kann maximal `PASS_MIT_ABWEICHUNGEN` erreichen.

### 4.7 Paarübereinstimmung

Die Paarübereinstimmung ist **kein Korrektheitsmaß**; sie wird getrennt vom Urteil berichtet.

**Merkmalsvektor je Fall** (nur anwendbare Merkmale):
`popupVisible`, `optionCount`, `optionLabels` (geordnet), `activeKey` (bzw. „keiner“), `inputDisplay` (Text + Placeholder-Flag), `statusText`, `viewportHeight`, `surfaceTopGap`, `surfaceLeft`, `surfaceWidth`, `rowHeight`, `inputHeight`, `radius`, `borderWidth`, `fontFamily`, `fontSize`, `statusFontSize`, `lineHeight`, Farben {surface, text, muted, border, focus, highlight, disabled, error} – jeweils nur, wenn im Fall sichtbar.

**Berechnung:**
1. `A_struct` = Jaccard-Index über die Mengen vorhandener (Fall, Pflichtteil)-Paare und der Optionslabel-Mengen.
2. `A_state` = Anteil der Fälle, in denen `popupVisible`, `activeKey`, `inputDisplay` und `statusText` zwischen beiden Designs übereinstimmen.
3. `A_vis` = Anteil der Merkmale aus dem Vektor (Geometrie, Farbe, Typografie), die zwischen beiden Designs innerhalb der Toleranzen aus 4.2 übereinstimmen.
4. **Paarwert** `A = 0.30·A_struct + 0.30·A_state + 0.40·A_vis` (Gewichtung ist eine frische Annahme, Abschnitt 6/AS13).

**Bänder:** `A ≥ 0.90` hoch, `0.75 ≤ A < 0.90` mittel, `A < 0.75` niedrig.

Zusätzlich Pflichtauswertung:
- `gemeinsam erfüllt` / `einseitig erfüllt` / `gemeinsam unzureichend` je Kriterium,
- Liste der Kriterien, bei denen **beide** Designs scheitern (Kandidaten für Definitionslücken oder systematische Fehlinterpretation),
- Liste der Kriterien, bei denen genau eines scheitert (Diskriminationskraft),
- expliziter Hinweis, wenn hohe Paarübereinstimmung bei gleichzeitigem FAIL beider Designs vorliegt („Konvergenz ohne Korrektheit“).

Freiheitsbereiche (FREE01–FREE12) gehen **nicht** in `A_vis` ein; abweichende Seitenanordnung senkt die Paarübereinstimmung nicht.

---

## 5. Prüfprotokoll (Reihenfolge, reproduzierbar)

1. Hashes der Definitionsdateien gegen `1d83935f…` prüfen (A08) und protokollieren.
2. Beide Dokumente laden, Öffnungsfehler protokollieren (A01).
3. Je Design Szenengraph dumpen (Pfad, Typ, Name, BBox, Text, Füllung, Kontur, Font, Sichtbarkeit).
4. Fallgruppen zuordnen; fehlende/überzählige Gruppen protokollieren (A02–A04, A12).
5. Je Fall Kriterien der Gruppen A, ST, AN, TX, GEO, CLIP, COL, TY, A11Y auswerten; `n/a` begründen.
6. Screenshot je Fall rendern; nur zur Bestätigung von Clipping/Überlappung/Highlight und zur Dokumentation.
7. Freiheiten erfassen (FREE01–FREE12) und mit A09-Offenlegung abgleichen.
8. Urteil je Design nach 4.6, Paarwert nach 4.7 berechnen.
9. Bericht: Evidenztabelle, Fail-Liste, Freiheitsliste, Paarwert mit Bändern, Liste „gemeinsam unzureichend“.

---

## 6. Frische Annahmen und Unterbestimmtheiten (transparent, vor Einsicht)

| Nr. | Stelle | Beobachtung | Frische Annahme / Behandlung |
| --- | --- | --- | --- |
| AS1 | `autocomplete/README.md` Z. 26 | „die drei unsichtbaren Daten“ passt nicht zur Rechnung: 7×32 = 224, Viewport 160 → 2 Zeilen (Berlin, Hamburg) geclippt. | Die Zahl „drei“ wird als Redaktionsfehler behandelt; bindend ist der Satz „Alle Ergebnislayer bleiben editierbar erhalten“. Geprüft werden 2 geclippte Zeilen; 3 werden nicht gefordert. Wird dieser Widerspruch im Export offengelegt, ist das positiv, aber nicht Pflicht. |
| AS2 | `accessibility.rules.json` `messages.results` = `{count} Städte verfügbar.` | `count` ist nicht definiert (7 Ergebnisse inkl. disabled vs. 6 auswählbar). | Beide Werte zulässig (FREE05), bevorzugt 7 = `results.length`. Kein Abzug für 6, kein Abzug für 7. |
| AS3 | `messages.opening` + `projections.opening` | `opening` hat eine Meldung, aber `popupVisible=false`; README Z. 24 nennt die Statuswiederholung nur für loading/empty/error. | `opening` zeigt die Meldung nur im Status unter dem Input, nicht im Popup. Eingestuft als `derived` (ST02), nicht als explizit. |
| AS4 | `layout.css` Selektoren `[data-state="ready"]` vs. Story-IDs | `active`/`scroll-end` haben Phase `ready`, nicht eigene data-states. | `data-state` wird auf die Story-`phase` abgebildet → Fokusrahmen auch in `active`/`scroll-end`. |
| AS5 | `stories.json` `ready` ohne Scrollangabe | Ausgangs-Scrollposition nicht definiert. | Ansicht am Listenanfang (scrollTop 0) → Berlin…Köln sichtbar, Wien/Zürich geclippt. Nur diese Lage erfüllt CLIP01; eine andere Lage ohne Angabe wäre eine stille Erfindung. |
| AS6 | README Z. 24 „eine Zeile“ | Höhe der Meldungszeile nicht tokenisiert. | Zeile 20–40 px; Standard 32 (= rowHeight). Gesamthöhe 124–144 px. |
| AS7 | `layout.css` Status; README Z. 24 | Status existiert immer, kann aber leer sein; ob ein leerer 20-px-Kasten sichtbar bleibt, ist offen. | Fehlender Statusknoten bei leerem Text ist zulässig (FREE08), wird aber als minor-Abweichung zu AN10 notiert; sichtbare Höhe > 0 mit leerem Text ist ebenfalls zulässig. |
| AS8 | README Z. 24 „verborgener Popup belegt keinen Platz“ | „verborgen“ ist nicht als `visible=false`, 0×0 oder „nicht vorhanden“ festgelegt. | Alle drei Varianten zulässig, solange nichts sichtbar ist und der Status nicht verschoben wird (FREE07, GEO12). |
| AS9 | `tokens.fontFamily` = Inter | Verfügbarkeit der Schrift im Export-/Prüfsystem ist nicht garantiert. | Inter ist Soll. Eine dokumentierte Ersatzschrift ist eine major-Abweichung (TY01), aber kein Gate-Fail; stillschweigender Ersatz ist ein Verstoß. |
| AS10 | `overlay/layout.css` Schatten | Canvas-Engines rendern Schatten unterschiedlich. | Näherung mit Versatz 0–3 px, Blur 6–10 px, Alpha 0.15–0.25 zulässig (FREE10). |
| AS11 | `layout.css` Input/Option | Vertikale Textausrichtung ist nicht ausdrücklich geregelt. | Zentriert oder symmetrisch mit ≥2 px Innenabstand; kein Anschneiden (FREE09). |
| AS12 | `scroll-area/layout.css` | Kein `overflow:hidden` an der Surface → Radius-Clipping der Zeilen unklar. | Beide Varianten zulässig (FREE06). |
| AS13 | Vergleichsgewichtung | Die Definition sagt nichts über Paar-Metriken. | Gewichte 0.30/0.30/0.40 (Struktur/Zustand/Visuell) sind eine frische, offengelegte Annahme; die Einzelwerte `A_struct`, `A_state`, `A_vis` werden zusätzlich roh berichtet. |
| AS14 | `layout.css` `[data-part="option"]` | Keine explizite Textfarbe für Optionen. | Optionstext erbt `--ac-text` (`#172B4D`), außer bei disabled (`#94A3B8`). |
| AS15 | `layout.css` `:disabled` + `::placeholder` | Vorrang von Placeholder-Farbe vs. Disabled-Farbe im Fall `disabled` ist offen. | Beide zulässig: `#64748B` oder `#94A3B8` (kein Abzug). |
| AS16 | `accessibility.rules.json` `projections` | Enthält nur fünf Zustände; `selected`/`disabled` fehlen (sie sind `closed`). | `selected`/`disabled` erben `closed` (expanded false, popupVisible false). |
| AS17 | `rules.selection.ariaSelected` | „True only for the active option“ – im geschlossenen `selected`-Fall gibt es keine aktive Option. | In `selected`/`closed`/`disabled` keine Selected-Markierung. |
| AS18 | `overlay/interface.json` `content`-Part | Ein zusätzlicher `content`-Knoten ist definiert, aber für die Darstellung nicht zwingend. | `content`-Wrapper optional; Pflicht ist die Reihenfolge surface ⊃ viewport ⊃ list ⊃ options. |
| AS19 | README Z. 26 „statische Darstellung“ | Interaktives Scrollen wird nicht verlangt. | Nur der statische Offset zählt; keine Scroll-Interaktion, keine Animation. |
| AS20 | README Z. 32 | „übersichtliche Seite“ ist nicht quantifiziert. | Seitenlayout völlig frei (FREE01); nur Lesbarkeit/keine Überlappung der Fallgruppen wird verlangt. |

---

## 7. Änderungsregel

Diese Datei ist ab jetzt eingefroren. Nach Einsicht in Builder-Ausgaben dürfen Kriterien, Toleranzen, Gewichte und Urteilsregeln nicht mehr geändert werden. Zulässig sind ausschließlich: Ausfüllen der Bewertungstabellen, Zitieren von Evidenz, Ergänzen neuer, klar markierter **nachträglicher** Anmerkungen (ohne Rückwirkung auf die Urteile), sowie das Protokollieren von Definitionslücken.
