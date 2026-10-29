# Preregistrierung · autocomplete-reproducibility-03 · Phase 1

- **Lauf-ID:** autocomplete-reproducibility-03
- **Phase:** Phase 1 — Preregistration (Kriterienableitung aus der Definition; **kein** Vergleich)
- **Datum:** 2026-10-29
- **Erlaubte Eingaben:** `components/**` (vollständig gelesen), eigener Ausgabeordner `examples/autocomplete/reproducibility/run-03/review/`
- **Verbotene Eingaben (nicht geöffnet):** `examples/**` außer eigenem Ordner (inkl. `run-03/builder-a/`, `run-03/builder-b/`), `docs/**`, `scripts/**`, `skills/**`, `tools/**`, `.git`, Root-`README.md`, Root-`TASKS.md`, jegliche Git-Befehle
- **Erklärung:** Es wurde keinerlei Builder-Ausgabe gesehen. Die Kriterien wurden ausschließlich aus der eingefrorenen Definition abgeleitet, bevor irgendeine Builder-Ausgabe vorlag. Keine Prognosen über künftige Outputs.

## Methode

Jede Datei der Definition (READMEs, `library.json`, `tokens.json`, `component.json`, `interface.json`, `layout.css`, `stories.json`, SCXML-Dateien, Accessibility-HTML-Dateien, `accessibility.rules.json`) wurde durchgegangen; daraus wurden alle für ein **statisches, editierbares OpenPencil-Design** prüfbaren Anforderungen abgeleitet:

- **explicit** — in der Definition ausdrücklich festgelegt (Datei + Stelle zitiert).
- **derived** — logisch aus ausdrücklich Festgelegtem abgeleitet (Ableitungsschritt im `source`-Feld benannt).
- **underdetermined** — prüfrelevanter Aspekt, den die Definition unzureichend bestimmt. **Nicht** als Verletzung zu werten; muss aber gelistet sein.

**deviationClass** — Einordnung, die eine Abweichung erhalten würde:
`Verletzung klarer Regel` | `erlaubte Freiheit` | `unzureichend bestimmte Regel`.

**Farbwerte:** HEX-Werte sind aus den sRGB-Komponenten in `components/tokens.json` berechnet (Komponente × 255, sRGB, alpha 1).

## Zählung

| Kategorie | Anzahl |
| --- | --- |
| explicit | 74 |
| derived | 10 |
| underdetermined | 7 |
| **Gesamt** | **91** |

| Domain | Anzahl | Kriterien |
| --- | --- | --- |
| document | 4 | E-001 … E-004 |
| cases | 6 | E-005 … E-009, D-001 |
| anatomy | 6 | E-010 … E-014, U-006 |
| naming | 1 | E-015 |
| text | 9 | E-016 … E-023, D-002 |
| dimensions | 11 | E-024 … E-032, D-003, D-004 |
| spacing | 5 | E-033 … E-037 |
| color | 8 | E-038 … E-045 |
| typography | 7 | E-046 … E-049, D-005, D-006, U-001 |
| geometry | 7 | E-050 … E-053, D-007, D-008, U-007 |
| clipping-scroll | 6 | E-054 … E-057, D-009, U-002 |
| popup-visibility | 5 | E-058, E-059, E-060, D-010, U-003 |
| editability | 2 | E-061, E-062 |
| accessibility | 14 | E-063 … E-074, U-004, U-005 |

Kurzel: **E** = explicit, **D** = derived, **U** = underdetermined. „Verl.“ = Verletzung klarer Regel, „Frei“ = erlaubte Freiheit, „Unter“ = unzureichend bestimmte Regel.

---

## Domain: document (4)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-001 | E | Die Datei muss sich tatsächlich als OpenPencil-Dokument öffnen lassen; ein Bild, eine umbenannte JSON-Datei oder ein nur im Speicher existierender Graph genügt nicht. | `autocomplete/README.md` „Exportrahmen“, letzter Absatz | Builder-Datei ist ein gültiges, editierbares OpenPencil-Dokument | Verl. |
| E-002 | E | Das Dokument enthält eine übersichtliche Seite mit den zehn benannten Fällen. | `autocomplete/README.md` „Exportrahmen“ | Alle zehn Fälle in einem Dokument auf einer Seite | Verl. |
| E-003 | E | Außenanordnung der Fälle, Seitentitel und beschreibende Hinweise sind **frei**. | `autocomplete/README.md` „Exportrahmen“ | Anordnung/Titel/Hinweise werden nicht beanstandet | Frei |
| E-004 | E | Definitionsdateien dürfen nicht geändert werden; Lücken sind zu dokumentieren, nicht still zu ergänzen. | `autocomplete/README.md` „Exportrahmen“; `components/README.md` „Unabhängiger erster Proof“ | Design konsistent mit unveränderter Definition; identifizierte Lücken dokumentiert | Verl. |

