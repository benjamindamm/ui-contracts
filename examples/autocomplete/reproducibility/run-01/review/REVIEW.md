# Unabhängige Prüfung · Definitions-Reproduzierbarkeit · run-01

## Ergebnis

Beide gespeicherten Designs sind mit dem unveränderten Originalreader lesbar und enthalten die zehn geforderten, separat benannten editierbaren Fälle. Die geprüften komponentenlokalen Darstellungen stimmen zwischen A und B überein. Gegen die Definition ergibt sich für beide **FAIL**, jeweils wegen derselben Platzhalterfarbe im deaktivierten Input. Alle übrigen im registrierten Umfang geprüften harten Kriterien sind erfüllt. Das ist ein eng begrenzter visueller Fehler, kein Befund über Laufzeitverhalten.

## Methode und Reihenfolge

Die Kriterien wurden vor Kenntnis der Ausgaben in `preregistered.json` und `preregistered.md` gespeichert. Grundlage war ausschließlich `components/`; die Vorabdateien wurden anschließend nicht geändert. Nach der ausdrücklichen Fertigmeldung wurden zuerst die beiden tatsächlichen `builder-a/autocomplete.fig` und `builder-b/autocomplete.fig` mit `parseFigFile({populate:'all'})` aus dem installierten Originalpaket `@open-pencil/core` 0.16.0 eingelesen. `original-a.json` und `original-b.json` halten die vollständigen gelesenen nativen Knoten fest. Danach wurden eigene PNGs mit dem Original-CanvasKit-Renderer erzeugt und betrachtet. Erst nach dieser direkten Prüfung wurden die beiden `REPORT.md` und `checks.json` gelesen.

`inspect-original.mjs`, `render-original.mjs` und `verify.py` dokumentieren die Hilfsmittel. Aufruf vom Projektstamm: `node examples/autocomplete/reproducibility/run-01/review/inspect-original.mjs`, danach entsprechend `render-original.mjs`, danach `python3 examples/autocomplete/reproducibility/run-01/review/verify.py`. Letzteres schreibt `native-checks.json` mit 396 Einzelbeobachtungen pro Artefakt sowie normalisierte Komponentenwerte. `results.json` enthält zusätzlich die manuelle Einordnung, Grenzen und Artefakthashes. Die Readerauszüge sind Belege und keine unabhängig gestalteten Ersatzdokumente.

Die Editierbarkeitsaussage beruht auf tatsächlichen nativen TEXT-/FRAME-Knoten, erhaltenen einzelnen Ergebniszeilen, getrennten Teilen und fehlenden Locks. Eine GUI-Öffnung, manuelle Editier-/Speicherprobe oder interaktive Preview wurde nicht durchgeführt. Ein erfolgreicher Originalimport plus Originalrender ist belegt.

## Befunde nach Vorabkriterium

Die Quellenpfade beziehen sich auf das unveränderte `components/`. Maschinenlesbare Einzelwerte mit tatsächlichen Reader-IDs und Sollwerten stehen in `results.json` beziehungsweise `native-checks.json`.

