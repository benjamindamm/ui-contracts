# Aktueller Nachweisstand

**Recherche abgeschlossen:** [Abschluss und Lesereihenfolge](RESEARCH-CLOSEOUT.md). iOS/Android sind spätere Perspektiven und keine Abschlussbedingung dieser Phase.


Stand: 25. Oktober 2026. Mit study.json und dem offenen Register abgeglichen. Historische Zahlen und widerlegte Erwartungen bleiben in ihren jeweiligen Berichten.

**2 offene Zellen: 2 Integration und 0 weitere. 702 unterschiedliche Bedingungen in 106 Gruppen.** 16/16 Kandidaten-Erstdurchgänge abgeschlossen. Ein ausgewählter Vier-Domänen-Webreferenzlauf ist begrenzt belegt; universelle Integration und vollständige IP-/native-/AT-Abnahme bleiben unbelegt. Abschlussstand auf Nutzerauftrag zur Versionierung und Übertragung auf origin/main freigegeben.

## Gemeinsamer Integrationsvorschlag

[IP-01](INTEGRATION-PROFILE.md) konsolidiert Rollen, Referenzen, Quellführung, Typ-/Event-/Zustandsbindung und die vollständige A/B→Overlay→ScrollArea-Komposition als Vorschlag. [Abnahmeplan](INTEGRATION-ACCEPTANCE.md) und [Belegindex](INTEGRATION-PROFILE-EVIDENCE.json) liegen vor. [Minimaler Bindungsentwurf](INTEGRATION-BINDING-DRAFT.md) und [konkrete Umsetzungsübergabe](IMPLEMENTATION-HANDOFF.md) ergänzen Zielarten, Instanzprüfung, Diagnosen und einen vorab spezifizierten Lifecyclekern. Der ursprüngliche Vorschlag ist Dokumentationsarbeit ohne neue Matrixbewertungen. Der ergänzende Lifecycleversuch ist unten separat gezählt; das T1-Datenmodell ist inzwischen statisch geprüft; der ausgewählte gemeinsame Hostablauf mit Events/Fokus/Scroll-/AX-Folge ist inzwischen konkret ausgeführt. Allgemeiner deklarativer Resolver, vollständige IP-Abnahme und native/AT-Übertragung bleiben offen. Versionierung des Abschlussstands auf Nutzerauftrag freigegeben.

## Belegte Nachweisblöcke, aktuellster zuerst

[Gemeinsamer Browserlauf abgeschlossen](experiments/2026-10-25/ip01-browser/REPORT.md): 20 vorregistrierte Bedingungen erfüllt. Original-SCXML-Interpreter, tatsächliche Events/Fokus/Scrollmessungen und echte Chromium-AX-Zustände in einer gepinnten Quellenrevision; eigener Invoker/Fehlerrelay/Hostadapter sichtbar. Eigene Erstfehler erhalten und voller finaler Block nach Korrektur wiederholt. Keine echte IME-/Screenreader-/Native-Abnahme. Die beauftragte Runde ist abgeschlossen; es läuft keine weitere Forschungs-/Testrunde.

[Gemeinsames statisches IP-01-Referenzpaket](experiments/2026-10-25/ip01-static/REPORT.md): drei Definitionen und vier Domänen an einem konkreten Quellenabschluss; 27 vorregistrierte Erwartungen erfüllt. Original-CEM-/SCXML-Schemas, tatsächlicher TypeScript-AST und zusätzliche Typ-/Wert-/Referenz-/Instanz-/Revisions-/Token-CSS-Bindungen getrennt. Statische Anteile A01–A04/A15 konkret, vollständige Gates und Hostlauf weiterhin offen.