## Domain: cases (6)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-005 | E | Genau die zehn Fälle: closed, opening, loading, ready, active, scroll-end, selected, empty, error, disabled. | `autocomplete/README.md` „Sichtbare Geometrie“; `stories.json` (10 ids) | Alle zehn Fälle vorhanden und so benannt | Verl. |
| E-006 | E | Jeder Fall als Komponenten-/Framelayergruppe benannt. | `autocomplete/README.md` „Exportrahmen“ | Jeder Fall = eigene, benannte Frame-/Komponentengruppe | Verl. |
| E-007 | E | active und scroll-end sind „ready mit activeKey“ — keine zusätzlichen SCXML-Zustände. | `autocomplete/README.md`; `stories.json` (phase ready + activeKey); `component.json` viewSemantics | ready-Layout (7 Zeilen, Popup) mit aktiver Option bzw. aktiver letzter Option | Verl. |
| E-008 | E | selected ist „closed mit value“ (abgeleiteter closed-Zustand). | `autocomplete/README.md`; `stories.json` (phase closed, value berlin); `component.json` viewSemantics.selectedView | closed-Layout (kein Popup), value vorhanden, Label von value im Input | Verl. |
| E-009 | E | disabled ist „closed mit enabled=false“. | `autocomplete/README.md`; `stories.json` (phase closed, enabled false) | closed-Layout, deaktivierter Input, keine Popupteile sichtbar | Verl. |
| D-001 | D | Die zehn Darstellungen entsprechen den sechs formalen Zuständen: closed; active mit opening/loading/ready/empty/error (active & scroll-end = ready+activeKey); closed-Varianten selected & disabled. | Ableitung aus `behavior.scxml` (Zustandsbaum) + `stories.json` („phase“) + `autocomplete/README.md` | Fall↔Zustands-Zuordnung in den Darstellungen konsistent | Verl. |

## Domain: anatomy (6)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-010 | E | Autocomplete besitzt Input, Listbox, Optionen und Status; Listbox, Overlayfläche und Scrollviewport sind unterschiedliche Teile. | `autocomplete/README.md` „Fachliche Regeln“ | Alle sechs Teilarten als unterscheidbare Teile erkennbar | Verl. |
| E-011 | E | Popup = eigene Overlay-Verwendung (anchorPart input, contentOwner Autocomplete); darin die eigene ScrollArea (contentPart list). | `autocomplete/component.json` „composition“ | Popup als eigene Overlay-Verwendung; Listbox = Scrollinhalt, Eigentum der Autocomplete | Verl. |
| E-012 | E | Anatomie & Eigentum: label (über Input; Input-Name leitet sich ab), input (editierbar, Autocomplete), overlay.surface (am Input verankert), overlay.scroll.viewport (geclippter Viewport im Popup), list (Listbox im Scrollinhalt, Autocomplete), option (ein Teil pro stabilem Key), status (unter Popup, sonst unter Input). | `autocomplete/component.json` „anatomy“ | Alle sieben benannten Teile vorhanden und korrekt zugeordnet | Verl. |
| E-013 | E | Option wird über den fachlichen Key identifiziert (instance + option key, nie Zeilenindex). | `autocomplete/README.md`; `component.json` viewSemantics.repeatedPartIdentity | Optionen über Keys berlin…zuerich verknüpft, nicht über Indizes | Verl. |
| E-014 | E | Ein Overlay besitzt keine zweite Auswahlmaschine (keine eigene Such-/Auswahlstate). | `autocomplete/README.md`; `overlay/component.json` „responsibility“ | Overlay/ScrollArea führen keine eigene Auswahl- oder Wertlogik | Verl. |
| U-006 | U | `error-relay.scxml` („ResearchErrorRelay“) existiert, wird aber keinem Designfall zugeordnet; Rolle im statischen Design undefiniert. | `autocomplete/error-relay.scxml`; keine Referenz in anatomy/stories/README | Vorhandensein/Fehlen einer Darstellung wird nicht beanstandet; kein Designfall | Unter |

