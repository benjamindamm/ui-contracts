# OpenPencil: konkrete Accessibility-Bindung eines Switches

Stand: 25. Oktober 2026. Dokumentarische E1/E2-Folgeprüfung; keine Komponentenimplementierung oder UI-/Assistenztechnikprüfung. Erweiterter Gegenstand ist der vorhandene Vue-Webpreviewpfad, nicht ein neues neutrales Accessibility-Dateiformat.

## Ergebnis und Umfang

A02 wird für den ausdrücklich begrenzten **Switch-Webpreviewbeitrag** von U zu R eingeordnet. Es ist nun eine konkrete, bestehende Referenzkette belegt: OpenPencil-Kind switch → Reka SwitchRoot → dokumentiertes Switch-Muster einschließlich Tastaturbedienung. Keine neue fachliche Bedeutung muss für diese Verbindung erfunden werden. Andere Kinds, Autocomplete/Combobox, ScrollArea, neutrale Paketkomposition und native Zielplattformen sind damit nicht mitbewertet. A01 und A03 bleiben U für ihre noch fehlenden vollständigen Nachweise.

## Nachvollziehbare Kette

| Glied | Originalbefund | Grenze |
| --- | --- | --- |
| OpenPencil controls/index.ts | switch wird über ON_OFF auf den importierten SwitchRoot gelegt; asChild verwendet eine Buttonbasis | Ein Kindname allein war zuvor kein genügender Nachweis; hier ist der konkrete Pfad gelesen |
| Wert und Sperre | modelValue und Updatecallback binden den Booleanwert, disabled wird übergeben | Keine Ausführung der Zustands-/Instanzisolierung |
| Renderpfad | renderNode ermittelt die Layerrolle, wrapRole wählt den Wrapper; renderElement erzeugt das Hostelement und führt Attribute/Props zusammen | Tatsächlich berechnete Accessibility-Tree-Ausgabe nicht geprüft |
| Externe Abhängigkeit | @open-pencil/vue 0.16.0 verlangt reka-ui ^2.10.5 | Ein Versionsbereich ist kein belegter tatsächlich aufgelöster Lockstand |
| Reka 2.10.5-Quellenbindung | Registry nennt gitHead a1d44a823240769cfd401a8e6589abc1e5d763e2; SwitchRoot und Dokumentation genau dort gelesen | Kein installierter OpenPencil-Build dieser Version ausgeführt; spätere Bereichsauflösungen können anders sein |
| Fokus/Tastatur | Die Dokumentation beschreibt Umschalten mit Space und Enter am fokussierten Switch; Code verwendet eine Buttonbasis und einen expliziten Enterhandler | Space folgt im gelesenen Pfad aus der nativen Buttonaktivierung; diese Ableitung ist kein getesteter Browsernachweis |
| Zustandssemantik | Reka schreibt switch-Rolle und aria-checked aus checked; disabled blockiert toggleCheck | Keine automatische Konformität aller gerenderten Instanzen |
| Leitfadenbezug | Gepinnte Reka-Dokumentation verweist ausdrücklich auf das WAI-ARIA-APG-Switch-Muster | APG ist ein informativer Leitfaden; seine Verlinkung ist keine Zertifizierung |

## Verbleibende A01-Fragen: Name und Beziehungen

Reka kann einen Namen über Attribute und einen zum id passenden Labeltext übernehmen. OpenPencil erhält beim Rendern vorhandene Attribute und Teile des Inhalts. Das belegt vorhandene Mechanismen, aber noch keine komplette Vertragszuordnung: Es ist nicht nachgewiesen, wie alle nötigen Labels und externen semantischen Ziele aus den Behaviour-Bindungen entstehen, ob sie bei Zustandswechsel stabil bleiben und bei mehreren Instanzen getrennt sind. Der APG-Leitfaden verlangt insbesondere eine stabile Switchbenennung. A01 bleibt U/C440; nicht alle Reka-Fähigkeiten werden pauschal OpenPencil zugerechnet.

Der vollständig gelesene Fieldpfad bildet Textlagen teilweise auf leere input/textarea-Elemente ab und übernimmt den gezeichneten Text unter Bedingungen als Placeholder. Ein Placeholder ist hier kein Beleg eines vollständig gebundenen zugänglichen Namens. Keine Aussage, dass andere Autoren-/Exportpfade grundsätzlich keinen Namen setzen können.

## Verbleibende A03-Fragen: Aktualisierung ist nicht gleich Ergebnisansage

Switchzustände und Progresswerte werden an Komponenten weitergegeben. Daraus folgt keine allgemeine vereinbarte Ergebnis-/Fehler-/Lademeldung mit Auslöser, Inhalt, Ziel und Vermittlungszeitpunkt. Die konkret gelesenen Preview-/Field-/Renderpfade liefern hierfür keinen vollständigen Nachweis. Eine pauschale Behauptung, Reka unterstütze keine dynamische Accessibility, wäre daraus ebenfalls unzulässig. A03 bleibt U/C441.

## Was sich daraus für das Integrationskonzept ergibt

Eine Bibliotheksreferenz muss mindestens den tatsächlich verwendeten Control-/Partpfad und die übergebenen Werte/Attribute benennen. Modus-/Stilzustand, Behaviourwert, zugänglicher Zustand und dynamische Rückmeldung sind verschiedene Bindungen. Der vorhandene Webpfad ist ein positiver Referenzbeitrag, aber weder ein neues neutrales Contractschema noch ein Nachweis externer Domänen-/Versions-/Ownershipregeln.

Originalquellen und UTF-8-Hashmanifest sind getrennt protokolliert; keine Originalquelltexte im Ergebnisordner mitverteilt. Die APG-Webseite ist ein datierter veränderlicher Abruf, die OpenPencil-/Reka-Quellen sind gepinnt. Keine zusätzlichen E3-Fälle aus bloßem Lesen gezählt. Kein Commit oder Push.
