# Bibliotheksmigration und historische Quellen

Nur für frühere Studien und alte Pfade lesen. Für neue Arbeit führt die [aktuelle Bibliotheksanleitung](README.md).


Die erste Migration am 29. Oktober 2026 verschob die 22 Forschungsquellen bytegleich von `components/` nach `libraries/example/`. Seit der Trennung vom 30. Oktober liegen aktuelle Komponenten unter `libraries/example/components/`; Tokens und optionale Fontbindung bleiben am Bibliotheksroot, gemeinsame Dateien unter `assets/`.

Historische Runs, Manifeste, Reports und Messdaten bleiben unverändert. Die ursprünglichen 22 Quelldateien sind bytegenau unter [frozen/example-v1](../docs/libraries/frozen/example-v1/README.md) erhalten; das ist ein Forschungsarchiv, keine zweite bearbeitbare Bibliothek. Ihre Definitionsrevision bleibt `1d83935fda4e2d98dc131758e90bd508d30b1ecd51a845b81dca44e02fcec727`. Der aktuelle Handoff-Resolver löst alte `components/...`-Locators in dieses Archiv auf, sofern kein alter Root existiert, und prüft weiterhin ihre Hashes. Auch der begrenzte historische Autocomplete-Gegenprüfer bleibt an das Archiv gebunden. Er prüft damit ausdrücklich nicht die aktuelle Bibliotheksrevision.

Die aktuelle Bibliothek hat durch neue relative Pfade eine neue Revision. Alte, direkt an `libraries/example/` gebundene Gesamtmanifeste müssen im ursprünglichen Checkout verwendet werden; sie werden nicht still auf neue Dateien oder Hashes umgebogen.

Diese Kompatibilität ersetzt keine alte Werkzeugversion: Hashgebundene historische Tasks erkennen geänderte Prüfer-/Skilldateien weiter als veraltet. Unveränderte historische Generatoren/Prüfscripte mit festem components-Pfad benötigen den ursprünglichen Checkout (z. B. den erhaltenen Stand `8ca5678` in einem separaten Worktree mit den gepinnten Abhängigkeiten). Alte Receipts werden durch eine aktuelle Wiederholung nicht nachträglich neu bestätigt.

[Migration und Tests](../docs/libraries/MIGRATION.md) · [Framework-Überblick](../README.md).

Vor der aktiven Revision 0.3.0 wurde die komplette 50-Datei-Eingabe von SELECTION-01 bytegleich unter docs/libraries/frozen/example-selection-01 bewahrt. Der [neue externe Replay](../docs/research/analyses/ACTIVE-UX-2026-10-31/replay_selection01.py) verwendet den unveränderten ursprünglichen Helper mit diesem Datenroot; alte Eingaben und Kriterien bleiben unverändert.
