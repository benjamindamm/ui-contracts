# UX-Fähigkeiten prüfen und Komponenten auswählen

**Dieser Prüfweg unterstützt die Frage: Welche vorhandene Komponente passt zu einer festen Wertauswahl?** Er prüft deklarierte Fähigkeiten gegen unterstützte Quellen-/Verhaltensprofile und wertet die Policy der ausdrücklich gewählten Bibliothek aus.

**Ergebnis:** Eine begründete Auswahl oder eine konkrete Rückfrage/Fehlerdiagnose, gebunden an Quellenstand und Prüfumfang. Die Auswahl ist noch keine Abnahme einer erzeugten UI.

## Mit einem Agenten beginnen

Nutze den [UI-Contracts-Skill](../../docs/skills/README.md) mit Bibliothek, Ziel und fachlichen Anforderungen. Der Agent lädt nur die benötigten Regeln. Für den manuellen Werkzeugweg folgen unten die Befehle.

> **Beispiel in der Bibliothek example**
>
> Drei feste Vorwahlen führen im vorhandenen Policyprofil zu Select; 30 zu Select mit Suche. Die Grenze von 15 Optionen ist eine gesetzte Beispielpolicy, keine allgemeine UX-Regel.

Originalquellen führen. JSON- und Prüfprofile sind eigene versionierte Projektkonventionen, kein universeller UX-Standard. Freie Texteingabe fällt ausserhalb dieser festen Auswahlpolicy.

## Manueller Ablauf

1. **Einrichten:** [Projektlaufzeit](RUNTIME.md) mit Python, Node und bei Policyauswertung Java bereitstellen.
2. **Fähigkeiten prüfen:** Bibliothek und ihre relevanten Quellen/SCXML-Fälle prüfen, bei Bedarf Fakten vorbereiten.
3. **Policy auswerten:** Tatsächliche Optionen und Anforderungen übergeben. Fehlende Fakten führen zur Klärung; ein ungültiger Contract stoppt die Auswahl.

## Bibliotheksquellen

`library.json` verlinkt unter `selection` die Policy und das Fähigkeitsschema. Jede beteiligte `component.json` verlinkt ihr `ux.json`. Dieses nennt deklarierte Fähigkeiten, vollständige Quellenhashes und ein **Prüfprofil**, keinen selbst gesetzten Erfolgsstatus.

```sh
# Begrenzte Quellen-/Identitäts-/Aliasprüfung; keine Runtimefreigabe:
tools/validation/.venv/bin/python tools/libraries/check.py --library example

# Aktuelle Quellen prüfen und native SCXML-Contractfälle ausführen:
tools/validation/.venv/bin/python tools/ux/check.py --library example --output /tmp/ux-example-new.json

# Fakten und Nachweisstatus für die Policy vorbereiten; trifft noch keine Wahl:
tools/validation/.venv/bin/python tools/ux/choose.py \
  --library example --context tools/ux/contexts/fixed-thirty.json --prepare-only
```

Einrichtung und ausführbare Quellen: [Runtime und Voraussetzungen](RUNTIME.md).

## Ergebnis verstehen

| Status je Komponente | Bedeutung für die Auswahl |
| --- | --- |
| `declared` | Fachliche Behauptung vorhanden; kein passendes ausgeführtes Profil. Nicht als nachgewiesen eligible verwenden. |
| `unverified` | Profil unbekannt oder notwendiges Werkzeug fehlt. Keine harte Erfüllung ableiten. |
| `invalid` | Quellen/Schema/Profil widersprechen sich oder tatsächliche Contractfälle schlagen fehl. Auswahl stoppt mit FAIL. |
| `verified-limited` | Aktuelle CEM-/HTML-Struktur und die im Profil unterstützten TypeScript-Signaturen passen; die tatsächlich ausgeführten SCXML-Gegenfälle bestehen. Gilt ausschliesslich für diesen Quellenstand und Prüfumfang. |

### Unterstützte Profile

