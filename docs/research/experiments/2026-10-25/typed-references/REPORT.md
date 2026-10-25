# Typisierte Referenzen von ARIA-Hostbeziehungen auf Originalmodelle

Stand: 25. Oktober 2026. **X03 / WAI-ARIA, begrenzter P1-Folgebeleg. 16 vorher benannte Bedingungen ausgeführt, sämtliche Regelerwartungen erfüllt.** CEM und SCXML werden in jeder Bedingung zusätzlich gegen ihre gepinnten Originalschemata geprüft und jeweils akzeptiert. Keine fehlgeschlagene Ausgangserwartung in diesem Paket, keine Wiederholungen als neue Bedingungen gezählt.

## Fehlender Beleg und Endbedingung

Bisher belegt: ARIA-IDREF findet ein reales DOM-Ziel; zusätzliches Instanzmapping kann falsche bestehende Ziele erkennen. Weiterhin fehlte die eindeutige, typisierte Verbindung auf separat beschriebene Originalmodellknoten. Ein CSS-Partname, DOM-ID oder Tokenpfad allein identifiziert noch keine externe Komponentendefinition oder SCXML-Zustandsdefinition.

Endbedingung: unveränderte Originalsprachen separat halten; Originalknoten mittels Quellhash, typisiertem Ziel und konkretem Locator auflösen; Zugehörigkeit zur gewählten Definition und zu A/B nachweisen. Richtige und gleichnamige eindeutig adressierte Definitionen müssen akzeptiert werden; falsche Zielart, fremde Definition, veraltete Quelle, mehrdeutiges Ziel und falsche Hostinstanz müssen abgewiesen werden. Diese Zielarten/Regeln sind ausdrücklich ein zusätzliches Forschungsprofil, keine bereits vorhandene neutrale ARIA-Dateisprache.

## Tatsächliche Quellen und Grenzen

artifacts.json enthält die bytegleichen Originalformat-Fixtures des Vier-Domänen-Basispakets: interface.json (CEM), behavior.scxml (SCXML), visual.css (CSS) und accessibility.html (HTML/ARIA). Quellhashes sind im Profil und Manifest festgehalten. CEM/SCXML/HTML sind auch bytegleich mit den Ausgangsquellen des Ownership-Pakets. Der Visualbeitrag dieser Probe ist das vorherige direkte visual.css, **nicht** die dortige DTCG-/CSS-Variablenableitung. Seine Bytes werden gepinnt, aber keine neue CSS-Anker-/Tokenprüfung daraus behauptet.

Original-CEM-JSON-Schema und W3C-SCXML-XSD aus den vorher gepinnten Prüfpfaden bleiben unverändert. jsonschema 4.25.1, lxml 6.1.1, Offline-XSD-Includes ohne Netzwerkauflösung. Keine neue Veröffentlichung oder vollständige Herstellerwerkzeugprüfung. HTML wird für konkrete Hostelemente/Beziehungen gelesen; **kein zusätzlicher axe-/HTML-Linter-, Browser-, SCXML-Interpreter- oder AT-Lauf** in diesem Paket.

## Zusätzliche Referenzkette

| Schritt | Originalziel / tatsächliche Prüfung |
| --- | --- |
| Artefakt | Originaldatei und SHA-256, kein Auflösen nur nach Dateibasisname |
| CEM-Komponente | Expliziter JSON-Pointer auf genau eine customElement-Klassendeklaration; Struktur und Art geprüft |
| CEM-Teil | Expliziter JSON-Pointer in cssParts; tatsächliche Zugehörigkeit zum aufgelösten Komponentenobjekt geprüft |
| SCXML-Maschine | Eigenes SCXML-Artefakt, namespace-gebundener XPath auf scxml-Wurzel |
| SCXML-Zustand | Namespace-gebundener XPath auf genau einen state-Knoten der gewählten Maschine; data ist kein state |
| Verwendung A/B | Getrennte uses-Referenz auf die ausgewählte Definition, eigener statischer Zustandsbezug und eigene Hostteile |
| Host-/ARIA-Zuordnung | Rollen combobox/listbox/option, eindeutige IDs, controls/activedescendant und eigene List-/Popup-Abstammung |
| Zustandsprojektion | Explizite Zusatzregel open → expanded=true, gegen gespeicherten Snapshot geprüft |

Der Namespace und die Zielart werden am tatsächlich aufgelösten XML-/JSON-Knoten geprüft, nicht nur aus dessen Referenzetikett übernommen. Gleiche Namen ersetzen keine Adresse: Eine zweite gleichnamige CEM-Deklaration ist zulässig, solange explizit die gewählte adressiert wird; ihr Teil wird nicht zum Teil der ersten Klasse.

