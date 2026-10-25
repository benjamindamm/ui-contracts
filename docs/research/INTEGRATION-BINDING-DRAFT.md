# IP-01: Entwurf der minimalen Bindungsbeschreibung

Stand: 25. Oktober 2026. **Vorschlag zur späteren Umsetzung**, keine verabschiedete Formatsyntax, kein Validator und kein ausführbares Paket. Dieser Entwurf konkretisiert [IP-01](INTEGRATION-PROFILE.md); er ergänzt ausschließlich Beziehungen zwischen den vier Domänen. Bestehende Schemas werden nicht erweitert. Neue Norm- oder Laufzeitnachweise entstehen dadurch nicht.

## 1. Drei getrennte Ebenen

1. **Originalquellen:** CEM deklariert Properties/Parts/Events, SCXML Verhalten, DTCG/CSS Visual, HTML/ARIA mit APG-Bezug Accessibility. Fachwerte und Fachregeln werden dort gepflegt.
2. **Bindungsbeschreibung:** Verweist auf Definitionen und konkrete Originalstellen, beschreibt Verwendungen, Ports und Ableitungen. Sie enthält keine zweite Auswahlmaschine, kopierte Tokens oder zweite Rollenbeschreibung.
3. **Auflösungsprotokoll:** Hält für einen Lauf tatsächliche Dateihashes, Norm-/Werkzeugpins, ausgewählte Adapter und aufgelöste Beziehungen fest. Es wird abgeleitet und ist kein zweites editierbares Original.

Eine weitere Datei ist nur dort gerechtfertigt, wo vorhandene Originalidentitäten die konkrete Beziehung nicht ausdrücken. Der erste Entwurf verwendet JSON als lesbares Beispiel. Ein späteres Schema muss genau diese kleine Struktur und ihre unterstützte Locator-/Typteilmenge festlegen; es darf daraus keine universelle UI-Sprache machen.

## 2. Minimale Struktur am Beispiel

**Alle folgenden Feldnamen sind vorgeschlagen.** Die Pfade unter `reference/` sind geplante neue Dateien, keine bereits erzeugten Fixtures. `locator` enthält absichtlich keine erfundenen echten JSON-Pointer oder XPath-Ausdrücke. Erst beim Erstellen der Originaldateien werden konkrete, auf Existenz und Zielart geprüfte Locator eingetragen. Ein gemeinsamer Prüfer muss diese unaufgelöste Beispielbeschreibung deshalb als **nicht ausführbar** melden.

```json
{
  "kind": "ui-contract-binding-draft",
  "profile": "IP-01",
  "status": "illustrative-unresolved",
  "sources": [
    {"id": "ac.interface", "domain": "interface", "format": "cem", "path": "reference/autocomplete/interface.json"},
    {"id": "ac.behavior", "domain": "behavior", "format": "scxml", "path": "reference/autocomplete/behavior.scxml"},
    {"id": "ac.a11y", "domain": "accessibility", "format": "html", "path": "reference/autocomplete/accessibility.html"},
    {"id": "ac.visual", "domain": "visual", "format": "css", "path": "reference/autocomplete/visual/layout.css"}
  ],
  "definitions": [
    {"id": "reference:Autocomplete", "sources": ["ac.interface", "ac.behavior", "ac.a11y", "ac.visual"]}
  ],
  "targets": [
    {"id": "ac.input", "source": "ac.interface", "kind": "part", "definition": "reference:Autocomplete", "locator": null},
    {"id": "ac.list", "source": "ac.interface", "kind": "part", "definition": "reference:Autocomplete", "locator": null},
    {"id": "ac.expanded", "source": "ac.a11y", "kind": "attribute-projection", "definition": "reference:Autocomplete", "locator": null},
    {"id": "ac.state", "source": "ac.behavior", "kind": "state-projection", "definition": "reference:Autocomplete", "locator": null}
  ],
  "uses": [
    {"path": ["A"], "definition": "reference:Autocomplete"},
    {"path": ["B"], "definition": "reference:Autocomplete"}
  ],
  "relations": [
    {"id": "expanded-state", "kind": "projection", "from": "ac.state", "to": "ac.expanded", "scope": "same-use", "ruleSource": "ac.a11y", "ruleLocator": null}
  ]
}
```

Das Beispiel zeigt nur die Form eines Autocomplete-Beitrags. Overlay, ScrollArea, Tokens und konkrete Port-/Anatomiebindungen müssen ergänzt werden, bevor die Quellenliste vollständig ist. Keine fehlende Quelle darf durch Namensheuristik gesucht werden. Die vier Rollen pro Definition sind logisch getrennt; mehrere eigene Beiträge können dieselbe ausdrücklich geteilte Tokenquelle referenzieren.

