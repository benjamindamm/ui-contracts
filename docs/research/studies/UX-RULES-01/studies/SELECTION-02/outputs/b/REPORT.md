# Lieferung SELECTION-02-b

`index.html` direkt lokal öffnen. CSS, eingebettete lokale Inter-Schrift, Datensatz und kompiliertes JavaScript benötigen keine Netzwerkverbindung oder Laufzeitabhängigkeit. Schriftlizenz: `FONT-LICENSE.txt`.

## Entscheidung

`decision.json` wurde vor der UI-Erstellung geschrieben und zurückgelesen. Die 30 Optionen überschreiten die explizite Projektgrenze 15. Select fehlt der geforderte Suchmodus. Autocomplete erlaubt Bearbeiten des gewählten Labels und widerspricht dem Kontext. SelectWithSearch ist definiert, hält den gewählten Wert nicht editierbar und bietet eine getrennte temporäre Suche. Keine allgemeine UX-Regel aus dieser Grenze abgeleitet.

## Umsetzung

Vier Input-Projektionen mit sichtbaren Labels, stabilen IDs, passenden Typen und Autocomplete-Hinweisen. Rufnummer bleibt eine Zeichenkette. Auswahl zunächst leer; nur gelieferte aktive Schlüssel werden im Komponentencode bestätigt. Reihenfolge unverändert, einschließlich CH/DE/FR. Filter: Groß-/Kleinschreibung ignorierender Teilstring aus Label plus Schlüssel. Keine erfundenen Optionen bei leeren Ergebnissen. Query wird beim Schließen zurückgesetzt und nie als countryKey gespeichert.

Nichtmodaler Dialog mit Suchfokus, roving Optionenfokus, Pfeilen, Home/End, Enter/Leertaste, Escape und Schließen bei Fokusverlust. aria-selected bezeichnet die bestätigte Auswahl. value-change liefert value/reason bei echter Benutzerauswahl bzw. entfernter Auswahl durch Optionsänderung. Input liefert value-change bei Textänderungen. Komponenten-Setter für Optionen, Wert und Aktivierung liegen am Country-Host vor. Erforderlichkeit ist für diesen konkreten Auftrag fest gesetzt.

Lokale Submit-Prüfung mit sichtbaren verknüpften Fehlermeldungen und Fokus auf erstem ungültigem Feld; keine Übertragung. Erfolgsanzeige wird bei Änderungen zurückgenommen. Telefonnummern werden nicht regional oder als E.164 validiert.

## Tatsächliche Prüfungen und Grenzen

Gepinnter TypeScript-Compiler mit ES2020, DOM und strict: Exit 0. Ein erster Compilerlauf meldete einen Namenskonflikt des globalen close mit DOM; danach Skript in lokalen Scope gesetzt und erneut erfolgreich kompiliert. Gespeichertes JS wurde zurückgelesen; finale Dateihashes und Quellen in TRACE.json.

Keine Browser-, visuelle, Tastatur- oder Screenreader-Laufzeitprüfung durchgeführt. Keine DMN-Engine oder SCXML-Ausführung. Die Entscheidung ist manuell aus den gelesenen Regeln abgeleitet, die Umsetzung eine abgeleitete HTML-Runtime. Farben und Maße aus DTCG aufgelöst und Original-CSS eingebunden; tatsächliche Darstellung ist nicht visuell verifiziert. Keine allgemeine Komponenten- oder Barrierefreiheitsfreigabe.
