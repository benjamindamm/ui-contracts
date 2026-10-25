# Panda X06: eigener Datenartefaktgegenstand und erforderliche Originaltyp-Anbindung

Stand: 25. Oktober 2026. **Endlicher offizieller Restzugriff abgeschlossen, keine neue Laufzeitbedingung.** Rust-Exporter, sein ausdrücklich referenziertes Design-Dokument und öffentliche JSON-Spec-Dokumentation wurden gezielt gelesen. Bereits ausgeführte Originaltyp-/Reader-Gegenproben P42 werden als bestehende Evidenz verwendet, nicht erneut gezählt.

## Originalgegenstand konkret geklärt

Unveränderter Panda-Repo-Pin **86f78a228204d63baa0b8bca2676d9f26190e449**. Der benannte Rustpfad crates/pandacss_codegen/src/artifacts/specs.rs schreibt specs/design-system.json mit einer festen SchemaVersion 1 und den Tabellen categories, paths, tokens, conditions, themes, values sowie bedingt weiteren Tabellen. Gezielt betrachtet: generate, build_design_system, Versionskonstante und token_refs. Kein kompletter Rust-Codeaudit oder Generatorbuild.

Die öffentliche JSON-Spec-Seite beschreibt dieses ausdrücklich generierte Datenartefakt für Werkzeuge außerhalb des Compilers, zeigt seinen öffentlichen parseDesignSystem-/indexDesignSystem-Zugriff und die opt-in-Ausgabe über --spec. Diese Website ist eine separat datierte Dokumentationsquelle, keine ungeprüft mit dem Repo-Pin bytegleiche Fassung.

Die Originaltypes.ts beschreibt konkret genau diesen JSON-Datendateigegenstand. Das unterscheidet ihn von einer beliebigen SDK-Maschinenkonfiguration, deren Funktionen/Actorimplementierungen erst eine neue neutrale Dateisprache erfordern würden. Die Datenform ist hier bereits vom Originalprojekt festgelegt; keine neue Produktsprache wurde gewählt.

## Wie die Originalgrenzen zusammenpassen

| Originalbeitrag | Tatsächlich belegt | Was nicht daraus folgt |
| --- | --- | --- |
| Rust-Exporter | Erzeugt ursprüngliches JSON-Artefakt mit Version und Tabellen | Kein Validator beliebiger externer Eingabedateien |
| DesignSystemSpec in types.ts | Deklaratives, dateibezogenes Original-Shapemodell für das JSON | Kein eingebauter Runtime-JSON-Schemachecker |
| parseDesignSystem | Öffentlich vorgesehener, bewusst flacher Reader mit eigenen Root-/Versionsprüfungen | Nicht sämtliche deklarierten Feld-/Zeilentypen durchgeprüft |
| Zusätzliche statische Literalzuweisung gegen Originaltyp | In P42 an neun identischen Originalreader-/Typbedingungen ausgeführt | Keine originale Runtime-API und keine vollständige Referenz-/Wertsemantik |

Der im Originalcode referenzierte Design-Note-Pfad beschreibt die Migration vom früheren Studio-Zod-Schema auf den gemeinsamen Parse-/Indexzugriff. Das ist eine konkrete historische Rollenklärung; **das Löschen dieses alten Schemas ist allein kein Beweis gegen jedes denkbare andere Schema**. Ebenso enthält die Notiz Aussagen zu Rezept-/Patternzukunft, während der am selben Pin gelesene aktuelle Exporter schon entsprechende Tabellen erzeugt. Deshalb wird die Notiz nicht über den tatsächlichen aktuellen Code gestellt und nicht als vollständige normative Formatdefinition behandelt. Die maßgeblichen konkreten aktuellen Shapeinformationen stammen aus Originaltypes/Reader/Exporter.

## Begründete Adaptereinordnung statt D oder endloses U

**Panda CSS X06: U → A/C477**, ausdrücklich für das Original-JSON-Spec-Shapemodell und dessen erforderliche zusätzliche Prüfbindung.

Grundlage sind zwei positive Befunde: Das Originalprojekt definiert einen eigenen unabhängigen JSON-Datenartefaktgegenstand samt zugehörigem Originaltyp; und eine zusätzliche Bindung an genau diesen unveränderten Originaltyp ist bereits tatsächlich ausgeführt. Es wird kein eigener strengerer JSON-Schemaentwurf an die Stelle des Originals gesetzt. Die Eingabedaten und ursprünglichen Shapeconstraints bleiben unverändert; die zusätzlichen Schritte Literalrepräsentation/Compileraufruf sind offengelegt.

**A bedeutet hier nicht D:** Weder der TypeScript-Compiler noch der eigene Probeaufruf wird zum nativen Original-JSON-Validator erklärt. Originalreader und statische Zusatzbindung behalten ihre getrennten Rollen. Die zusätzliche Compilerabhängigkeit und die beschränkte Prüfart sind gerade der nachgewiesene Adapterbedarf. Das ist kein positives Urteil zur neutralen gesamten Panda-Konfiguration oder zu allen Plugins.

Die früheren P42-Ergebnisse bleiben unverändert: Der Originaltyp erkennt fünf zusätzliche Shapefehler; Originalreader und statische Typbindung akzeptieren beide ein fehlendes refs-Ziel, einen unpassenden Kategorienbereich und schemaVersion=-1. Für X06 wird keine vollständige semantische Allprüfung verlangt. Referenz-/Bereichs-/Versionssemantik sind weiterhin separate Anforderungen. Eine produktiv sichere generische Datenimport-/Compilerbrücke wird nicht behauptet; ausgeführt sind die gespeicherten kontrollierten Datenfälle.

Diese Einordnung unterscheidet den **bereits existierenden Originaldatenartefakttyp** von einem SDK-Props-Typ beliebiger Codekonfiguration. Sie erfindet kein Originalschema und macht die zusätzliche statische Prüfung nicht heimlich zur veröffentlichten Originalfunktion.

## Producer-Garantie und externe Eingabe nicht verwechseln

Der gelesene token_refs-Pfad nimmt nur im bekannten Tokenpfadbestand enthaltene Ziele auf. Kategorienbereiche werden aus dem tatsächlich aufgebauten paths-Vektor erzeugt; die Versionskonstante ist im Exporter 1. Das stützt eine begrenzte E2-Aussage über die Erzeugung, **keinen ausgeführten Generatornachweis**. Dass ein externer beschädigter Export Reader/Typprüfung passiert, beweist nicht, dass der reguläre Producer denselben Fehler erzeugt.

Umgekehrt ersetzt eine plausible Producerkonstruktion keinen Checker einer importierten Datei. Die frühere Akzeptanz widersprüchlicher externer Daten wird weder gelöscht noch als nachträglicher Erfolg umgeschrieben.

## Status und Quellenbindung

Aktuell **50 U: 30 Integration und 20 weitere**. X06: **8 D, 1 A, 2 begrenzte N, 5 U**. Weiterhin **336 Bedingungen in 43 Gruppen**; vorhandene P42-Evidenz nicht doppelt gezählt. Keine neue Produktentscheidung, Produktionskomponente, Commits oder Pushes.

Manifest bindet die tatsächlich gelesenen Quellen/Lesefassungen und die unverändert wiederverwendeten P42-Outputs. Die Originaldateien werden nicht als eigene Implementierung mitverteilt. Die bereits ausgeführte Probe und ihre Reproduktion bleiben im benachbarten panda-artifact-types/REPORT.md; dieser Bericht ist die gezielte ergänzende E1/E2-Gegenstands-/Adaptereinordnung.
