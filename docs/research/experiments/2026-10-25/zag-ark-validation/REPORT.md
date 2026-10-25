# Zag und Ark: vorhandene Originalprüfungen und ungelöste X06-Artefaktfrage

Stand: 25. Oktober 2026. **13 vorab definierte Bedingungen in drei Gruppen ausgeführt, sämtliche Erwartungen erfüllt.** Zwei bestehende X06-U-Fragen präzisiert, keine automatische Neubewertung.

## Gegenstand und Endbedingung

Zag: Der ausdrücklich abgegrenzte veröffentlichte @zag-js/core 1.46.0 mit seinem tatsächlichen utils-/dom-query-Pfad. Original-Maschinenobjekt, createMachine/ensureStateIndex, Machine-/MachineSchema-Deklarationen und interne Fehlerprüfungen. Gesucht ist der Unterschied zwischen diesen Originalmechanismen und einem getrennten neutralen Originalartefakt-/Schema-/Validatorpaar.

Ark: Veröffentlichter React-SDK 5.39.3 mit seinen tatsächlichen Deklarationen; separat der schon zuvor gepinnte Original-Combobox-API-Metadatensatz am Repositorycommit c7af88a51b9dc32e5903a75b3d49b4deaa36e8dc. Typausdrücke, erforderliche Eigenschaften und Defaults sollen nach ihrer tatsächlichen Rolle eingeordnet werden. Keine eigene Umwandlung der Metadaten in ein angeblich originales neutrales Schema.

Endbedingung: Quellen/Abhängigkeiten eindeutig binden, vorhandene Prüfrollen mit kleinen Gegenkontrollen nachweisen und genau benennen, ob damit die X06-Frage des **jeweiligen gesamten Kandidatenumfangs** entscheidbar ist. Negative Suchtreffer oder ein begrenzter Core allein dürfen nicht still auf alle Toolkit-/Framework-/Repositorybeiträge übertragen werden.

## Originalidentität: eine tatsächlich relevante Abweichung

Registry-Metadaten am 25.10.2026 über BrowserOS gelesen, beide Distributionspakete ohne Skriptausführung mit exaktem Lock installiert. Inventar ohne mitinstallierte Unterabhängigkeiten: Core **35 Dateien**, Ark React **3874 Dateien**, jeweils identisch zur RegistryfileCount. Hashinventur ist keine vollständige semantische Prüfung aller Dateien.

| Originalstand | Konkrete Beobachtung |
| --- | --- |
| Direkter @zag-js/core 1.46.0 | Tatsächlich eigener utils-/dom-query-Pfad 1.46.0 |
| Veröffentlichter @ark-ui/react 5.39.3 | Registry/Originalpackage pinnen Zag-Pakete 1.45.0; tatsächliche Auflösung von Core/Combobox/Reactbindung jeweils 1.45.0 |
| Ark-Registry gitHead | 90eb2125a9ac6a8225b2e4053484da08cbb68a54 |
| Früherer Ark-Repositorysnapshot c7af88a… | Ebenfalls Versionsangabe 5.39.3, aber dort Zag-Paketangaben 1.46.0; historischer Quellenbefund bleibt getrennt |

**Gleiche Versionszeichenfolge ist hier kein Nachweis identischer Originalartefakte.** Der direkte Coretest 1.46.0 wird nicht zu einer Prüfung des in Ark ausgelieferten Core 1.45.0 erklärt. package-resolutions.json und Lock enthalten die tatsächlichen Auflösungen. Registry-Metadaten enthalten bei Ark vorverarbeitete src-Exportangaben; das installierte Originalpackage exportiert seine dist-Einstiege. Für die SDK-Proben wurden die tatsächlichen ausgelieferten dist-Deklarationen benutzt, nicht aus Registrystrings erfundene Pfade.

Die ursprünglichen gleichversionierten Repo-/NPM-Stände werden weder vermischt noch rückwirkend gleichgesetzt. Historische Matrixbeiträge anderer Ark-/Zag-Felder werden dadurch nicht ohne eigene Nachprüfung geändert.

## Zag: zehn Originalaufbaubedingungen

Node v24.22.1; fünf Fälle jeweils in einem eigenen Prozess mit NODE_ENV=development beziehungsweise production. Beide Läufe benutzen dieselben CommonJS-Originalpakete; die Umgebungsbedingung ist der kontrollierte Unterschied. Kein selbst geschriebener Maschinenvalidator oder eigener Serviceersatz.

| Fall | Development | Production |
| --- | --- | --- |
| Gültiges Maschinenobjekt | Akzeptiert | Akzeptiert |
| Fehlende obligatorische Root-initialState-Funktion | Aufbau akzeptiert Objekt trotzdem | Aufbau akzeptiert Objekt trotzdem |
| Doppelte Zustands-ID | Originalinvariant wirft | Aufbau akzeptiert |
| Compound-initial nennt nicht vorhandenes Kind | Originalinvariant wirft | Aufbau akzeptiert |
| Compound hat Kinder, aber kein initial | Originalensure wirft | Originalensure wirft |

Alle zehn Erwartungen erfüllt; Originalfehlertexte erhalten. createMachine ruft ensureStateIndex auf und gibt das Maschinenobjekt selbst zurück. Das ist eine echte begrenzte interne Prüfung, **kein vollständiger Shape-/Fachvalidator**. Dass ein Objekt ohne erforderliche Rootfunktion den Aufbau passiert, sagt ausdrücklich nicht, dass ein später gestarteter Service korrekt funktioniert. Kein solcher Service-, UI-, Tastatur- oder Assistenztest wurde ausgeführt.

