# RD-002 · Ergebnisprüfung und allgemeine Agentenunterstützung

**Beschlossen · 31. Oktober 2026 · Nutzerpräzisierung zu Paket 4.**

Das Framework soll Agenten im Allgemeinen durch fokussierte Aufträge, gezieltes Nachladen, persistierte Übergaben und überprüfbare Ergebnisse unterstützen. Es kann nicht sicherstellen, dass ein bestimmtes Modell gute Arbeit leistet. Ein erfolgreicher Vergleich mit einem schwächeren Modell ist deshalb **kein hartes Abnahmekriterium für den Frameworkeinsatz**.

Die bisherigen Modell-/Reproduktionsstudien bleiben nützliche Forschungsbelege, aus denen Verbesserungen und Fehlerquellen abgeleitet werden können. Ein neuer gestufter Modellvergleich bleibt optional. Seine fehlende Modellkonfiguration blockiert weder die Weiterentwicklung der Arbeitsmittel noch normale Agentenaufträge. Es wird dafür aktuell kein neuer Modelllauf gestartet und keine Modellrangfolge behauptet.

Harte technische Aussagen bleiben an konkrete Ergebnisse gebunden: stimmen Quellen und Revisionen, ist eine Übergabe vollständig, liegt ein benötigtes Artefakt vor, wurde eine angeführte Prüfung tatsächlich ausgeführt? `HANDOFF_READY` und ein abgeschlossener Ablauf ersetzen keine UI-Abnahme. Fehlende Zielprüfungen bleiben sichtbar.

Modellidentität, Requesttokens und tatsächliche Startkontexte werden nur bei einem entsprechend beauftragten Forschungsnachweis erfasst, soweit verfügbar. Sie werden nicht von jedem Builder als Pflichtaufgabe recherchiert. Für eine später gewünschte **kontrollierte** Modellstudie gelten weiterhin deren wissenschaftliche Vergleichsbedingungen; RD-002 erklärt unvollständige Metadaten nicht nachträglich zu vollständiger Provenienz.

[RD-001](RD-001-STAGED-GENERATION.md) bleibt der historische Entscheid zur gestuften Arbeitsweise. Dessen vorgeschlagener Modellpilot und das [datierte Protokoll](../protocols/STAGED-GENERATION-PILOT.md) werden nicht umgeschrieben oder als ausgeführt markiert. Die allgemeine Konsolidierung nutzt denselben bestehenden Auftrags-/Übergabevertrag; Details stehen im [aktuellen Ablauf](../../../tools/ux/WORKFLOW.md).

## Vorrang der Informationsarchitektur

Die Nutzerpräzisierung priorisiert die **umgekehrte Pyramide**: Wichtigstes und Handlungsrelevantes zuerst, Erläuterungen und Belege darunter. Wiederverwendbare Handlungsregeln führen im Skill; Details bleiben über gezielte Verweise erreichbar und werden nur nach Bedarf oder auf Nutzerwunsch geladen. Teilaufgaben dürfen getrennt arbeiten. Ein abschließender Abdeckungsplan prüft die betroffenen Originalregeln und Querverbindungen schrittweise wieder gemeinsam. Dieser Ausbau ist wichtiger als eine Optimierung auf ein bestimmtes Modell. Lesetiefe und Quellvorrang sind getrennt: Originalquellen bleiben auch dann führend, wenn sie erst später gelesen werden.