| Vorabkriterium | A | B | Quelle und tatsächliche Beobachtung |
|---|---|---|---|
| artifact | PASS | PASS | `autocomplete/README.md`, Exportrahmen: Originalreader liest gespeicherte FIG-Dateien; A 31.310 Bytes/127 Knoten, B 31.456 Bytes/136 Knoten. Native editierbare Texte/Frames; eigener Originalrender erfolgreich. |
| coverage | PASS | PASS | `autocomplete/README.md`, `stories.json`: alle zehn Fälle auf einer übersichtlichen Seite; A z.B. `closed` ID 0:7, B `Autocomplete / closed` ID 0:7. Namen eindeutig zuordenbar. |
| anatomy | PASS | PASS | `autocomplete/component.json`, README, Overlay-/ScrollArea-Definitionen: Input, Surface, geclippter Viewport, Listbox, Optionen, Label und Status getrennt. A bindet Liste direkt an Viewport, B fügt `overlay.scroll.content` ein. Beide erhalten alle verlangten editierbaren Teile. |
| fixtures | PASS | PASS | `stories.json`, `component.json`: alle Eingabetexte und sieben Ergebnislabels in richtiger Reihenfolge; München deaktiviert; Hamburg aktiv im Fall active, Zürich aktiv im Fall scroll-end; selected zeigt Berlin. Fachliche Keys stehen in Optionsnamen. Kein ausführbares value-Modell gefordert; statische Wert-/Aktivdarstellung konsistent. |
| visibility | PASS | PASS | `accessibility.rules.json`, README: closed/opening/selected/disabled ohne Popup; übrige Fälle mit Popup. Opening hat dennoch Fokusrahmen. Verborgene Popups beanspruchen keinen Komponentenplatz. |
| geometry | PASS | PASS | `tokens.json`, drei `layout.css`, README: Label (0,0,320,20); Input (0,28,320,44); Inputtext (12,12,296,20) relativ zum Input. Popup (0,80,320,32) für Meldungen oder Höhe160 für Ergebnisse. Status y80/120/248; Höhe20. Zeilen32, Textinset12/6, keine Listenmarker. |
| visual | **FAIL** | **FAIL** | `tokens.json`, `autocomplete/layout.css`, `overlay/layout.css`: alle geprüften Tokenfarben, Inter14/20, Status12/20, Radius8, Rahmen1, aktive Fläche und Schatten stimmen, **ausgenommen deaktivierter Platzhalter**: A Text 0:127 und B Text 0:136 verwenden #94A3B8 statt #64748B. |
| messages | PASS | PASS | `stories.json`, `accessibility.rules.json`, README: exakte deutschen Texte einschließlich Ellipse/Umlauten; opening-Meldung, 7 Städte, ausgewähltes Berlin und loading/empty/error-Meldungen korrekt. Popupmeldungen werden als Status wiederholt. Leerer Status bleibt als benannter Textknoten erhalten. |
| clipping | PASS | PASS | README und `scroll-area/layout.css`: tatsächliches `clipsContent=true`, Viewport160, Inhalt224, sieben editierbare Zeilen. scroll-end versetzt A die Liste, B den Content um −64. Zürich liegt im Viewportintervall [128,160] und ist im eigenen Render sichtbar. |
| semantic-design | PASS | PASS | `accessibility.rules.json`, `component.json`: verständliche benannte Semantik und sichtbare aktive/deaktivierte Stile. Keine zusätzliche sichtbare Auswahlmaschine im Overlay; keine Behauptung ausführbarer ARIA-Semantik. |
| source-integrity | PASS | PASS | Bibliotheks-README und Komponenten-README: sämtliche 22 Definitionsdateien stimmen mit den vorab gespeicherten SHA-256-Werten überein. Beide Berichte legen Annahmen offen. Hashprüfung belegt unveränderten Endstand, nicht lückenlose historische Zugriffskontrolle. |

## Harte Abweichung: deaktivierter Platzhalter

