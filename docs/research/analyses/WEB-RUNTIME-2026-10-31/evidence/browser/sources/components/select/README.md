# Select · 0.2.0

Einfaches natives Select für genau einen Schlüssel aus vorgegebenen Optionen. Neue Werte können nicht eingetippt oder bestätigt werden. Die Anzeige des gewählten Werts ist nicht editierbar. Kein eigenes Suchfeld und keine Filterung; plattformabhängiges Type-ahead ist kein Suchvertrag.

component.json verbindet die vier Domänen, ux.json projiziert überprüfbar gebundene Fähigkeiten als Forschungsentwurf. Optionen brauchen eindeutige, nichtleere Keys und nichtleere Labels. Die Reihenfolge wird vom Aufrufer vorgegeben und erhalten; country key ist nicht gleich Vorwahl. Es wird nicht geografisch geraten oder intern neu sortiert.

USER_SELECT bestätigt nur vorhandene, aktivierte Keys und meldet tatsächliche Änderungen. SET_VALUE aktualisiert kontrolliert ohne Userereignis. Bei Entfernen/Deaktivieren des gewählten Eintrags durch SET_OPTIONS wird value undefiniert und mit reason options-change gemeldet. Disabled ignoriert Userauswahl; SET_OPTIONS/SET_VALUE bleiben Hostupdates. USER_CLEAR ist nur bei nicht-required zulässig; der leere HTML-Platzhalter wird vom Adapter auf undefined abgebildet, echte Keys sind nie leer. Ungültige Optionen/Keys werden ignoriert, nicht still übernommen.

Required und Hostfehler müssen an native HTML-Validierung/aria-invalid angebunden werden. Popupbedienung und Fokus gehören zum nativen Browser; hier wird keine universelle SCXML-Steuerung des Browserpopups behauptet. Ein Select mit separater Suche müsste als neue Variante beschrieben und geprüft werden. Kleine Listen können damit direkt auswählbar bleiben; aus einer Optionsanzahl allein folgt keine universelle UX-Grenze.

Noch keine allgemeine Runtime-/Screenreader-/Designabnahme. [Selektionsstudie](../../../../docs/research/studies/UX-RULES-01/studies/SELECTION-01/README.md).

## UX-Alternative

Für feste Werte mit zusätzlichem Suchbedarf ist [SelectWithSearch](../select-with-search/README.md) in dieser aktiven Bibliothek definiert. Seine Suchabfrage ist vom gewählten Wert getrennt. Die Suchgrenze ergibt sich aus der jeweiligen Projektpolicy, nicht aus dem Namen Select.
