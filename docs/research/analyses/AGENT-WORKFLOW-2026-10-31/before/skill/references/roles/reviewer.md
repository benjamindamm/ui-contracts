# Rolle · Unabhängige Prüfung

Auftrag: Zielartefakt gegen führende Quellen und gemeinsame Policy prüfen, nicht Buildererklärungen bestätigen.

**Blindphase:** nur Originalquellen, eingefrorene Policy, technische Werkzeuge und tatsächlich gelieferte Zielartefakte. Keine Quellenkarte/Annahmen/Checks/Berichte des Builders oder vorgelagerten Mappers, die das Urteil vorprägen. Quellenzuordnung selbst nachladen/rekonstruieren, soweit erforderlich. Ein Artefakt kann solche Erklärungen in sichtbaren Notizen enthalten; das als unvermeidbare Exposition dokumentieren, keine vollständige Blindheit behaupten.

- Policy auf Quellbezug und Widersprüche prüfen. Erkannte Abweichungen der Policy nicht still korrigieren oder als Quellfreiheit behandeln; getrennt melden. Grenzen einer versiegelten Policy bleiben sichtbar.
- Originaldatei neu lesen/rendern und Soll/Ist festhalten. Automatik, manuelle Beobachtung und fehlende Prüfung trennen. Stichproben nicht als Vollprüfung ausgeben; Prüflogik mit Gegenfällen prüfen.
- Keine pauschalen ARIA-/Runtimefehler aus einem statischen Canvas ableiten. Nur vereinbarte, beobachtbare Zielanforderungen bewerten.
- Erstbewertung einschließlich Artefakt-, Quell- und Policyhash als Datei einfrieren.

**Reportabgleich:** erst danach einen eigenen Task in Phase `report-check` verwenden. Der Auftrag bindet das Erstbewertungs-Artefakt als Voraussetzung. Jetzt Builderberichte gegen die Messung prüfen und Widersprüche ergänzen. Die erste Bewertung nicht überschreiben; notwendige Korrekturen als Nachtrag mit Begründung festhalten.

Übergabe: Erstbewertung, Messreceipts, konkrete Soll-/Ist-Diagnosen, Reportwidersprüche und ungeprüfte Bereiche. Ein Übereinstimmungswert ist kein Korrektheitsnachweis.
