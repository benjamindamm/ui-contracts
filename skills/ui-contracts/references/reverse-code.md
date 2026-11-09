# Code → Contracts

Nur bei Codeeingaben laden; gemeinsamer Ablauf in [Rückwege](reverse.md).

1. Codebase, Revision, Komponente und relevante Abhängigkeiten eingrenzen. Öffentliche API, Styles/Tokens, Zustandslogik, Eventerzeugung, Templates und vorhandene Tests gezielt verfolgen. Nicht vorsorglich das ganze Repository oder gebaute Bundles einlesen.
2. API/Typen/Events nach CEM, visuelle Regeln nach DTCG/CSS, Verhalten nach SCXML und Semantik nach HTML/ARIA zuordnen. Präzise Datei-/Symbol-/Zeilenbezüge festhalten; Frameworksyntax ist keine direkte SCXML- oder CEM-Gleichwertigkeit.
3. Deklaration, erreichbaren Codepfad und tatsächliche Ausführung unterscheiden. Ein Handler beweist nicht, dass Fokus/Events zur Laufzeit wie beabsichtigt funktionieren. Bei ausführbarer Zielumgebung gezielte Gegenfälle nutzen; fehlende Runtime wird als ungeprüft ausgewiesen. Produktivsysteme und fremde Daten nicht ohne passenden Auftrag verändern.
4. Bestehendes Verhalten ist zunächst Beobachtung, nicht automatisch gewünschte UX. Widersprüche zum Handbuch, Tests und Design getrennt dokumentieren. Implizite Defaults und Framework-/Browserverhalten als solche benennen. Abwesende Fehlerbehandlung nicht still als fachlich gewollte Regel übernehmen.
5. Vom Nutzerauftrag gedeckte Entscheidungen in die führenden Quellen übernehmen, unbekannte Absichten im [Vollständigkeitsbericht](completeness.md) offen lassen. Bei Änderungen abhängige Komposition, gemeinsame Tokens und bestehende Zielprüfungen verfolgen. Erst nach aktuellen Quellen-/Laufzeitbelegen entsprechende Ergebnisbehauptungen machen.
