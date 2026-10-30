# AC-UX-01 · Autocomplete mit formal auswertbaren UX-Regeln

**Separate Forschungskandidatenrevision, keine Änderung der example-Bibliothek.** Stand: 30. Oktober 2026. DMN/FEEL führt die Bedingungen aus; ein begrenztes eigenes Profil bindet Regeln an die vorhandene Komponente, Revision und Quellen. Kein neuer universeller UX-Standard und keine allgemeine produktive Integration.

**43/43 Prüf-Erwartungen erfüllt:** elf Kontextauswertungen mit nativem Zeilentrace, 17 vorgelagerte Bindungs-/Metadatengegenfälle und zusätzliche Ergebnisinvarianten. [Checks](results/checks.json) · [Originalantworten](results/observations.json) · [Gegenfälle](results/negative-observations.json) · [Zusammenfassung](results/summary.json).

## Was diese Komponente aus UX-Sicht ausmacht

| Regel | Bedeutung | Verbindlichkeit im Kandidaten | Führende Belege |
| --- | --- | --- | --- |
| AC-UX-001 | Die Aufgabe darf nicht verlangen, dass dieses Control einen neuen, nicht in den Ergebnissen vorhandenen Wert bestätigt. | Fähigkeitsgrenze; nicht durch eine UX-Ausnahme übersteuerbar. | Bestehende Komponentenbeschreibung, CEM und SCXML; kein neues Verhalten eingeführt. |
| AC-UX-002 | Die Aufgabe darf nicht verlangen, mit derselben Instanz mehrere Einträge zusammen zu bestätigen. | Fähigkeitsgrenze; nicht übersteuerbar. | Ein gebundener bestätigter String-Key in der CEM-Signatur. |
| AC-UX-003 | Ergebnisbezeichnungen sollen für die vorgesehenen Nutzer im jeweiligen Kontext verständlich und vertraut sein. | Vorgeschlagene Empfehlung mit begründbarer, eng gebundener Ausnahme. | Eigene Übertragung der USWDS-Empfehlung; vorhandene Option-Label-Bindung. Keine neue WAI-ARIA-Pflicht. |

Die ersten beiden Regeln beschreiben Grenzen **dieser** Variante. Andere Autocomplete-Komponenten können freie Werte oder Mehrfachauswahl unterstützen. Eine zusätzliche Komponente zur Neuanlage wäre eine eigene Komposition und wird hier nicht ausgeschlossen oder erzeugt.

Die dritte Regel ist eine dokumentierte Empfehlung, keine automatisch bewiesene Eigenschaft jedes Labels. Ob Nutzer die Begriffe tatsächlich verstehen, erfordert menschliche Beurteilung oder Forschung. Es wird weder ein Schwellenwert für die Optionsanzahl noch eine generelle Empfehlung zur Verwendung von Comboboxen übernommen. Bekannte Einschränkungen einer fremden Implementierung sind nicht pauschal auf unsere Variante übertragen.

## Aufbau und Lesereihenfolge

1. [ux-profile.json](candidate/ux-profile.json): Bibliotheks-/Komponenten-/Revisionsbindung, Regel-IDs, Stärke und Belegverweise.
2. [context-vocabulary.json](candidate/context-vocabulary.json): Bedeutung, Typ und Herkunft der drei benötigten Fakten. Nur relevante Fakten bereitstellen.
3. [autocomplete-ux.dmn](candidate/autocomplete-ux.dmn): tatsächliche Bedingungen, Verzweigungen und Zusammensetzung in DMN/FEEL.
4. [sources.json](candidate/sources.json): lokale Quellen mit Hash/Ankern und attribuierte externe Empfehlung.
5. [Beispielkontext](contexts/existing-single.json) und [Erwartungen](expected.json).

`profile.schema.json` ist ein eigenes begrenztes Metadatenschema. Es beweist keine DMN-Semantik. Zweck, Begründung, Vokabularerläuterungen und exceptionPolicy sind erklärender Text, den die Engine **nicht** als Regeln interpretiert. Ausführbare Bedingungen stehen im DMN; Referenzprüfung, Fakten-/Provenienzstruktur und erlaubte Ausnahmen werden im eigenen Adapter explizit geprüft. Der Adapter ist auf diese drei Regeln und dieses Kandidatenprofil begrenzt, kein generischer Resolver beliebiger Komponenten.

## Konkrete Ergebnisse

| Kontext | Gesamtergebnis |
| --- | --- |
| Vorhandenen Eintrag einzeln wählen; Labels beurteilt vertraut | compatible |
| Neue Werte unmittelbar mit diesem Control bestätigen müssen | incompatible |
| Mehrere Einträge zusammen auswählen müssen | incompatible |
| Ergebnislabels als unvertraut beurteilt | compatible-with-guidance |
| Notwendige Information zur Wertneuanlage fehlt | undetermined |
| Nur die Beurteilung der Labels fehlt | compatible-guidance-unknown |
| Boolean als Text oder unbekannte Kardinalität geliefert | invalid-input |
| Erklärte Ausnahme nur für die Empfehlung, mit passender Bindung | compatible; Empfehlung bleibt als excepted sichtbar |
| Ausnahme soll eine fehlende Fähigkeit erlauben | BLOCKED vor Engineaufruf |

