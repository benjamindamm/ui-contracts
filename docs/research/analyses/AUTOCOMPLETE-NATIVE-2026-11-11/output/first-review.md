# Unabhängige Erstprüfung des nativen Autocomplete-Piloten

Erstlieferung der gemeinsamen Story `active` auf iPhone 17 Pro, iOS 26.5 (Simulator, 3 px/pt, Content Size `large`), und Android `sdk_gphone64_arm64` (Emulator, 420 dpi beziehungsweise 2.625 px/dp, Font Scale 1.0). Beide im hellen Modus ohne Bildschirmtastatur. Installation und Start aus den eingefrorenen Lieferdateien mit dem Story-Argument, eigene Bildschirmaufnahmen nach der Startanimation. Die vier vermessenen Ausschnitte (Label, Eingabe, Popup, Status) waren bei beiden Plattformen pixelgleich mit den entsprechenden gelieferten Ausschnitten. Geprüft wurden die Originalquellen, die gemeinsame Policy und die Zielartefakte. Builderberichte wurden nicht eingesehen.

## Führende Regeln und gemessene Geometrie

Die Autocomplete-, Overlay- und Scroll-Area-CSS-Regeln binden die gemeinsamen Tokens. `active` projiziert den Zustand `ready` mit sichtbarem Popup. Die eigene Barrierefreiheitsregel legt den Status nach dem sichtbaren Popup fest. Ein aktiver Treffer bleibt vom bestätigten Schlüssel getrennt. Die Policy legt für den Piloten die Umrechnung CSS-px → pt/dp und die geometrische Toleranz von 1 logischen Einheit fest. Die gebundenen Quelldateien stimmen, soweit im Web-Manifest aufgeführt, mit dessen Dateihashes überein. Das Manifest beschreibt einen Weblauf und identifiziert weder die Native-Builds noch deren Laufzeitnachweise.

| Mass | Soll | iOS pt | Android dp |
|---|---:|---:|---:|
| Eingabebreite | 320 | 320 (960 px) | 320 (840 px) |
| Eingabehöhe | 44 | 44 (132 px) | 44.19 (116 px) |
| Labelboxhöhe, Abstand zum Feld | 20, 8 | Label sichtbar, Boxkanten aus Raster nicht messbar | 20.19, 8.00 (53, 21 px) |
| Eingabe → Popup | 8 | 8 (24 px) | 8 (21 px) |
| Popupbreite | 320 | 320, aus Highlight-Band | 320, aus Highlight und Viewgrenzen |
| Zeile, Viewport | 32, 160 | 32, 160 (96, 480 px), fünf sichtbare Zeilen | 32, 160 (84, 420 px), fünf Viewgrenzen im XML |
| Popup → Statusbox, Statusboxhöhe | 8, 20 | Status unter Popup, Boxkanten aus Raster nicht messbar | 8.00, 20.19 (21, 53 px) |
| Eingaberadius | 8 | ca. 8.3, Rasterproxy an der ersten Randzeile | ca. 8.4, gleicher Proxy |
| Popupradius | 8 | ca. 8, erste weisse Innenpixel etwa 24 px eingerückt | ca. 8, erste weisse Innenpixel etwa 20 px eingerückt |
| Eingaberandstärke | 1 | 1 (3 px) | 1.14 (3 px) |

Die Kanten der weissen Popup-Fläche sind am Mittelschnitt vom Schatten abgegrenzt, iOS y=[582,1062), Android y=[390,810). Eckenwerte sind Rasterannäherungen. Das Schrift-Asset ist in beiden Paketen bytegleich mit Inter Regular aus der Quelle. Beide Bilder zeigen ähnliche Glyphen. Die effektiv gebundene Schrift sowie die nominellen Grössen 14/12 wurden nicht unabhängig über Laufzeitmetriken verifiziert. Die sichtbare Textposition liegt im erwarteten Bereich. Die tatsächliche Innenpolsterung wurde ohne Abgleich der Glyphenseitenlager nicht separat vermessen.

Die folgenden sRGB-Werte wurden in beiden neu aufgenommenen Bildern an Volltonpixeln gefunden. Die Messung nimmt geglättete Kanten aus und nutzt die getrennten Bildbereiche für Text, Feld, Popup und Status. Der Statusbereich wurde auch separat gemessen, damit der Platzhalter den Nachweis nicht ersetzt.

| Merkmal | Soll und gemessene Stichprobe auf beiden Plattformen |
|---|---|
| Feld- und Popup-Fläche, reguläre Zeilen | `#FFFFFF` |
| Label und reguläre Treffer | `#172B4D` |
| Platzhalter und Status | `#64748B` |
| Rahmen in `active` / `closed` | `#2563EB` / `#CBD5E1` |
| Hamburg-Hintergrund | `#EAF2FF` |
| München-Text | `#94A3B8` |
| Fehlerstatus | `#B91C1C` |

CSS-Schatten-Soll `0 2px 8px #0003`. Beide native Renderings zeigen einen weichen, nach unten stärkeren Schatten. Auf weisser Fläche an der horizontalen Popup-Mitte ergibt der erste Pixel unterhalb der Fläche iOS `#DDDDDD`, Android `#D9D9D9`. Oben reichen nichtweisse Pixel bis ins gemessene Umfeld und unterscheiden sich ebenfalls. Das sind native Schattenunterschiede. Eine CSS-Referenzrasterung des Schattens war kein Teil dieser Stichprobe.

## iOS

