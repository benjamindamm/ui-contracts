# Lauf 04 · ODRL-Grenzvergleich

**Nur Kodierungsprobe:** drei originale ODRL-Konfliktbegriffe in eigenem JSON-LD mit rdflib eingelesen. [Ergebnisse](results/observations.json) · [Zusammenfassung](results/summary.json). Keine native ODRL-Policy ausgewertet und keine normative Konformität geprüft.

Die Proben behalten je eine Permission und Prohibition für dasselbe Ziel und dieselbe Aktion sowie den jeweiligen Konfliktterm im RDF-Graphen. Der selbst gewählte Komponenten-URN ist dadurch lediglich eine IRI; die JSON-LD-Verarbeitung prüft weder unseren Index noch Revision, Hash oder Anker. Eingaben und Skript stehen im Freeze. Erneute Ausführung benötigt einen neuen Ergebnisstand, da results exklusiv angelegt wird.

Nach [ODRL 2.2, Abschnitt 2.10](https://www.w3.org/TR/odrl-model/#conflict), bestimmen perm, prohibit und invalid die Behandlung widersprechender Permission-/Prohibition-Regeln; default ist invalid. Diese fachliche Bedeutung wurde hier aus der Spezifikation geprüft, nicht durch einen selbst geschriebenen Interpreter nachgebaut und als Frameworknachweis ausgegeben.

UX-Eignung, Empfehlung, Freigabestatus und Nutzerforschung sind damit noch nicht als eigene Begriffe modelliert. Ein ODRL-Profil könnte erweitert werden; dessen Eignung und Kosten sind unbelegt. Für die erste Integrationsprobe wird ODRL deshalb nicht als führende UX-Sprache empfohlen. Das ist ein begründeter Vorschlag zum Arbeitsumfang, keine Aussage, dass die Sprache ungeeignet oder nicht erweiterbar wäre.
