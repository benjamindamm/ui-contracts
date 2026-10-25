**Aktueller Stand – 25. Oktober 2026:** 41 offene Nachweise (26 Integration, 15 weitere), 435 benannte Prüfbedingungen in 56 Gruppen. Vollständige Integration, Produkt-UI und Assistenztechnik sind weiterhin nicht nachgewiesen; statische HTML-Host-Fixtures wurden inzwischen im Browser geprüft. Historische Zahlen und „nicht ausgeführt“-Aussagen unten beziehen sich auf die jeweils benannte frühere Runde. Maßgeblich ist das [aktuelle Register](OPEN-FIELDS.md).

# Detailvergleich: UXSpec und SCXML

**Aktuelle Fortschreibung nach diesem dokumentarischen Stand:** [49 E3-Proben](experiments/2026-10-24/REPORT.md) sind inzwischen ausgeführt. CEM I02 ist nun A/C421; aktuell 65 U (41 Integration, 24 weitere). Frühere Aussagen „keine Ausführung“ und damalige Zählungen unten dokumentieren den Entstehungsstand. Keine vollständige UI-/AT-/Integrationsprüfung.


Stand: 24. Oktober 2026. Dokumentarischer Vergleich der isolierten Behavior-Beiträge. **Keine Konvertierung, Installation oder Ausführung.** Beispiele und erwartete Abläufe sind eigene Prüfentwürfe. Sie sind keine validierten Originalartefakte und kein Nachweis semantischer Gleichheit.

## Ergebnis

Beide Modelle beschreiben Zustände, Übergänge und Datenverarbeitung. SCXML normiert zudem Ausführungsschritte, Ereigniswarteschlangen und aufgerufene Dienste. UXSpec beschreibt eine eigene JSON-Ausdrucks-/Aktionssprache sowie UI-nahe Angaben. Eine gemeinsame Baumform oder der Hinweis „SCJSON-kompatibel“ belegt keine gleichwertige Ausführung. Gerade zwischen UXSpecs Format, Originalschema, CLI und Referenz-App bestehen relevante Grenzen.

