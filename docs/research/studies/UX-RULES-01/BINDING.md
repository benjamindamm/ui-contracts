# Bindungsprobe · Anforderungen, kein beschlossenes Format

Ausgewählte reale Referenzbibliothek: **example**. Aktuelle Pfade liegen unter `libraries/example/components/`; der Baseline-Snapshot steht in baseline.json. Die Bibliotheksquellen werden nur gelesen. Die vorhandenen Bindungen in component.json sind selbst Projektentwürfe, keine externen Standards.

## Was eindeutig sein muss

Eine UX-Aussage benötigt mindestens die gewählte Bibliotheksidentität, Komponentenidentität und die gebundene Revision/Hashes. Ein genauer Anker ergänzt Originaldatei und deren vorhandene Zielidentität: z. B. eine JSON-Stelle im CEM, ein Tokenpfad, eine SCXML-Zustands-ID oder eine HTML-/Accessibility-Regel. Dateipfad und URI allein garantieren keine semantisch passende Bindung. Die Ankerkonvention und ein etwaiger Resolver sind gesondert als eigene Integrationsleistung auszuweisen.

| Referenzziel | Vorhandener Ausgangspunkt | Zu prüfende Bindung |
| --- | --- | --- |
| Komponente | library.json → components["Autocomplete"] → components/autocomplete/component.json mit id ui-contracts:Autocomplete | Index-/Komponenten-ID stimmen überein; Bibliothek und Revision sind eindeutig. |
| Interface | components/autocomplete/interface.json | Original-CEM-Ziel mit Typ und Existenz prüfen, keine zusätzliche Property erfinden. |
| Visual | tokens.json und components/autocomplete/layout.css | Token oder Regelziel einschließlich Einheit/Typ erhalten; UX-Empfehlung ist keine alternative Farbdefinition. |
| Behavior | components/autocomplete/behavior.scxml | Zustands-/Übergangsbezug aus derselben Version; Verhalten bleibt hier führend. |
| Accessibility | components/autocomplete/accessibility.html und accessibility.rules.json | HTML-/Projektionsregel gezielt referenzieren; keine neue ARIA-Norm behaupten. |

Variante und Teil sind nur dann bindbar, wenn der betreffende Contract sie tatsächlich identifiziert. Kein freies Wort wie „dark“ als aufgelösten Variantenanker ausgeben. Bibliotheksweite Regelwiederverwendung ebenso separat testen, nicht als automatische Vererbung voraussetzen.

## Geplante Gegenfälle

Gleiche Komponenten-ID in zwei Bibliotheken; richtige ID bei falscher Revision; entfernte JSON-Stelle; fehlende SCXML-ID; falscher Zieltyp; umgezogene Datei mit und ohne bewusst neu gebundene Revision. Weder latest noch die eingefrorene example-v1 darf als stiller Ersatz für die aktuelle Library einspringen.

## Denkbare Ablage nach der Forschung

UX-Regeln könnten später bei `libraries/<id>/components/<name>/` liegen, gemeinsame Regeln am Bibliotheksroot. Der konkrete Dateiname, Originalsyntax, Indexeintrag und Adapter hängen von der Auswahl ab. Hier wird kein ux.yaml, kein neues Pflichtfeld in component.json und keine fünfte konkurrierende Contractdomäne eingeführt.

## Inzwischen erbrachte Teilprobe

Lauf 01 prüft eigene Referenzgates für alle vier Originaldomänen; [Lauf 03](runs/03/README.md) kombiniert den positiven Gate mit nativem DMN und blockiert eine falsche Revision vor dem Engineaufruf. Damit ist ein begrenzter eigener Integrationsweg erprobt, kein nativer Resolver der Frameworks. Die allgemeine Ankerkonvention und ein produktives Bindungsformat bleiben unbeschlossen.
