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
| [references/workflow.md](../../skills/ui-contracts/references/workflow.md) | Kontextauswahl, Abhängigkeiten und fokussierte Rollen |
| [references/handoff-contract.md](../../skills/ui-contracts/references/handoff-contract.md) | Gemeinsames versioniertes Auftrags-/Übergabeformat |
| [Rollen-Karten](../../skills/ui-contracts/references/roles/coordinator.md) | Koordination, Quellenzuordnung, Builder, Reviewer und Reparatur; aus workflow.md einzeln erschlossen |
| [assets/handoffs/task.json](../../skills/ui-contracts/assets/handoffs/task.json), [handoff.json](../../skills/ui-contracts/assets/handoffs/handoff.json) | Auszufüllende Vorlagen für Arbeitsaufträge und Lieferungen |
| [scripts/handoffs.py](../../skills/ui-contracts/scripts/handoffs.py) | Integritätsprüfung und kleines rollenbezogenes Kontextpaket; kein Agentenstart und keine Komponentenfreigabe |
| [scripts/contracts.py](../../skills/ui-contracts/scripts/contracts.py) | Portabler Aufruf mit explizitem `--repo`, strukturierte Prüfung/Blockierung |

Der installierte Bestand entspricht der versionierten Skillquelle bytegenau; der aktuelle [Workflow-Nachweis](../../tools/skill-tests/ui-contracts/workflow-verification.json) listet die Dateihashes. Ein Repositorypfad ist nicht fest in den Skill eingebaut; die Helper erhalten das Projekt ausdrücklich über `--repo` oder finden es wie dokumentiert im Arbeitsverzeichnis. Abhängigkeiten und Laufzeit liegen weiterhin beim jeweiligen Projekt.

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

## Fokussierte Rollen und Kontextmanagement

Das eigentliche Entwicklungsziel aus [RD-001](../research/decisions/RD-001-STAGED-GENERATION.md) sind bessere Skills, nicht bloß weitere Wiederholungsläufe. Neue Rollen-Karten begrenzen fachlichen Auftrag und Kontext; ein gemeinsamer [Übergabevertrag](../../skills/ui-contracts/references/handoff-contract.md) hält die benötigten Ergebnisse separat und quellengebunden fest. Unabhängige Aufgaben dürfen parallel laufen, Verbraucher warten auf gültige benötigte Lieferungen. Prüfer sehen Buildererklärungen erst nach ihrer eingefrorenen Erstbewertung.

Der neue Helper erzeugt nur Kontextdateien und Prüfberichte. Er startet keine Agenten, kontrolliert keinen Browser und erweitert keine Berechtigungen. Struktur-/Hashprüfungen verhindern versehentliche falsche Übergaben; sie beweisen keine sachliche Richtigkeit oder technische Abschottung.

[32 funktionale Übergabetests](../../tools/skill-tests/ui-contracts/results-handoffs.json) prüfen die lokale Installation anhand temporärer Repositories und echter Dateien: gezielte Claimauswahl mit Quellverweisen, veraltete Abhängigkeiten, fehlende Belege, Status-/Freigabetrennung, Reviewerphasen, Kontextgrenzen und geschützte Eingaben. Das ist **kein** empirischer Nachweis, dass ein schwächeres Modell die Rollen bereits zuverlässig nutzt. Diesen Verhaltenseffekt soll der vorbereitete Pilot erst untersuchen. Originalbelege und damalige Testergebnisse bleiben erhalten.

## Schlanker Einstieg und Kontexthygiene

[Separater Kontextaudit](../research/analyses/INITIAL-CONTEXT/README.md): neue Rollen starten mit `bootstrap` (nur hashgebundene Auftrags-/Rollenverweise); das erweiterte `context` wird erst bei Bedarf geladen. Originale und Nachweise bleiben erreichbar. Kein pauschales Einlesen aller verlinkten Dateien. Die Anfangsgröße des gesamten Modellrequests ist damit noch nicht gemessen.

Aktueller zusätzlicher Nachweis: [37 Funktionstests Quelle](../../tools/skill-tests/ui-contracts/results-bootstrap-source.json) und [Installation](../../tools/skill-tests/ui-contracts/results-bootstrap-installed.json). Frühere 32-Test-Receipts und Workflow-Verifikation dokumentieren den Stand vor diesem Kontextaudit.

## Mehrere Bibliotheken

Bibliotheken liegen unter `libraries/<id>/`; die frühere Draftbibliothek heißt jetzt `example`. Jeder Autorenauftrag wählt seine Bibliothek explizit. [Leere Bibliothek anlegen, auswählen und historische Pfade einordnen](../../libraries/README.md). `inspect --library ID` unterstützt die begrenzte Originalformatprüfung; keine allgemeine semantische Bibliotheksfreigabe.

## Einheitliches Vorschau-Layout

Für unterstützte native Zustandsübersichten das [gemeinsame Präsentationswerkzeug](OPENPENCIL-PREVIEW.md) verwenden, statt Seitengestaltung pro Agent neu zu erfinden. Die finale Komponenten-FIG und `preview.png` liegen gemeinsam im normalen Ergebnisordner; kein separater presentation-Bereich. Keine historische Lieferung überschreiben. Der Helper setzt Originalgruppen unverändert in Karten und prüft dies per Readback.

## Berechnete Formen und Charts

Die [Geometriehilfe für Builder](../../skills/ui-contracts/references/geometry.md) trennt native Grundformen von berechneten Pfaden. Für Pie-Sektoren steht [D3-Shape als gezieltes Werkzeug](../../tools/charts/README.md) bereit; Gestaltung und Legende bleiben frei. Weitere Chartfamilien benötigen eigene Adapter und Nachweise. Die Anleitung wird nur bei passender Aufgabe nachgeladen.