`compatible` bedeutet ausschließlich: kein Widerspruch zu diesen geprüften Fähigkeitsgrenzen; es ist weder „beste Komponente“ noch eine UX-/Accessibility-/Produktfreigabe. Alle drei Einzelergebnisse bleiben erhalten. Die Aggregation gibt invalid-input Vorrang; bekannte Unvereinbarkeit folgt vor unbestimmter Pflicht. Unbekannte Empfehlung wird nicht wie eine unbekannte Fähigkeitsvoraussetzung behandelt.

## Native Nachverfolgung und Integrität

Die Java-Bridge liest die tatsächlich vom DMN-Evaluator gemeldeten matchedRules und ihre row IDs aus. Der Adapter ordnet diese IDs den gebundenen Regel-/Belegdaten zu und prüft ihre Übereinstimmung mit dem nativen Ergebnis. Er wertet Bedingungen nicht nochmals selbst aus, um einen vermeintlichen Trace zu erfinden. Es wird genau eine passende Zeile je Regel verlangt.

Vor Aufruf: ausgewählte Bibliothek, Index-/Komponentenidentität, Originalrevision, alle 28 Baseline-Dateihashes, Quellenanker, Metadatenschema und Original-DMN-XSD prüfen. Fehlende/widersprüchliche Row-Mappings, veränderte Dateien und unerlaubte Ausnahmen blockieren vor der nativen Auswertung. Die beiden negativen Quellenvarianten in candidate/negative sind absichtlich ungültige Testeingaben, keine Alternativdefinitionen.

Die Fakten und die behauptete Ausnahmeentscheidung werden nicht als sachlich wahr oder kryptographisch autorisiert geprüft. Der erlaubte Reviewer research-author dient nur der kontrollierten Testpolicy. Die abgelegte Ausnahme ist eine deklarierte Szenarioannahme, keine echte Produktfreigabe. Ein reales Handbuch braucht einen eigenen Entscheidungs-/Freigabeprozess.

## Lokal ausführen

Mit der bereits erfassten DMN-Runtime aus [Lauf 03](../../runs/03/README.md) und jsonschema 4.25.1/lxml 6.0.2 der bestehenden lokalen Validierungsumgebung:

```sh
mkdir -p /tmp/ui-contracts-ux-rules-runtime/classes-ux
javac -cp "$(cat /tmp/ui-contracts-ux-rules-runtime/classpath.txt)" \
  -d /tmp/ui-contracts-ux-rules-runtime/classes-ux \
  docs/research/studies/UX-RULES-01/pilots/AC-UX-01/UxAuditProbe.java

tools/validation/.venv/bin/python \
  docs/research/studies/UX-RULES-01/pilots/AC-UX-01/evaluate.py \
  docs/research/studies/UX-RULES-01/pilots/AC-UX-01/contexts/existing-single.json
```

Der konkrete Harness enthält den lokalen Java-Pfad des geprüften Macs. Eine andere Umgebung benötigt eine neue dokumentierte Harnessrevision und passende Runtime, keine Änderung alter Messdaten. Der Metadatengate nutzt jsonschema, der DMN-Gate unveränderte Original-XSDs; die eigentliche Semantik läuft in DMN Scala 1.12.6. evaluate.py gibt BLOCKED mit Exitcode 2 zurück; ein auswertbares incompatible oder invalid-input ist ein fachliches Ergebnis mit Exitcode 0. Immer das Ergebnis lesen, nicht nur den Prozessstatus.

Die gesamte Probe über probe.py nur mit einem neuen Ergebnisstand wiederholen: results wird exklusiv angelegt. Vor Messbeginn sind Kandidatendateien, Kontexte, Erwartungswerte und Harness im Freeze gebunden. Explorative Vorbereitung und ein korrigierter eigener Schemafehler stehen in preflight.json; keine Blindstudie. Historische Probeordner und Definitionen nicht überschreiben.

## Grenzen und nächste Verwendung

Keine neue UI erzeugt, kein Agent gestartet und keine Kontextverständnisprobe behauptet. Noch keine automatische UX-Faktengewinnung, keine universelle Semantik aller Handbuchregeln, keine vollständige Lizenz-/Security-/DMN-Konformitätsprüfung. Die bestehende Bibliothek und installierte Skills bleiben unverändert. Dieser Kandidat zeigt, wie Regeln konkret pro Komponente formal auswertbar und nachverfolgbar werden können. Eine spätere Übernahme benötigt einen eigenen Entscheid und weitere Komponentenfälle.

[Integritätsnachweis dieses Piloten](verification.json). In results/runtime.json wird inheritedJarManifest.path relativ zu diesem Pilotordner aufgelöst. Ältere Forschungsreceipts bleiben Belege ihrer jeweiligen damaligen Dokumentfassung.
