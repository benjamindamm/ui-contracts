# Vorab registrierte unabhängige Prüfung

Vor Einsicht in Builder-Ausgaben wurde ausschließlich die Definitionsbibliothek `components/` gelesen. Die vollständigen harten Kriterien, Quellverweise, tolerierten Rundungen und SHA-256-Prüfsummen stehen in `preregistered.json`.

Zuerst werden die gespeicherten Originaldokumente mit dem unveränderten OpenPencil-Reader geöffnet und ihre editierbaren Ebenen sowie die sichtbare Darstellung geprüft. Erst danach werden Builderberichte gelesen. Jeder der zehn benannten Fälle wird einzeln gegen die Quellen geprüft; anschließend werden beide Designs nach Fall und komponentenlokalen Koordinaten verglichen.

PASS bedeutet belegte Erfüllung einer eindeutigen Vorgabe, FAIL einen belegten Widerspruch. UNSPECIFIED erfasst offene Definitionsentscheidungen oder fehlende Prüfbarkeit; OUT_OF_SCOPE umfasst insbesondere Laufzeitinteraktion und frei erlaubte Außenanordnung. Gleiche Artefakte sind nicht automatisch korrekt; Unterschiede in offenen Gestaltungspunkten sind nicht automatisch Fehler.

Harte Schwerpunkte sind Zustandsabdeckung, exakte deutsche Texte, getrennte editierbare Teile, 320×44-Input, 32px-Zeilen, 160px-Maximalviewport, Tokenfarben/-typografie und echtes Clipping mit allen sieben erhaltenen Ergebnislayern. Im Fall scroll-end muss Zürich aktiv und sichtbar sein. Technische IDs und Bytegleichheit werden nicht verglichen.

Offene Punkte sind unter anderem Schriftgewicht und exakte Glyphenbaseline, Meldungszeilen-Inset, Scrollbaroptik und konkrete native Metadatenkodierung. Diese werden nicht nach Kenntnis der Designs nachträglich zu harten Anforderungen erhoben. Die vollständige Mehrdeutigkeitsliste steht in JSON.
