# Register der offenen Matrixfelder

Stand: 25. Oktober 2026. **2 offene Nachweise: 2 Integrationsfelder und 0 weitere Felder.** Nach dem Ausgangsstand 73 wurde UXSpec V05 eingeordnet; die anschließende Gesamtprüfung aller 72 Restzellen hat fünf weitere Neubewertungen erbracht. [Vollständiges 72-Zellen-Protokoll](ALL-FIELDS-REVIEW.md). Eine dokumentarische Prüfung ist nicht gleich einem geschlossenen technischen Nachweis.

Alle 16 Kandidaten-Durchgänge bleiben abgeschlossen. Dieses Register enthält exakt die aktuellen U-Zellen aus study.json. Alte Claims und frühere Zahlen bleiben im Verlauf erkennbar; aktuelle Zahlen werden nicht aus Gesprächserinnerung geschätzt. P1 priorisiert Integration/Signaturen/A11y, P2 übrige Fachbeiträge.

## Kontrollzahlen je Integrationsfeld

| Feld | U-Zellen |
| --- | ---: |
| X01 | 0 |
| X02 | 0 |
| X03 | 0 |
| X04 | 0 |
| X05 | 0 |
| X06 | 2 |
| X07 | 0 |
| X08 | 0 |

## Aktuelle Fragen und Grenzen nach den E3-Proben und der statischen Signaturbindung

