# SELECTION-01-a · Erstlieferung

Bereit als abgeleitetes, lokal öffnbares Formular: `index.html` lädt ausschließlich `styles.css` und das kompilierte klassische Skript `form.js`. Keine Laufzeitpakete, Speicherung oder Netzwerkaufrufe.

Die vor der UI-Erstellung geschriebene `decision.json` wählt Select: drei Optionen, Suchbedarf nach Projektpolicy nicht erforderlich, beide Kandidaten zulässig, Projektpräferenz für einfache feste Auswahl. CH, DE und FR bleiben in vorgegebener Reihenfolge; die leere Platzhalteroption ist kein Länderschlüssel. Keine geografische Vorbelegung. Die vier benannten Felder verwenden native Input-Abbildungen mit den vorgegebenen Typen und autocomplete-Tokens. Eingaben bleiben Strings einschließlich führender Nullen und Unicode.

Hostentscheidung: Alle fünf Felder sind erforderlich; kein Feld war ausdrücklich optional angegeben. Lokale Prüfung nutzt native required-/E-Mail-Gültigkeit, konkrete Fehlermeldungen und Fokus auf das erste ungültige Feld. Die nationale Rufnummer wird nur auf Vorhandensein geprüft; keine internationale Nummernvalidierung wird behauptet. Select bleibt native Einzelauswahl mit nativer Tastaturbedienung. Pflichtauswahl kann nach Auswahl nicht durch den Platzhalter gelöscht werden. Geänderte Userwerte melden value-change. Kein allgemeiner SCXML-Interpreter und keine öffentliche Host-Update-API werden geliefert; SET_OPTIONS/SET_VALUE sind für dieses statische Formular nicht exponiert.

## Tatsächlich ausgeführte Prüfungen

- TypeScript mit `--target ES2020 --lib ES2020,DOM --strict` kompiliert: abschließend Exit 0. Erster Compilerlauf fand einen globalen Namenskonflikt mit `status`; vor Fertigstellung auf `formStatus` korrigiert.
- Erlaubter `evaluate.py inputs/a.json`: Exit 0, `PASS_LIMITED`, `release:false`, Scope `bounded selection research policy`. Ergebnis Select; beide Kandidaten eligible; reason `project-preference-for-simple-fixed-choice`. Warnung nur fehlender SLF4J-Loggeranbieter.
- Geliefertes HTML und erzeugtes JS textuell zurückgelesen; Feldtypen, IDs, Optionsreihenfolge, lokale Submit-Unterdrückung und Validierung vorhanden. Abschließende kleine Pflichtauswahl-Sicherung erneut fehlerfrei kompiliert.

Kein Browser-/Screenshot-/Screenreader-/IME-Test ausgeführt: entsprechende Werkzeuge waren im Auftrag nicht zugelassen. Native Popupdarstellung, reale Tastatur-/Assistenztechnikbedienung und visuelle Laufzeit bleiben ungeprüft. Inter wird nur benutzt, wenn lokal vorhanden; sonst sans-serif, keine Fontdatei geladen. Das Ergebnis ist keine allgemeine Komponentenfreigabe.