- `single-select/1`: ein fester Schlüssel, native Select-Struktur, Mitgliedschaft, Disabled, kontrollierte Updates und Ereignisse.
- `separate-search-select/1`: zusätzlich getrennte Query, Filterbezug, aktive Option ohne Commit und Escape. Die native SCXML-Logik wird ausgeführt; ein erzeugter Browserfilter ist damit noch nicht geprüft.
- `text-input/1`: Stringerhalt, ReadOnly/Disabled, kontrollierte Updates und tatsächliches Input-Ereignis.
- `composed-autocomplete/1`: frische verschachtelte Overlay-/ScrollArea-Instanzen, echte Provider-/Commitereignisse, Isolierung, Requestidentität, deaktivierte Hostschlüssel und Providerdaten-Gate. Die native MEASURED-Antwort ist synthetisch; reale Scrollgeometrie wird separat im [Weblauf](../web/README.md) geprüft.
- `declared-only`: bewusste, nicht automatisch bestätigte Fähigkeitsbeschreibung ohne native Freigabe.

`interactionIntent` bleibt eine fachlich gesetzte Zweckzuordnung. Sie wird nicht als durch Runtimefälle bewiesen aufgelistet. Keine automatische Ableitung aus Componentnamen. Ein gefälschter Status in `verification` wird vom Schema abgewiesen; gespeicherte Pass-Receipts werden für neue Entscheidungen nicht als Eingabe übernommen. Der Checker prüft jeweils neu.

**Grenze:** endlich viele Contractfälle und statische Strukturprüfung sind kein formaler Beweis beliebiger ECMAScriptprogramme. Browseradapter, Fokus/Scrollen, reale IME, Accessibility und Produktion benötigen ihre eigenen Nachweise. `release:false` und `targetValidationRequired:true` bleiben sichtbar.

## Native DMN-Auswahl

Die Bedingungen stehen weiterhin in der führenden `selection-policy.dmn`. Python prüft Fakten, Quellen und Nachweisstatus und übergibt sie an die Originalengine; es führt keine zweite eigene Rankinglogik.

```sh
tools/validation/.venv/bin/python tools/ux/choose.py \
  --library example --context tools/ux/contexts/fixed-three.json
```

Die Kontextdatei benennt die Bibliothek, tatsächliche Optionen und vier explizite Fakten: feste Werte gefordert, temporäre Suche erlaubt, direkte Bearbeitung des gewählten Labels erlaubt sowie Filterprovider vorhanden. Fehlende Fakten sind unbekannt und führen zu `needs-clarification`; Freitext-Schreibhilfe fällt ausserhalb der festen Auswahlpolicy. Ein Provider-Fakt ist eine deklarierte Kontextvoraussetzung, kein Nachweis einer erzeugten Implementierung.

Im example-Profil ist >15 eine ausdrückliche Produkt-/Studienregel. Der Runner berechnet die Optionsanzahl aus der tatsächlichen Liste. Er erfindet keine allgemeine UX-Grenze und keine geografische Priorität. Gleichlautende Vorwahlen dürfen verschiedene Länderschlüssel behalten.

## Regressionen

```sh
PYTHONDONTWRITEBYTECODE=1 tools/validation/.venv/bin/python -m unittest discover -s tools/libraries -p test_check.py
PYTHONDONTWRITEBYTECODE=1 tools/validation/.venv/bin/python -m unittest discover -s tools/ux -p test_ux.py
# Originalengine-Integration nur mit explizit eingerichteter Runtime:
UX_RULE_RUNTIME=/pfad/runtime tools/validation/.venv/bin/python -m unittest discover -s tools/ux -p test_dmn.py
```

Ohne Runtime werden die Integrationsfälle ausdrücklich übersprungen, nicht als bestandener Engine-Nachweis gezählt. Die anderen Fälle prüfen unter anderem falsche Suchbehauptung, falsches Profil, entfernten Membership-Guard bei ehrlich erneuerten Hashes, fremde Bibliotheksfakten, unvollständige Fakten und manipulierte Engine-JARs.

[UX-Leitlinie](../../docs/ux/AUTOCOMPLETE.md) · [Übernahme und neue Belege](../../docs/research/analyses/ACTIVE-UX-2026-10-31/README.md).

## Kleiner Toolkontext

Die drei CLI-Einstiege geben standardmässig eine kurze Zusammenfassung aus. `--output NEUE_DATEI` legt die vollständigen Quellen-/Prüfbelege separat mit SHA-256-Verweis ab; bestehende Dateien und Quell-/Historienverzeichnisse werden nicht überschrieben. `--details` lädt die volle Ausgabe ausdrücklich in den Toolkontext. Ein Agent muss die grossen Belege deshalb nicht vorsorglich lesen. Python-Funktionen liefern weiterhin die vollständigen strukturierten Ergebnisse für technische Integration.

Gemeinsamer Testeinstieg und aktuelle Targetprüfung: [tools/web](../web/README.md).