## Domain: naming (1)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-015 | E | Input, Overlayfläche, Scrollviewport, Listbox, einzelne Optionen und Status separat editierbar und verständlich benannt bleiben. | `autocomplete/README.md` „Exportrahmen“ | Benannte Teil-Layers, einzeln bearbeitbar, keine zusammengebackenen/unlesbaren Namen | Verl. |

## Domain: text (9)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-016 | E | Label-Text in allen Fällen: „Stadt auswählen“. | `interface.json` label default; `stories.json` (alle 10); `accessibility.html` | Exakt „Stadt auswählen“ in allen zehn Fällen | Verl. |
| E-017 | E | Platzhalter: „Stadt suchen …“ (Ellipsenzeichen, Leerzeichen davor). | `interface.json` placeholder default; `stories.json`; `accessibility.html` | Exakt „Stadt suchen …“ in Fällen mit leerem Query | Verl. |
| E-018 | E | Sieben Ergebnislabels in dieser Reihenfolge: Berlin, Hamburg, München, Dresden, Köln, Wien, Zürich. | `stories.json` results[].label (ready/active/scroll-end/selected) | Exakt diese sieben Labels in dieser Reihenfolge | Verl. |
| E-019 | E | Sieben Keys: berlin, hamburg, muenchen, dresden, koeln, wien, zuerich; eindeutig, nicht leer; nur muenchen disabled=true. | `stories.json` results[].key/.disabled; `autocomplete/README.md` | Korrektes Key↔Label-Mapping; „München“ als disabled markiert | Verl. |
| E-020 | E | Status-Text pro Fall: closed=''; opening='Suche wird geöffnet.'; loading='Städte werden geladen.'; ready/active/scroll-end='7 Städte verfügbar.' (Vorlage results, count=7); selected='Ausgewählt: Berlin.'; empty='Keine Städte gefunden.'; error='Städte konnten nicht geladen werden.'; disabled=''. | `accessibility.rules.json` messages; `autocomplete/README.md`; `stories.json` | Status-Text exakt je Fall (siehe Erwartung) | Verl. |
| E-021 | E | Query-Text pro Fall: closed=''; opening=''; loading='Be'; ready=''; active=''; scroll-end=''; selected='Berlin'; empty='Atlantis'; error='Be'; disabled=''. | `stories.json` inputs.query | Exakte Query-Texte je Fall | Verl. |
| E-022 | E | Bei selected steht das zu value gehörige Label („Berlin“) im Input. | `autocomplete/README.md`; `stories.json` (selected: query „Berlin“, value berlin) | Input zeigt „Berlin“ (kein Platzhalter) | Verl. |
| E-023 | E | Sichtbare Texte kommen ausschließlich aus Inputs, Ergebnislabels und accessibility.rules.json — nichts frei erfundenes. | `autocomplete/README.md` („In allen Fällen …“; „dürfen nicht still neu erfunden werden“) | Jeder sichtbare Text ist einer Quelle zuordenbar | Verl. |
| D-002 | D | Leerer Query → Platzhalter sichtbar; nicht leerer Query → Query-Text. | Ableitung aus `interface.json` (query/placeholder) + `layout.css` ::placeholder + `stories.json` | Platzhalter in closed/opening/ready/active/scroll-end/disabled; Query-Text in loading/selected/empty/error | Verl. |

