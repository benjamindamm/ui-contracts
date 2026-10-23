# Gesprächskontext und Entscheidungsstand

Stand: 23. Oktober 2026. Herkunft: [öffentlicher Originalchat](https://chatgpt.com/share/6adba3c9-accc-83ed-adbf-a78f5a880760), vollständig als Text gelesen; 71 Nachrichten und 36 Nutzerbeiträge. Nachrichtennummern entsprechen der beim Abruf sichtbaren Reihenfolge. Technische Behauptungen des damaligen Assistenten bleiben Gesprächsdaten, keine externen Nachweise.

## Vom Ausgangspunkt zum Projektziel

Der Nutzer verwendet OpenSpec und agentische Entwicklung. Er fragte zunächst nach Open Design und standardisierten textuellen Formaten. OpenPencil war das gegenwärtige Werkzeug, sollte aber nicht die Spezifikation bestimmen. Gefragt war ein Contract mit genügend Informationen für unterschiedliche Ausgaben. Als mögliche Ausgaben wurden HTML, Figma, PNG und technische Komponenten genannt. Ein Bild kann dabei nur einen Zustand zeigen; eine gemeinsame ausführbare Semantik war nicht nachgewiesen.

Die vier Domänen wurden vom Nutzer ausdrücklich bestätigt. Ein eigener Integrationsansatz wurde nicht grundsätzlich ausgeschlossen, aber wiederholte Recherche nach bestehenden Vorarbeiten verlangt. Das Motiv war auch, Weiterentwicklungen bestehender Modelle nutzen zu können und eigene langfristige Umbauten zu vermeiden.

Die visuelle Anforderung wurde präzisiert: verständliche Skalen wie im aktuellen Tailwind-Umfeld, Tokens und Varianten, Dark Mode, formal beschriebene Geometrie. Subpixelgleichheit wurde ausdrücklich relativiert. Aussagen im Chat über konkrete Tailwind-Umrechnungen sind keine allgemeingültige Vorgabe für jedes Theme.

## Entwicklung der Kandidatenhypothesen

1. CEM und DTCG als vorhandene Teilbeiträge; OpenPencil Behaviour Contracts als weitere Vorarbeit.
2. OpenUI Specification unter `openuispec.org` und AgentsORG DESIGN als frühe Vergleichskandidaten.
3. Panda CSS und Google DESIGN.md für Tokens/Varianten; der Nutzer wollte Googles Projekt priorisiert untersuchen. Unternehmensgröße wurde als Präferenz genannt, nicht als Eignungsnachweis bestätigt.
4. SCXML, Zag und Ark als Verhaltens-/Interaktionsvorarbeiten; später UXSpec und uSpec im agentischen Umfeld.
5. Kombination bestehender Substandards, strikte Ownership und Prüfung problematischer Überschneidungen.
6. Vier einzeln prüfbare Beschreibungen, anschließend Referenz- und Konfliktprüfung. Manifest/Resolver erst nach Nachweis der Teilmodelle.

Das ist eine Entwicklung von Untersuchungshypothesen, keine endgültige Standardauswahl. Insbesondere die zwischenzeitliche Empfehlung von UXSpec als zentralem Gesamtformat wurde später wegen der Überschneidungen wieder eingeschränkt.

## Beispiel und seine Grenzen

Der Nutzer erläuterte formale UX-Anforderungen an einem Autocomplete: Öffnung bei Fokus, relativer Abstand, fortgesetzte Texteingabe, begrenzte sichtbare Ergebnisliste, Scrollen, Pfeilnavigation, neue Ergebnisse und zugängliche Rückmeldungen. Die Werte acht Pixel und fünf sichtbare Einträge illustrieren Geometrie und Begrenzung. Light/Dark Mode stammt aus dem übergeordneten Designziel.

Enter/Escape, sieben Gesamtergebnisse, explizite öffentliche Feldnamen und konkrete ARIA-Abbildungen wurden im bestätigten Arbeitsmodell ergänzt. Sie dürfen nicht als allgemeine Pflichten aller UI-Komponenten ausgegeben werden. Fehler, asynchrones Laden und Fokusverlust waren noch nicht vollständig bestimmt.

Ein damaliger UXSpec-Entwurf wurde vom Nutzer wegen zu vager visueller Freitextbeschreibung kritisiert. Der damalige Assistent erklärte, ihn noch nicht erfolgreich mit dem offiziellen Compiler validiert zu haben. Diese Aussage ist ein historischer Bericht; Datei und Versuch wurden hier nicht rekonstruiert oder als E3-Nachweis übernommen.

## Integrationsideen, keine bereits vorhandene Infrastruktur

Besprochen wurden gemeinsame Komponentenidentität, stabile Teile, Zustands-/Variantenbindung, Aktions-/Eventzuordnung, Versionsbindungen und Konfliktprüfung. Für UXSpec neben DESIGN.md wurden drei Modelle vorgeschlagen: parallel vollständig, UXSpec nur für Verhalten oder DESIGN.md vorgelagert. Bevorzugt wurde isoliertes Verhalten, falls das Originalformat es erlaubt. Diese Bedingung ist weiterhin zu prüfen; die gelesene UXSpec-Schemadefinition erzwingt `$visual` nicht.

Für die abstrakte Schnittstelle wurde OpenUI als Kandidat und CEM als mögliche Web-Abbildung vorgeschlagen. Die technische API durfte nicht unabhängig den Zeitpunkt fachlicher Auswahl bestimmen. Accessibility sollte Patternanforderungen liefern, Behavior die konkrete Produktvariante. Keine unbelegte vollständige Übertragbarkeit zwischen Web und nativen Systemen annehmen.

Zwei bestätigte nächste Vergleiche waren DESIGN.md gegen vorhandene deklarative Layoutmodelle und UXSpec gegen SCXML. Die alte Aussage, die Identität dieser Vergleiche sei nicht rekonstruierbar, ist durch den vollständigen Zugriff überholt.

## Spätere Präzisierungen

Die Beispielkomponente ist nur Illustration. Die README beschreibt das allgemeine Forschungsvorhaben; die Matrix verwendet Anforderungen als Zeilen und Kandidaten als Spalten. Das zunächst gemeinte Zielartefakt ist das Contract-Paket, keine Auswahl bestimmter Renderer. Vier getrennte Domänendateien sind bevorzugt. JSON/YAML sind Möglichkeiten, keine Formatwahl.

Zusätzlich genannt wurden Referenzen zwischen separat beschriebenen Elementen, mögliche URNs und die Wiederverwendung eigenständiger Komponenten, etwa eine ScrollArea innerhalb eines Overlays. Definition, Instanz, externe Version und Referenzvalidierung sind damit ausdrücklich Untersuchungsgegenstände. Eine URI-/URN-Wahl ist nicht beschlossen.

## Noch nicht entschieden

Kein endgültiges Integrationsschema, keine universelle Laufzeit, keine Rendererstrategie, keine feste Plattform-Supportmatrix, kein Ownership-Personalmodell und keine pauschale Abdeckungsbewertung. Auch die Abbildung von Accessibility-Regeln in maschinenprüfbare Assertions ist noch Forschungsarbeit. Ein früher vorgeschlagener Vergleich zweier unabhängig generierender Agenten war eine mögliche spätere Reproduzierbarkeitsprüfung, kein bereits durchgeführtes Experiment und kein aktueller Implementierungsauftrag.
