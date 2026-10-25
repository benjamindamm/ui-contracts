# APG: vier Quellen neben derselben ursprünglichen Beispielklasse

25. Oktober2026. **X01 A/C522**, nur für den tatsächlichen ursprünglichen Beispielimplementierungsbeitrag mit zusätzlicher Host-/Interfacebindung. Drei native Bedingungen erfüllt.

Interface: separate eigene CEM-Beschreibung des tatsächlich vorhandenen comboboxNode-Felds als HTMLInputElement, gebunden an input-a. Behavior: vollständige unveränderte ursprüngliche combobox-autocomplete.js. Visual: separate visual.css mit max-height/overflow-y am tatsächlich kontrollierten list-a. Accessibility: separate eigene HTML-Quelle mit label/for, combobox/listbox-Rollen und aria-controls. Die HTML-Datei referenziert das Behavior-Script; sie kopiert dessen fachliche Definition nicht. Der eigene Initialisierer und die Feld-/Quellhashbindung sind Zusatzcode. Der ursprüngliche Bootstrap findet null eigene Wrapper, ein echter Konstruktor wird explizit erzeugt.

Kontrolle: native Maximalhöhe160, Labeltext Search A, ursprüngliche list-Filterung auf Alaska. Visualrevision: allein CSS160→192, übrige Quellen bytegleich, Filter und Label unverändert. Accessibilityrevision: allein Labeltext Search A→Find A, ursprüngliche Klasse/Interface/CSS bytegleich, native Höhe und Filter unverändert. Der CEM-Nativtyp und tatsächliche input→list-Kontext stimmen überein. [Erwartungen](cases.json), [Ergebnisse mit Quellhashes](results.json).

Das ist ein konkreter Nachweis unabhängiger führender Beiträge, kein Anspruch auf ein von APG veröffentlichtes neutrales Contractformat oder stabile öffentliche Implementierungs-API. Der ursprüngliche JS-Beitrag erzeugt selbst Zustands-ARIA und display-Ausgaben; diese sind abgeleitete Runtimeausgabe, nicht eine zusätzliche manuell gepflegte Masterdatei. Alle abgeleiteten Felder allgemein zu synchronisieren ist nicht nachgewiesen. Für den geprüften Modus gibt es den getrennten X08-Befund, der ausdrücklich den Konstruktor-Snapshot begrenzt.

Labeltext/for-Verbindung beobachtet, hier kein eigenständiger nativer Accessible-Name-/AT-Test. Kein physischer Keyboard-, Produktions- oder Crossplattformnachweis. Die Behaviorquelle bleibt JavaScript; X01 A macht G02 nicht neutral.

Reproduktion: prepare.py, unveränderte Originalklasse nach Manifest bereitstellen, eigener HTTP-Host, body[data-ready=true], independenceResearch(). Die gezeigten script-URLs laden dieselbe bytegleiche ursprüngliche Behaviorquelle. Eigene Prüfschritte verifizieren diese Gleichheit. Originalcode nicht als eigene Implementierung verteilt.