## Domain: dimensions (11)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-024 | E | Gesamtbreite der Komponente 320px (autocomplete.width). | `tokens.json` autocomplete.width; `layout.css` [data-component] width | 320px in jedem Fall | Verl. |
| E-025 | E | Input-Höhe 44px (inputHeight), box-sizing border-box. | `tokens.json` inputHeight; `layout.css` [data-part=input] | 44px in allen Fällen | Verl. |
| E-026 | E | Input-Breite 100% der Komponente (= 320px). | `layout.css` [data-part=input] width | 320px in allen Fällen | Verl. |
| E-027 | E | Label-Höhe 20px (= lineHeight). | `layout.css` [data-part=label]; `tokens.json` lineHeight | 20px in allen Fällen | Verl. |
| E-028 | E | Status-Höhe 20px (= lineHeight). | `layout.css` [data-part=status]; `tokens.json` lineHeight | 20px in Fällen mit Status-Region | Verl. |
| E-029 | E | Optionen bleiben 32px hoch (rowHeight; height + min-height). | `tokens.json` rowHeight; `layout.css` [data-part=option]; `autocomplete/README.md` | 32px pro Zeile in allen Fällen | Verl. |
| E-030 | E | Viewport max-height 160px (maxHeight = base.max), overflow-y auto. | `tokens.json` maxHeight; `scroll-area/layout.css` [data-part=viewport] | 160px; Viewport clippt/scrollt | Verl. |
| E-031 | E | Input-Rahmen 1px solid (borderWidth). | `tokens.json` borderWidth; `layout.css` [data-part=input] border | 1px Rahmen (surface ausgenommen, dort border 0) | Verl. |
| E-032 | E | Radius 8px (radius) für Input und Overlayfläche. | `tokens.json` radius; `layout.css` [data-part=input]; `overlay/layout.css` [data-part=surface] | 8px Eckenradius an Input und Popupfläche | Verl. |
| D-003 | D | Viewporthöhe bei Ergebnislisten = min(Anzahl × rowHeight, maxHeight); bei 7 Ergebnissen = min(224, 160) = 160px. | Ableitung aus `autocomplete/README.md` + `tokens.json` + `stories.json` (7 Ergebnisse) | Viewport 160px in ready/active/scroll-end/selected | Verl. |
| D-004 | D | 160px Viewport ÷ 32px Zeile = 5 sichtbare Zeilen. | Ableitung aus D-003 + E-029 | Maximal 5 Zeilen gleichzeitig sichtbar | Verl. |

## Domain: spacing (5)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-033 | E | Label→Input: 8px (labelGap, Label margin-bottom). | `tokens.json` labelGap; `layout.css` [data-part=label]; `autocomplete/README.md` | 8px in allen Fällen | Verl. |
| E-034 | E | Input→Popup: 8px (gap); Popup-Oberkante am Inputende plus gap. | `tokens.json` gap; `overlay/layout.css` [data-part=surface] margin-top; `autocomplete/README.md` | 8px in Fällen mit sichtbarem Popup | Verl. |
| E-035 | E | Status-Abstand: 8px (statusGap, Status margin-top). | `tokens.json` statusGap; `layout.css` [data-part=status]; `accessibility.rules.json` statusPlacement | 8px zum Bezugselement (Popup oder Input) | Verl. |
| E-036 | E | Input padding 0 12px (paddingInline). | `tokens.json` paddingInline; `layout.css` [data-part=input] | Links/rechts 12px, oben/unten 0 | Verl. |
| E-037 | E | Option padding 6px 12px. | `layout.css` [data-part=option] | Oben/unten 6px, links/rechts 12px | Verl. |

## Domain: color (8)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-038 | E | Die acht Farbtokens exakt: surface #FFFFFF; text #172B4D; muted #64748B; border #CBD5E1; focus #2563EB; highlight #EAF2FF; disabled #94A3B8; error #B91C1C (alle sRGB, alpha 1). | `tokens.json` autocomplete (alle acht Farbtokens; HEX = Komponente × 255) | Nur diese Farben im Design; keine still neu erfundenen | Verl. |
| E-039 | E | Input: Hintergrund surface #FFFFFF; Text text #172B4D; disabled → Text disabled #94A3B8. | `layout.css` [data-part=input] + :disabled; `tokens.json` | Weisser Input, Text #172B4D; Fall disabled: #94A3B8 | Verl. |
| E-040 | E | Input-Rahmen: Standard border #CBD5E1; in opening/loading/ready/empty/error focus #2563EB; disabled → border #CBD5E1. | `layout.css` (State-Regeln) + `tokens.json` | Je Fall: closed #CBD5E1; opening #2563EB; loading #2563EB; ready #2563EB; active #2563EB; scroll-end #2563EB; selected #CBD5E1; empty #2563EB; error #2563EB; disabled #CBD5E1 | Verl. |
| E-041 | E | Platzhalterfarbe muted #64748B. | `layout.css` ::placeholder; `tokens.json` | Platzhalter in #64748B | Verl. |
| E-042 | E | Optionstext text #172B4D (erbt); Option aria-disabled=true → disabled #94A3B8. | `layout.css` [data-part=option][aria-disabled=true] + Vererbung; `tokens.json` | Normale Optionen #172B4D; „München“ #94A3B8 in allen Sichtbarkeitsfällen | Verl. |
| E-043 | E | Aktive Option (aria-selected=true): Hintergrund highlight #EAF2FF, Textfarbe unverändert. | `layout.css` [data-part=option][aria-selected=true]; `tokens.json` | Nur die aktive Option (active: „Hamburg“, scroll-end: „Zürich“) mit #EAF2FF | Verl. |
| E-044 | E | Status-Text muted #64748B; im error-Zustand error #B91C1C. | `layout.css` [data-part=status] + [data-state=error]; `tokens.json` | Status #64748B, nur im Fall error #B91C1C | Verl. |
| E-045 | E | Overlayfläche: Hintergrund surface #FFFFFF, border 0, box-shadow 0 2px 8px #0003 (= rgba(0,0,0,0.2)), z-index 10. | `overlay/layout.css` [data-part=surface] | Weiße, rahmenlose Fläche mit 8px Radius und dezentem Schlagschatten | Verl. |