Für einen späteren Coding-Agenten ist daher zuerst eine enge gemeinsame Teilmenge zu prüfen. Das ist ein Vorschlag, keine Auswahl von SCXML oder UXSpec. Originalquellen: [S09](SOURCES.md), [S49](SOURCES.md#s49), erneuter gezielter Abgleich [S63](SOURCES.md#s63). Zusätzliche Befunde [C414–C417](CLAIMS.md#c414).

## Gegenstände und Zuständigkeiten

| Gegenstand | UXSpec am gespeicherten Snapshot | SCXML 1.0 Recommendation 2015 |
| --- | --- | --- |
| Dokument | JSON; `$machine` mit `id`, `initial`, `states` | XML mit SCXML-Namensraum, `initial`, Zustandsknoten |
| Behavior isoliert | Originalschema macht `$visual` optional; `$schema`, `$description`, `$machine` erforderlich | Visuelle Angaben sind keine Pflicht des Standards |
| Kontext | `$context` mit primitiven Typnamen, Default und optional required | `datamodel`/`data`; konkrete Ausdrucks- und Datentypsemantik hängt vom Datenmodell ab |
| Ereignisdaten | `$events` mit Payloadfeldern; Verarbeitung über `event.*` | Ereignisobjekt, insbesondere `_event.data`; `send`, `param`, `content` für Kommunikation |
| Öffentliche API | Lokales `$events` und `emit` sind nicht automatisch öffentliche Komponentenereignisse | Ausführbares `send` ist kein unabhängiger öffentlicher API-Signaturkatalog |
| Guards/Aktionen | Ausdrucksarrays und definierte Aktionsarten, etwa assign | `cond`, ausführbarer Inhalt und datenmodellabhängige Ausdrücke |
| Untermaschinen | Import-/Invoke-Beschreibungen im Format; tatsächliche Enginefähigkeit getrennt prüfen | `invoke`, neue logische Dienstinstanz, eigene Daten, Parameter, Abbruch und Abschlussereignis |
| UI-Anbindung | Visual-/Elementangaben und Host-/Effektpfade | Zusätzliche UI-/Hostbindung erforderlich |
| Validierung | Originalschema, ausgewählte CLI-Regeln und Compiler als verschiedene Pfade | XSD prüft Struktur; Interpreter/Datenmodell/Host liefern weitere Semantik |
| Portabilität | JSON allein beweist keine plattformgleiche Ausdrucks-/Effektausführung | XML allein beweist keine Portabilität des gewählten Datenmodells oder Hostcodes |

## Semantik, die eine Übersetzung erhalten müsste

| Frage | Gesicherter Befund | Konsequenz für eine spätere Prüfung |
| --- | --- | --- |
| Reihenfolge bei einfachem Zustandswechsel | UXSpec-App: exit, Übergangsaktionen, Ziel setzen, entry, always, Benachrichtigung, anschließend rekursiv emittierte Events. SCXML: Austrittsmenge, Übergangsinhalte, Eintrittsmenge innerhalb des normierten Algorithmus | Nur für den einfachen Fall eine plausible Zuordnung; Hierarchien und Nebenwirkungen gesondert protokollieren |
| Eventauswahl | UXSpec-App sucht den ersten passenden exakten Eventnamen mit erfülltem Guard | SCXML-Ereignisdeskriptoren und Konfliktauswahl nicht durch bloß gleiche Strings ersetzen |
| Ereignislose Übergänge | UXSpec-App begrenzt die lokale always-Schleife auf zehn Iterationen | Begrenzung ist kein Nachweis des SCXML-Makroschrittmodells; Zyklen/Fehlerzustände separat definieren |
| Interne Ereignisse | UXSpec-App sammelt emittierte Namen und ruft nach notify rekursiv send auf | SCXML-Warteschlangen-/Run-to-completion-Semantik und Beobachtungszeitpunkt nicht automatisch gleich |
| Ohne Ziel / Selbstübergang | SCXML unterscheidet zielos, intern und extern; externe Selbstübergänge können exit/entry auslösen | Nur explizite Zielwechsel in die erste gemeinsame Teilmenge aufnehmen |
| Hierarchie und Parallelität | SCXML definiert Ausführungsmengen und Konflikte; UXSpecs Formatbaum und App-Zustandspfad sind andere Nachweisgegenstände | Keine vollständige Statechart-Kompatibilität behaupten |
| Invoke und Cancellation | UXSpec-SPEC fordert aktive Effekte während des Zustands und Abbruch beim Austritt. Im erneut gelesenen App-Interpreter richten enterState/exitState keine allgemeinen state.invoke-Dienste ein/ab | Formatversprechen nicht der gelesenen App als implementiert zurechnen. Compiler und andere Engines bleiben separat |
| Ereignistypen | App-send baut ein Objekt aus type und Payload; in diesem Pfad keine Payloadschema-Prüfung | Typdeklaration ist kein Beweis, dass fehlerhafte Eingaben zur Laufzeit abgewiesen werden |
| Ausdrucksprüfung | CLI kennt eine konkrete Menge unterstützter Operatoren; Schema erlaubt weitere Ausdrucksarrays strukturell | Schemaerfolg und CLI-Erfolg getrennt festhalten |
| Automatische Vorschau | App-Initialisierung kann nach 800 ms einen synthetischen Folgeevent mit Mockdaten senden, unter anderem bei fehlendem Visualinhalt | Eine Behavior-only-Vorschau ist ohne kontrollierten Simulationsmodus keine neutrale Vergleichslaufzeit |

Die letzten beiden Enginebefunde sind E2-Quelltextbefunde, keine beobachteten Ausführungsfehler. Der Apppfad ist ausdrücklich **kein Audit aller UXSpec-Interpreter**. [C415](CLAIMS.md#c415)

## Enger gemeinsamer Prüffall – Vorschlag

Zwei flache Zustände `closed` und `open`; numerischer Kontext `count` mit Startwert 0. `OPEN` enthält `allowed:boolean` und `delta:number`. Ein wahrer Guard wechselt von closed nach open und addiert delta. `CLOSE` wechselt zurück. Keine Visualdaten, keine Nebenwirkungen, keine internen Emit-Ereignisse, keine Invoke-Dienste, keine Hierarchie. Beide Inputs werden vom späteren Prüfharness typgeprüft; das wird nicht stillschweigend einer Engine zugeschrieben.

### UXSpec-Entwurf

Der Schemazeiger ist ausdrücklich auf den gespeicherten Originalsnapshot gebunden. Er wurde für diesen Entwurf nicht durch einen Validator ausgewertet.

```json
{
  "$schema": "https://raw.githubusercontent.com/johnlindquist/uxspec/20dfae0e7224d952e198afdf4ffed26d6fd67180/schema/uxspec.schema.json",
  "$description": "Prüfentwurf: expliziter Zustandswechsel mit Guard und Zähler",
  "$context": { "count": { "type": "number", "default": 0 } },
  "$events": {
    "OPEN": { "payload": {
      "allowed": { "type": "boolean" },
      "delta": { "type": "number" }
    } },
    "CLOSE": { "payload": {} }
  },
  "$machine": {
    "id": "counter",
    "initial": "closed",
    "states": {
      "closed": { "on": { "OPEN": {
        "target": "open",
        "guard": ["==", ["var", "event.allowed"], true],
        "actions": [{
          "kind": "assign", "path": "context.count",
          "value": ["+", ["var", "context.count"], ["var", "event.delta"]]
        }]
      } } },
      "open": { "on": { "CLOSE": { "target": "closed" } } }
    }
  }
}
```

### SCXML-Entwurf

Die Wahl `datamodel="ecmascript"` ist nur eine offengelegte Vergleichsannahme für diesen Versuch, keine allgemeine Architekturentscheidung. Payload liegt unter `_event.data` statt unter UXSpecs `event`.

```xml
<scxml xmlns="http://www.w3.org/2005/07/scxml"
       version="1.0" datamodel="ecmascript" initial="closed">
  <datamodel><data id="count" expr="0"/></datamodel>
  <state id="closed">
    <transition event="OPEN" cond="_event.data.allowed === true" target="open">
      <assign location="count" expr="count + _event.data.delta"/>
    </transition>
  </state>
  <state id="open">
    <transition event="CLOSE" target="closed"/>
  </state>
</scxml>
```

### Papiererwartung, keine Messergebnisse

| Schritt | Eingabe | Erwarteter Zustand | Erwarteter count |
| --- | --- | --- | ---: |
| 0 | Start | closed | 0 |
| 1 | OPEN, allowed=false, delta=2 | closed | 0 |
| 2 | OPEN, allowed=true, delta=2 | open | 2 |
| 3 | CLOSE | closed | 2 |
| 4 | OPEN, allowed=true, delta=3 | open | 5 |

Die Erwartung setzt genau diese Typen, keine Zusatzereignisse und eine kontrollierte Laufzeit voraus. Die gelesene UXSpec-App kann für den visualfreien Entwurf automatische Mockevents einplanen. Dieser Pfad darf deshalb nicht unverändert als Messung der Papiererwartung ausgegeben werden.

## Konkrete negative und erweiterte Fälle

| Fall | Was der nächste praktische Auftrag festhalten müsste | Noch nicht belegt |
| --- | --- | --- |
| delta fehlt / ist String | Fehlerpolitik und Stelle der Abweisung für beide Inputs | Gleiche automatische Payloadprüfung |
| Unbekannter Operator | Originalschema, CLI und Engine getrennt aufrufen | Gleichheit ihrer akzeptierten Sprachen |
| Zielzustand fehlt | Struktur-/Semantikdiagnose mit Zeile/Pfad speichern | Einheitliche Originalvalidator-Diagnose |
| always-Zyklus | Makroschritte und Abbruch/Fehler protokollieren | Gleiche Terminierungsstrategie |
| Emit während entry | Ereignisfolge einschließlich Beobachterzeitpunkt speichern | Gleiche Warteschlangenordnung |
| Invoke mit spätem Ergebnis nach exit | Child-ID, Abbruch und ignorierte/empfangene Folgeereignisse protokollieren | Vollständige Umsetzung im gelesenen UXSpec-Apppfad |
| Zwei gleiche Definitionen | Verschiedene Instanzen, Eingaben und Kontexte vergleichen | Gemeinsame UI-/DOM-Identität oder native Abbildung |
| Schema-machineInvoke | Konkreten gültigen machineInvoke gegen Originalschema prüfen | In stateNode.invoke überlappen `$ref:machineInvoke` und `{type:object}` innerhalb oneOf; manuell folgt ein Mehrfachtreffer für passende machine-Objekte, aber kein Validator wurde ausgeführt |

Der oneOf-Befund ist eine eng begrenzte Ableitung aus dem Originalschema, keine ausgeführte Fehlermeldung und keine eigenmächtige Reparatur. Eine zusätzliche Konvertierung muss solche Originalabweichungen sichtbar lassen. [C416](CLAIMS.md#c416)

## Abschluss und offene Entscheidung

Der dokumentarische Detailvergleich ist ausgearbeitet: Unterschiede, schmaler Prüffall, erwartete Folge und negative Fälle liegen vor. **Nicht abgeschlossen** sind praktische Äquivalenz, Auswahl von Interpreter/Datenmodell und die Vier-Domänen-Integration. Ein Coding-Agent kann darauf aufbauen, ohne eine bereits bewiesene UXSpec↔SCXML-Konvertierung vorauszusetzen. Der öffentliche Eventvertrag bleibt bei beiden eine gesonderte Integrationsaufgabe.
