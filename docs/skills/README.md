# Mit dem UI-Contracts-Skill arbeiten

**Beschreibe die Aufgabe. Der Skill führt den Agenten zu den passenden Regeln und Werkzeugen.** Diese Seite hilft beim Einstieg; sie ist keine zusätzliche Pflichtlektüre für bereits beauftragte Worker.

## In drei Schritten starten

1. **Projekt öffnen:** Der Agent braucht Zugriff auf dieses Repository und die gewählte Bibliothek.
2. **Skill bereitstellen:** Die versionierte Quelle liegt unter [skills/ui-contracts/](../../skills/ui-contracts/SKILL.md). Unterstützt dein Agent lokale Skills, richte diesen Ordner über dessen Skillverwaltung ein. Alternativ beauftrage ihn ausdrücklich, die Projektdatei `skills/ui-contracts/SKILL.md` als Einstieg zu lesen. Das ist ein manueller Arbeitsweg, keine automatische Skillregistrierung.
3. **Auftrag geben:** Bibliothek, fachliche Anforderung und gewünschtes Ergebnis nennen. Eine neue Bibliothek zuerst [anlegen](../../libraries/README.md); sie beginnt leer.

> **Beispielauftrag**
>
> Nutze den UI-Contracts-Skill und ausdrücklich die Bibliothek `example`. Wähle geeignete Komponenten für ein Telefonnummernformular mit drei festen Ländervorwahlen. Erstelle zuerst einen Designentwurf. Halte offene Regeln und tatsächlich ausgeführte Prüfungen fest.

**Erwartetes Ergebnis:** Ein quellengebundener Entwurf mit nachvollziehbarer Komponentenwahl, offenen Fragen und ausgewiesener Prüfung. Der Skill führt durch die Arbeit; eine vollständig richtige Ausgabe ist dadurch nicht garantiert.

## Nur den passenden Arbeitsweg laden

Der Skill bündelt Schnittstelle, Gestaltung, Verhalten und Barrierefreiheit. UX-Eignung unterstützt die Komponentenwahl. Ein Worker mit Rollenauftrag beginnt stattdessen mit seiner Taskdatei und Rollenkarte; Detailquellen folgen nach Bedarf.

| Bedarf | Nur diesen Einstieg laden |
| --- | --- |
| Originaldefinition ändern | [Autorenarbeit](../../skills/ui-contracts/references/authoring.md) |
| Komponentenwahl | [UX](../../skills/ui-contracts/references/ux.md) |
| Aufgaben zerlegen und übergeben | [Workflow](../../skills/ui-contracts/references/workflow.md) |
| Abschließend zusammenführen | [Gesamtabgleich](../../skills/ui-contracts/references/integration-review.md) |
| Passenden Zielprüfer wählen | [Validierung](../../skills/ui-contracts/references/validation.md) |
| Fehler wiedererkennen | [Fehlerregister](ISSUES.md), dann gezielt dessen Beleg |
| Explizite Forschungs-/Reproduktionsfrage | [Forschungsvertrag](REPRODUCIBILITY.md) und [datierte Nachweise](../research/DOCUMENT-INDEX.md) |

Die Helper prüfen begrenzte Quellen, Struktur und Bindungen. Ein `HANDOFF_READY` oder abgeschlossener Ablauf garantiert weder gute Modellarbeit noch eine freigegebene UI. Nur tatsächliche zielgerechte Prüfungen werden als Nachweis ausgegeben.

[Aktuelle Kontext-/Workflowprüfung](../research/analyses/AGENT-WORKFLOW-2026-10-31/README.md) · [Werkzeuggrenzen](../STATUS.md). Bei lokaler Installation (etwa `~/.codex/skills/ui-contracts`) wird die Kopie nur nach geprüftem Vergleich mit der Projektquelle aktualisiert; andere gleichnamige Bestände nicht überschreiben.

Für OpenPencil bei Bedarf [Vorschau](OPENPENCIL-PREVIEW.md) und [Geometriehilfe](../../skills/ui-contracts/references/geometry.md) laden. Frühere Anleitungen und Teststände sind vollständig in [HISTORY.md](HISTORY.md) erhalten; sie sind keine Pflichtlektüre zum Einstieg.
