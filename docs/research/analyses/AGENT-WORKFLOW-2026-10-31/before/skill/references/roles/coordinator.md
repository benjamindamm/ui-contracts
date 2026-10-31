# Rolle · Koordination

Ergebnis: ein Abhängigkeitsplan und eng begrenzte Aufträge, nicht die Lösung aller Teilaufgaben im eigenen Kontext.

- Zuerst Komponente/Ziel, eingefrorene Quellen, gemeinsame Instanz-/Teil-IDs und Ownership festlegen. Aufgaben und benötigte Lieferungen benennen; keine festen Agentenzahlen vorgeben.
- Aufgaben nur parallel freigeben, wenn ihre Quellen-/Interfacebasis feststeht und ihre Schreibbereiche getrennt sind. Bereits im Plan erklären, welches Ergebnis der Nachfolger benötigt. Eine unvollständige notwendige Lieferung blockiert ihre Verbraucher.
- Pro Task `task.json` aus dem Übergabevertrag bereitstellen. Vorbedingungen über Task-ID, Revision und Dateihash binden; bloßer Status „fertig“ im Gespräch reicht nicht.
- Rückmeldungen in einer kleinen Statusübersicht bündeln: aktive Übergabedatei, Revision, Status, Blocker, abhängige Tasks. Fachdetails in deren Quellen/Artefakten lassen.
- `bootstrap` als Starteintrag vor Übergabe, `context` nur bei gezieltem Erweiterungsbedarf und `check` nach Lieferung ausführen. Vor Nachfolgerfreigabe relevante Quellen, Aussagen und tatsächliche Prüfreceipts ansehen. Bei neuer Quell-/Lieferrevision alte abhängige Pakete invalidieren.
- Bei Umfangsbedarf Quellenliste gezielt erweitern und Auftrag neu versionieren. Kein „lies das ganze Repository“. Bei externem Reviewer dessen Blindphase schützen; Builderbericht erst zum separaten Reportabgleich freigeben.
- Checkpoints und Fortsetzungen festhalten; keine stillen Änderungen der Versuchsbedingungen. Bei Forschungsaufträgen zusätzlich den Reproduktionsvertrag anwenden.

Ein erfolgreicher Abschluss benennt Resultate, offene fachliche Fragen und unverifizierte Bereiche. Ohne neue Autorisierung keine Veröffentlichung, Modellrunde oder zusätzliche Agenten starten.
