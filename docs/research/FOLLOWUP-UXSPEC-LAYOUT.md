# UXSpec: Folgeprüfung der drei offenen Layoutfelder

Stand: 24. Oktober 2026. Gepinnter Quellenstand und Fundstellen: [S59](SOURCES.md#s59). Keine Implementierung oder ausgeführten Contract-/Laufzeittests.

| Feld | Vorher | Jetzt | Konkretes Ergebnis |
| --- | --- | --- | --- |
| V04 Ankergeometrie | U | U / C397 | Lokale Layerüberlagerung belegt; neutrales Ziel-/Richtungs-/Abstandsmodell weiterhin nicht ausreichend nachgewiesen |
| V05 Flächenbegrenzung | U | A / C398 | Vorhandener Webadapter liest size.maxHeight/maxWidth; Container verwenden das Ergebnis tatsächlich als div-Style. Für einen neutralen Vertrag bleibt eine explizite Bindung nötig |
| V06 Overflow/Scrollen | U | U / C399 | Die gelesenen Mapper-/Containerpfade definieren keine entsprechende Contracteigenschaft; maximale Höhe allein bedeutet nicht Scrollen |

**Warum die V05-Neubewertung belastbarer ist:** Die erste Runde hatte mapSize bereits gesehen. Die Folgeprüfung verbindet nun die konkrete Funktion über mapContainerStyle/mapElementStyle mit den aufrufenden Containerkomponenten und der Styleausgabe. A entspricht der bestehenden Methodenregel für einen belegten Mechanismus mit nötiger zusätzlicher Übersetzung. Es wird weder eine universelle neutrale Layoutsprache noch eine erfolgreiche Ausführung behauptet.

**Grenzen:** Die Eingangsdaten sind in diesen Rendererpfaden offen typisiert; Strings und Einheiten werden nicht durch einen vollständigen neutralen Layoutvertrag validiert. Fünf Zeilen bei variabler Zeilenhöhe, unabhängige Overlayanker, native Abbildung und Scrollzuständigkeit bleiben offen. Der vorherige Einheitenbefund C395 bleibt bestehen: direkter Stylemapper und vorgeschaltete Tokenauflösung sind verschiedene Pfade.

**Auswirkung auf den Gesamtstand:** 72 U-Zellen verbleiben, davon unverändert 45 Integrationsfelder und jetzt 27 weitere Felder. Ein Feld wurde U→A eingeordnet; es wurde kein fehlender Mechanismus implementiert. Alle 16 Kandidaten-Durchgänge bleiben abgeschlossen. Die historische Ausgangszahl 73 ist weiterhin nachvollziehbar, aber keine aktuelle Restzahl.

uSpec V04/V06 wurden anschließend ebenfalls gezielt geprüft; siehe [uSpec-Folgeprüfung](FOLLOWUP-USPEC-LAYOUT.md). Die separat vorgemerkte Gegenüberstellung von DESIGN.md und deklarativen Layoutmodellen bleibt offen. Der UXSpec-/SCXML-Detailvergleich bleibt ein eigener Arbeitsblock.
