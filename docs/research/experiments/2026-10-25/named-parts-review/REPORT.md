# I03 gesondert bewertet: benannte Teile über zusätzliche CEM-Bindung

Stand: 25. Oktober 2026. **Zwei begrenzte I03-Einordnungen anhand vorhandener ausgeführter Bindungen. Keine neuen Laufzeitbedingungen, keine Wiederholungszählung.** Der aktuelle Stand beträgt danach 44 U: 26 Integration und 18 weitere; weiterhin 395 Bedingungen/49 Gruppen.

## Frage und unverändertes Kriterium

I03 verlangt strukturiert benannte Anatomie beziehungsweise Teile, auf die andere Beschreibungen bezogen werden können. Instanzstabile IDs sind darin ausdrücklich ein zusätzlicher Nachweis, kein Ersatz für die Teilebeschreibung. Die ursprünglichen CSS-/ARIA-Beiträge stellten selbst keinen entsprechenden fachlichen Komponententeilekatalog bereit. Deshalb blieben diese Zellen U.

Die bestehende Methodik hält sachfremde Zellen zunächst offen. Eine bloße Spezialisierung oder weitere erfolglose Suche begründet hier **keine** neue N-Bewertung. Diese Regel bleibt unverändert. Geprüft wird stattdessen, ob die inzwischen tatsächlich ausgeführten **zusätzlichen** CEM-/Hostbindungen das konkrete I03-Teilkriterium erfüllen. Das Ergebnis ist A, keine nachträglich zugeschriebene native CSS-/ARIA-Anatomiesprache. Hashes von REQUIREMENTS.md und METHODS.md sind im Audit gebunden.

## CSS Layout I03: eigener Nachweisbezug

Der ursprüngliche CSS-Beitrag benennt Anker und Selektorziele. Diese Namen allein werden nicht zu Komponentenbestandteilen erklärt. Die ausgeführte zusätzliche Bindung aus P46 führt dagegen tatsächlich zum separat beschriebenen ursprünglichen CEM-Komponentenobjekt und seinen benannten input-/popup-Teilen:

- Originalformat-CEM: expliziter Komponentenpointer und zwei Partpointer innerhalb genau dieses Objekts; die gespeicherte CEM-Schemakontrolle ist positiv.
- Originalformat-CSS: tatsächliche anchor-name-/position-anchor-Deklarationen und Selektoren mit Quellrevision und Deklarationsort.
- Zusätzliches Binding: semantisch festgelegte input-/popup-Teilrollen, Zugehörigkeit zu A beziehungsweise B und konkrete Host-ID.

Das Kontrollpaket und die konsistente Namensänderung lösen die Teile korrekt auf. Ein Anker auf dem Listenteil oder der anderen Instanz wird tatsächlich abgewiesen. Damit ist nicht nur irgendein DOM-Ziel vorhanden, sondern ein strukturierter, extern beschriebener und gegen die gewählte Definition geprüfter Bestandteil.

**CSS Layout I03 U → A/C492**, im Umfang dieses zusätzlichen CSS-/CEM-/Host-Teilbinders. Die Teilesemantik stammt aus dem getrennten CEM-Modell; CSS liefert seinen realen Anker-/Selektorbeitrag. Eine eigene Teilebeschreibung innerhalb des CSS-Standards wird nicht behauptet. Native Anchorbox-Auswahl, vollständige Kaskade und allgemeine beliebige Komponenten bleiben außerhalb des Nachweises.

## WAI-ARIA I03: eigener Nachweisbezug

Rollenbezeichnungen alleine werden weiterhin nicht als vollständige Interfaceanatomie ausgegeben. P36 hat jedoch bereits die vier externen ursprünglichen CEM-Teile input/popup/list/option mit typisierten JSON-Pointern, Definitionsmitgliedschaft und den jeweiligen Hostteilen beider ARIA-Instanzen verbunden. Der eigene Binder kontrolliert die tatsächlichen Zielrollen und die eigenen controls-/activedescendant-Beziehungen.

Das Kontrollpaket und eine zweite gleichnamige, aber eindeutig anders adressierte Definition bleiben korrekt. Ein fremder gleichnamiger Komponentenpart, ein Behaviorziel statt Interfacepart, ein falscher Partname und ein vorhandenes Listziel der anderen Instanz werden abgewiesen. Die Bedeutung der Teilnamen entsteht durch die dokumentierte zusätzliche Abbildung; sie wird nicht aus bloßer Namensgleichheit geraten.

**WAI-ARIA I03 U → A/C493**, im Umfang dieser zusätzlichen CEM-/ARIA-Host-Teilebindung. WAI-ARIA bleibt für Rollen und Hostbeziehungen zuständig, CEM für benannte Komponententeile; die Zuordnung ist der eigene Adapterbeitrag. Keine neue native ARIA-Dateisprache, kein allgemeines Widget-Anatomieschema, kein Accessibility-Tree-/AT-Nachweis.

## Reichweite der Neubewertung

Die ursprünglichen Berichte hatten eine automatische Umbewertung anderer Kriterien ausdrücklich ausgeschlossen. Hier erfolgt eine neue, **gesonderte kriteriumsbezogene Auswertung** ihrer gespeicherten Ergebnisse: I03 fragt nach benannten Teilen, X03 nach der eindeutigen Beziehung zwischen getrennten Domänen. Dieselben tatsächlichen Bindungszeugen können beide unterschiedlichen Aussagen stützen. Das sind zwei neue Bewertungen, keine zwei neuen Versuche und keine zusätzliche Zählung der früheren Bedingungen.

Keine automatische Änderung von CSS I01/I02/B01–B04/A01–A03 oder WAI-ARIA V06/X08. Ein eingebundener CEM-Partname ersetzt weder öffentliche Payloadsignatur noch Zustandslogik, Tastenmuster oder Statusmeldung. Andere offene Zellen benötigen ihre eigenen kriteriumsgerechten Original- oder Zusatzbelege.

Der Restplan wird von 46 auf 44 aktuelle Schlüssel fortgeschrieben: 42 unabhängig untersuchbar, 2 konkrete Originalklärungen. Seine ursprüngliche 46-Zellen-Baseline bleibt separat erhalten. Eine Reduzierung ausschließlich durch fachfremdes U→N oder eine Änderung der Vergaberegel wurde nicht vorgenommen.

## Reproduktion und Quellen

audit.json hält Quell-/Methodenhashes, die wiederverwendeten Ergebnisdateien, konkreten positiven/negativen Fall-IDs und tatsächlichen Auflösungszeugen fest. Originale Berichte, Cases und Fehlbefunde aus P36/P46 werden nicht umgeschrieben oder neu ausgeführt. Diese Auswertung prüft vorhandene Ergebnisse; sie erzeugt **null** neue benannte Laufzeitbedingungen. Keine neue Daten-/Produktsprache oder Komponente, kein Commit/Push.
