# AgentsORG: ursprünglicher CSS-Export, Diff und begrenzte Quellführung

Stand:25. Oktober2026. **AgentsORG X08 A/C507** für genau die eigene normative Tokenquelle→ursprünglicher CSS-Export-Kette mit zusätzlichem Hash-/Änderungsnachweis. **36 U:21 Integration,15 weitere.495 Bedingungen/64 Gruppen.** Der widersprechende shadcn-Pfad bleibt als konkreter Gegenbefund erhalten.

## Endbedingung und ursprünglicher Gegenstand

Die Spezifikation erklärt .design zur führenden Repositoryquelle, Ausgaben zu Ableitungen und Tokenwerte gegenüber zugeordneten shadcn-CSS-Werten zum Vorrang. Zu prüfen war ein tatsächlicher Originalexport mit einer konkret führenden Information, nachvollziehbarer Änderung und Gegenfällen statt bloßer Wiederholung dieses Anspruchs.

Revision `014a1864c641f8e9792ed76de93c95493489dd8c`. Vollständige unveränderte export_design.py- und diff_design.py-Programme als echte CLIs mit Python3.12 und isoliertem PyYAML6.0.3 ausgeführt. Keine Originalfunktion ersetzt. Alle eigenen .design-Eingaben werden zusätzlich gegen das unveränderte ursprüngliche Draft202012-Schema mit jsonschema4.25.1 geprüft und akzeptiert. Das ist strukturelle Originalschemaakzeptanz, kein vollständiger Norm-/Linter-/Semantiknachweis. Der Original-Linter und Figma-Sync wurden in diesem Block nicht ausgeführt.

Die .design-Dateien sind synthetische Forschungsfixtures. Ihr agent.instructions-Feld ist ausschließlich erforderliche Schemametadaten, keine ausgeführte Agentenanweisung. Auch locked-Fälle betreffen nur diese eigenen Fixtures; keine tatsächlichen gesperrten Projektverträge bearbeitet und keine Benutzerfreigabe/Authentifizierung simuliert.

## Führende Information und tatsächliche Ableitung

/tokens/spacing/popupHeight ist160 im Ausgangs-.design. Der Originalexporter erzeugt tatsächlich --spacing-popup-height:160px. Ein zweiter ursprünglicher Alias popupMaxHeight bleibt als CSS-var-Verweis auf diese Eigenschaft erhalten. Beim eigenen Quellwechsel auf192 erzeugt derselbe vollständige Originalexport192px.

[change-record.json](change-record.json) bindet die konkrete Originalinformation und ihren Pointer, tatsächliche Quellbytes vor/nach, tatsächliche Originalausgaben vor/nach, Originalexporterhash und Originalrevision. Andere CEM-/SCXML-/HTML-Beiträge bleiben unverändert und sind gehasht. Die Datei-/Exporthashes und dieser Änderungsnachweis sind zusätzliches Forschungsmetadatum, keine native signierte AgentsORG-Provenienzfunktion.

Der Themefall besitzt eine andere führende Stelle: Ein ausdrücklich ausgewählter Defaultmodus wide überschreibt den Basiswert mit192 und wird vom ursprünglichen CSS-Exporter in den Rootblock übernommen. Das wird nicht als allgemeiner Vorrang des Basistokens über jeden Themenwert ausgegeben.

## Acht vorab benannte Bedingungen P64

[Erwartungen](cases.json), [Resultate einschließlich vollständiger CLI-Argumente, Status und Ausgaben](results.json).

