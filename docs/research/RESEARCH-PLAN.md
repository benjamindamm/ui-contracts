# Forschungslücken und nächste validierbare Prüfungen

**Historischer Forschungsplan:** Aussagen über nicht ausgeführte Prüfungen gelten für die jeweils benannte frühere Runde. Aktuelle Matrixnachweise stehen in [CURRENT-STATUS](CURRENT-STATUS.md); die noch offene projektweite Integration in [PROJECT-GAPS](PROJECT-GAPS.md).


Plan angelegt am 23. Oktober 2026; Fortschreibung 24. Oktober. Dokumentarische Vergleiche sind inzwischen ausgearbeitet (siehe Abschlussabschnitt); keine der nachfolgenden praktischen Prüfungen wurde ausgeführt. Es geht zunächst um kleine Contract-Artefakte und deren Werkzeuge, nicht um eine Komponentenimplementierung.

## 1. Gemeinsame Referenzen und Komposition

**Frage:** Kann das Paket getrennte Domänendateien behalten und trotzdem dasselbe Element beziehungsweise dieselbe Komponenteninstanz eindeutig meinen?

Prüfartefakt: Zwei Instanzen einer Komponente mit Input und Overlay. Das Overlay verwendet eine separat definierte ScrollArea derselben Bibliothek. Alle vier Domänen referenzieren dieselben fachlichen Teile. URN, URI oder lokale IDs sind Kandidaten, noch keine Auswahl.

Erwartete Positivfälle: Definition einmal, zwei getrennte Instanzen; Parameter und Ereignisse eindeutig gebunden; Version der Unterkomponente reproduzierbar aufgelöst. Negativfälle: fehlende Komponente, falscher Teilname, doppelter Instanzbezeichner, falscher Parameter-/Payloadtyp, inkompatible Version, Zyklus und verwaiste Accessibility-Beziehung.

Untersuchen: UXSpec `$imports`/`$ref`/machine invoke, CEM package/module/name, Ark ids/asChild, OpenPencil ID-Bindung. Ihre Referenzen haben unterschiedliche Zielarten. Ein gemeinsames Stringformat schafft keine gemeinsame Semantik. Ein Schema-`$ref` verweist auf eine Schemadefinition und ist nicht automatisch eine UI-Komponenteninstanz.

**Erfolgskriterium:** Originalvalidatoren akzeptieren die vier Domänenartefakte und eine nachvollziehbare zusätzliche Prüfung erkennt jede absichtlich beschädigte Verbindung. Falls eine Übersetzung nötig ist, deren neue Semantik und Informationsverlust benennen. Die tatsächliche Zusammensetzung von Overlay und ScrollArea bleibt bis dahin unbewiesen.

## 2. Bestätigter Vergleich: DESIGN.md gegen deklarative Layoutmodelle

Anforderungen: V01–V06, X02–X04. Dasselbe Geometrieproblem in Google DESIGN.md, UXSpec-Layout und einem vorhandenen Layoutmodell beschreiben. CSS Anchor Positioning/Overflow sind erste Referenzen; Flexbox/Grid und gegebenenfalls neutrale Modelle weiter prüfen.

Testdaten: referenzierter Anker, Abstand als Dimension/Token, begrenzte Höhe, Overflow, Varianten und zwei Themes. Acht Pixel und fünf Zeilen sind illustrative Werte. Variable Zeilenhöhen, Schriftänderungen und mehrere Instanzen prüfen.

**Erfolgskriterium:** Eigenschaften besitzen dokumentierte Typen und Semantik; falsche Einheit/falscher Anker wird abgewiesen. Ein Freitextsatz oder beliebiger Propertybag genügt nicht. CSS-Abdeckung belegt noch keine native Abbildung. Bei Lücke zuerst weitere bestehende Modelle suchen, bevor eine neue Layoutsprache entworfen wird.

## 3. Bestätigter Vergleich: UXSpec gegen SCXML

Anforderungen: B01–B04, X01, X04–X07. Eine kleine Maschine mit zwei Zuständen, Ereignisdaten, Guard und Zustandsmutation jeweils ohne visuelle Regeln beschreiben. Für SCXML das Datenmodell und den Interpreter explizit wählen.

**Erfolgskriterium:** Gültige Eingabe akzeptiert, ungültiger Zustand/Operator abgewiesen, gleiche vorab definierte Ereignisfolge ergibt gleiche erwartete Zustände. Eintritts-/Austrittsreihenfolge, Fehler und Abbruch getrennt prüfen. UXSpec-Schema und Compiler nicht gleichsetzen; die manuelle Schemaprüfung C17 ist nur der Ausgangspunkt.