| Priorität | Kandidat | Feld | Befund | Nachprüfung / weiterhin nötiger Nachweis |
| --- | --- | --- | --- | --- |
| P1 | Google DESIGN.md | X06 | [C483](CLAIMS.md#c483) | Original-Konfigurationsschema mit sechs Gegenfällen belegt; Subjekt ist Redaktionskonfiguration, nicht Dokumentdaten. **Externe Originalklärung (T):** Benannter Dokument-Schemaeinstieg und Ergebnisbedeutung für Roottypen/Optionalität fehlen. Keine eigene Prosaabbildung als Original ausgeben. |
| P1 | OpenUI | X06 | [C484](CLAIMS.md#c484) | Entwurf/Katalog und Spec.ts weichen bei license/group, Stringprops, enum/required und default konkret ab. **Externe Originalklärung (T):** Maßgebliche Definition und gebundenen Originalvalidator benötigen. Kein eigener Reparaturtyp und keine Nutzerentscheidung über technische Wahrheit. |

## Historische Fortschreibungen

Die folgenden Notizen enthalten frühere Zwischenstände und sind keine aktuelle Queue. Die2 aktuellen Tabellenzeilen oben sind maßgeblich.

Die damals41 offenen Einträge waren keine41 unabhängigen Produktfehler. Gemeinsame Paketfragen treten bei mehreren Kandidaten auf. Originalschema, tatsächliches Tooling, praktische Integration und Produktionsreife bleiben getrennte Nachweisgegenstände.

**E3-Fortschreibung:** CEM I02 ist nun A/C421. UXSpec-Anker-/Overflowgrenzen und WAI-ARIA-Checkergrenzen sind konkret geprüft, ihre vollständigen Nachweise bleiben U. [Ergebnisse und Grenzen](experiments/2026-10-24/REPORT.md).

**Weitere E3-Fortschreibung:** SCXML I02 ist A/C425 für das begrenzte zusätzliche Referenzprofil. Original-XSD und statische Payloadbindung sind getrennt geprüft; keine öffentliche Hostroute implementiert. [SCXML-Bericht](experiments/2026-10-24/scxml/REPORT.md).

**Referenz-Folgeprüfung:** 14 Originalpfad-Erkundungen sind gespeichert. Schema-konforme doppelte Maschinen-IDs werden still überschrieben; ein Token verliert seine Einheit. Andere Referenz-/Rekursionsfälle scheitern separat am Originalschema und werden entsprechend begrenzt interpretiert. X03 bleibt U, Gesamtzahl unverändert 65. [Befunde](experiments/2026-10-24/references/REPORT.md).

**Visual-Fortschreibung:** OpenPencil V01/V03 sind nach ausdrücklich erweitertem Untersuchungsumfang D/C432 und D/C433. Somit aktuell 63 U; frühere 65-Zahlen oben beschreiben den Verlauf. [Bericht](experiments/2026-10-24/openpencil-visual/REPORT.md).

**Layoutfortschreibung:** OpenPencil V05 nun A/C436 für vorhandene geometrische CSS-Abbildung. V04/V06 bleiben U; weitere Felder unverändert. Aktuell 62 U (41 Integration, 21 weitere).

**25.10.2026 – Accessibility-Fortschreibung:** A02 bei OpenPencil nun R/C439 für einen konkreten referenzierten Switch-Webbeitrag; A01/A03 bleiben offen. Aktuell 61 U. [Begründung](experiments/2026-10-25/openpencil-a11y/REPORT.md).

**25.10.2026 – begrenzter Vier-Domänen-Nachweis:** Vier X01-Zellen nun A/C447, nur für CEM/SCXML/CSS/WAI-ARIA im ausgeführten zusätzlichen Webprofil. Aktuell 57 U (37 Integration, 20 weitere). Andere Kandidaten und dynamische Gesamtintegration bleiben getrennt offen.

**Endlicher offizieller X06-Umfang:** [Acht Ausgangsfragen mit Originalpin, bereits geprüftem Beitrag und genauem Restzugriff](experiments/2026-10-25/x06-official-scope/REPORT.md). WAI-ARIA 1.2 ist aufgrund ausdrücklicher Modell-/Hostsprachenabgrenzung N/C471; sieben X06-U bleiben. Externe Plugins und zukünftige Releases sind keine pauschale Abschlussbedingung.

**Ark-Originalpfad abgeschlossen:** [Types-Collection-Schema gefunden und ausgeführt](experiments/2026-10-25/ark-mcp-scope/REPORT.md). API-JSON als eigener Originalartefaktgegenstand, nicht nur MCP-Anfrageparameter/SDK-Typen. Ark X06 D/C474; nun sechs X06-U.

**Panda-Originaldatenmodell geklärt:** [Versionierter Originalexport und zusätzliche Originaltypbindung](experiments/2026-10-25/panda-original-scope/REPORT.md). X06 A/C477 für tatsächlichen Adapterbedarf, kein nativer Original-JSON-Schemavalidator. Vorhandene P42-Evidenz wiederverwendet, keine neuen Fälle gezählt; fünf X06-U bleiben.

**CSS-Originalgrammatikbindung:** [Vier Properties mit unveränderten Originalsyntaxstrings](experiments/2026-10-25/css-original-grammar/REPORT.md), X06 A/C479. Keine pauschale Gesamt-Draft-/DOM-Prüfung; unsupported_scope/unsupported_value bleiben sichtbar. Vier X06-U verbleiben.

**Letzte vier endliche X06-Zugriffe durchgeführt:** [Originalmodellgrenzen und zwei externe Originalklärungen](experiments/2026-10-25/final-x06-scope/REPORT.md). Zag und APG begrenzt N/C481/C482; Google und OpenUI bleiben U/C483/C484. Andere unabhängige Nachweise bleiben bearbeitbar.

**CSS X03 zusätzlicher statischer Referenzbeleg:** [14 Bedingungen](experiments/2026-10-25/css-semantic-anchors/REPORT.md), A/C485. Original-CSS-Ankerdeklaration an CEM-Teil und richtige A/B-Hostinstanz gebunden; native Zielwahl/Kaskade/Layout und Accessibility bleiben getrennt. 46 U, davon 26 Integration und 20 weitere.

**OpenPencil V06 nachgeprüft, weiter offen:** [Zwölf Originalfragment- und drei native CSS-Bedingungen](experiments/2026-10-25/openpencil-overflow-import/REPORT.md). Konkrete semantische Verluststelle belegt, keine künstliche Schließung der U-Zelle. Weiter 41 U (26 Integration, 15 weitere), 383 Bedingungen/48 Gruppen.

**Endlicher Restplan:** [41 U-Zellen in priorisierten Paketen](REMAINDER-PLAN.md): 39 unabhängig untersuchbare Fragen, 2 konkrete Originalklärungen, 0 ausschließlich produkt-/umgebungsbedingt blockierte aktuelle Matrixzellen. Native/AT-/Produktabnahme bleibt separat offen. Planung ist keine Umbewertung.

**I03 getrennt nachgewiesen:** [Vorhandene Teilbinder kriteriumsbezogen bewertet](experiments/2026-10-25/named-parts-review/REPORT.md). CSS Layout A/C492 und WAI-ARIA A/C493 ausschließlich mit zusätzlicher CEM-/Hostbindung; keine native Anatomiesprache und keine neuen Bedingungen. Aktuell 44 U: 26 Integration, 18 weitere.

**Originaler Switch-Namens-/Updatepfad nachgewiesen:** [Publizierter Graph bis Vue/Reka/Host](experiments/2026-10-25/openpencil-projection-origin/REPORT.md), A01 R/C494 und A03 R/C495 im begrenzten Switch-Webprofil. Allgemeine Meldungen, fremde Widgetbeziehungen, Neutralität und Gesamtintegration nicht mitbehauptet. Aktuell 42 U: 26 Integration, 16 weitere; 423 Bedingungen/54 Gruppen, zwei anfängliche Namensprüferwartungen erhalten.

**Eigene feste Original-Overflowpolitik ausgeführt:** [Vollständige Originalexporte und native Hosts](experiments/2026-10-25/openpencil-layout-runtime/REPORT.md), OpenPencil V06 A/C498 im begrenzten hidden-/visible-Webadapterumfang. Importverluste und nicht unterstützte Scrollpolitiken bleiben erhalten. V04 U/C499 mit explizitem unerfülltem Input-Ankergegenfall. Aktuell 41 U: 26 Integration, 15 weitere; 435 Bedingungen/56 Gruppen.