Das Beispielprofil verlangt zusätzlich gleiche Komponenten-/Maschinennamen für das festgelegte Paar und feste Partnamen input/popup/list/option. **Dies sind eigene Bedingungen dieses begrenzten Beispiels, keine allgemeine CEM-/SCXML-Pflicht und keine allein ausreichende Identität.** Andere Modelle mit abweichenden Namen benötigen eine andere ausdrücklich definierte Abbildung. Die strukturellen Adressen, Quellrevisionen und Definitionszugehörigkeit bleiben die wesentlichen zusätzlichen Nachweise.

## 16 Fälle

| Fall | Beobachtung |
| --- | --- |
| Kontrollpaket | Definition und beide Instanzen vollständig aufgelöst |
| Zweite gleichnamige Komponente, eindeutige Adresse | Gewählte erste Definition bleibt eindeutig; akzeptiert |
| Input-Part aus anderer gleichnamiger Komponente | foreign-component-part |
| Behaviorzustand als Interface-Part referenziert | reference-kind |
| Nicht vorhandener Part-Pointer | missing-target |
| List-Part als Input-Part | part-name |
| Mehrdeutiger Zustands-XPath | nonunique-target |
| Datamodellknoten als Zustand | target-kind |
| Veränderte Quelldatei bei altem Hash | source-revision |
| Bestehende Liste der anderen Instanz | same-instance-relation |
| Vorhandenes Listziel mit Rolle button | host-role |
| Doppelte Host-ID | host-unique-target |
| HTML-expanded widerspricht open-Projektion | state-projection |
| Maschine außerhalb des festgelegten Namenspaars | machine-component-binding |
| Ungebundene Namenssuche statt Locator | locator-kind |
| use verweist auf fehlende Definition | undefined-definition |

Alle 16 Erwartungen erfüllt. **Alle 16 CEM-/SCXML-Schema-Kombinationen akzeptiert**: Viele Fehler liegen im zusätzlichen Profil oder HTML; einzelne Originalschemas sind nicht für diese domänenübergreifende Bedeutung zuständig. Daraus folgt weder ein Fehler ihrer Schemas noch, dass sämtliche HTML-Fälle native ARIA-/HTML-Regeln bestehen würden. Diese stärkere Aussage wurde nicht geprüft.

results.json speichert pro Fall Originalschemaergebnisse, Quellhashes, das verwendete Profil und tatsächliche Auflösungszeugen für Definition/Instanzen. Die eigenen Varianten werden durch die gespeicherten Mutationseingaben und den Runner reproduzierbar erzeugt. Intentional geänderte Fixturequellen erhalten neue Hashpins, außer im ausdrücklich veralteten Revisionsfall. Kein stilles Überschreiben der vorigen Basispakete.

## Bewertung und verbleibende Lücke

**WAI-ARIA X03: U → A/C462** für diese zusätzliche statische Host-/Originalmodellbindung. Es ist nun konkret belegt, welcher externe CEM-Teil und welcher externe SCXML-Zustand der jeweiligen ARIA-Hostinstanz zugeordnet werden. Native IDREF-Semantik wird nicht zur Originalmodellreferenz umgedeutet; der eigene Adapter ist erforderlich.

Keine automatischen Umbewertungen von Zag, Ark UI, UXSpec, uSpec, OpenPencil, APG oder CSS X03: deren eigene Referenzmechanismen/Beiträge sind andere Gegenstände. Das ist keine Auswahl eines gemeinsamen Produktformats.

Aktuell **54 U-Zellen: 34 Integration und 20 weitere**. Weiterhin offen: originales neutrales A11y-Schema/Validatorpaar, vollständige Livezustands-/Datenbindung, native Ziele, Schema-/Artefaktmigration und nicht abgedeckte Referenzformen. Dieser statische Zustandsverweis beweist keine laufende SCXML-Instanz oder vollständige Accessibility-Konformität. Keine Produktionskomponente, Commits oder Pushes.

## Reproduktion

prepare.py erzeugt Baseline, Zusatzprofil und die 16 Erwartungen. run.py nutzt Python mit lxml/jsonschema und die bereits gepinnten Originalschemas aus den vorigen Prüfordnern; JSON-Pointer- und XPath-Auflösung sind Zusatzcode. Originalartefakte, relevante Werkzeugversionen und Schema-/Quelldateihashes sind im Manifest gebunden. Keine zusätzlichen Tests für Authentifizierung, Schemaevolution, generische externe Netzreferenzen oder unsichere Eingabeausführung behauptet.