## 3. Feldbedeutungen und Resolverpflichten

| Feld / Begriff | Bedeutung | Erforderliche Prüfung |
| --- | --- | --- |
| `sources.id` | Lokaler eindeutiger Quellalias; kein globaler Komponentenname | Doppelte Aliase ablehnen; Pfad innerhalb des erlaubten lokalen Quellenbestands. |
| `domain`, `format` | Führende fachliche Rolle und tatsächliche Originalsyntax | Passenden Originalprüfpfad und begrenzten Adapter wählen. Ein Formatname allein beweist keine Validierung. |
| `definitions.id` | Bibliotheksnamespace und Definitionsname | Einmalige Definition im aufgelösten Abschluss; Revision über Protokoll binden. |
| `targets.id` | Alias einer konkreten Stelle in einem Original | `source`, unterstützter Locator und Zielart gemeinsam auflösen; keine freie Suche nach gleichem Namen. |
| `targets.definition` | Fachliche Zugehörigkeit des Originalziels | Fremde Definition und falsch zugeordneter Part werden auch bei existierendem Locator erkannt. |
| `uses.path` | Hierarchischer Instanzpfad als Segmentliste | Präfixe und Eltern eindeutig; keine Mehrdeutigkeit durch zusammengeklebte Strings. A/overlay/scroll und B/overlay/scroll sind verschieden. |
| `relations.kind` | Eine ausdrücklich unterstützte Bindungsart | Unbekannte Art als nicht unterstützt melden; nicht einfach ignorieren. |
| `scope: same-use` | Beide Definitionsziele werden auf dieselbe konkrete Verwendung spezialisiert | Das Schema allein genügt nicht; Resolver muss den tatsächlichen Instanzkontext prüfen. |
| `ruleSource` / `ruleLocator` | Originalstelle, welche die fachliche Projektion führt | Der Resolver transportiert diese Regel; er erfindet deren Auswahl-/ARIA-Semantik nicht. |

**Locatorpolitik für die erste Umsetzung:** JSON-Pointer für unterstützte CEM-/Tokenstellen; namespacebewusste XPath-Auswahl für SCXML. Für HTML und CSS jeweils eine ausdrücklich eingeschränkte, am tatsächlichen Syntaxbaum geprüfte Auswahl festlegen. Das ist noch eine Umsetzungsentscheidung. DOM-ID, CSS-Ankername und Definitionsalias sind verschiedene Zielarten. Ein `#name` darf nicht automatisch alle drei meinen. Null-Locator, Mehrfachtreffer und nicht unterstützte Ausdrücke verhindern einen ausführbaren Abschluss.

## 4. Vollständiger Beziehungsumfang

Die spätere Beschreibung muss mindestens folgende Beziehungen auflösen. Diese Tabelle ist zugleich eine Vollständigkeitsliste für den Coding-Agenten.

| Beziehung | Führende Fachinformation | Konkrete Bindung / ausgeschlossener Kurzschluss |
| --- | --- | --- |
| Autocomplete verwendet Overlay | Behavior: Lifecycle und Parameter | A→A/overlay und B→B/overlay; niemals globale Verwendung nur anhand des Namens `overlay`. |
| Overlay verwendet ScrollArea | Overlay-Behavior: Child-Lifecycle | A/overlay→A/overlay/scroll und entsprechend B; eigene Daten, Parentroute und Epoche. |
| Öffentliche Signatur → Laufzeitport | Interface: Typ und Eventname | Behavior-Port und Payload müssen kompatibel sein; gleicher Ereignisname genügt nicht. |
| Ergebnisdaten → Optionen | Interfaceform plus Behavior-Annahme aktueller Daten | Wiederholte Teile instanzbezogen über Datenkey auflösen; Arrayindex ist keine dauerhafte Identität. |
| Eingabe → Overlayanker | Visual: relative Geometrie | Input derselben Suche → eigene Overlayfläche; keine zugängliche Beziehung aus dem Anker ableiten. |
| Input → Listbox | Accessibility: Relationsregel | Tatsächliche semantische Listbox derselben Suche; nicht Overlayfläche oder Scrollviewport. |
| Aktiver Key → zugängliches Ziel | Behavior liefert Key; A11y definiert Projektion | Existierende aktuelle Option verwenden; stale oder entfernte Option darf kein aktives Nachfahrenziel bleiben. |
| Aktiver Key → Reveal | Behavior fordert Sichtbarkeit; ScrollArea misst | Option im eigenen Inhalt und aktueller Request; gemessene Sichtbarkeit statt bloß übernommener Wunschoffset. |
| Token → Hostlayout | Visual: typisierter Wert und Einheit | Ausdrücklich unterstützte DTCG-Alias-/Wertteilmenge übersetzen; Einheit erhalten. |
| Zustand → Visual/A11y | Behavior: Zustand; Ziel-Domäne: Darstellungs-/Semantikregel | Beide Verbraucher lesen denselben Instanzzustand; kein zweiter separat editierter expanded-/selected-Zustand. |
| Zustandsänderung → Meldung | Behavior: Auslöser; A11y: Text-/Locale-Regel | Nur aktuelle Instanz/Generation; keine Ansage aus bloßer Themeänderung. |
| Führende Änderung → Ableitungen | Je Information festgelegte Quelldomäne | Quellenabschluss und betroffene Ausgaben aktualisieren; Ableitungsänderung ohne führende Änderung als Konflikt melden. |

