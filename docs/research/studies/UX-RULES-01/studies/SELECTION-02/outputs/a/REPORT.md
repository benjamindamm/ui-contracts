# SELECTION-02-a · Builderbericht

Bereit zur unabhängigen Prüfung. Ausschließlich eigene Aufgabe/Eingabe und relevante Kandidatenbibliotheksdateien verwendet.

## Entscheidung

`decision.json` wurde vor index.html, CSS und TypeScript geschrieben. Tatsächlich sind drei Optionen CH, DE, FR geliefert. Nach selection-policy.dmn verlangt erst >15 Optionen Suche; searchExplicitlyRequired=null. Select ist eligible und erste Policywahl. SelectWithSearch wäre ebenfalls geeignet, wird aber nicht benötigt. Autocomplete ist wegen valueDisplayEditable=true mit selectedLabelEditingAllowed=false inkompatibel. Die widersprechende historische Notiz in Select ux/README über eine noch undefinierte Suchvariante wurde nicht als Quelle für deren Existenz verwendet; library.json und eigene SelectWithSearch-Definition sind aktueller Bestandteil derselben Kandidatenbibliothek.

## Lieferung

index.html direkt lokal öffnen. Vier native Input-Felder und ein natives required Select mit gelieferten Labels/Reihenfolge. Keine Vorbelegung oder geografische Vermutung. Adapter implementieren value-change und die relevanten Hostupdates aus SCXML einschließlich Optionsvalidierung, unbekannter/disabled Keys, options-change, enabled/readOnly und stiller SET_VALUE-Semantik. Browser übernimmt Select-Popup, Fokus und Tastatur. Nichtleere Fehler werden über aria-describedby gebunden; aria-invalid erscheint erst bei tatsächlicher lokaler Prüfung. Fehler fokussiert das erste Feld. Änderungen entfernen veralteten Erfolg. Telefonnummer bleibt String. Kein Versand, Speicher oder Backend; tel ist keine Rufnummernformatprüfung.

CSS übernimmt Input/Select layout.css und aufgelöste DTCG-Tokens. Inter-Schriften und Lizenz lokal kopiert. Formularrahmen, Button und responsive Begrenzung sind Hostgestaltung.

## Tatsächlich geprüft

- Gepinnter TypeScript-Compiler: --strict, ES2020, DOM, DOM.Iterable, module none; erfolgreich ohne Diagnose, form.js erzeugt.
- Statischer Readback aus geschriebenem index.html mit HTMLParser: eindeutige IDs, verbundene Labels, vier Pflichtinputs mit Typ/Autocomplete, Optionen exakt leer/CH/DE/FR in Reihenfolge; bestanden.
- Kompiliertes JavaScript vorhanden und nicht leer; Artefakt- und Quellhashes in TRACE.json.

## Grenzen

Keine Browserausführung, visuelle Prüfung, reale Tastatur-/Screenreaderprüfung oder dynamische Eventtests ausgeführt. SCXML ist manuell in native Adapter übertragen, nicht von einem SCXML-Interpreter ausgeführt. DMN-Ausdrücke wurden anhand konkreter Fakten nachvollzogen, nicht mit einer DMN-Engine ausgeführt. Diese begrenzten Nachweise sind keine allgemeine Runtime-, Accessibility- oder Designfreigabe.
