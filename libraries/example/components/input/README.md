# Input · 0.1.0

Einzeilige freie Texteingabe für z. B. Vorname, Familienname oder lokale Rufnummer. inputType text/email/tel und native autocompleteHint-Tokens sind explizite Hostbindungen. Native Browser-Autovervollständigung ist nicht die Autocomplete-Komponente und keine feste Optionsliste.

value ist immer ein String: führende Nullen, Leerzeichen und Unicode werden nicht abgeschnitten oder numerisch umgedeutet. USER_INPUT meldet tatsächliche Änderungen nur bei enabled und nicht readOnly; SET_VALUE ist ein stilles Hostupdate. Disabled/readOnly sind unterschiedliche Zustände. Required, E-Mail- und Telefonvalidierung benötigen ihre jeweilige native/Produktprüfung; type=tel validiert keine internationale Nummer. Die Vorwahl wird in der Fallstudie separat aus einer festen Liste gewählt.

component.json verbindet die vier Domänen; ux.json ist eine quellgebundene Fähigkeitsprojektion als Forschungsentwurf. Farben/Typografie sind an die aktuellen gemeinsamen Beispielwerte gebunden. Noch keine allgemeine Runtime-/Assistenztechnik-/Designabnahme. [Selektionsstudie](../../../../docs/research/studies/UX-RULES-01/studies/SELECTION-01/README.md).