## 5. Auflösungsprotokoll

Ein späterer Lauf erzeugt für jede Originaldatei Pfad, tatsächlichen SHA-256, Quellen-/Formatstand, Adapterstand und Prüfergebnis. Für jede Beziehung enthält er Quell- und Zielrevision, konkrete Locator, aufgelöste Zielarten und Instanzkontext. Der Paketfingerprint folgt einer einzigen dokumentierten deterministischen Regel für Ausgangs- und Folgerevision. Ein noch nicht aufgelöstes Paket besitzt keinen als gültig ausgegebenen Fingerprint.

Pfadnormalisierung und erlaubter lokaler Abschluss werden explizit geprüft; keine impliziten Netzwerkzugriffe oder Versionsbereichsupdates. Für Dateien mit mehreren Rollen wird die Zuordnung ausdrücklich protokolliert, nicht aus der Endung geraten. Geplante neue Dateien erhalten erst bei ihrer tatsächlichen Erstellung echte Hashes. Der vorhandene [Dokumentations-Belegindex](INTEGRATION-PROFILE-EVIDENCE.json) erfüllt diese Laufzeitrolle ausdrücklich nicht.

## 6. Diagnoseform

Vorgeschlagene gemeinsame Hülle: `code`, `phase`, `severity`, `profile`, `revision`, `relation`, `instancePath`, `source`, `locator`, `expected`, `actual`, `leadingSources`. Fehlende Werte werden als fehlend ausgewiesen, keine erfundenen Revisionen eingetragen.

| Diagnoseklasse | Beispiel | Wirkung im ersten Profil |
| --- | --- | --- |
| `ORIGINAL_INVALID` | Originalschema weist Datei ab | Abschluss blockieren; Originaldiagnose erhalten. |
| `UNSUPPORTED` | Nicht unterstützter Typ oder Locator | Betroffene Funktion nicht freigeben; keine allgemeine Ungültigkeit des Originals behaupten. |
| `SOURCE_MISMATCH` | Inhalt stimmt nicht mit dem aufgelösten Pin überein | Lauf vor Ausführung blockieren. |
| `TARGET_MISSING` / `TARGET_AMBIGUOUS` | Kein oder mehrere passende Originalziele | Beziehung blockieren. |
| `TARGET_KIND_MISMATCH` | Viewport anstelle von Listbox | Semantischen Konflikt trotz existierendem Ziel melden. |
| `INSTANCE_MISMATCH` | A-Relation adressiert Option von B | Beziehung beziehungsweise Laufzeitrückmeldung zurückweisen. |
| `TYPE_MISMATCH` | Zahlenwert für string-Payload | Übergabe blockieren, keine stille Konvertierung. |
| `OWNERSHIP_CONFLICT` | Ableitung widerspricht führender Quelle | Betroffene Revision nicht abnehmen. |
| `STALE_IGNORED` | Antwort gehört zu alter Epoche | Daten ohne fachliche Wirkung verwerfen und beobachtbar protokollieren; kein kaputtes Originalschema behaupten. |
| `RUNTIME_FAILED` | Kindinitialisierung scheitert | Vereinbarten Fehler-/Cancelpfad ausführen; gesondertes tatsächliches Ergebnis protokollieren. |

Codebezeichnungen sind Vorschläge und keine bereits implementierte API. Die Diagnose muss den fachlichen Fehler vom Integritätsfehler unterscheiden können; deshalb benötigt die [Abnahme](INTEGRATION-ACCEPTANCE.md) korrekt neu gepinnte semantische Gegenfälle.
