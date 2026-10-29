# REVIEW · run-03 · Phase 2 (Vergleich) · autocomplete-reproducibility-03

Prüfer: frische Phase-2-Session (Subagent). Datum: 29.10.2026. Repository: `/Users/kcnpxcp/Dev/GitHub/ui-contracts`.
Kriterienbasis: ausschließlich das versiegelte Kriterienset (`preregistered.json`, `preregistered.md`, Siegel `preregistration-seal.json`). 91 Kriterien: 74 explizit, 10 abgeleitet, 7 unzureichend bestimmt.

---

## 1. Methode und Reihenfolge

Strikte Reihenfolge gemäß Auftrag, eingehalten:

1. **Schritt 0 — Siegel verifiziert (Laufstart):** Die frisch berechneten SHA-256-Werte der aktuellen Bytes passen exakt zum Siegel:
   - `preregistered.json` → `2faa6a867ae24f1bd9bbc020259b3fa4b84336022768374e0ee417e887de012c` (Siegel: identisch)
   - `preregistered.md` → `64f9604460374e9029f54310d57840619c7087caeea3d8b7e11e4aad8ff131fd` (Siegel: identisch)
   Ab diesem Punkt galten die Kriterien unverändert; sie wurden in keiner Phase geändert (erneute Bestätigung am Laufende, §9).
