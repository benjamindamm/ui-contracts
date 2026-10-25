# uSpec: Normalisierung, Quellidentität und Objektalias

25. Oktober2026. **X08 bleibt U/C516.** Fünf neue vorab festgelegte Bedingungen erfüllt. Das ist eine neue Prüfung des ursprünglichen Identitätsnormalisierers, keine Wiederholung der bisherigen Hash-/Wertkonfliktfälle und keine positive Gesamtkonformität.

## Ausführung

Vollständiger ursprünglicher Builder, Cachevalidator und target-identity am Pin1e25e9b8bc2e694689ba0489594f38807a341f14, unverändert aus dem eingefrorenen Bestand S103 ausgeführt. Tatsächliches Ajv8.17.1. Eigene minimale Caches mit zwei variantTrees und unterschiedlichen Layerzugehörigkeiten; normalizeCaches:false. Keine Obligation-Evidence-Dateien, Figma-Extraktion, LLM-Ausgabe oder komplette Pipeline. Der ursprüngliche ENOENT-Pfad für nicht vorhandene Obligation-Evidence bleibt explizit.

## Fünf Ergebnisse

| Fall | Beobachtung |
| --- | --- |
| Kontrollfall | Anchor vA/input-1 wird resolved; Quelldateien unverändert. |
| Unbekannte explizite Variante | nonexistent wird auf vA normalisiert; Layer input-1 bleibt, kein invalidVariant-Marker. Das ist beobachteter Fallback, keine bestätigte externe Referenz. |
| Falsche Layerzugehörigkeit | Explizit vA mit input-2 aus vB: layerId wird null, _invalidLayerId input-2, _invalidTargetVariantId vA, disposition unresolved. Builder liefert dennoch ein Ergebnis. Diagnose anerkannt; kein stiller Gesamterfolg. |
| Rückgabeobjekt | Anchor.variantProperties und sourceModel.variantTrees[0].variantProperties sind tatsächlich dasselbe Objekt. Eigene Mutation am Anchor auf tampered verändert auch die zurückgegebene sourceModel-Darstellung. Quelldateien und bereits geschriebenes Canonical-JSON bleiben small. |
| JSON erneut laden | loadCanonicalComponentContract lädt getrennte Objekte; gleiche Mutation verändert sourceModel nicht. Das ist JSON-Repräsentationsverhalten, keine zusätzliche Cache-Neuvalidierung. |

[Vorab-Erwartungen](cases.json), [Ergebnisse](results.json), [eigener ausführbarer Versuch](run.cjs).

## Bewertung

Der Originalpfad besitzt konkrete Normalisierungs- und Zugehörigkeitsregeln. Diese werden anerkannt. Rückgabeobjekt, gespeichertes Canonical-JSON und unabhängige Quelldateien sind jedoch drei verschiedene Ebenen: Ein gemeinsames In-Memory-Objekt belegt keine Änderungszuständigkeit über getrennte Originaldomänen hinweg. Keine zugesicherte Unveränderlichkeit des ursprünglichen APIs behauptet, also auch kein allgemeiner APIvertragsbruch daraus abgeleitet.

X08 bleibt U: Es fehlt die konkrete unabhängige Domänenquelle→führende Information→nachverfolgbare Ableitung mit fachlicher Konfliktentscheidung. Die fünf Bedingungen erschöpfen diesen hier benannten neuen Normalisierungspfad; ohne weiteren entscheidenden Originalzusammenhang wird er nicht erneut gezählt. X01/X03 werden aus ihm nicht automatisch umbewertet. Kein neuer universeller Adapter zum Abhaken erfunden.

## Reproduktion

node run.cjs verwendet ../uspec-ownership/compiled und dessen isoliertes tool/node_modules. Originalsource-/Kompilatshashes aus dem früheren Manifest sind im aktuellen Manifest gebunden. Der Versuch schreibt eigene minimale JSON-Fixtures unter fixtures/. Originalcode und Abhängigkeiten werden nicht als eigene Implementierung verteilt. Keine Produktionskomponente, kein Commit/Push.
