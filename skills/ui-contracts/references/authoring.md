# Autorenarbeit an Originalartefakten

Zuerst Bibliotheks-ID aus dem Auftrag auswählen, dann nur deren `libraries/<id>/library.json` und betroffene `components/<name>/component.json` lesen. Bibliotheken mit `tools/libraries/manage.py list` entdecken; `init ID` legt eine leere an. Ohne eindeutige Auswahl nicht stillschweigend example verwenden. `libraries/example/` enthält die erhaltene Forschungsbibliothek als gezielt nachladbare Orientierung. Eigene Bibliotheken erben weder Tokens noch Komponenten oder Prüffreigaben automatisch. Details: `libraries/README.md` im Zielrepository.

| Führende Domäne | Originalformat und Aufgabe |
| --- | --- |
| Interface | CEM-JSON: öffentliche Properties, Typen, Events/Payloads und benannte Teile. Kein Verhalten aus bloßer Namensgleichheit ableiten. |
| Visual | DTCG-Tokens plus ausgewiesenes CSS für Maße, Layout, Farben und Zustandsdarstellung. Typen/Einheiten/Aliase erhalten; CSS-Geometrie ist keine native Plattformabbildung. |
| Behavior | SCXML: Zustände, Übergänge, Guards, Aktionen und Commit-/Lifecycleentscheidungen. Der vorhandene Ausdrucksumfang verwendet ECMAScript. |
| Accessibility | HTML-/WAI-ARIA-Semantik; APG für Bedienmuster. Ergänzende Projektions-/Meldungsregeln ausdrücklich als eigene Bindungen kennzeichnen. |

`component.json`, `accessibility.rules.json` und die vorhandene Bindungssyntax sind eigene Entwürfe. Sie sind weder zusätzliche Originalstandards noch schon allgemein validierte Produktformate.

Beim neuen Bibliothekseintrag den Pfad-/Indexstil des Projekts übernehmen. Schnittstelle, führende Domänenpfade, Komposition, Anatomie und benötigte Fälle benennen. Nur für den Auftrag nötige Dateien und Zustände anlegen. Einen bestehenden Referenzeintrag nicht blind unter neuem Namen kopieren und dessen Semantik oder Prüffreigabe erben lassen.

Für zusammengesetzte Komponenten besonders festhalten:

- Definition gegenüber konkreter Instanz; Teil gegenüber wiederholtem Teil mit stabilem fachlichem Key.
- Aktive Option gegenüber gemeldeter Auswahl und bestätigtem Wert; ein Eventname definiert noch keine Payloadgleichheit.
- Führende Quelle jeder Regel, deren abgeleitete Projektion und verbleibende Konflikte.
- Gleiche Instanz in Referenzen, Verhalten, Host und Accessibility; eigene Overlay-/ScrollArea-Kontexte nicht versehentlich verschmelzen.
- Einheiten, Versionen und Zustands-/Lifecyclebezüge an Dateigrenzen erhalten.

Bei unklaren Regeln Entscheidung oder Annahme sichtbar dokumentieren. Wenn sie das gewünschte Verhalten wesentlich bestimmt, klären statt still erfinden. Bestehende Defaults nicht durch unbelegte Universalregeln ersetzen.

Speichere erzeugte Designs/HTML/TypeScript unter dem vorgesehenen Ziel-/Beispielpfad. Die vorhandene OpenPencil-Zielabnahme betrifft editierbare Zustandsdarstellungen, nicht automatisch eine interaktive Combobox. Für ein neues Ziel explizit prüfen, ob ein tatsächlich ausführbarer Adapter und passende Abnahme existieren.

Aus der abgeschlossenen Forschung bei Bedarf gezielt lesen: `docs/research/INTEGRATION-PROFILE.md`, `INTEGRATION-BINDING-DRAFT.md`, `IMPLEMENTATION-HANDOFF.md`. Einmalige Forschungsbefunde nicht zu universellen Produktversprechen erklären. Für Herkunft und Konflikte existieren `CLAIMS.md`, `SOURCES.md` und die verlinkten Originalgegenbefunde.

Bei tatsächlichen Schriftdateien die optionale `fonts.json` der ausgewählten Bibliothek gezielt lesen. Family-Tokens allein belegen keine geladenen Fontbytes. `tools/fonts/check.py --library ID` prüft die begrenzt unterstützten Assetbindungen; `tools/fonts/preview.mjs` liefert einen getrennten lokalen Renderingnachweis. Formate, Quell-/Lizenz-/Dateihashes und Grenzen stehen in `docs/fonts/README.md`; keine automatische Bereitstellung im Live-Editor behaupten.

Eine separate Lizenzdatei für Fontassets ist keine technische Testvoraussetzung. Fehlt sie, den Nachweis als ungeprüft dokumentieren und technisch unabhängig weiterprüfen; keine Berechtigung erfinden oder deswegen eine zusätzliche Nutzerbestätigung verlangen. Ausdrücklich deklarierte Dateiverweise müssen dennoch stimmen.

Bibliotheksweite Tokens bleiben in `tokens.json` am Root (von einer Komponente aus `../../tokens.json`). Gemeinsame Fonts, Icons und Bilder liegen unter `assets/`; relative Pfade stets vom bindenden Dokument auflösen. Komponentenübergreifende Verweise innerhalb derselben Bibliothek bleiben relativ zwischen ihren Unterordnern. `library.json` führt die Pfade `components/<name>/component.json`.

Explizite CSS-Regeln nicht zur Wahlfreiheit umdeuten: Element, Pseudoelement und Vererbung getrennt auswerten. Eine eigene `::placeholder`-Farbe wird nicht durch die Inputfarbe von `:disabled` überschrieben. Bewusste Quellenabweichungen melden. Statische OpenPencil-Zustände sind keine interaktive Combobox-Implementierung; nur tatsächlich vorhandene Zieladapter verwenden.

Repository bei unklarem Arbeitsverzeichnis anhand `tools/validation/check.py`, `tools/validation/profile.json` und `libraries/` finden; alte Checkouts können `components/library.json` führen. Fehlen die benötigten Projektvoraussetzungen, als konkrete Blockierung melden statt einen zweiten Quelldatenbestand zu erfinden.
