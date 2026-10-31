# UX-Eignung aus der gewählten Bibliothek

Nur bei Komponentenwahl oder UX-Definition laden. Die Bibliothek steht ausdrücklich im Auftrag; Beispielpolicy und Forschungskandidaten sind keine impliziten Vorgaben für andere Bibliotheken.

1. In `library.json` die optionale `selection`-Bindung und nur relevante Komponenten verfolgen. `component.json` verweist mit `ux` auf deren Fähigkeitsprofil.
2. Führenden Wertevertrag klären: vorhandener Schlüssel oder freier Text, separate Suche oder editierbares Wertelabel. Unbekannte Fakten nicht als false behandeln. Bei entscheidenden Lücken gezielt nachfragen.
3. Für einen nachweisgestützten Vorschlag `tools/ux/check.py` bzw. `tools/ux/choose.py` im gefundenen Repository mit dessen Projektlaufzeit ausführen. Die operative Anleitung im ausgewählten Repository unter `tools/ux/README.md` nur nach Bedarf laden. Der Skill besitzt keine zweite Fähigkeits- oder Policykopie.
4. `declared`/`unverified` sind keine harte Erfüllung. `verified-limited` bezeichnet aktuelle Quellstruktur und native Contractfälle, keine abgenommene Browserimplementierung. Ein widersprüchlicher Claim stoppt die Empfehlung; kein altes Pass-Receipt übernehmen.
5. Die Ausgabe mit tatsächlichen Kontextfakten, Policybezug, Einschränkungen und notwendigen Zielprüfungen begründen. Keine optimale UX oder universelle Optionsanzahl aus einem Projektprofil ableiten.

Das aktive example-Profil enthält Select, Select mit separater Suche und die vorhandene Autocomplete-Variante. Freie Adress-Schreibhilfe ist ein eigener noch nicht implementierter Vertrag: fehlende Vorschläge eines Kartendienstes allein beweisen keine ungültige Adresse. Die konkrete Definition führt, nicht der allgemeine Controlname.

Die Projektlaufzeit lässt sich mit `python3 tools/setup.py` einrichten (JDK 17+, Node 22+ als Voraussetzungen). Für die unterstützten vier Profile führt der aktuelle Webweg über `tools/web/README.md` im gewählten Repository; nur bei tatsächlicher Targetprüfung laden. `python3 tools/test.py --browser-run LAUF --out NEUER_ORDNER` verbindet Regressionen und quellengebundene Browserabnahme. Fehlender Browserbeleg bleibt blockiert; `--unit-only` ist ein ausdrücklich kleinerer Prüfumfang. Der historische Helper-validate-Pfad bleibt ein separates Referenzprofil.
