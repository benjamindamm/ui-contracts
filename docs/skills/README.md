# Lokaler Agent-Skill · UI Contracts

Stand: 29. Oktober 2026. **`$ui-contracts` ist erstellt, lokal unter `~/.codex/skills/ui-contracts` verfügbar und geprüft.** Die wiederverwendbare Projektquelle liegt unter [skills/ui-contracts/](../../skills/ui-contracts/SKILL.md). Es wurde kein vorhandener fremder Skill überschrieben und nichts veröffentlicht.

Beispielauftrag:

> Nutze $ui-contracts, um eine Disclosure-Komponente als getrennte Contractartefakte zu entwerfen. Prüfe die vorhandenen Originalformate und kennzeichne fehlende semantische oder Laufzeitnachweise ausdrücklich.

## Was der Skill tut

Der Agent erstellt oder bearbeitet Originalartefakte in CEM-JSON, DTCG/CSS, SCXML und HTML/ARIA. Die vier führenden Domänen, eigene Bindungen und offene fachliche Entscheidungen bleiben getrennt. Für tatsächliche Prüfungen nutzt er den mitgelieferten Helper und die vorhandene [Projektprüfkette](../validation/README.md); der Skill enthält keine zweite Kopie der Schemas oder Forschungsdaten.

- Neue/geänderte Contractartefakte: tatsächliche verfügbare Syntax-/Originalschemaprüfungen. Auch ein wohlgeformter neuer Entwurf bleibt ohne passendes Semantik-/Runtimeprofil insgesamt `BLOCKED`, mit separat bestandenen Teilprüfungen.
- Unterstütztes Referenzpaket: ausdrückliche statische Teilprüfung als `PASS_LIMITED`/`release:false` oder gemeinsame Webprüfung mit explizitem aktuellem Browsernachweis.
- Geänderte oder neue Komponenten: keine Übernahme alter Captures oder der festen Referenzfreigabe. Keine Behauptung eines allgemeinen Renderers/Validators.
- Reparaturen: Kandidatendaten dürfen korrigiert werden; notwendige Prüfungen danach erneut ausführen. Kriterien, Originalschemas, Profil und Quellen-/Zeitbindungen dafür nicht abschwächen.

Ein fehlender notwendiger Prüfer oder fehlende erforderliche Abdeckung blockiert die entsprechende Freigabe. Reale IME, Screenreader und Nativeziele bleiben außerhalb des nachgewiesenen Umfangs.

## Quelle und lokaler Bestand

| Datei | Zweck |
| --- | --- |
| [SKILL.md](../../skills/ui-contracts/SKILL.md) | Auswahl, Arbeitsablauf, Grenzen und Ergebnisvertrag |
| [agents/openai.yaml](../../skills/ui-contracts/agents/openai.yaml) | UI-Metadaten und Beispielaufruf; automatische Auswahl bleibt im Standard erlaubt |
| [references/authoring.md](../../skills/ui-contracts/references/authoring.md) | Originalformate, Quellführung und neue/geänderte Artefakte |
| [references/validation.md](../../skills/ui-contracts/references/validation.md) | Reale Prüfeinstiege und Browserablauf |
| [references/reproducibility.md](../../skills/ui-contracts/references/reproducibility.md) | Reproduktions-/Modellvergleich, Provenienz und externe Analyse |
| [scripts/contracts.py](../../skills/ui-contracts/scripts/contracts.py) | Portabler Aufruf mit explizitem `--repo`, strukturierte Prüfung/Blockierung |

Der installierte Bestand entspricht diesen sechs Dateien bytegenau. Ein Repositorypfad ist nicht fest in den Skill eingebaut; der Helper findet das ausgewählte Projekt im Arbeitsverzeichnis oder erhält es ausdrücklich über `--repo`. Abhängigkeiten und Laufzeit liegen weiterhin beim jeweiligen Projekt.

Die lokale Installation ist eine Kopie. Spätere Änderungen der Projektquelle aktualisieren sie nicht automatisch. Vor einem Update Identität und Änderungen prüfen; keinen anderen gleichnamigen Skill ungeprüft überschreiben.

## Tatsächlich geprüft

- `skill-creator/scripts/quick_validate.py` für Projektquelle und lokale Installation: beide bestanden.
- [18 funktionale Fälle](../../tools/skill-tests/ui-contracts/results.json): alle Erwartungen erfüllt. Darunter gültige statische Referenz, noch gültiger aktueller Webnachweis, neue Originalformat-Artefakte ohne fälschliche Gesamtfreigabe, Originalschemafehler, fehlender Prüfer, fehlender/veralteter Browsernachweis und eine statisch gültige Änderung, die die Webreferenzfreigabe nicht übernehmen darf.
- [Reproduzierbarer Funktionstest](../../tools/skill-tests/ui-contracts/test_skill.py): nutzt den installierten Helper von einem anderen Arbeitsverzeichnis aus; Kandidatenkopien werden temporär angelegt und entfernt. Bestehende Originalartefakte bleiben unverändert.
- [Erster Funktionstest](../../tools/skill-tests/ui-contracts/results-initial.json) und [Laufprotokoll](../../tools/skill-tests/ui-contracts/initial.log) bleiben erhalten. Fünf erwartete Diagnosen waren zunächst nur innerhalb der Prüfphasen statt zusätzlich im vereinbarten Ergebnisfeld vorhanden. Die [damalige Helperfassung](../../tools/skill-tests/ui-contracts/helper-initial.py) ist gesichert; der aktuelle Helper ergänzt das oberste Diagnosefeld, ohne Kriterien oder tatsächliche Ablehnungen zu ändern.

Diese Tests prüfen den installierten Helper und seine realen Prüfeinstiege. Sie sind kein unabhängiger Agenten-Forwardtest und keine allgemeine Aussage über Modellqualität. Es wurde kein neuer Browserlauf für die Skillerstellung behauptet: Der positive Webfall prüfte den unveränderten, zum Testzeitpunkt noch gültigen vorhandenen Lauf. Nach dessen Ablauf muss eine aktuelle Prüfung wieder blockieren und ein neuer Browserlauf erfolgen.

[Integrität und Validierungsnachweise](../../tools/skill-tests/ui-contracts/manifest.json). Keine neuen Kandidatenmatrixbedingungen, keine Produktionskomponente und keine Veröffentlichung.

## Aus AC-R02 abgeleitete Reparaturen

Die [externe Analyse](../research/analyses/AC-R02/README.md) zeigt eine falsche Quellauslegung und Prüflücken. [Fehlerregister](ISSUES.md) und [Laufprotokollvertrag](REPRODUCIBILITY.md) halten jede Ursache, aktuelle Gegenmaßnahme, Regression und offene Grenze fest. Die neue Skillreferenz wird nur für diese Arbeitsart geladen. Eine tatsächliche Nutzung des bisherigen Skills durch die historischen Builder ist nicht belegt.

Der [begrenzte native Gegenprüfer](../../tools/design-review/README.md) und der Metadatenprüfer haben eigene Regressionen; sie verändern weder den historischen run-02 noch die feste Webvalidierung. Die ursprünglichen 18 Helper-Testfälle und ihr damaliges Manifest bleiben historische Belege der damaligen Fassung; sie sind kein vollständiger Nachweis für die neuen Reviewfunktionen. Aktuelle Nachweise stehen separat unter [AC-R02 setup-verification.json](../research/analyses/AC-R02/setup-verification.json).
