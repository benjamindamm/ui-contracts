# SELECTION-01-b · Erstlieferung

Bereit als abgeleitetes lokales Formular; keine Komponentenfreigabe.

Die vor der UI-Erstellung gespeicherte Entscheidung wählt **Autocomplete**: 30 Optionen überschreiten den Projektgrenzwert 15. Select bietet keinen Filtervertrag. Query-Bearbeitung und ein lokaler Filterprovider sind erlaubt; bestätigt werden ausschließlich vorhandene Schlüssel. Die vier persönlichen Felder verwenden Input. Ein Land ist erforderlich, die anderen Felder sind mangels Pflichtfeldvorgabe optional.

`index.html` direkt lokal öffnen. HTML, CSS und kompiliertes JS benötigen weder Netzwerk noch Installation. Der Provider filtert Länderlabel/Vorwahl/Schlüssel ohne Umordnung; leere Suche liefert die vollständige vorgegebene Reihenfolge. IDs der Optionen basieren auf Länderschlüsseln. Pfeiltasten bewegen die aktive Option ohne Commit, Enter bestätigt, Escape und Blur schließen. Bei Blur wird eine zuvor bestätigte Auswahl wiederhergestellt; neue freie Texte werden nie als Länderwert übernommen. IME-Komposition blockiert Navigation und Commit. Der Eingabefokus bleibt bei Tastaturnavigation im Combobox-Input. Formulardaten werden lokal geprüft und nicht übertragen.

## Tatsächlich ausgeführte Prüfungen

- TypeScript mit dem vorgegebenen Compiler, ES2020/DOM und `--strict`: bestanden, Exit 0. Der erste Compilerlauf meldete Namenskollisionen mit DOM-Globals; die Lieferung kapselt ihren Zustand jetzt in einer Funktion. Nach der letzten Änderung erneut erfolgreich kompiliert.
- Vorgegebener Policy-Evaluator auf `inputs/b.json`: `PASS_LIMITED`, `release:false`, Autocomplete eligible, Select incompatible-search. Vollständige Ausgabe: `policy-evaluation.json`. Dieser Check prüft die begrenzte Auswahlpolicy, nicht das Formular.
- Dateireadback der gelieferten HTML-/CSS-/JS-Dateien: eindeutige statische IDs, vier Input-Komponenten, vorhandene Combobox und kompiliertes JS, keine entfernten URLs; Einzelresultate in TRACE.json.

## Grenzen und Ableitungen

Kein Browser-, Screenshot-, Screenreader- oder realer IME-Test ausgeführt; die zugelassenen technischen Werkzeuge umfassen Compiler und Policy-Evaluator. Inter ist als bevorzugte Schrift mit Arial-/sans-serif-Fallback deklariert, jedoch nicht eingebettet; ohne lokale Inter-Installation weicht die Schrift ab. Abstände, Höhen, Farben und Radien folgen den Bibliothekstokens; Formularlayout und Schaltfläche sind Hostgestaltung. Die Bibliotheksmeldungen nennen Städte; der auftragsbezogene Host verwendet Länder. Overlay-Anker sind durch eine relative CSS-Positionierung statt CSS Anchor Positioning umgesetzt. Status steht durch reservierten Platz unter dem sichtbaren Popup. Die synchronen lokalen Provider-/Popup-Schritte projizieren direkt ready/empty; keine asynchronen Request-Rennen, Fehler- oder vollständigen SCXML-Lifecycle-Nachweise. `type=tel` ist keine regionale Telefonnummernvalidierung; hier wird nur die native E-Mail- und Landesauswahlvalidierung verwendet.