## Domain: typography (7)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-046 | E | Schriftart Inter (fontFamily). | `tokens.json` fontFamily; `layout.css` [data-component] | Alle Komponententexte in Inter | Verl. |
| E-047 | E | Basisgröße 14px (fontSize) für Komponente/Input/Optionen/Label. | `tokens.json` fontSize; `layout.css` [data-component], [data-part=input] font:inherit | Label/Input/Optionen 14px | Verl. |
| E-048 | E | Line-height 20px. | `tokens.json` lineHeight; `layout.css` [data-component] | 20px (auch Grundlage für Label-/Status-Höhe) | Verl. |
| E-049 | E | Status-Größe 12px (statusFontSize). | `tokens.json` statusFontSize; `layout.css` [data-part=status] | Status in 12px | Verl. |
| D-005 | D | Label, Input, Optionen erben Inter 14px, line-height 20px, Farbe text #172B4D (keine eigenen Overrides). | Ableitung aus `layout.css` (Vererbung) + fehlende font-/color-Regeln für label/option + `tokens.json` | Einheitliche Inter-14px-Typo mit #172B4D | Verl. |
| D-006 | D | Optionstext vertikal zentriert: 6px + 20px + 6px = 32px = Zeilenhöhe. | Ableitung aus `layout.css` [data-part=option] + `tokens.json` lineHeight | Text sitzt mittig in der Zeile | Verl. |
| U-001 | U | Schriftstärke (font-weight) — und letter-spacing/Transformation — ist nirgends festgelegt. | Fehlen in `tokens.json`, allen `layout.css` | Jede gewählte Stärke zulässig; nicht als Verletzung | Unter |

## Domain: geometry (7)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-050 | E | Label oben; Input darunter nach labelGap (8px). | `autocomplete/README.md` „Sichtbare Geometrie“; `layout.css` [data-part=label] | Vertikal: Label → 8px → Input in allen Fällen | Verl. |
| E-051 | E | Popup-Oberkante am Inputende plus gap (8px). | `autocomplete/README.md`; `overlay/layout.css` top: anchor(bottom) + margin-top | 8px zwischen Input-Unterkante und Popup-Oberkante | Verl. |
| E-052 | E | Popup: dieselbe Breite (320px) und dieselbe linke Kante wie der Input. | `autocomplete/README.md`; `overlay/layout.css` left: anchor(left), width: anchor-size(width) | Popup 320px, linke Kante flucht mit Input | Verl. |
| E-053 | E | Ein verborgener Popup belegt keinen Platz. | `autocomplete/README.md` | In closed/opening/selected/disabled kein Layout-Platz; Status direkt unter Input | Verl. |
| D-007 | D | Status steht nach statusGap (8px) unter dem tatsächlich sichtbaren Popup, sonst unter dem Input. | Ableitung aus `autocomplete/README.md` + `accessibility.rules.json` statusPlacement + `layout.css` margin-top | Bezugskante = Popup-Unterkante (sichtbar) bzw. Input-Unterkante (verborgen), + 8px | Verl. |
| D-008 | D | Status-Position je Fall: unter Popup in loading/ready/active/scroll-end/empty/error; unter Input in closed/opening/selected/disabled. | Ableitung aus E-058 (Projections) + D-007 + E-008/E-009 | Korrekte Status-Position in jedem Fall | Verl. |
| U-007 | U | Ob versteckte Popup-Layer (closed/opening/selected/disabled) als platzneutrale Layer vorhanden sein müssen oder gar nicht erzeugt werden, ist nicht festgelegt. | `autocomplete/README.md` („belegt keinen Platz“, „keine Popupteile sichtbar“); keine Existenzpflicht | Beide Varianten zulässig, solange nichts sichtbar ist und der Status korrekt positioniert ist | Unter |

