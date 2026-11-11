# Draft-Vollständigkeit und gezielte Rückfragen

**Der Check hält fehlende Entscheidungen einer Komponente sichtbar.** Er prüft ein ausdrücklich gewähltes Anforderungsprofil und erzeugt eine stabile Fragenliste. Ein Designimport kann damit Gestaltung belegen und Verhalten weiterhin offen lassen.

Er ergänzt die vorhandenen Quellen-/Schemaprüfer und Zieltests. Er liest ausschliesslich Dateien, führt weder importierten Code noch SCXML aus und verändert weder Komponente noch Record beim Prüfen.

## Mit dem Agenten arbeiten

[UI-Contracts-Skill](../../skills/ui-contracts/SKILL.md) → [Rückwege](../../skills/ui-contracts/references/reverse.md). Der Agent gewinnt zuerst belegte Regeln aus Design/Code, legt sie innerhalb des Auftrags in den führenden Contracts ab und führt dann den Check aus. Rohes Design oder Code ersetzt keine noch fehlende Contractentscheidung.

> „Nutze Bibliothek meine-app. Erschliesse diese Designdatei als Draft. Halte unbekanntes Verhalten offen, führe den Vollständigkeitscheck aus und frage mich gezielt nach den fehlenden fachlichen Entscheidungen.“

## Manueller Ablauf

Projektlaufzeit über `python3 tools/setup.py` bereitstellen. Alle Komponentenpfade sind relativ zur ausdrücklich gewählten Bibliothek; Reportpfade sind relativ zum Arbeitsverzeichnis.

```sh
# Einmalig: Record mit allen Fragen offen erstellen, niemals überschreiben.
tools/validation/.venv/bin/python tools/completeness/check.py \
  --library meine-app --component components/select/component.json \
  --record libraries/meine-app/components/select/completeness-v1.json \
  --init --profile interactive-control/1

# Record inhaltlich bearbeiten; neue Revisionen separat ablegen. Danach:
tools/validation/.venv/bin/python tools/completeness/check.py \
  --library meine-app --component components/select/component.json \
  --record libraries/meine-app/components/select/completeness-v1.json \
  --output .runtime/select-completeness-v1.json
```

Die Beispielbibliothek meine-app wird nicht automatisch angelegt. `component.json` benötigt `format: ui-contract-component-draft` und eine stabile `id`; fehlende Domänenverweise dürfen für diesen Draftcheck fehlen. Der bestehende strengere `tools/libraries/check.py` wird nicht gelockert: Er erwartet vollständige Domänenbindungen und kann einen solchen Draft ablehnen. **Gültiger Draft im Coverage-Weg bedeutet nicht gültige vollständige Komponente.** Keine Dummydateien anlegen, um diese Trennung zu verstecken.

## Profile und Entscheidungen

[profiles.json](profiles.json) ist die versionierte eigene Checkliste, kein fünfter UI-Standard:

- **interactive-control/1:** 11 Fragen zu Wert/API, Events, Tokens/Layout, Lebenszyklus, Bestätigung, Abbruch, Semantik, Name, Tastatur/Fokus und UX-Eignung.
- **decorative-visual/1:** vier Fragen zu Darstellung, Ausblendung für assistive Technik und dekorativem Zweck. Kein Ersatzprofil für interaktive Controls, informative Charts oder fachlich bedeutsame Inhalte.

Die Profile sind bewusst begrenzt; sie decken nicht jede Komponente ab. Der Agent muss Profileignung und zusätzliche fachliche Anforderungen separat prüfen. Ein neues Profil ist eine bewusste Werkzeugrevision mit Gegenfällen. Es gibt keinen automatischen Profilfallback und keinen Schalter, der unbekannte Anforderungen pauschal als nicht relevant schliesst.

Der Record bindet auch den Hash von `profiles.json`; geänderte Profile blockieren alte Records statt sie still neu auszuwerten. Nach bewusster Profilprüfung eine neue Recordrevision anlegen.

Der [Coverage-Record](record.schema.json) hält Zuordnungen und offenen Status fest, keine Kopie führender Werte. Jedes Profilkriterium hat eine stabile ID. Nicht aufgeführte Kriterien gelten als offen; unbekannte IDs blockieren, damit Tippfehler keine Frage verschwinden lassen.

| Status im Record | Wirkung |
| --- | --- |
| `open` | Frage bleibt offen, auch wenn Dateien oder Evidenz vorhanden sind |
| `conflict` | Blockierende Frage; `note` beschreibt widersprechende Aussagen |
| `mapped` | Quellenhash und nichtleeren Locator prüfen; bei Fehler Frage wieder öffnen |

`note` ist eine ungeprüfte Autorennotiz und kann keine Lücke schliessen. Eine ausdrückliche Regel „Escape bewirkt keine Änderung“ kann belegt werden; blosses N/A wird nicht akzeptiert. Antworten und Entscheidungen führt der Agent in einem nachvollziehbaren Arbeitsbericht mit Herkunft, danach in den passenden Contractquellen. Der Record ersetzt weder Entscheidungsprotokoll noch Quellenkarte.