Die explizite CSS-Regel `[data-part="input"]::placeholder { color: var(--ac-muted); }` setzt die Farbe des Pseudoelements. `[data-part="input"]:disabled { color: var(--ac-disabled); ... }` setzt die Farbe des Inputs und damit grundsätzlich eine vererbbare Farbe; sie überschreibt die ausdrücklich gesetzte Farbe des Platzhalter-Pseudoelements nicht. Für den vorhandenen leeren disabled-Fall gilt deshalb muted (#64748B). Beide Originalgraphen enthalten stattdessen disabled (#94A3B8), deutlich außerhalb der registrierten Rundungstoleranz.

Die Vorabregistrierung hatte diese Kombination bereits erfasst und entschieden, dass der Platzhalter unter gewöhnlicher CSS-Auswertung muted bleibt. Die Builderberichte nennen denselben Punkt eine nicht ausdrücklich priorisierte Kombination und legen ihre disabled-Entscheidung offen. Diese Offenlegung ist hilfreich, hebt die explizite CSS-Regel aber nicht auf. Es wurde keine neue Erwartung nach Einsicht in die Designs eingeführt. Wer die Definition absichtlich anders priorisieren möchte, müsste dies in einem künftigen Versuch ausdrücklich ändern; diese Studie bewertet den unveränderten Stand.

## Paarvergleich

Nach Zuordnung der zehn Fallnamen und Normalisierung der Außenpositionen stimmen alle erfassten Komponentenwerte in `normalized-a.json` und `normalized-b.json` überein: Eingabetexte, Meldungen, lokale Boxen, Farben und die sichtbaren Optionsintervalle. Alle Font-/Rahmen-/Radius-/Schattenchecks treffen für beide dieselben Sollwerte, mit der genannten gemeinsamen Farbausnahme. Diese Feststellung ist umfangreicher als ein Bildähnlichkeitsurteil, aber keine Behauptung bytegleicher Dokumente oder vollständiger Gleichheit jeder nativen Eigenschaft.

Erlaubte Unterschiede: A hat feste Fallrahmenhöhe280, B fallabhängig100/140/268; Seitentitel, Außenpositionen und Abstände unterscheiden sich. A verwendet 65 native TEXT-Knoten, B ebenfalls65; die gesamte Knotenanzahl ist verschieden. B besitzt sechs zusätzliche ScrollContent-Gruppen und drei Meldungsframes. Namen und technische IDs sind verschieden beziehungsweise zufällig teilweise gleich. Diese Unterschiede verletzen keine registrierte Gleichheitsanforderung. A verschiebt im Scroll-Ende die Liste selbst, B ihren Content; die resultierende Komponentenprojektion ist gleich.

Die eigenen Originalrenders zeigen vollständige Fälle, sichtbare aktive Optionen und nicht überlappende Beschriftungen. Beim Scroll-Ende reicht die rechteckige aktive Fläche bis an das Viewportende; beide führen keine zusätzliche Rundclipregel auf der Surface aus. Das ist keine zusätzliche Fehlerwertung, weil eine solche Regel nicht definiert wurde.

## Definitionslücken und Widersprüche

UNSPECIFIED bleiben die bereits registrierten Punkte: Schriftgewicht und exakte native Inputbaseline; eigene CSS-Regel und Inset für Popupmeldungen; Scrollbarstil; native Metadaten-/Wrapperkodierung; exakte Pixelrasterung von CSS- gegenüber Skia-Schatten; zusätzliche Rundclipform der Popupoberfläche. Beide wählen Schriftgewicht400, zentrierten Inputtext sowie 12/6-Padding für Meldungszeilen. Ihre Übereinstimmung macht diese Entscheidungen nicht nachträglich normativ.

Ein beim Vergleich bemerkter Textwiderspruch ist ausdrücklich getrennt festgehalten: README nennt „die drei unsichtbaren Daten“, während Stories sieben Ergebnisse, rowHeight32 und maxHeight160 fünf sichtbare und zwei außerhalb liegende Zeilen ergeben. Die eindeutigen numerischen Vorgaben und das ausdrückliche Erhalten aller sieben Layer wurden angewandt; keine dritte unsichtbare Zeile wurde gefordert. Die Vorabdateien wurden hierfür nicht nachträglich ergänzt.

OUT_OF_SCOPE sind Tastatur-/IME-/Provider-/SCXML-Ausführung, tatsächliche Requestidentität, Screenreader/ARIA-Ausführung, HTML-/TypeScript-Ziel sowie dynamisches Scrollen. Diese statischen Dokumente können die entsprechenden Laufzeitregeln nicht nachweisen.

## Grenzen und Fazit

Dies ist eine kleine Stichprobe aus zwei Erzeugungen derselben Definition und derselben Werkzeug-/Modellkonfiguration. Es gibt keine statistische Generalisierung, keinen Vergleich unterschiedlicher Modelle oder Werkzeuge und keinen Nachweis vollständiger Prozessunabhängigkeit. Eine physische Dateisystemsandbox fehlte; die Trennung ist eine verfahrensmäßige Beschränkung und kann aus ähnlichen Bildern oder Enddateihashes nicht bewiesen werden. Die installierten Originalpakete wurden verwendet, aber nicht unabhängig gegen Upstream-Checksummen auditiert. Die GUI und eine manuelle Editierprobe wurden nicht ausgeführt.

Der Versuch liefert konkrete Evidenz dafür, dass zwei getrennte Erzeugungen die eng bestimmte statische Komponentenprojektion sehr ähnlich und in den erfassten Werten gleich umsetzen können. Gleichzeitig reproduzieren sie denselben kleinen Definitionsverstoß. Vollständige Definitionstreue ist daher für diesen Durchlauf nicht erreicht; die hohe gegenseitige Übereinstimmung ersetzt die unabhängige Quellenprüfung nicht.

## Nachweise

`results.json`: kriteriumsweise Urteile, Quellen, Original-IDs, Rohmessungen, Paarvergleich, Lücken und Grenzen. `native-checks.json`: reproduzierbare Einzelprüfungen. `original-{a,b}.json`: Originalreader-Auszüge. `render-{a,b}.png`: unabhängig erzeugte Originalrenders. `hashes.json`: SHA-256 der untersuchten FIG-Dateien, Berichte und sämtlicher Review-Nachweise außer der Hashdatei selbst.