Zag/XState als zusätzliche Referenzen verwenden. SCJSON- oder SCXML-Nähe nicht mit semantischer Äquivalenz verwechseln. Funktionsnamen ohne Definition dürfen keinen scheinbar vollständigen Verhaltensvertrag erzeugen.

## 4. Interface und Datentypen

Anforderungen: I01–I03, G02, X03/X05. OpenUI draft-01 gegen tatsächliches Repositoryschema abgleichen; widersprüchliche Repositorylinks der Website klären. Einfache Props, verschachtelte Typen und öffentliche Ereignis-Payloads getrennt behandeln. CEM-Typtext und dessen Referenzen auf einen abstrakten Kern abbilden und Verlustfälle aufzeigen. Swift/TypeScript/Angular/React bleiben mögliche spätere Bindungen, kein aktueller Implementierungsauftrag.

## 5. Accessibility und Konflikte

Anforderungen: A01–A03, B04, X07/X08. ARIA-Semantik und gewählte APG-Variante referenzieren. Produktregel für dynamische Ergebnisansage mit Auslöser/Inhalt separat formulieren. Einen absichtlichen Widerspruch zwischen UX-Tastaturbindung und vereinbartem Fokusmodell einfügen.

**Erfolgskriterium:** Konflikt ist erkennbar, jede Regel hat eine führende Quelle. Statische Assertions, Tastatur-/Fokustest und echte assistive Technik liefern unterschiedliche Nachweise. Kein einzelner automatischer Check beweist vollständige Barrierefreiheit. Native Plattformquellen sind eine eigene noch offene Recherche.

## 6. Quellen- und Werkzeuglücken

- Veränderliche Dokumentation von XState/Zag/Ark/Panda/OpenPencil/APG vor Versuchen pinnen oder datierten Snapshot mit Lizenzprüfung sichern.
- uSpec-Kanonikschema und konkrete Referenzdateien untersuchen; README-Versprechen nicht als Feldnachweis übernehmen.
- Panda-Theming über gültigen offiziellen Navigationspfad prüfen; die versuchte ältere URL lieferte 404.
- Originalschemata und verfügbare Validatoren von Google/AgentsORG/CEM/DTCG lokalisieren und konkrete Positiv-/Negativfälle ausführen.
- DTCG Format und Resolver separat testen; Konvertierung zwischen YAML und JSON sagt nichts über DTCG- oder sonstige Schemakompatibilität.
- AgentsORGs Behauptung verlustfreien DESIGN.md-Imports unabhängig prüfen, statt sie als Ergebnis zu übernehmen.
- OpenPencil Verhalten an konkreten Paket-/Quellständen prüfen; `.fig`-ID-Umbenennung berücksichtigen.

## Entscheidungstor vor eigenem Integrationsformat

Erst wenn die Einzelbeiträge und mindestens eine Referenz-/Kompositionskette geprüft sind, über Paketmanifest, Identitätsformat und Resolver entscheiden. Neue Regeln nur für konkret nachgewiesene Lücken einführen. Änderungen der Substandards sollen durch Versionsbindung und nachvollziehbare Migration behandelbar bleiben. Kein Gesamtpunktwert und kein „Gewinner“, solange Prioritäten und Nachweise fehlen.

## Nächste begrenzte Aufgabe: Validierung, Sprache und Reifegrad

**Vorgemerkt am 24. Oktober 2026, nach Abschluss des XState-Durchgangs.** Diese Ergänzung beauftragt noch keine neue Gesamtrecherche. Bei der nächsten sequenziellen Kandidatenprüfung sind drei Vergleichskriterien getrennt zu erfassen; Anforderungen bleiben Zeilen, Kandidaten die Spalten.