[Gezielte Lifecyclefolgevarianten](experiments/2026-10-25/ip01-followup/REPORT.md): sechs neue vorregistrierte Bedingungen erfüllt; acht LC-Erwartungen als nicht erneut gezählte Regression erfüllt. Drain und native idlocation getrennt geprüft; expliziter Fehlerrelay leitet echte Parserfehler an die aktuelle Sitzung weiter. Die zwei vorherigen Original-/Adaptergegenbefunde bleiben erhalten. Kein vollständiges IP-Gate abgenommen.

[Zweistufiger IP-01-Lifecyclekern](experiments/2026-10-25/ip01-lifecycle/REPORT.md): acht vorregistrierte Bedingungen tatsächlich ausgeführt, sechs erfüllt und zwei verletzt. LC-06 verliert beim sofortigen Reopen nach alter Bereinigung die neue Invoke-Route; LC-07 leitet Initialisierungsfehler nicht an den richtigen Root weiter. IP-A05/A06 nur teilweise untersucht und weiterhin offen. Keine Matrixbewertung geändert.

[Acht autonome Restfragen konkret ausgeführt](AUTONOMOUS-8-REVIEW.md):38 neue Bedingungen in7 Gruppen, alle final erfüllt. uSpec-Fremdreferenz/Quellführung, zwei getrennte Fachbeiträge und vier zusätzliche Layoutbindungen jeweils A/C536–C543. Initialer Flex-/Zeilen-Erwartungsfehler erhalten. [Zwei konkret fehlende Originalklärungen](REMAINING-2.md); keine neue Frage an Autoren und keine volle Gesamtintegration behauptet.

[Zehn getrennte CSS-/ARIA-Ergänzungsbindungen](experiments/2026-10-25/css-complement-runtime/REPORT.md):27 Erwartungen in tatsächlicher Original-SCXML-Laufzeit, nativer CSS-/DOM-/Fokusfolge und echtem Browser-AX-Baum erfüllt. C526–C535 jeweils A nur mit eigener konkreter Zusatzbindung. Originale query42-Akzeptanz und gültige clip-Syntax mit unsichtbarer aktiver Option bleiben sichtbar. [Genau verbleibende10 Nachweise](REMAINING-10.md).

[Gesamter 29-Zellen-Arbeitsblock](REMAINING-29-REVIEW.md): neun begrenzte Neubewertungen,26 neue Bedingungen/10 Gruppen. Sieben getrennte X01-Beiträge, APG X08 und referenzierte OpenPencil-Slidergeometrie.20 Nachweise bleiben offen; zwei ursprüngliche SSR-Erwartungen bleiben widerlegt, eigene Fehler separat erhalten.

[uSpec Normalisierung und Rückgabealias](experiments/2026-10-25/uspec-normalizer-ownership/REPORT.md): X08 bleibt U/C516. Fünf neue ursprüngliche Normalisierungs-/Zugehörigkeits-/Aliasbedingungen erfüllt; Objektalias, Canonical-JSON und unabhängige Quelldateien ausdrücklich getrennt. Dieser Normalisierungspfad ist ohne neuen Originalbeitrag erschöpft.

[OpenPencil: ursprüngliche Quellführung](experiments/2026-10-25/op-owner-precedence/REPORT.md): X08 A/C515, acht vorab definierte Bedingungen erfüllt. Ursprüngliche Set-/Varianten- und Definitions-/Instanzvorränge bis zur tatsächlichen Controlprojektion ausgeführt; zusätzliche Änderungsbindung. Keine allgemeine Governance oder X01-Zusage.

[APG-Originalklasse und tatsächliche Kontexte](experiments/2026-10-25/apg-original-reference/REPORT.md): X03 A/C513 für zusätzliches CEM-Klassenfeld-/Native-Typ-/Instanzbinding, X04 A/C514 für dieselbe echte Definition mit zwei tatsächlichen Originalinstanzen und eigenen Parametern/Daten. Acht native und zwei Originalschemabedingungen erfüllt; keine stabile normative APG-API, generelle Kompositionssprache oder Keyboard-/AT-/Lifecyclezusage.