## Domain: clipping-scroll (6)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-054 | E | Viewport clippt seinen Inhalt (overflow-y auto), max-height 160px. | `scroll-area/layout.css` [data-part=viewport]; `scroll-area/component.json` responsibility | Inhalt > 160px wird geclippt | Verl. |
| E-055 | E | scroll-end muss die aktive letzte Option (zuerich) tatsächlich im sichtbaren Viewport darstellen. | `autocomplete/README.md`; `stories.json` (activeKey zuerich) | „Zürich“ vollständig im sichtbaren Viewportbereich | Verl. |
| E-056 | E | Der geclippte Viewportinhalt darf für das Design entsprechend versetzt werden (statische Darstellung, kein dynamisches Scrollen). | `autocomplete/README.md` | Listeninhalt so versetzt, dass die letzte Zeile sichtbar ist; keine Scroll-Dynamik behauptet | Verl. |
| E-057 | E | Alle Ergebnislayer bleiben editierbar erhalten; unsichtbare Daten werden nicht gelöscht. | `autocomplete/README.md` („nicht einfach die … unsichtbaren Daten löschen“) | Alle 7 Zeilen als (auch geclippte) Layers vorhanden und editierbar | Verl. |
| D-009 | D | ready/active: 7 Zeilen à 32px bei 160px Viewport → 5 sichtbar, 2 geclippt; bei Scroll-Position oben sichtbar: Berlin, Hamburg, München, Dresden, Köln; geclippt: Wien, Zürich. | Ableitung aus D-003 + E-029 + `stories.json` (Reihenfolge) | Sichtbereich = erste fünf Zeilen (bei obiger Scroll-Position); Wien/Zürich geclippt, aber vorhanden | Verl. |
| U-002 | U | Die exakte Scroll-Position (Offset) in scroll-end und die Anzahl sichtbarer/geclippter Zeilen sind nicht festgelegt. **Inkonsistenz:** README nennt „die drei unsichtbaren Daten“, die Arithmetik (7 Zeilen, 5-zeiliger Viewport) ergibt bei maximalem Scroll maximal 2 geclippte Zeilen. | Fehlen einer Offset-Vorgabe (README nur „entsprechend versetzt“, `scroll-area/behavior.scxml` REVEAL ohne Ziel-Offset); Widerspruch `autocomplete/README.md` vs. tokens/stories-Arithmetik | Jede Position zulässig, bei der „Zürich“ sichtbar ist und alle 7 Zeilen existieren; Lücke ist zu dokumentieren, nicht als Verletzung | Unter |

## Domain: popup-visibility (5)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-058 | E | popupVisible je Zustand: closed=false, opening=false, loading=true, ready=true, empty=true, error=true. | `accessibility.rules.json` projections | Sichtbares Popup nur in loading/ready/empty/error (und abgeleiteten active/scroll-end) | Verl. |
| E-059 | E | Bei disabled sind keine Popupteile sichtbar. | `autocomplete/README.md` | Keine sichtbare Fläche, kein Viewport, keine Listbox in disabled | Verl. |
| E-060 | E | loading/empty/error: Popupinhalt zeigt eine Zeile mit der Meldung; Statusregion wiederholt den Text als benannter Status darunter. | `autocomplete/README.md`; `accessibility.rules.json` messages | loading: „Städte werden geladen.“; empty: „Keine Städte gefunden.“; error: „Städte konnten nicht geladen werden.“ — jeweils in Popup-Zeile und Status | Verl. |
| D-010 | D | Popup je Fall: sichtbar in loading/ready/active/scroll-end/empty/error; nicht sichtbar in closed/opening/selected/disabled. | Ableitung aus E-058 + E-008 (selected=closed) + E-009 (disabled=closed) + `stories.json` | Genau 6 Fälle mit sichtbarem Popup, 4 ohne | Verl. |
| U-003 | U | Höhe/Styling der Meldungszeile (loading/empty/error) nicht vollständig festgelegt: die Formel „min(Anzahl × rowHeight, maxHeight)“ gilt laut README nur „bei Ergebnislisten“; die Textfarbe der Meldungszeile ist nicht definiert. | `autocomplete/README.md` („bei Ergebnislisten“); Fehlen eigener Regeln in `layout.css` | Korrekter Meldungs-Text Pflicht; exakte Zeilenhöhe/-farbe nicht als Verletzung | Unter |

