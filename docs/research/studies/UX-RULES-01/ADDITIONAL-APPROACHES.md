# Ergänzende Kandidatensuche · 30. Oktober 2026

Begrenzte gezielte Suche, keine erschöpfende Marktübersicht. Neu gefundene Begriffe nicht automatisch als aktuelle, interoperable Standards behandeln. Primärquellen stehen unten und in sources.json.

| Ansatz | Dokumentierter Beitrag | Einordnung / Aufnahmeentscheidung |
| --- | --- | --- |
| UGL (Unified Guidelines Language) | Autorenpublikation beschreibt XML-Guidelines und ihre Umsetzung in XQuery-Tests für Web-Accessibility. | Als UX-nahes Forschungsmodell aufnehmen. Heutige Werkzeuge, Originalschema und allgemeine Eignungsregeln für Komponenten noch unbelegt. Ein Abruf des historischen Schema-Links ist kein Wartungsnachweis. |
| GDL in der Usability-Forschung | Historische Publikationsspuren zu Guideline Definition Language; Original-PDF-Abruf in dieser Runde nicht zuverlässig zugänglich. | Recherchekandidat, keine Ausführung und keine vollständige Modellbewertung. Aussagen aus Referenzlisten nicht mit geprüfter Originalsyntax verwechseln. |
| ACT Rules Format 1.1 | W3C beschreibt u. a. Anwendbarkeit, Erwartungen, Annahmen und Ergebnisarten. | Nützlicher Maßstab für Regelqualität. Kein belegter alleiniger Ersatz für unsere ausführbare UX-Logik; maschinenprüfbare Bindungs-/Ausdruckssyntax separat nachweisen. |
| EARL 1.0 | RDF-Vokabular für Testaussagen mit Ergebnissen wie passed, failed, cantTell und inapplicable; W3C Working Group Note. | Kandidat für Ergebnis-/Belegmodell, nicht mit einer Sprache für die Regel selbst verwechseln. |
| openEHR GDL | Formalisierte klinische Guideline-Sprache mit Archetypbindungen. | Fachfremder Vergleich für Bindung und Metadaten; nicht mit der gleichnamigen Usability-Sprache verwechseln. Keine klinischen Vorgaben oder Archetypen ins UI-Modell übernehmen. |

Die zusätzliche Suche verschiebt den Fokus: Ein geeignetes Gesamtmodell muss Regelinhalt, auswertbare Bedingung, Komponentenbindung und Ergebnisbeleg getrennt behandeln. Diese Einordnung ist unsere Schlussfolgerung, kein von ACT/EARL zugesagter universeller UX-Standard.

## Primärquellen und Abrufgrenzen

- [UGL-Autorenpublikation, Arrue/Vigo/Abascal](https://dl.ifip.org/db/conf/ehci/ehci2007/ArrueVA07.pdf), insbesondere Abschnitte 3 und 4. Das dort genannte Schema lautet `http://sipt07.si.ehu.es/evalaccess3/ugl.xsd`.
- [GDL-Originalpublikation, institutioneller Repository-Link](https://dial.uclouvain.be/pr/boreal/object/boreal%3A18267/datastream/PDF_01/view): Abrufprobleme transparent im Quellenzugangsprotokoll; kein Beweis, dass es keine Kopien oder Implementierungen gibt.
- [ACT Rules Format 1.1](https://www.w3.org/TR/act-rules-format/), Struktur und Anwendbarkeit.
- [EARL 1.0 Schema](https://www.w3.org/TR/EARL10-Schema/), Ergebnisvokabular und Dokumentstatus.
- [openEHR GDL](https://specifications.openehr.org/releases/CDS/latest/GDL.html), eigenständiger klinischer Fachkontext.

Keine Nutzungszahlen, aktuelle Projektaktivität oder verfügbare Evaluatorqualität dieser zusätzlichen Modelle wurden gemessen. Weiterführende Vertiefung bleibt als eigene Aufgabe sichtbar.
