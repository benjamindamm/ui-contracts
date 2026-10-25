# uSpec: vollständiger Originalbuilder und seine Ownershipgrenzen

Stand: 25. Oktober 2026. **Zehn neue Bedingungen P58, zehn Beobachtungserwartungen erfüllt. X01 und X08 bleiben U/C503 beziehungsweise U/C502. 40 offene Zellen;453 Bedingungen/58 Gruppen.** Akzeptierte Gegenfälle belegen Prüfgrenzen, keine allgemeine Integrationskonformität.

## Tatsächlich ausgeführter Gegenstand

Revision `1e25e9b8bc2e694689ba0489594f38807a341f14`, vollständige ursprüngliche Module component-contract.ts, cache-validation.ts und target-identity.ts. TypeScript5.9.3 transpiliert sie mit CommonJS/ES2022 und esModuleInterop; keine Funktion ersetzt, kein Validator gestubbt. Tatsächliche buildCanonicalComponentContract und loadCanonicalComponentContract, ursprüngliche Cache-/Zielprüfung und Ajv8.17.1 laufen mit eigenen isolierten Dateien. Native Node-Dateizugriffe lesen und schreiben ausschließlich die Forschungsfixtures. Die komplette Figma-/LLM-/Renderpipeline wurde nicht ausgeführt.

Die eigenen minimalen API-/Dictionary-/Structure-/Color-/Voice-/Reconciliation-Caches, Rendererbelege, Manifest und Plan sind synthetische Forschungsdaten. Die zusätzlichen domain-obligation-Evidence-Dateien fehlen ausdrücklich. Im Originalcode überspringt validateEvidenceObligations diese Teilprüfung bei ENOENT. Daher keine Aussage über einen vollständigen nachweisgestützten Figmaexport oder semantische Gesamtvalidierung. Die sechs vorhandenen Cacheprüfungen werden tatsächlich aufgerufen.

Die Quellhashwerte in den Eingaben sind deklarierte Vergleichswerte; der Builder vergleicht hier Strings und berechnet nicht selbst einen tatsächlichen Extraktionsdigest aus einer Figmaquelle. Experimentdateien und Originalstand sind separat in [source-manifest.json](source-manifest.json) gehasht.

## Führende Eingaben und tatsächliche Übernahme

- Manifest führt Slug, source-Metadaten, vorbereiteten Zeitstempel und den deklarierten baseSourceHash.
- Plan führt Übersicht, Generierungszeit und Confidence; Plan-Slug und -Hash müssen dem Manifest entsprechen.
- renderer evidence führt sourceModel; sein deklarierter Hash wird gegen das Manifest geprüft. variants und anatomy werden daraus abgeleitet.
- API-/Structure-/Color-/Voice-Caches liefern ihre jeweiligen semantischen Daten; Dictionary und Reconciliation werden ebenfalls übernommen. semanticData klont die Daten und entfernt darin obligationLedger; das ist keine allgemeine fachliche Konfliktentscheidung.
- normalizeStructureTargetIdentity bearbeitet die geklonte Struktur anhand der SourceModel-Varianten/Layer. Im Kontrollfall werden Variante, scope und resolved-Metadaten ergänzt; keine Quellcache-Rückschreibung bei normalizeCaches:false.

Diese Originalzuordnung ist konkret. Die internen Kategorien sind dennoch nicht identisch mit Interface/Visual/Behavior/Accessibility. Ein eigenständiger Behaviorvertrag wird vom Canonicalbuilder nicht eingeführt; er müsste als zusätzlicher externer Beitrag gebunden werden.

## Vorab festgelegte Fälle

[Erwartungen](cases.json), [Beobachtungen](results.json), [Runner](run.cjs).