[uSpec mit tatsächlicher Obligation-Evidence](experiments/2026-10-25/uspec-external-reference/REPORT.md): X03 weiter U/C512. Acht Originalvalidatorfälle belegen lokale Outputpointer-/Typprüfung, aber keine Auflösung beliebiger fremder sourcePaths oder Erkennung der geänderten tatsächlichen Fremdquelle. Keine neue Adaptersemantik zum bloßen Abhaken erfunden.

[Zag-/Ark-spezifische Referenzpfade](experiments/2026-10-25/zag-ark-references/REPORT.md): X03 A/C510 beziehungsweise A/C511. Acht eigene Beobachtungserwartungen erfüllt; tatsächliche ursprüngliche Machine/Connect- und Ark-Komponenten-/Context-SSR-Pfade an separate CEM-/HTML-Rollen-/Relationsziele gebunden. Vier vom Originalrenderer akzeptierte Konfliktfälle durch Zusatzbinder erkannt, keine DOM-/Interaktions-/AT- oder X01-Zusage.

[UXSpec externer Zeitbezug](experiments/2026-10-25/uxspec-duration-reference/REPORT.md): X03 A/C509 für explizite DTCG-Dauer→UX-Timereingang-Projektion. Zehn Referenz-/zwei Originalschemabedingungen erfüllt; umhüllter Originalwert bleibt fälschlich1 statt1000. Keine tatsächliche Hook-/Timerlaufzeit, native DTCG-Direktkonformität oder beschlossene Produktkopplung; generiertes Maschinenpflichtgerüst offengelegt.

[AgentsORG unabhängig geführter Viererbeitrag](experiments/2026-10-25/agentsorg-independence/REPORT.md): X01 A/C508. Schema-/Originalexporthashes gebunden, drei andere Originaldateien unverändert, tatsächliche SCXML-A/B-Instanzen open und native Höhen192→160. Vier neue Bedingungen, keine erneute Exportzählung; statische zusätzliche Webbindung, keine allgemeine Hostlaufzeit.

[AgentsORG-Originalexport und Quellführung](experiments/2026-10-25/agentsorg-export-ownership/REPORT.md): X08 A/C507 nur für Tokenquelle→tatsächliches CSS mit zusätzlicher Hash-/Änderungsbindung. Acht Erwartungen erfüllt. Ursprüngliche Regeneration stellt CSS wieder her; der widersprechende shadcn-Literalexport trotz Mapping bleibt ausdrücklich erhalten. Keine allgemeine Governance oder automatische Editierfreigabe.

[Panda-Originalquellführung eines Visualwerts](experiments/2026-10-25/panda-source-ownership/REPORT.md): X08 A/C506 für konkrete Wertprovenienz mit zusätzlicher CSS-/Änderungsbindung. Neun Erwartungen erfüllt; Beschreibungserweiterung ändert nicht den Wertowner, DEFAULT erhält Herkunft. Eigene Spec-Fixture, kein behaupteter Rust-/Gesamtcompileroutput und keine universelle Governance.

[OpenPencil-Property auf externen CEM-Booleanwert gebunden](experiments/2026-10-25/op-external-reference/REPORT.md): X03 A/C505, elf Referenz- und zwei Original-CEM-Schemafälle erfüllt. Tatsächliche ursprüngliche IDbindung und Instanzwerte; zusätzlicher Binder statt nativer CEM-Unterstützung. Mehrdeutiger ursprünglicher Namenstreffer ausdrücklich erhalten, kein allgemeiner Resolver oder X01-/X08-Nachweis.

[ARIA-Namensquelle und Hostableitung](experiments/2026-10-25/aria-ownership/REPORT.md): WAI-ARIA X08 A/C504 für genau eine zusätzliche, journalgebundene Namens-Ownershipkette. Zehn Bindungsbedingungen und zwei native listbox-Namenspaare erfüllt; Instanz B unverändert. Keine ursprüngliche ARIA-Paketgovernance, Live-DOM-, AT- oder APG-Zusage.

