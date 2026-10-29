# Einstiege verschiedener Agentenprogramme

29. Oktober 2026. Ergänzung zum [Kontextaudit](README.md). **Die Agentenlaufzeit bestimmt das Laden von Dateien; der Modellname allein bestimmt es nicht.** Ein Open-Source-Modell kann durch unterschiedliche Programme mit ganz anderem Startkontext aufgerufen werden.

## Gemeinsamer Einstieg und dünne Wegweiser

| Datei / Laufzeit | Vorgehen im Repository | Beleg / Grenze |
| --- | --- | --- |
| [AGENTS.md](../../../../AGENTS.md) | Gemeinsame kurze Regeln, konkreter Auftrag, Rolle und gezielte Verweise | Für entsprechende Hosts; keine vollständige Skill- oder Forschungskopie. OpenCode dokumentiert AGENTS.md als Projektregeln. [Offizielle OpenCode-Regeln](https://opencode.ai/docs/rules/) |
| [CLAUDE.md](../../../../CLAUDE.md) | Kurzer Wegweiser zur gemeinsamen AGENTS.md; bereits geladenen Text nicht erneut laden | Claude Code dokumentiert CLAUDE.md, zusätzliche Regeln und automatische Erinnerungen. Seine AGENTS-Unterstützung hängt auch von Version und anderen Instruktionsdateien ab; kein identisches Verhalten aller Installationen voraussetzen. [Offizielle Claude-Dokumentation](https://code.claude.com/docs/en/memory) |
| [GEMINI.md](../../../../GEMINI.md) | Derselbe kleine Wegweiser | Gemini CLI dokumentiert globale, Workspace- und später geladene Instruktionen; Dateinamen konfigurierbar. [Offizielle Gemini-Dokumentation](https://geminicli.com/docs/cli/gemini-md/) |
| Andere Hosts / Modelle | Gemeinsamen Einstieg explizit in der Laufkonfiguration referenzieren, falls deren Instruktionsmechanismus ihn nicht selbst lädt | Keine unbekannte Laufzeit durch einen zusätzlichen Fantasiedateinamen als unterstützt deklarieren. Erst dokumentierten Mechanismus und tatsächliche Startladung prüfen. |

Die Wegweiser verwenden normale Markdownverweise, keine automatischen Dateiimporte. Damit ziehen sie nicht vorsorglich den Skill, Forschungsindex oder sämtliche Quellen in den Startkontext. Sie bleiben bewusst klein; die gemeinsame Regeldatei bleibt führend. Ein Agent, der AGENTS.md schon erhalten hat, muss sie nicht nochmals lesen.

## Vor jedem neuen Vergleichslauf feststellen

1. Agentenprogramm und Version **getrennt von Modell/Provider** notieren; Startverzeichnis und Konfigurationsprofil festhalten.
2. Tatsächlich geladene Projekt-, Eltern-, globale und verwaltete Instruktionsdateien sowie automatische Erinnerungen auflisten. Relevante lokale Dateien mit Revision/Hash binden; keine geheimen Konfigurationswerte in Studien kopieren.
3. Dateiimporte, breite Instruktionsglobs, globale Regeln, zusätzliche Workspaces, vorab eingefügte Verzeichnisbäume und aktivierte Skills prüfen. Kein pauschales Ausschalten bestehender Nutzervorgaben und keine globale Konfiguration ohne Auftrag ändern.
4. Vorhandene Speicher-/Kontextanzeige oder Debugdaten der jeweiligen Laufzeit nutzen. Gemini CLI dokumentiert beispielsweise `/memory show`; bei anderen Hosts deren aktuelle Möglichkeit prüfen. Falls Rohrequestdaten nicht verfügbar sind, bleibt die Gesamtgröße ausdrücklich unbekannt.
5. Frische Worker ohne Elternhistorie starten; Memory-Inhalte und Fortsetzungen als Versuchsbedingungen behandeln. Repozugriff ist keine automatische Kontextladung, und ein frischer Gesprächsverlauf ist kein vollständig leerer Systemkontext.
6. Das geladene Initialset und später nachgeladene Dateien getrennt protokollieren. Technische Probe und reale Studiengeneration getrennt ausweisen. Bei einer Blindprüfung dürfen frühere Builds/Reports nicht über Erinnerungen oder globale Anweisungen einfließen.

## Nachweisstatus

Die drei Repositoryeinstiege wurden ergänzt und statisch auf Größe, vorhandene Verweisziele und fehlende automatische Imports geprüft. [Maschinenlesbare Prüfung](../../../../tools/skill-tests/ui-contracts/entrypoints-verification.json).

Es wurden **keine Claude-, Gemini- oder OpenCode-Sessions gestartet**. Deren globale Konfiguration und automatische Erinnerungen wurden weder gelesen noch verändert. Tatsächliche Erkennung, zusätzliche Tool-/Systemtexte und Requesttokens müssen deshalb für jeden konkreten Host vor dem nächsten Pilot noch gemessen werden. Dokumentierte Ladewege ersetzen diesen Laufzeitnachweis nicht.
