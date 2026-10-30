# Lauf 02 · Rego-Proberegel korrigiert

Separate Reparatur nach Lauf 01, keine unabhängige Reproduktion. Die expliziten Guards prüfen fehlende/null-Felder über object.get, bevor boolesche Bedingungen ausgewertet werden. Ungültige Typen werden zusätzlich als invalid-input behandelt. Diese Klassifikation ist unsere experimentelle Policy, keine eingebaute UX-Semantik von OPA.

**6/6 Erwartungen erfüllt**, bei unveränderter OPA-Binärdatei. [Originalantworten](results/observations.json) · [Zusammenfassung](results/summary.json) · [Neue Regel](policy.rego). Der frühere Fehlbefund bleibt in Lauf 01 erhalten. Die sechs erwarteten Ausgaben sind vor dem Folgelauf in freeze.json gebunden; sie wurden nach dem bekannten Fehler festgelegt und sind daher keine Blindstudie.

Zum erneuten Ausführen eine separate Ergebniskopie nutzen; probe.py überschreibt results nicht. Gleiche sechs Kontexte aus Lauf 01. Kein Nachweis für die noch offenen Pflicht-/Empfehlungs-, Vererbungs-, Agenten- oder vollständigen Frameworkfragen.