1. **Offizielles Schema und tatsächlich verfügbares Validierungs-Tooling:** Für beide getrennt Quelle, Version und Verfügbarkeit nennen. Konkret unterscheiden, welche Properties, Typen, Payloads und Referenzen geprüft werden; Syntax-/Strukturprüfung von semantischer Prüfung und domänenübergreifender Referenzprüfung trennen. Ein veröffentlichtes Schema beweist weder ein nutzbares Werkzeug noch dessen ausgeführte Prüfung.
2. **Beschreibungsformat und ausführbarer Code:** JSON, YAML, TypeScript, JavaScript oder andere Sprache benennen. Zusätzlich erforderliche Funktionen, Guards, Actions, Ausdrücke, Hostbindungen und Laufzeiten ausdrücklich nennen. Serialisierbare Konfiguration oder Snapshot nicht als vollständig portable ausführbare Semantik behandeln.
3. **Reifegrad und Kompatibilität:** Draft, experimentell oder stabil jeweils anhand einer konkreten Quelle und Version festhalten. Spezifikation, Compiler, Validator und Laufzeit getrennt betrachten; dokumentierte Kompatibilitäts-/Migrationszusagen nennen. Fehlende Zusagen bleiben offen. Marketing und Unternehmensgröße ersetzen keinen Stabilitätsnachweis.

**Erwartete Übergabe:** Pro untersuchtem Kandidaten ein kurzer belegter Befund zu diesen drei Kriterien, konkrete Lücken und Folgen für die spätere produktive Nutzung. Den erforderlichen Mindestgrad an Stabilität/Marktreife sichtbar offen halten, bis er vereinbart ist. Bestehende Bewertungen nur bei neuem Nachweis ändern. Keine neuen Skills, keine Technologieauswahl, keine Implementierung, keine Commits oder Pushes im Rahmen dieser Vormerkung.


## Präzisierung nach dem Integrationsabgleich – 24. Oktober 2026

Die oben stehende Erwartung, alle vier Domänenartefakte durch Originalvalidatoren akzeptieren zu lassen, setzt deren Existenz voraus. Das ist insbesondere für ein neutrales Accessibility-Artefakt noch nicht nachgewiesen. Im nächsten praktischen Prüfauftrag daher je gewähltem Originalformat Schema, Werkzeug, Hostbindung und manuelle Anforderungen getrennt erfassen. Zusätzliche Projektbeschreibungen erhalten keine erfundene Originalkonformität. Der Vorschlag steht ausführlich in [BINDINGS](BINDINGS.md#7-präzisierung-des-prüfungstors); bestehende Fachanforderungen und die Erhaltung verfügbarer Originalprüfungen bleiben bestehen. Keine praktische Prüfung wurde dadurch gestartet.

Die nächste Recherche orientiert sich am [Register aller offenen Felder](OPEN-FIELDS.md). Ein Registereintrag ist keine gelöste Matrixzelle.


## Vergleichsstand nach der Werkzeugzusammenführung – 24. Oktober 2026

Der [dokumentarische Vergleich aller 16 Kandidaten](TOOLING-COMPARISON.md) ist jetzt zusammengeführt. Die historische Vormerkung oben ist damit als Vergleichssicht bearbeitet. Offene Originalschemaidentitäten, tatsächliche Versuche, belastbare Kompatibilitätsnachweise und die Festlegung des produktiven Mindest-Reifegrads bleiben eigenständige Aufgaben im Feldregister und in TASKS. Keine Kandidatenauswahl oder Produktionsfreigabe.

## Gesamtprüfung und Detailvergleiche – 24. Oktober 2026

Der Nutzerauftrag, alle verbleibenden Felder und beide Detailvergleiche zu bearbeiten, ist als dokumentarisches Gesamtpaket gespeichert: [72-Zellen-Protokoll](ALL-FIELDS-REVIEW.md), [UXSpec/SCXML](COMPARE-UXSPEC-SCXML.md), [DESIGN.md/Layout](COMPARE-DESIGN-LAYOUT.md). Fünf Neubewertungen sind übernommen; 67 technische Nachweise bleiben offen. Keine Ausführung, Implementierung oder Technologieauswahl.

Die nächste technische Phase benötigt die im Register benannten Originalartefakt-/Host-/Patternentscheidungen und reproduzierbare Nachweise. Ein neu vorgeschlagenes Profil darf fehlende Originalunterstützung nicht rückwirkend ersetzen. Keine neuen Skills und kein Commit oder Push dieses Pakets.

## Erste E3-Nachweise

Nach dem dokumentarischen Gesamtpaket wurden [49 begrenzte Forschungsproben](experiments/2026-10-24/REPORT.md) tatsächlich ausgeführt. CEM I02 ist im begrenzten TypeScript-/CustomEvent-Profil A; aktuell 66 U. Fehlende Instanz-/Referenzdiagnosen sind praktisch sichtbar, nicht durch die Existenz eines Checkers erledigt. Weitere Arbeit soll konkrete Originalpfade und zusätzliche Bindungsregeln getrennt prüfen. Kein Commit oder Push, keine UI-Komponente.