Die Typdeklaration MachineSchema ist ein generischer SDK-Typ; Machine.initialState ist eine Funktion, weitere Kontext-/Aktions-/Effektteile sind ebenfalls ausführbare SDK-Definitionen. Ein bloßer Exportname MachineSchema wird nicht als neutrales Datendateischema ausgegeben. Der zuvor nur aus Quellcode belegte Modusunterschied C406 ist jetzt tatsächlich ausgeführt.

## Ark: Originalmetadaten und drei SDK-Typbedingungen

Der separat gelesene Original-API-Metadatensatz beschreibt unter anderem:

- collection als Typausdruck ListCollection<T>, erforderlich.
- open als optionalen Typausdruck boolean.
- onValueChange als Callback-Typtext.
- alwaysSubmitOnEnter mit Typtext boolean und Defaulttext false als Zeichenfolge.

Diese Daten sind originale Dokumentations-/SDK-Metadaten. Eine daraus neu gebaute JSON-Schemaprüfung müsste Typbedeutung, Klassen-/Callbackbezüge und Defaultkonversion festlegen; sie wäre Zusatzcode. Es wurde kein solcher Ersatzprüfer geschrieben. Capture-/Objekthash und ausgewählte Metadateneigenschaften stehen in api-observations.json; der Repositorysnapshot wird nicht als byteidentisch zur NPM-Distribution behauptet.

Aus der **tatsächlich installierten Distribution** wurde UseComboboxProps über seine Originaldeklaration und die referenzierten Zag-Props benutzt. TypeScript 5.9.3, strict/noEmit/skipLibCheck; ausgewählte Originaleigenschaften werden mit Pick typgeprüft. Keine gesamte Ark-Projekttypprüfung und kein Frameworkrender.

| Fall | Ergebnis |
| --- | --- |
| open=true | Keine Diagnose |
| open als String | TS2322, String nicht boolean/undefined |
| collection als einfaches Array | TS2740, erforderliche ListCollection-Struktur/-Methoden fehlen |

Alle drei Erwartungen erfüllt. Der SDK-Typpfad ist real; ein neutraler JSON-Contract mit bloßem Array wird dadurch nicht automatisch zum SDK-Collectionobjekt. Es wurde kein zusätzlicher Ark-Laufzeitvalidator oder Reactservice ausgeführt.

## Einordnung der weiterhin offenen Fragen

**Zag X06 bleibt U/C466.** Der getestete Core besitzt keine durch diese Untersuchung belegte neutrale Artefaktprüfung; seine konkreten internen Regeln sind nun genau bekannt. Die Zag-Spalte umfasst gemäß S33–S38 ausdrücklich das Toolkit mit benannten Hilfs-/Komponentenbeiträgen und nicht nur diesen Core. Die begrenzten Aufbauprüfungen oder die Inventur des Core reichen weder zum D für einen neutralen Originalartefaktvalidator noch zum N über den gesamten bereits definierten Toolkitumfang. Noch fehlend: ein eindeutig identifiziertes neutrales Originalartefakt-/Schema-/Validatorpaar im Kandidatenumfang oder ein separat belegter abschließender Modellgrenzenbefund für diesen gesamten Gegenstand.

**Ark UI X06 bleibt U/C467.** Die ausgewählte React-Combobox-Deklaration und die separate API-Metadatendatei sind keine Originalschema-/Dateivalidatorkette. Der Kandidat umfasst mehr als diese drei Props beziehungsweise nur das Reactpaket. Die Untersuchung belegt keinen neutralen Validator und widerlegt nicht sämtliche übrigen Artefaktbeiträge/Frameworks. Noch fehlend: ein konkretes Original-Contractartefakt samt eigener Schemaversion und nachgewiesenem Aufruf/Regelumfang; mögliche Generatoren und eigene Ableitungen getrennt halten.

Die Grenzen der konkret geprüften Originalwerkzeuge sind damit geklärt. Das ist mehr als eine offene Überschrift, aber **keine Erfüllung der darüber hinausgehenden X06-Fragen**. Diese Restfragen bleiben mit genauem fehlendem Beleg im Register; weder N noch D werden aus der Untersuchung kleinerer Einheiten erfunden. Keine neue Produkt-/Technologieentscheidung erforderlich oder getroffen.

Aktuell weiterhin **53 U-Zellen: 33 Integration und 20 weitere**. X06 unverändert sieben D, ein begrenztes XState-Core-N und acht U. 321 benannte Bedingungen in 41 Gruppen sind Umfang, kein Erfolgszähler geschlossener Fragen. Keine Produktionskomponente, Commits oder Pushes.

## Reproduktion

tool/package-lock.json erhalten, npm ci --ignore-scripts --legacy-peer-deps. run-zag.cjs getrennt mit beiden gespeicherten NODE_ENV-Werten ausführen. check-types.cjs nutzt den zuvor gebundenen TypeScript-5.9.3-Ordner und die tatsächlich installierten Originaldeklarationen. Zusätzliche Originalquellen, Auflösung, Inventare und Prüfergebnisse sind gehasht. Wiederholungen werden nicht als neue Fälle gezählt; keine Expectation wurde geändert, um Fehler zu verdecken.
