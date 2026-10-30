# Lauf 03 · DMN-XML-Ausführung, Regelstärken und Wiederverwendung

**33/33 Check-Erwartungen erfüllt; 26 native Engineaufrufe.** [Rohantworten einschließlich stderr](results/observations.json) · [Checks](results/checks.json) · [Zusammenfassung](results/summary.json) · [exakte Runtime/JAR-Hashes](results/runtime.json).

## Werkzeuge und Reproduktion

Camunda DMN Scala `org.camunda.bpm.extension.dmn.scala:dmn-engine:1.12.6`, Java 25.0.2 und Jackson Databind 2.22.1; OPA-Binärdatei unverändert aus Lauf 01. Maven 3.9.11 sowie Binärdateien/JARs/Kompilate liegen außerhalb Git in `/tmp/ui-contracts-ux-rules-runtime`. Das hier gespeicherte pom.xml bindet die direkten Abhängigkeiten; runtime.json hält alle 15 tatsächlich aufgelösten JARs mit Koordinaten und Hashes fest. Keine vollständige DMN-Konformitätszertifizierung behauptet. Der Java-Adapter verwendet nur die native Parser-/Evaluierungs-API und normalisiert Scala-Ergebnisse für JSON, er implementiert keine eigene DMN-Logik.

Vom Repositoryroot, mit lokalem Maven/JDK:

```sh
mvn -q -f docs/research/studies/UX-RULES-01/runs/03/pom.xml \
  org.apache.maven.plugins:maven-dependency-plugin:3.8.1:build-classpath \
  -Dmdep.outputFile=/tmp/ui-contracts-ux-rules-runtime/classpath.txt
javac -cp "$(cat /tmp/ui-contracts-ux-rules-runtime/classpath.txt)" \
  -d /tmp/ui-contracts-ux-rules-runtime/classes \
  docs/research/studies/UX-RULES-01/runs/03/DmnProbe.java
```

Den Ordner classes vorher anlegen. Der konkrete Messlauf nutzte zusätzlich `-Dmaven.repo.local=/tmp/ui-contracts-ux-rules-runtime/m2`. probe.py nimmt `UX_RULE_RUNTIME` als alternativen Runtimeordner an; der Java-Pfad im historischen Harness entspricht dem gemessenen Mac. Auf anderen Hosts eine neue Harnessrevision verwenden, alte Messdaten nicht umschreiben. Ausführen mit der Pythonumgebung aus Lauf 01 und einer separaten Ergebniskopie; results wird exklusiv angelegt. Java-Methode-/SLF4J-Warnungen und ein eigener behobener Jackson-Setupfehler stehen in preflight.json. Dies sind keine gemessenen DMN-Fähigkeitsfehler.

## Tatsächlich geprüft

- Sechs bekannte Eignungskontexte über ein vollständiges natives DMN-XML-Literalmodell, einschließlich fehlendem/null/falschem Typ.
- Acht gleiche Normativitätskontexte in DMN und Rego: verletzte Pflicht versus verletzte Empfehlung, gültige Ausnahme, falsches Ausnahmeziel, keine Übersteuerung der Pflicht durch die Empfehlungsausnahme sowie Fremdbibliothek/-komponente.
- Eine gemeinsame Pflichtberechnung als referenzierte DMN-Decision bzw. separates Rego-Modul. Der lokale Ausnahmeausdruck ändert den gemeinsamen Pflichtkörper nicht. Das belegt explizite Wiederverwendung in diesen Artefakten, keine automatische Regelvererbung oder jede Bibliothekskomposition.
- Native Hit-Policies mit zwei gegensätzlichen passenden Zeilen: UNIQUE liefert Evaluierungsfehler, FIRST liefert recommend, COLLECT liefert beide Ergebnisse. Tabellenreihenfolge stellt keine fachliche Normenhierarchie dar.
- Positiver eigener Referenzgate für alle vier Contractdomänen vor nativem DMN-Aufruf; falsche Revision blockiert vor dem Engineaufruf. Hashauflösung bleibt eigene Integrationslogik.
- Alle fünf erzeugten DMN-Dateien erfüllen das unveränderte Original-XSD.
- Technischer gezielter Dateizugriff: Rego wird nur mit gemeinsamem und komponentenspezifischem Modul aufgerufen; ein absichtlich ungültiges fremdes Modul wird nicht geladen. Dateigrößen gemessen, kein Agenten-/Tokenbudgettest.

## Was die Proben nicht beweisen

`mandatoryMet`, `preferenceMet` und `exceptionApproved` sind synthetische, bereits bewertete Fakten zur Prüfung der Zusammenführungslogik. Ihre fachliche Wahrheit wurde nicht aus einem realen Nutzerprojekt abgeleitet. Die resultierenden Statusbegriffe sind unsere experimentelle Policy, keine nativen DMN-/Rego-UX-Kategorien. Produktentscheidungen brauchen zusätzlich präzise definierte Fakten, Evidenz und Autorisierung von Ausnahmen.

Kein SBVR-Engine-Test, keine allgemeine Konfliktlösung, keine automatische Komponentensuche, kein Modellvergleich mit Agenten, keine UX-/Accessibility-Freigabe. Beide Engines bekommen dieselben eigenen Annahmen; Übereinstimmung beweist nur deren begrenzte technische Umsetzung.