**Visuell.** Leeres Suchfeld mit «Stadt suchen …», Label «Stadt auswählen», Status «7 Städte verfügbar.» und fünf vollständige Zeilen in der Originalreihenfolge Berlin, Hamburg, München, Dresden, Köln. Hamburg ist hervorgehoben, München erscheint in der deaktivierten Textfarbe. Die Story-Datei im App-Bundle stimmt bytegenau mit der Quelle überein und enthält `activeKey=hamburg`, `muenchen.disabled=true` und die exakten sieben Schlüssel. Das sichtbare Bild belegt Text und Markierung. Der intern aktuell bestätigte Schlüssel wurde nicht ausgelesen. Die separate `scroll-end`-Vorschau zeigt unten Wien und Zürich und markiert Zürich. Eine Wischgeste in der iOS-App wurde nicht ausgeführt.

**Ergänzende visuelle Zustände.** Eigene Starts von `closed`, `loading`, `empty`, `error` zeigen geschlossen den neutralen Rahmen und Platzhalter ohne sichtbaren Status, sonst «Be» / «Atlantis» / «Be», blauen Rahmen und die jeweilige Meldung «Städte werden geladen.», «Keine Städte gefunden.» und «Städte konnten nicht geladen werden.». Die Popup-Sichtbarkeit/Beschäftigt-Projektion ohne Treffer ist aus den Bildern nicht entscheidbar.

**Laufzeit und Zugänglichkeit.** Status im Bild belegt. Zugänglicher Feldname, Fokus, Rolle/Projektion, hörbare Meldungen sowie Bedienfälle für Suche, altes Ergebnis, deaktivierten Treffer, genau ein Bestätigungsereignis und Abbruch sind offen. Die lokale Bedienung über die macOS-Zugänglichkeitsschnittstelle war nicht freigegeben; die Simulations-Starts und Bildmessungen waren ausführbar.

## Android

**Visuell.** Gleicher sichtbarer Inhalt und gleiche Markierung. Der in der APK mitgelieferte Story-Datensatz stimmt bytegenau mit der Quelle überein. Der unabhängig ausgelesene Android-Baum zeigt fünf Zeilen im ScrollView, `selected=true` für Hamburg und `enabled=false` für München. Aufwärtswisch in `active` von (690,650) nach (690,320) über 650 ms bringt München, Dresden, Köln, Wien und Zürich in den Viewport. In der separaten `scroll-end`-Story ist zusätzlich Zürich markiert.

**Ergänzende visuelle Zustände.** Dieselben vier Story-Starts und sichtbaren Feldtexte, Rahmen und Meldungen wie bei iOS. Die visuelle Aufnahme belegt bei den drei leeren Ergebniszuständen die jeweilige Meldung. Ob der native Popup- und Busy-Zustand semantisch projiziert ist, wurde für diese Storys nicht festgestellt.

**Bedienung.** Unabhängiger Start `interactive`, Eingabetap, Text `B`, Pfeil abwärts, Enter, anschliessend Ergänzung `zz` und Escape. Vor Navigation zeigt der XML-Auszug Suchtext «B» und Berlin ohne Auswahl. Danach ist Berlin aktiv und der Suchtext weiterhin «B». Enter schliesst die Liste und zeigt «Berlin» und «Ausgewählt: Berlin.». Nach Bearbeitung zu «Berlinzz» erscheint «Keine Städte gefunden.». Escape schliesst den Popup-Zustand, belässt den Suchtext «Berlinzz» und zeigt wieder den bisherigen Auswahlstatus für Berlin. Das stützt die Trennung von Query, aktiver Zeile und Auswahl. Der interne bestätigte Schlüssel und die Anzahl der Ereignisse bleiben offen. Gegenprobe mit `M`: nur München, als deaktivierter Treffer. Ein Tap auf seine Zeile ändert weder Suchtext noch Status noch Markierung. Ein alter Provider-Response wurde nicht gezielt mit beobachtbarer Reihenfolge injiziert.

**Zugänglichkeit.** XML belegt Eingabefokus bei Suche und Pfeilnavigation sowie aktiv/deaktiviert am Treffer. In der tastaturlosen `active`-Vorschau liegt der Eingabefokus am Vorschaucontainer. Das Label ist als separater Text und der Listenname als `content-desc` erfasst. Der Feldknoten enthält Text und Hint «Stadt suchen …», seine `content-desc` ist leer. Eine etwaige native Labelbeziehung wird in diesem XML-Format nicht ausgegeben, daher bleibt der effektive zugängliche Feldname offen. Der Statusknoten ist erfasst. Live-Region-Verhalten und hörbare TalkBack-Meldungen sind offen.

## Evidenz und Grenzen

`measurements.txt` enthält Messfenster, exakte RGB-Treffer, Mittelschnitt, Bildvergleich und SHA-256 je Quelldatei bzw. Lieferbestandteil. `evidence.sha256` bindet die unabhängig erfassten Screenshots und XML-Auszüge. Aufnahme per `simctl` und `adb`; Pixelmessung mit Pillow; Android-Interaktion per `adb input` und Hierarchieaufnahme per UI Automator; Texte und sichtbare Zustände zusätzlich anhand der Bildaufnahmen geprüft. Farbmessung schneidet Antialiasing aus. Vergleich zwischen Plattformen erfolgt in pt/dp. Physische Geräte, reale Screenreader, ein eventbasierter Nachweis der Provider-Reihenfolge und exakt eines Bestätigungsereignisses wurden nicht geprüft. Die visuelle Stichprobe innerhalb der dokumentierten Grenzen und die Android-Bedienbelege bewerten diese beiden Simulator-Konfigurationen.
