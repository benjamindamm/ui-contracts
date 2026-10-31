# Korrekturen der unabhängigen Gegenprüfung · 31. Oktober 2026

Ausgangspunkt: [unveränderter unabhängiger Bericht](../INDEPENDENT-AUDIT-2026-10-31/INDEPENDENT-REVIEW.md). Die dortigen Gegenproben und Quellhashes bleiben historische Belege, nicht der aktuelle Prüfstatus.

## IA-01 · behoben im begrenzten Aliasprofil

Ursache: `Inspector.tokens()` folgte nur vollständigen Stringwerten; Aliasstrings in Objekt-/Listenwerten wurden nicht besucht. Der Abschlussnachweis war dadurch zu weitgehend.

Änderung: `tools/libraries/check.py` durchläuft nun Objektwerte und Listen rekursiv. Jede vollständige `{token.path}`-Referenz muss existieren und darf auch über zusammengesetzte Werte keinen Zyklus bilden. Der bestehende Typvergleich für vollständige Token-Aliase bleibt erhalten. Für einzelne Composite-Felder werden ausdrücklich keine Typen aus dem Typ des Eltern-Tokens abgeleitet. Der Bericht nennt Composite-Typsemantik, JSON-Pointer-Referenzen und vollständige DTCG-Konformität als ungeprüft.

Regression: `tools/libraries/test_check.py` prüft fehlende Ziele in Objekten und Listen, Selbstzyklen, einen gemischten Zyklus über einen direkten Alias, gültige verschachtelte Referenzen sowie den weiterhin abgewiesenen direkten Typkonflikt (sieben Gegenfälle). Zusätzlich reproduziert ein vollständiger Bibliothekscheck auf einer temporären Kopie das ursprüngliche Problem: jetzt `FAIL` / `TOKEN_ALIAS_MISSING`, weiterhin `release:false`. Die gültige example-Bibliothek bleibt `PASS_LIMITED`.

## IA-02 · aktive Metadaten korrigiert

`libraries/example/library.json` ist jetzt Version **0.4.1**. Der Webeintrag benennt die vier vorhandenen begrenzten Profile und verweist auf `tools/web/README.md`; allgemeine HTML-/TypeScript-Generierung bleibt ausdrücklich außerhalb des Nachweises. Komponenten und ihre Definitionen wurden nicht verändert. Die vorherigen Indexbytes sind als [library-0.4.0.json](library-0.4.0.json) erhalten; bestehende eingefrorene Bibliotheken/Studien bleiben unverändert. Durch den geänderten Index entsteht absichtlich eine neue Bibliotheksrevision; frühere Receipts gelten weiterhin ausschließlich für ihre alten Quellenbindungen und wurden nicht neu gebunden.

## Prüfungen und Grenzen

37 Bibliotheksregressionen bestanden. Zusätzlich wurde der gemeinsame Testtreiber mit `--unit-only` ausgeführt; Protokolle und Ergebnis liegen unter [tests/](tests/results.json). Der aktuelle begrenzte Bibliothekscheck liegt unter [library-check.json](library-check.json). Quell-/Beleghashes und alte/neue Bibliotheksrevision stehen in [verification.json](verification.json).

Kein neuer Browser-, OpenPencil-, Screenreader- oder Modelllauf. Die Änderung betrifft Aliasabschluss und Metadaten; sie liefert keine allgemeine Design-/Runtime-/DTCG-Freigabe. Kein Commit oder Push. Frühere Forschungsberichte werden nicht nachträglich korrigiert; dieser Nachtrag dokumentiert die Reparatur separat.