| Fall | Beobachtung |
| --- | --- |
| baseline | Vollständiger Originalbuilder akzeptiert minimale Caches und erzeugt Canonical-JSON; alle sechs Cacheprüfungen ok. |
| renderer-hash-conflict | Abweichender Rendererhash abgewiesen. |
| plan-hash-conflict | Abweichender Planhash abgewiesen. |
| plan-slug-conflict | Abweichender Planslug abgewiesen. |
| cross-specialist-identity | Fremder fileKey in Color führt zu Fehlern in Structure/Color/Voice. |
| api-dictionary-name-conflict | Widersprechender API-/Dictionaryname abgewiesen. |
| specialist-hash-drift | Abweichender baseSourceHash allein im Color-Cache wird im geprüften Pfad akzeptiert. Der Contract trägt weiterhin den Manifesthash. |
| measured-value-conflict | SourceModel-Inputhöhe20 und gemessene Structure-Zeile80 bleiben beide im akzeptierten Contract erhalten. Kein automatischer Vorrang oder Zahlenvergleich daraus ableitbar. |
| cache-source-preserved | Bei normalizeCaches:false bleiben alle eingegebenen Dateien bytegleich; Ausgabe ist eine separate Datei. |
| canonical-load-after-cache-change | Anschließend ungültiges Color-Cache-JSON hindert das Laden des vorher gebauten gültigen Canonical-JSON nicht; cacheValidations ist dabei leer. |

Der Zahlenkonflikt betrifft die eigene explizit benannte Height-Zeile und dieselbe input-1-Zielidentität. Er beweist keine globale Untauglichkeit: zusätzliche Evidence-/Orchestratorprüfungen sind nicht ausgeführt. Ebenso ist Laden einer eingefrorenen Canonicaldatei eine andere Operation als ihr erneutes Bauen aus geänderten Caches.

## Bewertung und weitere Endbedingungen

**X08 bleibt U/C502:** Interne Zuständigkeiten und mehrere konkrete Konfliktprüfungen sind vorhanden. Die akzeptierten Gegenfälle belegen, welche Garantien daraus nicht folgen. Für eine A-Einstufung zwischen unabhängigen Originaldomänen fehlt weiterhin eine konkret zusätzliche per-information Regel samt nachgewiesener Bindung; eine solche eigene Policy wurde hier nicht als Originalfähigkeit eingeführt.

**X01 bleibt U/C503:** Die tatsächliche Cachetrennung und abgeleitete Contractausgabe sind nun ausgeführt. Diese Spezialisten bleiben fachlich anders geschnitten; ein externer Behaviorbeitrag und die führenden unabhängigen Originalartefakte des gewünschten Vierers sind nicht gebunden. Die ausgeführte Trennung ist ein positiver Teilbefund, keine volle Viererbelegung.

Keine identischen Required-/Hash-Leseschleifen: Dieser vollständige Builderpfad ist jetzt begrenzt ausgewertet. Erneute Bearbeitung nur mit konkreter zusätzlicher Originalevidence-/Ownershipbindung oder einem benannten anderen Originalpfad. Die nächste unabhängige Restplangruppe kann fortgesetzt werden, ohne diese beiden Fragen als gelöst auszugeben. Kein Produktionsformat, keine Komponente, kein Commit/Push.

## Reproduktion

prepare.cjs transpiliert die drei vollständigen Originalmodule aus sources/; run.cjs legt die zehn Eingabesätze an und führt die Fälle aus. Quellen werden über die exakten Manifest-URLs bereitgestellt und gegen die gespeicherten Lesekopie-Hashes geprüft. Der isolierte tool/package-lock.json pinnt Ajv8.17.1 einschließlich Abhängigkeiten; TypeScript5.9.3 wird aus der vorhandenen isolierten ts-tool-Installation verwendet. Originalmodule, generierter Originalcode und node_modules werden nicht als eigene Bibliothek mitgeliefert. Eigene Eingaben, Programme, Resultate, Locks und Inventar sind gespeichert. METHODS.md und REQUIREMENTS.md bleiben unverändert.