## Domain: editability (2)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-061 | E | Das Ergebnis ist ein editierbares OpenPencil-Design; interaktive Canvas-Preview wird nicht gefordert. | `autocomplete/README.md` (Abs. 1); `components/README.md` „Unabhängiger erster Proof“; `library.json` targets.openpencil | Editierbare benannte Komponenten, keine flache Abbildung | Verl. |
| E-062 | E | Keine interaktive Combobox-Verhalten, keine ARIA-Ausführung, keine Canvas-Interaktion gefordert (ausdrücklich ausgenommen). | `autocomplete/component.json` targetScope.openpencil; `components/README.md`; `library.json` | Fehlende Interaktivität wird nicht beanstandet | Frei |

## Domain: accessibility (14)

| ID | Kat. | Anforderung | Quelle | Erwartung | Abweichung |
| --- | --- | --- | --- | --- | --- |
| E-063 | E | Rollen: Input=combobox, List=listbox, Option=option, Status=status. | `accessibility.html` (role-Attribute) | Rollen den entsprechenden Teilen zugeordnet | Verl. |
| E-064 | E | Input trägt aria-autocomplete="list". | `accessibility.html` | combobox-Annotation enthält aria-autocomplete=list | Verl. |
| E-065 | E | aria-expanded je Zustand: closed=false, opening=false, loading=true, ready=true, empty=true, error=true. | `accessibility.rules.json` projections (expanded); `accessibility.html` (Template false) | closed/opening/selected/disabled → false; loading/ready/active/scroll-end/empty/error → true | Verl. |
| E-066 | E | aria-selected wahr nur für die aktive Option; bestätigt keinen value. | `accessibility.rules.json` selection.ariaSelected | Maximal eine selected Option pro Fall, genau die aktive | Verl. |
| E-067 | E | aria-selected je Fall: active → „Hamburg“ (hamburg); scroll-end → „Zürich“ (zuerich); alle übrigen → keine. | `stories.json` (activeKey nur in active/scroll-end) + `accessibility.rules.json` | Genau diese Zuordnung | Verl. |
| E-068 | E | aria-disabled einer Option = result.disabled; disabled Optionen werden nicht aktiv/confirmiert. | `accessibility.rules.json` selection.ariaDisabled | Nur „München“ aria-disabled=true | Verl. |
| E-069 | E | „München“ (muenchen) ist in allen Sichtbarkeitsfällen disabled. | `stories.json` (muenchen disabled:true) + E-068 | In ready/active/scroll-end/selected als disabled markiert (und #94A3B8, s. E-042) | Verl. |
| E-070 | E | aria-activedescendant = aktuelle Option für activeKey; ohne aktive Option nicht vorhanden. | `accessibility.rules.json` selection.ariaActivedescendant | Nur in active (hamburg) und scroll-end (zuerich) gesetzt | Verl. |
| E-071 | E | Status trägt role=status, aria-live="polite", aria-atomic="true". | `accessibility.html` | Status-Region entsprechend annotiert | Verl. |
| E-072 | E | Namensquellen: Input-Name aus Label; List-Name aus Label; Option-Name aus result.label; Platzhalter aus interface.placeholder. | `accessibility.rules.json` labelSource/placeholderSource/optionNameSource/listNameSource; `component.json` anatomy.label | Input-/List-Name „Stadt auswählen“; Optionennamen = Labels; Platzhalter „Stadt suchen …“ | Verl. |
| E-073 | E | Fokus: Input behält während Navigation den DOM-Fokus; Popup/Viewport erhalten keine zusätzliche Rolle oder Tabstop. | `accessibility.rules.json` focus | Keine zusätzlichen Fokus-/Tabstop-Annotationen für Popup/Viewport | Verl. |
| E-074 | E | ARIA-Werte sind semantische Annotationen (benannte Teile, Label, Status-Text, active- und disabled-Stile) — keine Behauptung von Screenreader-Verhalten. | `accessibility.rules.json` designTarget | Werte als semantische Annotationen abgebildet; kein funktionales SR-Testen erwartet | Verl. |
| U-004 | U | Die genaue Darstellungsform der ARIA-Attribute (Layer-Label, Notiz, Property, Kommentar) ist nicht spezifiziert — „semantic annotations“. | `accessibility.rules.json` designTarget | Jede Darstellungsform zulässig, wenn die Werte korrekt und nachvollziehbar ablesbar sind | Unter |
| U-005 | U | Ob die Status-Region bei leerem Text (closed, disabled) als (leerer) Layer vorhanden sein muss oder weggelassen werden darf, ist nicht abschließend festgelegt („Ohne Meldung ist sein Text leer“). | `autocomplete/README.md`; `component.json` anatomy.status; keine explizite Pflicht | Leerer Status-Text korrekt; Pflicht eines leeren Layers wird nicht geprüft | Unter |

---

## Zusammenfassung der underdetermined-Aspekte (U-001 … U-007)

Diese Punkte sind **keine Verletzungen**; sie werden in Phase 2 gelistet, aber nicht geahndet:

1. **U-001** (typography): font-weight/letter-spacing/Transformation nicht festgelegt.
2. **U-002** (clipping-scroll): exaktes Scroll-Offset in scroll-end offen; Inkonsistenz „drei unsichtbare Daten“ vs. arithmetisch maximal 2 geclipte Zeilen.
3. **U-003** (popup-visibility): Höhe/Farbe der Meldungszeile in loading/empty/error nicht vollständig festgelegt (Formel gilt nur „bei Ergebnislisten“).
4. **U-004** (accessibility): Darstellungsform der ARIA-Annotationen nicht spezifiziert.
5. **U-005** (accessibility): Pflicht zur Existenz eines leeren Status-Layers in closed/disabled offen.
6. **U-006** (anatomy): Rolle von `error-relay.scxml` im statischen Design nicht definiert.
7. **U-007** (geometry): Existenz (vs. Abwesenheit) platzneutraler Popup-Layer in verborgenen Fällen offen.

## Fallübersicht (aus der Definition abgeleitet; für Phase 2 als Referenz)

| Fall | Zustand | Popup sichtbar | Input-Text | Rahmen | Aktive Option | Status-Text | Status-Position |
| --- | --- | --- | --- | --- | --- | --- | --- |
| closed | closed | nein | (Platzhalter) | #CBD5E1 | — | (leer) | unter Input |
| opening | active/opening | nein | (Platzhalter) | #2563EB | — | Suche wird geöffnet. | unter Input |
| loading | active/loading | ja (Meldungszeile) | Be | #2563EB | — | Städte werden geladen. | unter Popup |
| ready | active/ready | ja (7 Zeilen, 5 sichtbar) | (Platzhalter) | #2563EB | — | 7 Städte verfügbar. | unter Popup |
| active | active/ready+activeKey | ja (7 Zeilen, 5 sichtbar) | (Platzhalter) | #2563EB | Hamburg | 7 Städte verfügbar. | unter Popup |
| scroll-end | active/ready+activeKey | ja (verschoben, Zürich sichtbar) | (Platzhalter) | #2563EB | Zürich | 7 Städte verfügbar. | unter Popup |
| selected | closed+value | nein | Berlin | #CBD5E1 | — | Ausgewählt: Berlin. | unter Input |
| empty | active/empty | ja (Meldungszeile) | Atlantis | #2563EB | — | Keine Städte gefunden. | unter Popup |
| error | active/error | ja (Meldungszeile) | Be | #2563EB | — | Städte konnten nicht geladen werden. (in #B91C1C) | unter Popup |
| disabled | closed, enabled=false | nein | (Platzhalter, Input-Text #94A3B8) | #CBD5E1 | — | (leer) | unter Input |

*Hinweis: Die Zeile „München“ ist in ready/active/scroll-end/selected durchgehend in #94A3B8 (disabled). Die Fallübersicht ist eine Ableitung (aus stories.json + accessibility.rules.json + layout.css + tokens.json) und dient der Phase-2-Referenz; verbindlich sind die einzelnen Kriterien.*