2. **Schritt 1 — Originaldateien zuerst, selbst gemessen:** `inspect-original.mjs` liest beide `autocomplete.fig`-Dateien mit dem Original-Reader der gepinnten Werkzeugumgebung (`tools/openpencil/node_modules`, `@open-pencil/fig` 0.16.0, `parseFigBuffer` + `materializeFigArchive` = vollständige Population) wieder ein und schreibt `original-a.json` / `original-b.json` (alle Knoten mit Geometrie, Text, Fills, Strokes, Effekten, Style-Runs, pluginData, absoluten Positionen). `render-original.mjs` rendert aus den **wiedereingelesenen** Graphen (`@open-pencil/core` 0.16.0, `headlessRenderNodes`, Scale 2) `render-a.png` / `render-b.png`. Ergebnis: A = 1 Seite, 136 Knoten (136 Kiwi-Records, kiwiVersion 101); B = 1 Seite, 122 Knoten (122 Records, kiwiVersion 101). Beide Dateien öffnen sich als vollständige, binäre OpenPencil-Dokumente (ZIP-Container mit `canvas.fig` + `thumbnail.png` + `meta.json`, jeweils 3 Einträge — verifiziert per Archiv-Liste). **Kreuzkontrolle:** die neu gerenderten PNGs sind byte-identisch zu den Builder-Previews (A: `f8ff307d…`, B: `f430d56d…`) — der Read-back-Rendepfad ist deterministisch und die Previews stammen tatsächlich aus den Dateien.
3. **Schritt 2 — REPORTs und checks.json der Builder gelesen und gegen die eigenen Messungen eingeordnet** (vor der Kriterienprüfung): Die Kernangaben beider REPORTs wurden an den eigenen Read-back-Dumps nachgemessen und bestätigen sich (Geometrie 0/28/80, Popup-Höhen 160/32, Zeilen 32, scroll-end-Versatz −64, Schatten (0,2)/8/#00000033, Status-Positionen y=80/120/248, Farben, Texte, Namen). Abweichende Angaben: **B-REPORT Punkt 4** behauptet, der Platzhalter bleibe im disabled-Fall muted — das Artefakt zeigt `#94a3b8` (disabled-Token) → Report↔Artefakt-Widerspruch (§6.2). **B-REPORT** nennt „121 Knoten geschrieben = 121 wiedereingelesen“; der Read-back-Graph auf Disk hat 122 Knoten — Erklärung: die 121 zählen Seite + 120 Ebenen ohne den Document-Root-Knoten, den der Writer auf Disk zusätzlich speichert (CLI „120 nodes“ = 122 − Seite − Root). A-REPORT „136 Knoten = 1 Document + 1 Seite + 22 Top-Knoten + 112 Fall-Knoten“ — Rechenprobe stimmt. Beide REPORTs benennen ihre Adapter-Entscheidungen und Definitionslücken (A: 19 Punkte, B: 18 Punkte) — dokumentiert, nicht still ergänzt. A-REPORT `checks.json` (178 Prüfungen, 0 fehlgeschlagen) dokumentiert selbst die selbst-erfüllenden Checks (d01–d05, r01, p01, p03, x02) — die belastbare Last liegt in den 160 Fall-Prüfungen; B-REPORT `checks.json` (109/109) analog. Beide Manifeste `source-sha256.json` wurden gegen die aktuellen Definitionsdateien neu verglichen: A 21/21 identisch (`error-relay.scxml` nicht im Manifest), B 22/22 identisch.
4. **Schritt 3 — Maschinelle Kriterienprüfung:** `verify.py` prüft alle 91 Kriterien an den eigenen Read-back-Dumps (`original-a/b.json`) und schreibt `native-checks.json` (Einzelbeobachtungen wert-für-wert), `normalized-a/b.json` (normalisierte Komponentenwerte), `criterion-results.json` (Status + Beobachtung je Kriterium je Builder) und `definition-hash-check.json`. **Vor der Ausführung wurde das Skript (bestehende Fassung eines unterbrochenen Vorlaufs, s. §8/L3) gegen das versiegelte Kriterienset auditiert.** Erwartungswerte (Texte, Farben, Maße, Toleranzen, Fall-Sets) stimmen mit der Preregistrierung überein. Drei dokumentierte, judgments-neutrale Anpassungen (Ergebnis vor/nach Änderung identisch — beide Artefakte teilen die betroffenen Werte):
   - **E-056:** strenger Offset-Check (`== −64`) durch den versiegelten EXP-Radius ersetzt („Listeninhalt so versetzt, dass die letzte Zeile sichtbar“); der Offset-Spielraum ist Prüfbereich von U-002, nicht von E-056.
   - **E-060:** Zusatzpflicht „Meldungszeile h = 32px“ entfernt (U-003: die exakte Höhe der Meldungszeile wird ausdrücklich nicht als Verletzung gewertet); Höhe wird nur beobachtet (beide Builder: 32px).
   - **E-064 (B):** obs-Text korrigiert (B trägt kein pluginData; die Altfassung enthielt den A-Text „nur Writer-Artefakte layoutDirection/textDirection“).
   Altfassung erhalten unter `verify.py.prev-1216`. Nach dem frischen Lauf: **alle 182 Kriterienstatus mit dem Vorlauf identisch**; `native-checks.json`, `normalized-*.json`, `definition-hash-check.json` byte-identisch; in `criterion-results.json` nur die drei dokumentierten obs-Texte geändert.
5. **Schritt 4 — Vergleich und Einordnung:** Definitionstreue zuerst (§5, §6), danach semantische A↔B-Unterschiede (§7), jede Abweichung eingeordnet als *Verletzung klarer Regel | erlaubte Freiheit | unzureichend bestimmte Regel*. Freie Seitenanordnung, generierte IDs und Byte-Gleichheit sind keine Erfolgsbedingungen.
6. **Schritt 5/6 — Auswertung und Integrität:** `REVIEW.md`, `results.json`, `hashes.json`; Definitions-Hashes und Siegel am Ende erneut berechnet (§9).

Kontext-Disziplin: Tool-Ausgaben wurden gezielt gefiltert (grep/sed/python), Zwischenergebnisse in Dateien geschrieben, große Dumps nie mehrfach vollständig neu gelesen.

---

## 2. Befund pro Kriterium (91 Kriterien × 2 Designs)

Regelklasse/Kategorie aus dem versiegelten Set. „erfüllt“ bei Kriterien der Klasse *erlaubte Freiheit* (E-003, E-062) bedeutet: keine Beanstandung. Beobachtungen vollständig in `criterion-results.json` (mit allen Werten, Knotennamen, Fällen).

| ID | Kategorie | Regelklasse (versiegelt) | A | B | Befund (Wert/Beobachtung) |
|---|---|---|---|---|---|
| E-001 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Datei mit Original-Reader der gepinnten Umgebung vollständig eingelesen: figKiwiVersion=101, records=136, nodes=136, bytes=42176; render aus dem Wiedereingelesenen Graph… |
| E-002 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | 1 Seite &#x27;Autocomplete&#x27; mit 10 benannten Fall-Frames: closed, opening, loading, ready, active, scroll-end, selected, empty, error, disabled |
| E-003 | explicit | erlaubte Freiheit | erfüllt | erfüllt | Außenanordnung frei (keine Beanstandung); beobachtet: 22 Top-Knoten der Seite |
| E-004 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | 22/22 Definitionsdateien auf Disk (frische SHA-256 berechnet); Manifest Builder A: 21 Einträge, 21 identisch; Abweichungen: keine; nicht vom Manifest abgedeckt: [&#x27;autoco… |
| E-005 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Fall-Namen: [&#x27;closed&#x27;, &#x27;opening&#x27;, &#x27;loading&#x27;, &#x27;ready&#x27;, &#x27;active&#x27;, &#x27;scroll-end&#x27;, &#x27;selected&#x27;, &#x27;empty&#x27;, &#x27;error&#x27;, &#x27;disabled&#x27;] |
| E-006 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Jeder Fall ist ein eigener benannter FRAME mit eigener Teil-Hierarchie |
| E-007 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | active: ready-Layout (Popup 320×160, 7 Optionen), Highlight-Optionen=[&#x27;hamburg&#x27;] |
| E-008 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | selected: Popup-Präsenz=False, Input-Texte=[&#x27;Berlin&#x27;], Status=&#x27;Ausgewählt: Berlin.&#x27; |
| E-009 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | disabled: Popup-Präsenz=False, Rand-Token=border, Input-Texte=[&#x27;Stadt suchen …&#x27;] (Farben [&#x27;muted&#x27;]) |
| D-001 | derived | Verletzung klarer Regel | erfüllt | erfüllt | alle 10 Fälle: Popup/Rand/Aktiv-Option/Status konsistent mit Zustand (closed; active/{opening,loading,ready,empty,error}; active &amp; scroll-end = ready+activeKey; selected… |
| E-010 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | alle Teilarten (input, listbox/list, option, status, overlay.surface, overlay.scroll.viewport) als unterscheidbare benannte Knoten (Liste in den Listenfällen, Meldung in… |
| E-011 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Popup = eigener Surface→Viewport→Content-Zweig; Listbox = Scrollinhalt (Kind von overlay.scroll.content), Eigentum der Autocomplete |
| E-012 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | label über Input; Surface am Input verankert (y=80); Viewport im Popup geclippt; List im Scrollinhalt; eine Option pro stabilem Key; Status unter Popup bzw. Input |
| E-013 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Optionen über fachliche Keys benannt (21 Optionen): [&#x27;Option: berlin&#x27;, &#x27;Option: dresden&#x27;, &#x27;Option: hamburg&#x27;, &#x27;Option: koeln&#x27;, &#x27;Option: muenchen&#x27;, &#x27;Option: wien&#x27;, &#x27;Option… |
| E-014 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Keine zweite Auswahlmaschine im Overlay: Surface/Viewport/Content tragen keine zusätzlichen Knoten, Annotationen oder Zustandsdaten (nur Strukturkinder) |
| E-015 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Teil-Layers einzeln vorhanden und verständlich benannt, z. B. [&#x27;Label&#x27;, &#x27;Input&#x27;, &#x27;Status&#x27;, &#x27;Label&#x27;, &#x27;Input&#x27;, &#x27;Status&#x27;, &#x27;Label&#x27;, &#x27;Input&#x27;] … |
| E-016 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Label &#x27;Stadt auswählen&#x27; in allen 10 Fällen |
| E-017 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | &#x27;Stadt suchen …&#x27; (Ellipsenzeichen + Leerzeichen davor) in 6 Fällen mit leerem Query: [&#x27;closed&#x27;, &#x27;opening&#x27;, &#x27;ready&#x27;, &#x27;active&#x27;, &#x27;scroll-end&#x27;, &#x27;disabled&#x27;] |
| E-018 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | 7 Labels in der Reihenfolge [&#x27;Berlin&#x27;, &#x27;Hamburg&#x27;, &#x27;München&#x27;, &#x27;Dresden&#x27;, &#x27;Köln&#x27;, &#x27;Wien&#x27;, &#x27;Zürich&#x27;] in allen Listenfällen |
| E-019 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Key↔Label-Mapping korrekt; nur muenchen in disabled-Farbe (#94a3b8) markiert (alle 3 Listenfälle) |
| E-020 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Status-Text exakt je Fall (10/10) |
| E-021 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Query-Texte exakt je Fall: loading/error=&#x27;Be&#x27;, empty=&#x27;Atlantis&#x27;, selected=&#x27;Berlin&#x27;, übrige leer → Platzhalter |
| E-022 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | selected-Input zeigt [&#x27;Berlin&#x27;] (kein Platzhalter) |
| E-023 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | alle sichtbaren Texte der Fälle stammen aus Label/Placeholder/Query/Ergebnislabels/Statusmeldungen (stories.json, interface.json, accessibility.rules.json); Seitenmöbel … |
| D-002 | derived | Verletzung klarer Regel | erfüllt | erfüllt | leerer Query → Platzhalter; nicht leerer Query → Query-Text (10/10 Fälle konsistent) |
| E-024 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Komponentenbreite: 320 in 10 Fällen |
| E-025 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Input-Höhe: 44 in 10 Fällen |
| E-026 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Input-Breite: 320 in 10 Fällen |
| E-027 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Label-Höhe: 20 in 10 Fällen |
| E-028 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Status-Höhe: 20 in 10 Fällen |
| E-029 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Optionen 32px hoch (21/21 in 3 Listenfällen) |
| E-030 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Viewport max-height 160px, geclippt: [&#x27;loading: 32px, geclippt&#x27;, &#x27;ready: 160px, geclippt&#x27;, &#x27;active: 160px, geclippt&#x27;, &#x27;scroll-end: 160px, geclippt&#x27;, &#x27;empty: 32px, geclip… |
| E-031 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Input 1px-Rahmen (weight 1, INSIDE) in 10 Fällen; Overlayfläche border 0 (kein Stroke) in 6 Fällen |
| E-032 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Radius 8px an Input (10) und Overlayfläche (6) |
| D-003 | derived | Verletzung klarer Regel | erfüllt | erfüllt | Viewport 160px = min(7×32, 160) in ready/active/scroll-end |
| D-004 | derived | Verletzung klarer Regel | erfüllt | erfüllt | maximal 5 Zeilen gleichzeitig sichtbar (160/32=5) in allen 3 Listenfällen |
| E-033 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Label→Input = 8px in 10 Fällen |
| E-034 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Input→Popup = 8px in 6 Fällen |
| E-035 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Status-Abstand 8px zum Bezugselement (Popup bei 6, Input bei 4 Fällen) |
| E-036 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Input-Text links bei x=12 in 10 Fällen; Rahmenschlagwörter (padding-Properties): [&quot;{&#x27;paddingTop&#x27;: 0, &#x27;paddingRight&#x27;: 0, &#x27;paddingBottom&#x27;: 0, &#x27;paddingLeft&#x27;: 0}&quot;]; vertikal… |
| E-037 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Option-Text bei (12,6) in 21/21 Optionen = Padding 6px/12px |
| E-038 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | alle verwendeten Farben ⊆ [&#x27;#000000&#x27;, &#x27;#172b4d&#x27;, &#x27;#2563eb&#x27;, &#x27;#64748b&#x27;, &#x27;#94a3b8&#x27;, &#x27;#b91c1c&#x27;, &#x27;#cbd5e1&#x27;, &#x27;#eaf2ff&#x27;, &#x27;#ffffff&#x27;] + Schlagschatten #000000@α0.2; Fills={&#x27;#172… |
| E-039 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Input-Hintergrund surface #ffffff (10); echte Query-Texte in #172b4d (loading/error/empty/selected); disabled-Fall hat nur Platzhalter (siehe E-041/Befund) |
| E-040 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Input-Rand je Fall: [&#x27;closed=border&#x27;, &#x27;opening=focus&#x27;, &#x27;loading=focus&#x27;, &#x27;ready=focus&#x27;, &#x27;active=focus&#x27;, &#x27;scroll-end=focus&#x27;, &#x27;selected=border&#x27;, &#x27;empty=focus&#x27;, &#x27;error=focus… |
| E-041 | explicit | Verletzung klarer Regel | erfüllt | verletzt | A=erfüllt | B=verletzt — disabled: #94a3b8 (disabled) |
| E-042 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Optionstext #172b4d; muenchen #94a3b8 (alle 3 Listenfälle) |
| E-043 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Aktive Option mit #eaf2ff (Hintergrund), Textfarbe unverändert: [&#x27;ready: highlight=[]&#x27;, &quot;active: highlight=[&#x27;hamburg&#x27;]&quot;, &quot;scroll-end: highlight=[&#x27;zuerich&#x27;]&quot;] |
| E-044 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Status #64748b; nur error #b91c1c (10/10) |
| E-045 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Overlayfläche weiß, border 0, Radius 8, Schatten 0 2px 8px #00000033: [&#x27;loading: #00000033 offset(0,2) r=8&#x27;, &#x27;ready: #00000033 offset(0,2) r=8&#x27;, &#x27;active: #00000033 offse… |
| E-046 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | alle Komponententexte (Label, Input, Optionen, Status, Meldung) fontFamily=Inter |
| E-047 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Label/Input/Optionen/Meldung 14px (alle Fälle) |
| E-048 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | line-height 20px an allen Komponententexten (Label/Input/Optionen/Status) |
| E-049 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Status 12px in allen 10 Fällen |
| D-005 | derived | Verletzung klarer Regel | erfüllt | erfüllt | Label/Input/Optionen: Inter 14/20 #172b4d ohne eigene Overrides (muenchen-Ausnahme regelt E-042) |
| D-006 | derived | Verletzung klarer Regel | erfüllt | erfüllt | Optionstext mittig: 6px + 20px + 6px = 32px Zeilenhöhe (21/21) |
| U-001 | underdetermined | unzureichend bestimmte Regel | nicht anwendbar | nicht anwendbar | A=nicht anwendbar | B=nicht anwendbar — font-weight/letter-spacing/Transformation in der Definition nicht festgelegt; beobachtet: Builder A setzt fontWeight=400 an allen Komponententexten (erlaubt) |
| E-050 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Label oben (0,0, h=20), Input darunter bei y=28 (10/10) |
| E-051 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Popup-Oberkante bei y=80 = Input-Unterkante 72 + 8 (6/6) |
| E-052 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Popup 320px breit, linke Kante fluchtet mit Input (x=0, 6/6) |
| E-053 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | closed/opening/selected/disabled: keine Popupteile, kein Layout-Platz, Status direkt unter Input (y=80) |
| D-007 | derived | Verletzung klarer Regel | erfüllt | erfüllt | Status nach 8px unter tatsächlich sichtbarem Popup bzw. Input |
| D-008 | derived | Verletzung klarer Regel | erfüllt | erfüllt | Status-Position je Fall korrekt: unter Popup in loading/ready/active/scroll-end/empty/error, unter Input in closed/opening/selected/disabled |
| E-054 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Viewport clippt seinen Inhalt (clipsContent=true, 6/6); Inhalt &gt; 160px wird geclippt (Listefälle: 224px Inhalt) |
| E-055 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | scroll-end: Zürich abs. y 208…240 in Viewport 80…240 (vollständig sichtbar) |
| E-056 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Statischer Content-Versatz relativ zur Viewport-Oberkante: [&#x27;loading:0&#x27;, &#x27;ready:0&#x27;, &#x27;active:0&#x27;, &#x27;scroll-end:-64&#x27;, &#x27;empty:0&#x27;, &#x27;error:0&#x27;] (scroll-end -64 = 224−160, maxima… |
| E-057 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | alle 7 Ergebniszeilen als editierbare Layers in jedem Listenfall vorhanden, inkl. geclippter (wien/y=160, zuerich/y=192) — nichts gelöscht |
| D-009 | derived | Verletzung klarer Regel | erfüllt | erfüllt | ready/active (Scroll oben): sichtbar Berlin…Köln (5), geclippt wien+zuerich — beide vorhanden |
| U-002 | underdetermined | unzureichend bestimmte Regel | nicht anwendbar | nicht anwendbar | A=nicht anwendbar | B=nicht anwendbar — Scroll-Offset in scroll-end nicht numerisch festgelegt; beobachtet: Builder A wählt y=-64 (maximaler Scroll, 224−160=64); damit 2 Zeilen geclippt — Inkonsistenz README &#x27;… |
| E-058 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Popup sichtbar genau in loading/ready/active/scroll-end/empty/error; opening laut Projection popupVisible=false → kein Popup (beide Builder) |
| E-059 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | disabled: keine sichtbaren Popupteile (kein Surface-/Viewport-/List-Knoten) |
| D-010 | derived | Verletzung klarer Regel | erfüllt | erfüllt | genau 6 Fälle mit sichtbarem Popup, 4 ohne |
| E-060 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Meldungszeile im Popup wiederholt den Status-Text; beobachtete Zeilenhöhe {&#x27;loading&#x27;: 32, &#x27;empty&#x27;: 32, &#x27;error&#x27;: 32} (U-003: exakte Höhe/Farbe nicht als Verletzung gewert… |
| U-003 | underdetermined | unzureichend bestimmte Regel | nicht anwendbar | nicht anwendbar | A=nicht anwendbar | B=nicht anwendbar — Höhe/Farbe der Meldungszeile nicht vollständig festgelegt; beobachtet: Builder A nutzt 32px (rowHeight) mit Textfarbe #172b4d — dokumentierte Annahme, nicht geahndet |
| E-061 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | editierbares OpenPencil-Design: 136 Vektor-/Text-Knoten mit editierbaren Properties (Fills/Strokes/Texte/Geometrie), benannte Hierarchie; keine Rasterkopie (0 IMAGE-Knot… |
| E-062 | explicit | erlaubte Freiheit | erfüllt | erfüllt | Keine Interaktivität/ARIA-Ausführung/Canvas-Interaktion gefordert — nichts derartiges vorhanden, wird nicht beanstandet (erlaubte Freiheit) |
| E-063 | explicit | Verletzung klarer Regel | verletzt | verletzt | A=verletzt | B=verletzt — Rollen-Zuordnung über lesbare Namen: input=combobox: False; list=listbox: False; option: True; status: True. Teil-Namen im Dokument: [&#x27;Autocomplete/active&#x27;, &#x27;Autocomplet… |
| E-064 | explicit | Verletzung klarer Regel | verletzt | verletzt | A=verletzt | B=verletzt — Wert &#x27;aria-autocomplete=list&#x27; nicht ablesbar: keine aria-Annotation in Layer-Namen, Text, Captions oder pluginData (es ist kein pluginData vorhanden) |
| E-065 | explicit | Verletzung klarer Regel | verletzt | verletzt | A=verletzt | B=verletzt — Werte false/true von aria-expanded nicht ablesbar (nirgends &#x27;expanded&#x27;); B: Fall-Namen enthalten den Zustandsnamen; Werte selbst fehlen |
| E-066 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | genau eine hervorgehobene (aria-selected-repräsentierende) Option pro Fall = die aktive; keine zweite; selected bestätigt keinen value (selected-Fall ohne Highlight) |
| E-067 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | active → hamburg hervorgehoben; scroll-end → zuerich; ready → keine; alle übrigen Fälle ohne Popup/Optionen |
| E-068 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | nur muenchen in disabled-Farbe (aria-disabled-Repräsentation); keine andere Option |
| E-069 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | muenchen in allen drei Sichtbarkeitsfällen (ready/active/scroll-end) disabled (#94a3b8) |
| E-070 | explicit | Verletzung klarer Regel | verletzt | verletzt | A=verletzt | B=verletzt — Attributwert &#x27;aria-activedescendant&#x27; nicht ablesbar; B: nur Highlight-Füllung, keine Annotation des Keys |
| E-071 | explicit | Verletzung klarer Regel | verletzt | verletzt | A=verletzt | B=verletzt — Status-Region: Rolle &#x27;status&#x27; lesbar via Layer-Name=True; aria-live=&#x27;polite&#x27;=False; aria-atomic=&#x27;true&#x27;=False — live/atomic-Werte in keinem Namen, Text, Caption oder plug… |
| E-072 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | Namensquellen realisiert: Input-/List-Name aus Label &#x27;Stadt auswählen&#x27; (Label-Knoten über Input); Option-Name = result.label; Platzhalter &#x27;Stadt suchen …&#x27; aus interface.… |
| E-073 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | keine zusätzlichen Fokus-/Tabstop-Annotationen an Popup/Viewport (negativer Check: nirgends tabindex/focus-Annotation); Input-Fokus semantisch im Input (Fokusrand), nich… |
| E-074 | explicit | Verletzung klarer Regel | erfüllt | erfüllt | ARIA-Werte nur als semantische Annotationen (benannte Teile, Label-, Status-, Aktiv-/Deaktiv-Stile); statisches Design ohne funktionales Screenreader-Verhalten — keine B… |
| U-004 | underdetermined | unzureichend bestimmte Regel | nicht anwendbar | nicht anwendbar | A=nicht anwendbar | B=nicht anwendbar — Darstellungsform der ARIA-Attribute nicht spezifiziert; beobachtet: Builder A = Layer-Namen + Captions mit Phase/SCXML-Pfad/aktiv-/value-Angaben; maschinenlesbare aria-*… |
| U-005 | underdetermined | unzureichend bestimmte Regel | nicht anwendbar | nicht anwendbar | A=nicht anwendbar | B=nicht anwendbar — Pflicht eines leeren Status-Layers in closed/disabled offen; beobachtet: Builder A lässt Status-Knoten mit leerem Text vorhanden (closed: w=0, disabled: w=0) |
| U-006 | underdetermined | unzureichend bestimmte Regel | nicht anwendbar | nicht anwendbar | A=nicht anwendbar | B=nicht anwendbar — error-relay.scxml keinem Designfall zugeordnet; beobachtet: kein Fall im Dokument; fehlt zusätzlich im Quell-Manifest des Builders (21/22 Dateien), im REPORT dokumentiert |
| U-007 | underdetermined | unzureichend bestimmte Regel | nicht anwendbar | nicht anwendbar | A=nicht anwendbar | B=nicht anwendbar — Existenz platzneutraler Popup-Layer in verborgenen Fällen nicht festgelegt; beobachtet: Builder A erzeugt in closed/opening/selected/disabled keine Overlay-Knoten (Varia… |

---

## 3. Kriterien-Zählung

| Builder | erfüllt | verletzt | nicht anwendbar | Summe |
|---|---|---|---|---|
| A gesamt | 79 | 5 | 7 | 91 |
| A explizit | 69 | 5 | 0 | 74 |
| A abgeleitet | 10 | 0 | 0 | 10 |
| A unzureichend bestimmt | 0 | 0 | 7 | 7 |
| B gesamt | 78 | 6 | 7 | 91 |
| B explizit | 68 | 6 | 0 | 74 |
| B abgeleitet | 10 | 0 | 0 | 10 |
| B unzureichend bestimmt | 0 | 0 | 7 | 7 |

Die 7 „nicht anwendbar“-Fälle sind die U-Kriterien (U-001…U-007) — bei beiden Buildern beobachtet und dokumentiert, aber nicht bemessbar (s. Tabelle).

---

## 4. Definitionstreue — was beide Designs exakt treffen

Beide Artefakte sind im Kern deckungsgleich und treffen die ganze geometrische, typografische, textliche und strukturelle Definition:

- **Fälle und Anatomie:** 10 benannte Fall-Frames (A: `closed`…; B: `Autocomplete/closed`…), pro Fall label/input/status; in 6 Fällen overlay.surface → overlay.scroll.viewport (geclippt) → content → list (7× option, pro Fach-Key) bzw. Meldung; alle 7 Keys `berlin…zuerich` in der festen Reihenfolge; Listbox ist der Scrollinhalt (Eigentum der Autocomplete); keine zweite Auswahlmaschine im Overlay.
- **Geometrie (identisch in beiden):** Label (0,0), 20px; Input (0,28), 320×44, Radius 8, 1px-Rahmen; Popup (0,80), 320×160 (Listen) bzw. 320×32 (Meldungen), Radius 8, weiß, border 0, Schatten 0/2px/8px/#00000033; Zeilen 320×32 bei y=0/32/…/192; Status y=80 (ohne Popup) bzw. y=120 (Meldungs-Popup) bzw. y=248 (Listen-Popup), 20px, 12px-Schrift; Gaps durchweg 8px (Label→Input, Input→Popup, Popup/Input→Status).
- **Typografie/Farbe:** Inter 14/20 (Label, Input, Optionen, Meldungen), Status 12/20; Optionstext (12,6) = Padding 6/12; Input-Text x=12; Tokenfarben exakt (alle verwendeten Farben ⊆ der 8 Token + Schatten-Schwarz); Fokusrand #2563EB genau in opening/loading/ready/active/scroll-end/empty/error, sonst #CBD5E1; Input-Füllung #FFFFFF; Platzhalter #64748B (A in allen 6 leeren Fällen; B in 5 von 6 — §6.2); Optionstext #172B4D, `München` #94A3B8; Highlight #EAF2FF nur an der aktiven Option; Status #64748B, im error-Fall #B91C1C.
- **Texte:** Label „Stadt auswählen“ (10/10), Placeholder „Stadt suchen …“ (Ellipsenzeichen + Leerzeichen) bei leeren Queries, Query-Texte „Be“/„Atlantis“/„Berlin“ exakt, Status-Texte je Fall exakt (inkl. leer in closed/disabled), 7 Ergebnislabels in fester Reihenfolge, Meldungszustände wiederholen den Status-Text als Zeile im Popup.
- **Zustandssemantik:** Popup sichtbar genau in loading/ready/active/scroll-end/empty/error (opening ohne Popup laut `projections.popupVisible=false`); active/scroll-end = ready + activeKey (`hamburg` bzw. `zuerich` hervorgehoben, `aria-selected`-Semantik visuell); selected = closed + value („Berlin“ im Input, Status „Ausgewählt: Berlin.“); disabled = closed + enabled=false (keine Popupteile, border-Farbe, leerer Status); `München` disabled in allen Sichtbarkeitsfällen.
- **Clipping/Scrolling:** Viewport clippt (clipsContent=true in beiden), 160px = min(7×32,160); ready/active: Zeilen 1–5 (Berlin…Köln) sichtbar, Wien/Zürich geclippt aber vorhanden; scroll-end: Content-Versatz −64 (in beiden), Zürich (letzte, aktive Option) vollständig im Viewport, alle 7 Zeilen editierbar erhalten.
- **Dokument/Editierbarkeit:** echte binäre OpenPencil-Dateien, vollständige Population, 0 IMAGE-Knoten, benannte editierbare Hierarchie, kein flaches Raster; keine Interaktivität (ausdrücklich nicht gefordert).
- **Definition unverändert:** 22/22 frische SHA-256-Hashes unter `components/` (unabhängig berechnet) decken sich mit beiden Quell-Manifesten und dem Lauf-Check (§9).

---

## 5. Gemeinsame Verletzungen (beide Designs)

Fünf explizite Kriterien verletzt, in beiden Artefakten dieselbe systematische Lücke: **der Accessibility-Annotationsvertrag der Definition ist nicht als lesbare Annotation in das Design-Document übertragen.**

| Kriterium | Versiegelte Erwartung | Beobachtung (A | B) |
|---|---|---|
| **E-063** | Rollen combobox/listbox/option/status den Teilen zugeordnet | A: 3/4 Rollenwerte lesbar (Listbox, `Option: <key>`, Status) — **combobox fehlt**; B: 2/4 (`option/<key>`, status) — **combobox und listbox fehlen** (B nennt die Listbox `list`) |
| **E-064** | `aria-autocomplete=list` ablesbar | kein Vorkommen in Layer-Namen, Text, Captions (A) oder pluginData |
| **E-065** | `aria-expanded`-Wert je Zustand ablesbar | nirgends „expanded“; A-Captions nennen Phase/SCXML-Pfad — der Wert selbst ist nur über die externe `accessibility.rules.json` ableitbar |
| **E-070** | `aria-activedescendant` auf aktive Option (hamburg/zuerich), sonst nicht vorhanden | Attributwert nirgends; A: Caption „aktiv: hamburg“/„aktiv: zuerich“ (Key lesbar, Attribut fehlt); B: nur Highlight-Füllung |
| **E-071** | Status mit role=status, `aria-live=polite`, `aria-atomic=true` | Rolle „status“ lesbar (beide), **live/atomic-Werte in keinem Namen, Text, Caption oder pluginData** |

Einordnung: U-004 (unzureichend bestimmte Regel) lässt die **Darstellungsform** der ARIA-Annotationen frei (Label-Text, Notiz, Property, Kommentar), verlangt aber, dass die ARIA-**Werte** „korrekt und nachvollziehbar abbildbar“ sind. Die Werte sind in beiden Artefakten nicht in ablesbarer Form vorhanden → die expliziten Kriterien E-063/E-064/E-065/E-070/E-071 (Regelklasse „Verletzung klarer Regel“) gelten als verletzt. Beide Builder wussten darum und dokumentierten es selbst (A-REPORT Punkt 11: „ARIA/semantik wird nicht in die Datei geschrieben … nicht maschinenlesbar zurückgewinnbar“; B-REPORT Punkt 16: „Keine Interaktivität/ARIA im Canvas … werden im Design nicht ausgeführt“). Die Teil-Erfüllungen (E-066/E-067: exakt eine hervorgehobene aktive Option; E-068/E-069: nur `muenchen` disabled; E-072: Namensquellen; E-073: keine zusätzlichen Tabstops; E-074: Annotationsemantik ohne SR-Verhaltensanspruch) sind in beiden Designs erfüllt — die Verletzungen beschränken sich auf die fehlenden attributiven ARIA-Werte.

## 6. Verletzungen nur in einem Design

### 6.1 A (keine weiteren)

A verletzt ausschließlich die fünf gemeinsamen Kriterien.

### 6.2 B: E-041 — Platzhalterfarbe im disabled-Fall

- **Beobachtung (eigene Messung an `original-b.json`):** `Autocomplete/disabled` → `input` → `input.query`: Text „Stadt suchen …“, Farbe **`#94a3b8`** (Token `disabled`). In A derselbe Knoten: **`#64748b`** (Token `muted`).
- **Versiegelte Regel (E-041, explizit, „Verletzung klarer Regel“):** Platzhalterfarbe = muted #64748B, „in allen Fällen mit leeren Query“ — der disabled-Fall hat einen leeren Query.
- **Report↔Artefakt-Widerspruch:** B-REPORT Punkt 4 dokumentiert die Entscheidung „Strenge gelesen bleibt der Placeholder auch im disabled-Fall muted“ — das Artefakt implementiert das Gegenteil. Der Report beschreibt also nicht den tatsächlichen Dateiinhalt.
- **Hintergrund (Definitionslücke):** `components/autocomplete/layout.css` enthält das spannungsbehaftete Paar `::placeholder { color: muted }` und `:disabled { color: disabled }`; bei leerem Query ist der sichtbare Input-Text der Platzhalter, sodass die beiden CSS-Regeln (und damit die daraus abgeleiteten Kriterien E-041 und die disabled-Klausel von E-039) nicht gleichzeitig vollständig erfüllbar sind. A wählte muted (E-041 erfüllt), B wählte im Artefakt disabled (E-041 verletzt, obwohl der Report muted dokumentiert). Die Spannung ist in der Preregistrierung **nicht** als U-Kriterium erfasst (Provenienz-Limitation L1) — bemessen wurde nach dem versiegelten Wortlaut (E-041).
- **E-039** (Input-Textfarbe; disabled-Klausel „Textfarbe = disabled“): in beiden Designs ist im disabled-Fall kein echter Query-Text sichtbar (nur Platzhalter); die messbaren Klauseln (Hintergrund surface, Query-Texte #172B4D) sind in beiden erfüllt. Die disabled-Klausel bleibt als Teil der genannten Definitionsspannung unbeobachtbar, nicht als zusätzliche Verletzung gezählt.

---

## 7. Unterschiedsanalyse A↔B (semantisch, Komponentenlevel)

Alle Abweichungen der Wert-für-Wert-Vergleich (`pair-comparison.json`) mit Einordnung:

| # | Unterschied (A | B) | Einordnung | Kriterienrelevanz |
|---|---|---|---|---|
| 1 | Fall-Frame-Namen `closed`… | `Autocomplete/closed`… (10×) | erlaubte Freiheit (E-003/E-006: „bzw. klar darauf bezogene Namen“; E-015: verständlich benannt — beide erfüllt) | keine |
| 2 | Textbreiten Label/Input/Status: A schmaler (z. B. Label 110 | 126, Status 109 | 137) (30×) | erlaubte Freiheit — Textbreiten sind in der Definition nicht festgelegt; Ursache: unterschiedliche Metriken-Quellen (A: echte Inter-Metriken via CanvasKit, B: System-Fallback beim Messrender, B-REPORT Punkt 18). Sichtbare Konsequezen: keine (Autosize-Texte, keine festgelegten Breiten) | keine |
| 3 | `input.clipsContent` true | false (10×) | erlaubte Freiheit — Input-Clipping ist kein Kriterium (E-025/E-031 legen Höhe/Rahmen fest, nicht Clipping) | keine |
| 4 | `surface.clipsContent` true | false (6×) | erlaubte Freiheit — nur das Viewport-Clipping ist normativ (E-054/E-030: in beiden true); das Surface-Clipping ist redundante Absicherung bei A | keine |
| 5 | Meldungsfälle: A umschließt `Message Row` in einem `Listbox`-Frame; B hängt `message` direkt unter `overlay.scroll.content` (3×) | — | erlaubte Freiheit — Teilzuordnung (E-010/E-011) bleibt in beiden erfüllt; B-REPORT Punkt 6 dokumentiert die Namenskürzung, A-REPORT Punkt 9 die Schichtnamen | keine |
| 6 | Leerer Status-Layer in closed/disabled: A Breite 0 | B Breite 100 (2×) | unzureichend bestimmte Regel (U-005: ob ein leerer Layer Pflicht ist, offen; beide vorhanden mit leerem Text → E-020 erfüllt) | keine |
| 7 | **Platzhalterfarbe disabled: A `#64748b` (muted) | B `#94a3b8` (disabled)** | **Verletzung klarer Regel (E-041) nur bei B**; zugrundeliegend eine in der Preregistrierung nicht erfasste Definitionsspannung (E-039/E-041, §6.2) | **ja — einzige kriterienrelevante Abweichung des Laufs** |
| 8 | Seitenmöbel: A 22 Top-Knoten (Titel, Quellenzeile, 10 Frames, 10 Captions mit Phase/SCXML/aktiv-/value-Infos) | B 11 Top-Knoten (1 Seitentitel, 10 Frames); Knotenzahl 136 | 122 | erlaubte Freiheit (E-003); A-Captions sind die einzige (unzureichende) ARIA-Näherung, B verzichtet | keine |
| 9 | pluginData: A trägt Writer-Artefakte (`layoutDirection`, `textDirection`); B keins | — | erlaubte Freiheit (Writer-Implementationsdetail, keine Kriterienvorgabe) | keine |

**Keine Unterschiede** in: Positionen aller Teile, Höhen, Radien, Rahmen, Füll-/Strich-/Schatten-Token (außer #7), Schriften, Größen, Zeilenhöhen, allen Texten, Keys, Labels, Highlight-/disabled-Versatz, Scroll-Versatz, Popup-Sichtbarkeits-Matrix, Status-Texten.

## 8. Paarübereinstimmung (Maß + Band)

- **Maß:** Wert-für-Wert-Vergleich der normalisierten Komponentenwerte (identische Extraktion aus beiden Read-back-Dumps; `pair-comparison.json`): alle Teil-Attribute pro Fall (Positionen, Maße, Radien, Clips, Fills/Strokes/Schatten, Texte, Typografie, Keys, Labels, Scroll-Versatz, Sichtbarkeits-/Clipping-Fakten). Ausgeschlossen: Layer-Namen und generierte IDs sowie freie Seitenmöbel (keine Erfolgsbedingungen laut Auftrag).
- **Ergebnis:** **1145 von 1208 Vergleichswertepaaren identisch = 94,78 %**.
- **Band:** 90–95 % (definierte Bänder: 100 % / 99–<100 % / 95–<99 % / 90–<95 % / <90 %).
- **Einordnung:** Die 63 abweichenden Paare setzen sich zu 10 aus Namen (#1), 30 aus Textbreiten (#2), 10 aus `input.clipsContent` (#3), 6 aus `surface.clipsContent` (#4), 3 aus der Meldungsrahmen-Struktur (#5), 2 aus der leeren-Status-Breite (#6) zusammen — zusammen mit den 2 Paaren der Platzhalterfarbe disabled (#7: color + colorToken) ergibt das 63. **Auf kriterienrelevante Werte (alle durch E/D-Kriterien bemessenen Attribute) beträgt die Paarübereinstimmung 100 % mit der einen Ausnahme #7** — die beiden Designs sind also in allen regelbelegten Dimensionen identisch; die Unterschiede liegen in der frei gewählten Realisierung.
- **Zusatzbeobachtung (keine Erfolgsbedingung):** Die vom Prüfer unabhängig aus den Originaldateien neu gerenderten PNGs sind byte-identisch zu den Builder-Previews (A `f8ff307d…`, B `f430d56d…`) — die Render-Kette ist deterministisch; bytegleiche Artefakte zwischen A und B bestehen **nicht** (unterschiedliche Writer-Id/Session, Layout-Namen, Textmetriken).

## 9. Integrität (Schlussprüfung, frisch berechnet)

- **Definitionen (22 Dateien unter `components/`):** alle 22 SHA-256-Hashes am Laufende unabhängig neu berechnet — **unverändert**; sie decken sich mit (i) `definition-hash-check.json` (frischer verify.py-Lauf) und (ii) den Quell-Manifesten beider Builder (A: 21/21 identisch, `error-relay.scxml` nicht im Manifest — dort als nicht verwendet dokumentiert; B: 22/22 identisch). Die Definition wurde von keinem der Builder geändert; `error-relay.scxml` ist in keinem Design repräsentiert (U-006, nicht bemessbar).
- **Siegel:** `preregistration-seal.json` zum **Laufstart** und erneut zum **Lauflende** verifiziert — beide SHA-256-Werte (preregistered.json `2faa6a86…`, preregistered.md `64f96044…`) in beiden Prüfungen identisch mit dem Siegel. Die Kriterienbasis wurde während des Laufs nicht berührt.

## 10. Provenienz und Limitationen (mit Auswirkung auf die Aussagekraft)

- **L1 — Getrennte Prüfer-Sessions (Prämissen-Limitation des Laufs):** Phase 1 (Kriterienableitung aus der Definition allein, Versiegelung 2026-10-29T09:29Z) lief in einer anderen Session, die durch einen Providerfehler (HTTP 413) verloren ging. Phase 2 (dieser Bericht) arbeitet in einer frischen Session **ausschließlich von den versiegelten Kriterien auf Datenträger** — beabsichtigt, aber damit: (a) die Ableitung der Kriterien aus der Definition ist für Phase 2 nicht nachvollziehbar oder gegenprüfbar; (b) Abweichungen zwischen versiegeltem Set und Definition können nicht rückwirkend korrigiert werden — sie werden nur ausgewiesen. Konkret betroffen: die E-039/E-041-Platzhalter-Spannung im disabled-Fall ist in der Definition real (CSS), aber in der Preregistrierung nicht als U-Kriterium erfasst, sodass B nach versiegeltem Wortlaut E-041 verletzt — obwohl beide Builder den Konflikt selbst korrekt dokumentiert hatten. Die Aussagekraft des Kriteriensets als „aus der Definition abgeleitet“ beruht damit auf dem versiegelten Zustand zum Zeitpunkt der Phase 1.
- **L2 — Builder-A-REPORT aus zweiter Session:** Die Erzeugungssession von A wurde nach dem Schreiben aller sechs Artefakte (alle 11:07) durch denselben Providerfehler (HTTP 413) beendet, **bevor** `REPORT.md` existierte; eine Fortsetzung war unmöglich. `REPORT.md` (A) wurde von einer neuen Session ausschließlich aus vorhandenen Artefakten, `components/` und der gepinnten Werkzeugumgebung geschrieben (kein Zugriff auf verbotene Eingaben durch beide Sessions). Auswirkung: der A-Report ist eine nachträgliche Rekonstruktion ohne Kenntnis der Erzeugungsintention im Speicher; **alle** seine inhaltlichen Aussagen wurden vom Prüfer eigenständig an den Originaldateien verifiziert (§1/2) — keine Report-Aussage wurde ungeprüft übernommen. Auf die Artefakte selbst hat die Unterbrechung keine nachweisbare Auswirkung (Vollständigkeit, Konsistenz, Reimport-Stabilität bestätigt). B lief in einer einzelnen, durchgehenden Session ohne Unterbrechung.
- **L3 — Unterbrochener Phase-2-Vorlauf im Ausgabeordner:** Zum Start dieser frischen Session lagen im `review/`-Ordner Skripte und Zwischendateien eines unterbrochenen Phase-2-Vorlaufs (11:34–12:16) vor. Der Prüfer hat das vorhandene `verify.py` **vor** der Ausführung gegen das versiegelte Kriterienset auditiert und drei dokumentierte, judgments-neutrale Anpassungen vorgenommen (§1, Schritt 3; Altfassung `verify.py.prev-1216`); die komplette Messkette (Read-back, Render, verify) wurde **neu** ausgeführt. Kreuzvalidierung: die frischen Read-back-Dumps und Renders sowie `native-checks.json`/`normalized-*.json`/`definition-hash-check.json` sind mit dem Vorlauf byte-identisch; in `criterion-results.json` sind nur die drei dokumentierten obs-Texte geändert, **alle 182 Kriterienstatus unverändert** — die Vorlauf-Ergebnisse sind damit als deterministisch reproduzierbar bestätigt.

## 11. Grenzen des Laufs

- Keine signifikanten Tests, keine Erfolgsquoten über den Lauf hinaus: Zustandsfälle und Assert-Felder sind Teilbeobachtungen derselben Komponente, keine unabhängigen Stichproben (91 Kriterien × 2 Designs = 182 Bemessungen derselben zwei Artefakte).
- Die Paarübereinstimmung (94,78 %) beschreibt die zwei vorliegenden Artefakte; sie ist keine Aussage über die Verteilung möglicher Builder-Interpretationen (insbesondere bei den unter U-Kriterien ausgeblendeten Freiheitsgraden).
- Bilder (Renders, Previews) ersetzen keine Knoten-/Wertbeobachtungen; sie dienten der Bestätigung (byte-Identität der Renderkette), nicht der Bemessung.
- Textbreiten sind von den jeweiligen Metriken-Quellen der Builder abhängig (siehe #2); dies ist kein Kriterium, aber eine Ursache für die Nicht-Byte-Identität der Artefakte.
- Die ARIA-Bemessung ist an ablesbare Werte in Namen/Text/Captions/pluginData gebunden (einzige maschinenlesbare Kanäle des OpenPencil-Formats); eine „implizite“ Zuordnung über externe Definitionsdokumente zählt nach versiegeltem Wortlaut (U-004: „nachvollziehbar abbildbar“) nicht als Abbildung im Dokument.

---

## 12. Ergebnis (Zusammenfassung)

- **Urteil je Design:**
  - **A:** Substanziell erfüllt — 79/91 erfüllt, 5 verletzt (alle: ARIA-Annotationswerte nicht ablesbar, §5), 7 nicht anwendbar (U-Kriterien). Keine Report-Abweichung; Adapter-Entscheidungen und Definitionslücken vollständig dokumentiert (19 Punkte).
  - **B:** Substanziell erfüllt — 78/91 erfüllt, 6 verletzt (die 5 gemeinsamen + E-041 Platzhalterfarbe im disabled-Fall, §6.2), 7 nicht anwendbar. Zusätzlich: B-REPORT Punkt 4 widerspricht dem eigenen Artefakt (muted dokumentiert, disabled implementiert).
- **Gemeinsame Verletzungen (beide):** E-063, E-064, E-065, E-070, E-071 — systematische Lücke: ARIA-Werte der Definition (combobox, aria-autocomplete, aria-expanded, aria-activedescendant, aria-live/atomic) sind in keinem der beiden Artefakte als lesbare Annotation vorhanden (beide Builder haben dies in ihren Reports selbst ausgewiesen).
- **Paarübereinstimmung:** 1145/1208 Wertepaare = **94,78 %** (Band 90–95 %); auf kriterienrelevante Werte 100 % mit einer Ausnahme (disabled-Platzhalterfarbe, nur B verletzt).
- **Wichtigste Grenzen:** L1 (Prüfer-Phasen in getrennten Sessions; Phase 2 nur von versiegelten Kriterien → Ableitung nicht gegenprüfbar, E-039/E-041-Spannung unbehandelt im Set), L2 (A-Report aus zweiter Session — verifiziert, aber Rekonstruktion), L3 (Vorlauf-Artefakte im Ordner — auditiert, neu gelaufen, byte-/statusidentisch).
- **Siegel-/Integritätsprüfung:** bestanden — Siegel zum Laufstart und Lauflende identisch (Kriterien unverändert); 22/22 Definitionsdateien hash-stabil (unabhängig neu berechnet, deckungsgleich mit beiden Builder-Manifesten).

*Beobachtungsbasis: `original-a.json`/`original-b.json` (frische Read-backs), `native-checks.json`, `normalized-a/b.json`, `criterion-results.json`, `definition-hash-check.json`, `pair-comparison.json`, `render-a/b.png` (neu gerendert, byte-identisch zu den Builder-Previews). Alle Hashes in `hashes.json`.*
