---
name: ui-contracts
description: UI-Komponenten als CEM-, DTCG/CSS-, SCXML- und HTML/ARIA-Contracts erstellen, bearbeiten und begrenzt prüfen; auch für UX-Eignung und Komponentenwahl anhand einer ausdrücklich gewählten Contractbibliothek. Nicht für beliebige App-Implementierung oder allgemeine Konformitätszertifizierung.
---

# UI Contracts · Handlungsregeln

1. **Auftrag eingrenzen:** Repository, Bibliotheks-ID (`libraries/<id>`), Komponente und Ziel ausdrücklich bestimmen. Kein implizites example und keine Freigabe aus einer anderen Bibliothek übernehmen.
2. **Gezielt lesen:** Bei Rollenauftrag nur Task und eigene Rollenkarte unter `references/roles/` zuerst. Sonst unten den passenden Einstieg wählen. Verweise sind Nachlademöglichkeiten; Forschung, andere Rollen und fremde Versuche nicht vorsorglich einlesen. Technisch erreichbares Wissen muss nicht im Startkontext stehen.
3. **Originalquellen führen:** CEM, DTCG/CSS, SCXML und HTML/ARIA getrennt halten. Quellenregeln, Ableitungen, Annahmen und Beobachtungen unterscheiden. Identitäten, Teile, Zustände, Typen und Einheiten über Grenzen erhalten.
4. **In prüfbaren Schritten arbeiten:** Nötige Vorgängerartefakte mit Pfad/Hash übergeben, Details auf Datenträger halten. Unabhängige Teilaufgaben erst nach geklärten Abhängigkeiten bearbeiten; abhängige Schritte bei Konflikten blockieren. Kein Auftrag zu zusätzlichen Agenten entsteht allein durch den Skill.
5. **Zum Schluss integrieren:** Ergebnis gegen betroffene Originalquellen, Fachanforderungen und Verbindungen prüfen; Teil-Pässe nicht zum Gesamt-Pass addieren. Dafür [Gesamtabgleich](references/integration-review.md) gezielt laden. Fehlende Prüfungen sichtbar lassen.
6. **Begrenzt berichten:** Nur tatsächlich ausgeführte Prüfungen nennen. `HANDOFF_READY` ist keine UI-Freigabe; statisches Design beweist keine Webbedienung. Kein Versprechen guter Modellarbeit oder allgemeiner Konformität. Modellmetadaten sind für normale Aufgaben keine Pflicht.
7. **Nachweise bewahren:** Historische Quellen/Läufe unverändert halten; neue Revisionen getrennt ablegen. Neue Fehler mit Beleg, Ursache, Reparatur und Regression in `docs/skills/ISSUES.md` dokumentieren. Commit, Push und Veröffentlichung brauchen Nutzerauftrag.

## Nur den benötigten Einstieg laden

- Originalartefakte erstellen/ändern: [Autorenarbeit](references/authoring.md).
- Konkrete Prüfung oder Reparatur: [Prüfwege und Grenzen](references/validation.md); Helper `scripts/contracts.py`, `--repo` ausdrücklich.
- UX-Eignung oder Komponentenwahl: [UX](references/ux.md).
- Berechnete Kurven/Chartformen: [Geometriehilfe](references/geometry.md); Grundformen nativ.
- Mehrstufigen Ablauf planen: [Workflow](references/workflow.md). Zugewiesene Worker laden stattdessen nur ihre dort verlinkte Rollenkarte.
- Expliziter Reproduktions-/Forschungsauftrag: [Reproduktion](references/reproducibility.md). Historische Ergebnisse von außen prüfen.