## Quellenbelege

Jeder Beleg enthält `sha256` der aktuell gebundenen Domänendatei sowie `selector: {kind, value}`. Seine Datei ergibt sich ausschliesslich aus `component.json`, nicht aus einem beliebig gewählten Fremdpfad:

| Domäne | Locator |
| --- | --- |
| CEM, Tokens, UX | `json-pointer`, etwa `/modules/0/declarations/0/members/0` |
| SCXML, HTML | `xpath`, etwa `//s:transition[@event="ESCAPE"]`; Präfix `s` bezeichnet SCXML |
| CSS | `lines`, etwa `1:8`; Kommentartext allein genügt nicht |

Zusätzlich prüft das Profil ausgewählte Formen: CEM-Feld/Event mit Name und Typ, Token mit Wert und explizitem oder geerbtem Typ, CSS-Regelgestalt, gültiger initialer Zustandsverweis, ereignisbezogener SCXML-Übergang, natives Element/gesetzte Rolle sowie ein konkreter Labelbezug. Beim dekorativen Profil muss `aria-hidden="true"` ausdrücklich vorliegen. Das sind endliche Strukturtests, keine vollständigen Originalschemas oder Beweise der Fragebedeutung. Das interaktive Profil erwartet für Bestätigung, Abbruch und Tastatur eine explizit ereignisbezogene SCXML-Stelle; andere Modellierungsformen brauchen ein begründetes eigenes Profil.

Quellenstellen müssen nichtleer sein und dürfen keine erkannten TODO/TBD/FIXME-/Platzhaltermarker enthalten. Ein explizites `false` oder `0` gilt als Wert. Parser, Grössenlimit, Pfadgrenzen und Symlinkverbot begrenzen Eingaben; sie sind keine vollständige Sandbox. Ändert sich eine Domainquelle, öffnen sich alle noch an ihre alten Hashes gebundenen Kriterien. Eine geänderte Komponentenbindung öffnet sämtliche Kriterien. Quellen nach Änderung erneut prüfen, nicht nur Hashes nachtragen.

## Ergebnis lesen

| Ergebnis | Exit | Bedeutung |
| --- | --- | --- |
| `DRAFT_INCOMPLETE` | 1 | Offene, konfliktbehaftete oder nicht mehr belegte Profilfragen |
| `COVERAGE_RECORDED` | 0 | Alle Profilfragen haben aktuelle, nichtleere Quellenlocators |
| `BLOCKED` | 2 | Eingabe, Record oder Profil ungültig; zuerst Werkzeugauftrag reparieren |

Die Standardausgabe enthält alle offenen Fragen mit ID, Domäne und Grund. Grosse Quellenbelege liegen bei `--output` in einer neuen Datei; `--details` ist optional. Reports überschreiben keine Quellen, historischen Dateien oder existierenden Ausgaben. `--init` erstellt ausschliesslich eine neue Recorddatei; geschützt sind insbesondere historische Verzeichnisse.

**Bedeutung bleibt zu prüfen:** Der deterministische Check beweist Locator-/Hashintegrität, nicht dass eine Textstelle die Frage fachlich richtig beantwortet. Er erkennt keine beliebigen Widersprüche aus Prosa und erschliesst keine fehlende Absicht. Alle Kriterien können falsch zugeordnet sein, obwohl ihre Locators stimmen. Deshalb bleiben `componentStatus: draft`, `semanticReviewRequired: true`, `targetValidationRequired: true` und `release:false` auch bei Exit 0 bestehen. Ein vollständiger Record macht die Komponente nicht automatisch freigabefähig.

Der Agent stellt echte fachliche Fragen, etwa „Welche Auswahl soll Escape wiederherstellen?“. Technische Gründe wie `SOURCE_BINDING_STALE` oder ein falscher Locator sind zunächst selbst zu bearbeiten. Fragen nach ID bündeln und nach Antworten neu prüfen; eine Frage verschwindet erst, wenn ihre Zuordnung belegt wurde.

## Beispiele und Wiederholung

[Beispieldaten und Ablauf](examples/README.md). Das ist eine neue synthetische Demobibliothek, keine nachträglich geänderte Forschungsdefinition. Sie zeigt Quellenzuordnung und Fragenverwaltung, nicht eine vollständig implementierte Auswahlkomponente.

```sh
PYTHONDONTWRITEBYTECODE=1 tools/validation/.venv/bin/python -m unittest discover \
  -s tools/completeness -p 'test_*.py'
```

Die Suite ist auch in `tools/test.py` eingebunden. Native Designimporte, Code-Rückgewinnung und unabhängige Modellbefolgung wurden durch diese Werkzeugtests nicht nachgewiesen.