[uSpec-Originalbuilder und Ownershipgrenzen](experiments/2026-10-25/uspec-ownership/REPORT.md): zehn Beobachtungserwartungen erfüllt. Plan-/Rendererhash und konkrete Identitätskonflikte zurückgewiesen; Spezialistenhashdrift und widersprechende Messwerte im geprüften Pfad ohne Domain-Evidence akzeptiert. X01/X08 weiter U/C503 beziehungsweise U/C502; keine allgemeine Vier-Domänen-Konfliktlösung daraus abgeleitet.

[XState unabhängig geführter SDK-Beitrag](experiments/2026-10-25/xstate-independence/REPORT.md): X01 A/C501, acht neue Erwartungen erfüllt. Drei ursprüngliche Fachartefakte bytegleich, zwei ursprüngliche Actors unabhängig; eigener zusätzlicher Binder erkennt drei Fehlzuordnungen. Kein neutraler XState-Schemabeleg und keine vollständige Autocomplete-/Host-/AT-Integration.

[uSpec-Messanker und Strukturbelege](experiments/2026-10-25/uspec-layout-scope/REPORT.md): Originalanker identifizieren Design-Messziele; Clipping und Wrapperdimensionen bleiben erhalten. Eine Runtime-Zielrelation beziehungsweise Scrollpolitik ist damit nicht definiert. V04/V06 unverändert U, null neue Fälle. Der begrenzte Quellenpfad ist ausgewertet; als nächste unabhängige Gruppe folgt X01.

[UXSpec-Layoutpfad einschließlich Formatspezifikation und Aufrufern](experiments/2026-10-25/uxspec-layout-scope/REPORT.md): offene Schemafelder werden nicht automatisch als CSS weitergegeben; Schichtung und dynamische Eigenschaften belegen noch keinen benannten Inputanker. V04/V06 unverändert U, keine neuen Laufzeitbedingungen. Die konkret fehlenden Bindungen sind dokumentiert.

[Vollständiger Originalframeexport](experiments/2026-10-25/openpencil-layout-runtime/REPORT.md): vorhandener Webadapter erzeugt für clipsContent:true eine feste hidden-Politik beider Achsen; der native begrenzte Host scrollt programmgesteuert. V06 A/C498 im genauen Policyumfang. Parentkoordinaten sind belegt, Input-Unterkantenanker unter Größenänderung bleibt U/C499: Abstand8→-12. Zwölf numerische Beobachtungserwartungen erfüllt, die gewünschte Ankerrelation im Gegenfall ausdrücklich nicht.


[Originaler Scenegraph bis zum zugänglichen Switch-Update](experiments/2026-10-25/openpencil-projection-origin/REPORT.md): Original-Graph-/Instanz-/Projektions-/Role-APIs, ursprüngliche Vue-Statefunktionen und tatsächliches Reka bis zum Host ausgeführt. A01 R/C494 für den konkret benannten Switchbeitrag, A03 R/C495 für seine on/off-Zustandsrückmeldung. Namensinhalt kommt aus gezeichnetem TEXT; keine unabhängige Accessibility-Masterdatei oder universelle Meldungssprache daraus abgeleitet.

28 neue Bedingungen: 12 Graph/SSR, 3 anfängliche Namensprüfungen, 3 passende Namensdiagnosen, 4 Switch-Namensprüfungen, 6 Liveschritte. 26 numerische Erwartungen erfüllt; zwei anfängliche Diagnoseerwartungen widerlegt, die dortige Regel nicht anwendbar. Diese Ergebnisse bleiben erhalten und gelten nicht als positive Konformität. Eigene API-/Buildharnischfehler ebenfalls protokolliert.

Die Liveschritte zeigen getrennte A/B-Werte, stabile Namen und passende aria-checked-Änderungen. Das gebundene Forschungsprofil ist durch Original-/Paket-/Quellhashes reproduzierbar; keine globale Identität zwischen Repo und Distribution behauptet. Kein vollständiger Editor, Graphpersistenz-, physischer Tastatur- oder Assistenztechniknachweis.

