# Accessibility-Zielbeziehungen: Originalprüfer und zusätzliches Instanzprofil

Stand: 25. Oktober 2026. Zehn statische HTML-Fälle mit zwei Combobox-/Listbox-Instanzen, je einmal gegen axe-core und ein ausdrücklich zusätzliches Instanzprofil geprüft. 20 benannte Fall-/Prüferbedingungen. Keine Autocomplete-Komponente implementiert, kein Tastatur-/Fokusablauf und keine Assistenztechnik ausgeführt.

## Original-Hostprüfung: axe-core 4.14.0

Der vorherige Nu-HTML-Befund wird um eine andere Originalprüfbibliothek ergänzt. Das unveränderte öffentliche Paket axe-core 4.14.0 ist exakt installiert. Im eigenen Browser-Prüftab lädt dieselbe axe.min.js über einen festen Distributionspfad; der Browser erzwingt den SHA-384-Integritätswert der lokal installierten Datei. Keine eigene ARIA-Regel in axe konfiguriert oder ersetzt. Versionsrückgabe 4.14.0 und Chrome-155-User-Agent sind gespeichert.

Neun vorhandene Regeln wurden ausdrücklich ausgewählt: aria-allowed-attr, aria-required-attr, aria-required-children, aria-required-parent, aria-valid-attr, aria-valid-attr-value, aria-input-field-name, duplicate-id-aria und label. duplicate-id-aria wurde explizit aktiviert. Das ist keine unveränderte Vollausführung sämtlicher Standard-/WCAG-Regeln.

| Fall | Tatsächliches Originalprüfergebnis |
| --- | --- |
| Zwei richtig benannte und zugeordnete Instanzen | Keine violation oder incomplete unter den gewählten Regeln |
| Offene Combobox mit fehlendem Popupziel | aria-valid-attr-value-Verstoß |
| Geschlossene Combobox mit fehlendem Popupziel und ohne aktive Option | Keine Diagnose unter den gewählten Regeln; offene/geschlossene Fälle nicht gleichsetzen |
| Aktive Option stammt aus Instanz B | Keine Diagnose unter den gewählten Regeln |
| Kontrollierte Liste stammt aus Instanz B | Keine Diagnose unter den gewählten Regeln |
| Liste und aktive Option gemeinsam auf B vertauscht | Keine Diagnose unter den gewählten Regeln |
| Nicht existierende aktive Option | aria-valid-attr-value-Verstoß |
| Doppelte referenzierte Option-ID | incomplete bei duplicate-id-aria; manuelle Klärung, keine als sicher bestätigte violation ausgeben |
| Ungültiges aria-expanded | aria-valid-attr-value-Verstoß |
| Fehlender Name der Eingabe | label-Verstoß |

Alle zehn vorher gespeicherten Erwartungen wurden erfüllt. „Keine Diagnose“ ist kein vollständiger Accessibility-Nachweis. Der kohärente Bezug auf B kann auf Hostebene gültige ARIA-Ziele besitzen und trotzdem die getrennte Produktinstanzregel des Forschungsfalls verletzen. Das ist kein pauschaler Fehler des Originalprüfers: Ihm fehlt die externe fachliche Zuordnung.

## Zusätzliches Instanzprofil: bewusst eigene Prüfregeln

Separat vom Originalchecker legt das Experiment ausdrücklich fest: A besteht aus input-a/list-a/option-a, B aus input-b/list-b/option-b. Das sind Testdaten, keine vorgeschriebene Namenskonvention oder ausgewählte neue Contract-Serialisierung. Ein eigener kleiner statischer Prüfschritt vergleicht die DOM-Ziele mit dieser Tabelle, prüft Eindeutigkeit und kontrolliert die Zugehörigkeit der aktiven Option zur erwarteten Liste.

Damit werden die drei instanzfremden Bezüge erkannt, die der generische Hostprüfer nicht als Verletzung der ausgewählten Regeln meldet. Auch fehlende Ziele und doppelte Identitäten werden in diesem begrenzten Profil diagnostiziert. Umgekehrt prüft dieses Profil keine Namen oder Booleanwerte: Die Fälle mit fehlendem Namen und ungültigem aria-expanded bleiben für diesen Zusatzschritt ohne Diagnose und werden durch den Originalchecker abgedeckt. Alle zehn separat gespeicherten Erwartungen treffen zu.

**Grenze:** Das zusätzliche Profil ist Forschungszusatzcode. Seine eigene Tabelle ist weder aus einem vollständig gebundenen CEM-/UX-/Visualpaket hergeleitet noch mit Originalvalidatoren aller vier Domänen verbunden. Es ist kein vollwertiger Resolver, kein Beweis allgemeiner Semantik und kein fertiger Konfliktvalidator. Ein zukünftiges Paket muss die Zuordnung aus führenden Originalquellen gewinnen und versions-/änderungsfest binden.

## Bedeutung für die offenen Matrixfelder

WAI-ARIA X06 bleibt U: reale Hostchecker sind jetzt praktisch belegt, aber kein vollständiges separates neutrales Accessibility-Artefaktschema und dessen Originalvalidator. X03 bleibt U: die externe Instanzsemantik stammt hier aus einer ausdrücklich hinzugefügten Tabelle, nicht aus einem nachgewiesenen ursprünglichen Vier-Domänen-Resolver. Positive Teilnachweise und offener Gesamtbedarf werden getrennt geführt.

## Reproduktion und Ausführungsart

Eigenen leeren Browser-Prüftab öffnen; niemals eine fremde Webseite oder vorhandene Benutzeroberfläche überschreiben. bootstrap.js, browser-run.js und binding-run.js sind die tatsächlich verwendeten BrowserOS-run-Skripte und erwarten einen eigenen about:blank-Tab. Der Originalprüfer läuft zuerst, dann der zusätzliche Schritt; die beiden Fall-/Outputdateien bleiben getrennt. Der zusätzliche Schritt wurde zum Speichern des strukturierten Outputs einmal unverändert wiederholt; keine neuen Fälle dadurch gezählt.

Die HTML-Fixtures wurden tatsächlich in einem isolierten Browser-DOM gerendert. Dies erweitert die bisherige reine Schema-/Funktionsprüfung um **statische Host-Fixtures**, nicht um eine implementierte oder bediente Produktkomponente. Kein Actor-/SCXML-Interpreter, keine asynchronen Updates, keine Fokus-/Tastaturautomation, kein Screenreader. Aktueller Originalcode, Versionen, SRI, SHA-256 und Inputs sind protokolliert. Paketinstallation bleibt im Arbeitsordner; Originalbibliothek wird nicht mitverteilt. Kein Commit oder Push.