| Fall | Beobachtung |
| --- | --- |
| baseline-css | Originalschema gültig; ursprünglicher Export160px, ursprünglicher Alias und Normativitätsheader vorhanden. |
| token-update-and-diff | Quelländerung192 ergibt tatsächlichen Export192px; Originaldiff meldet Regression und Exit2 mit --fail-on-regression. |
| default-theme-value | Gewählter Defaultmoduswert192 wird tatsächlicher Rootwert. |
| regenerate-tampered-output | Eigener generierter CSS-Wert absichtlich999px; erneuter Originalexport stellt bytegleich die ursprüngliche160px-Ausgabe her, .design-Quellbytes bleiben unverändert. Keine Rücksynchronisation aus dem manipulierten Export. |
| shadcn-mismatch | Trotz explizitem map_from_tokens.primary=tokens.color.primary und Token#ffffff übernimmt der Originalregistryexport den widersprechenden css_vars.light.primary-Literalwert#000000. |
| locked-entry-removed | Entfernen des eigenen locked-Eintrags wird vom Originaldiff als Regression/Exit2 gemeldet. Keine Prüfung einer Editierfreigabe. |
| informational-diff-default | Derselbe erkannte Tokenkonflikt ohne Fehlerflag gibt Exit0 zurück, Diagnose weiterhin Regression. |
| version-bump-still-regression | Versionsänderung1.0.0→1.1.0 wird gemeldet; Regression bleibt mit Fehlerflag Exit2. Kein vollständiger SemVer-Policyprüfer daraus abgeleitet. |

Acht Beobachtungserwartungen erfüllt. Ein erster Eingabesatz ohne ausdrückliches map_from_tokens ist als initial-unmapped-input-results.json erhalten. Der entscheidende Gegenfall ergänzt diese konkrete ursprüngliche Quellzuordnung und bestätigt, dass der Registryexport sie dort nicht auswertet. Wiederholung zählt nicht als weitere Bedingung.

## Normativer Anspruch gegenüber Werkzeuggrenze

SPEC erklärt Tokens zum Vorrang bei widersprechender shadcn-Zuordnung. Der gelesene und ausgeführte export_shadcn_registry-Pfad kopiert dagegen die css_vars-Literale; er führt in diesem Fall weder die Mappingableitung noch die Konfliktreparatur aus. Die übrige Agenten-/Linter-/Syncpipeline ist nicht geprüft, daher keine globale Behauptung, dass niemand diesen Konflikt beheben könnte. Aus erfolgreicher Registrydateierzeugung darf jedenfalls keine durchgesetzte Tokenpriorität folgen.

Das Diffprogramm klassifiziert Veränderungen, Rücknahmen und entfallene locked-Einträge. Es ist weder ein Freigabe-/Berechtigungssystem noch ein vollständiger SemVer-Korrektheitsprüfer; sein Fehlerstatus ist optional. Die gelesenen Autorenregeln werden nicht mit automatischer Durchsetzung verwechselt.

## Bewertung

X08 U→A/C507 im konkreten CSS-Tokenbeitrag: ursprüngliche normative Quellrichtung, tatsächliche Originalableitung und Regeneration vorhanden; zusätzlicher Hash-/Informationspfad-/Änderungsnachweis erforderlich und gespeichert. Keine universelle Governance über vier Originalformate und keine automatische Übertragung auf shadcn, Figma oder sonstige Ausgabeziele. AgentsORG X01 bleibt offen. UI-Rendering, Assistenztechnik, Figmaauthentifizierung und persistente Transaktionsatomarität wurden nicht geprüft.

## Reproduktion

Die eigenen .design-Eingaben und erzeugten CSS-/Registryausgaben sind gespeichert. run.py führt die vollständigen Originalskripte als Unterprozesse aus; die unveränderten Originalquellen werden anhand der Manifest-URLs am Pin bereitgestellt und gegen Lesekopie-Hashes geprüft. PyYAML6.0.3 ist isoliert installiert; vorhandenes jsonschema4.25.1 wird genutzt. Originalskripte/Schema und installierte Fremdbibliotheken werden nicht als eigene Projektimplementierung ausgegeben. METHODS.md und REQUIREMENTS.md unverändert. Kein Commit/Push und keine Produktionskomponente/-sprache.