## Offene Zellen je Kandidat

| Kandidat | D | R | A | N | U | Offene Kriterien |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| CEM | 4 | 1 | 3 | 18 | 0 |  |
| DTCG | 6 | 0 | 1 | 19 | 0 |  |
| SCXML | 6 | 0 | 4 | 16 | 0 |  |
| XState | 6 | 0 | 4 | 16 | 0 |  |
| Zag | 16 | 1 | 4 | 5 | 0 |  |
| Google DESIGN.md | 4 | 0 | 1 | 20 | 1 | X06 |
| OpenUI | 3 | 0 | 1 | 21 | 1 | X06 |
| AgentsORG | 7 | 0 | 2 | 17 | 0 |  |
| UXSpec | 14 | 2 | 5 | 5 | 0 |  |
| Ark UI | 10 | 9 | 3 | 4 | 0 |  |
| Panda CSS | 8 | 1 | 6 | 11 | 0 |  |
| uSpec | 12 | 2 | 5 | 7 | 0 |  |
| OpenPencil | 7 | 4 | 10 | 5 | 0 |  |
| WAI-ARIA | 6 | 2 | 6 | 12 | 0 |  |
| APG | 6 | 2 | 7 | 11 | 0 |  |
| CSS Layout | 5 | 2 | 15 | 4 | 0 |  |

## Endliche nächste Schritte

Der [aktive Restplan](REMAINDER-PLAN.md) enthält genau2 U-Schlüssel, beide X06-Originalklärungen bei Google DESIGN.md und OpenUI. Keine der zuvor konkret benannten8 autonomen Restzellen bleibt U; ihre jeweils begrenzten Zusatzbindungen sind tatsächlich ausgeführt. Die46er Baseline und44 begrenzten Schließungen bleiben separat erhalten.

[Genau fehlende Originalinformation](REMAINING-2.md): Dokument-Schema-/Ergebnisbinding bei Google und kanonische Vorrang-/Validierungsregel bei OpenUI. Bekannte Config-/Parser-/widersprüchliche Typstände entscheiden diese Herausgeberfragen nicht; keine identischen Proben ohne neue Originalinformation und keine Autorenanfrage. Das ist kein Beweis, dass künftig nie neue Information verfügbar wird.

Einzelne A/R/D-Befunde ersetzen keine universelle Interoperabilität oder fertige Produktionsbibliothek. Gesamtformatwahl, alle Kandidatenkombinationen, Produktionsreife, Lifecycle und Crossplattform-/AT-Abnahme bleiben stärkere getrennte Ziele. Die vollständige Vier-Domänen-Gesamtintegration ist weiterhin nicht belegt.

## Weitere bereits belegte Beiträge

- [I03-Teilebinder](experiments/2026-10-25/named-parts-review/REPORT.md): CSS und ARIA jeweils A mit eigenen konkret nachgewiesenen CEM-/Hostbindungen; null neue Fälle.
- [CSS-Anker-/Instanzbindung](experiments/2026-10-25/css-semantic-anchors/REPORT.md): zusätzliche statische Referenzprüfung, kein nativer Anchorlookup.
- [OpenPencil-Overflowverlust](experiments/2026-10-25/openpencil-overflow-import/REPORT.md): Originalfeldpfad und native hidden/clip-Folge; V06 bleibt offen.
- [X06-Originalumfänge](experiments/2026-10-25/final-x06-scope/REPORT.md): aktueller Stand8 D,2 A, 4 begrenzte N,2 U; Subjekte/Originalmodelle getrennt.

Alle Bedingungen, Grenzen und historischen Gegenfälle im [Experimentindex](experiments/INDEX.md). Es gibt keine universelle Bestenliste und keine vollständige Produktkonformitätszusage.
