# RD-003 · Rückwege mit sichtbaren Draftlücken

**Entschieden am 6. November 2026 auf Nutzerauftrag.** Bestehende Designs und Code können Ausgangspunkte für das Handbuch sein. Fehlendes Verhalten darf nicht aus einer Darstellung erfunden werden; die Komponente bleibt Draft und offene Entscheidungen werden sichtbar.

## Entscheidung

Ein UI-Contracts-Skill routet bedarfsabhängig zu Design-Rückweg, Code-Rückweg und gemeinsamem Draftcheck. Die führenden vier Domänen bleiben unverändert. Ein eigener Coverage-Record ist eine Arbeits-/Nachweiskonvention, keine neue Quelle für Designwerte oder Verhalten und kein fünfter UI-Standard.

Der deterministische Prüfer arbeitet gegen ein ausdrücklich gewähltes, versioniertes Anforderungsprofil. Stabile Kriterien-IDs werden an aktuelle Quellen und konkrete Locators gebunden. Offene oder konfliktbehaftete Entscheidungen, fehlende/alte Belege und erkannte Platzhalter erzeugen blockierende Fragen. Weder Dateivorhandensein noch Autorennotizen schliessen eine Frage.

Teil-Drafts dürfen in diesem Arbeitsweg fehlende Domänenbindungen auslassen. Der bestehende strengere Komponenten-/Originalschemaweg wird nicht gelockert. Die Ausgaben unterscheiden `DRAFT_INCOMPLETE`, `COVERAGE_RECORDED` und `BLOCKED`. Auch vollständige Zuordnung bleibt Draft mit notwendigem Bedeutungs- und Zielabgleich; kein automatisches Lifecycle-/Release-Upgrade.

## Warum diese Grenze?

Ein deterministischer Locatorprüfer kann nicht entscheiden, ob beliebige Prosa, Code oder eine Designannotation tatsächlich die fachliche Frage beantworten. Beliebige automatische semantische Vollständigkeit wäre eine unbelegte Behauptung. Der Checker weist deshalb Profil-/Bedeutungsprüfung als offen aus. Neue Profile müssen die tatsächlich geforderte Komponentengattung abbilden; ein dekoratives Profil darf nicht interaktive Lücken ausblenden.

Quellenkonflikte entscheidet der Agent nicht nach Reihenfolge, Dateityp oder Mehrheit. Er legt belegte Alternativen vor. Nutzerantworten werden nach Herkunft festgehalten und in führende Contracts übernommen. Bereits im Auftrag autorisierte Übernahmen brauchen keine zusätzliche pauschale Freigabeschleife.

## Umsetzung und Prüfung

[Werkzeug und Beispiele](../../../tools/completeness/README.md) · [neue Rückweg-Anleitungen](../../../skills/ui-contracts/references/reverse.md) · [konkrete Prüfbelege](../analyses/REVERSE-COVERAGE-2026-11-06/README.md).

Synthetische Beispiele und Regressionen prüfen Fragenstatus, Quellintegrität, Aktualisierung und begrenzte Berichtsaussagen. Kein neuer Live-Figma-/Codeimport, kein unabhängiger Modelllauf und keine kausale Beschleunigungsstudie. Historische Definitionen, Studien und Prüferprofile bleiben unverändert.
