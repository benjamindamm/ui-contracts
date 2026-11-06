# UX-Prüflaufzeit und Voraussetzungen

Nur für Einrichtung, Enginefehler oder technische Wiederholung laden. Der [UX-Einstieg](README.md) erklärt Zweck, Ablauf und Ergebnisse.

## Einrichtung und ausführbare Quellen

Die Python-/Node-Abhängigkeiten sind die vorhandenen gepinnten Bestände aus tools/validation und tools/openpencil. Einrichtung: `python3 tools/setup.py` mit vorhandenem JDK 17+ und Node 22+. Der Setupbefehl installiert die gepinnten Projektabhängigkeiten lokal; bei Bedarf `--java PFAD`. `check.py` führt die ECMAScript-Regeln lokaler SCXML-Dateien tatsächlich aus; nur die zur Prüfung vorgesehenen vertrauenswürdigen Projektartefakte verwenden. Die Profile sind keine Sandbox für fremden Code.

## Native Policyengine

Die vorbereitete Runtime stellt `classpath.txt` mit vollständigen JAR-Pfaden bereit. Deren Namen und SHA-256 müssen `runtime.lock.json` entsprechen. `DmnProbe.java` wird vor Auswertung aus dieser Repositoryquelle temporär mit einem JDK 17+ kompiliert. Nach `tools/setup.py` werden die lokal eingerichtete Runtime und ihr JDK aus `.runtime/config.json` verwendet. Alternativ wird Java über PATH oder ausdrücklich `--java /pfad/java` bestimmt; `UX_RULE_RUNTIME` ist eine Alternative zu `--runtime`. Es wird weder ein temporärer Standardpfad noch Homebrew vorausgesetzt. `choose.py` lädt nichts aus dem Netz; nur der ausdrücklich gestartete Setupbefehl lädt gepinnte Abhängigkeiten.

Der [Setup-/Browsernachweis](../../docs/research/analyses/WEB-RUNTIME-2026-10-31/README.md) dokumentiert eine saubere Arbeitskopie ohne mitkopierte Laufzeitabhängigkeiten. Ohne eingerichtete Engine endet choose mit `UX_ENGINE_NOT_CONFIGURED` oder einer konkreten Werkzeugdiagnose. Der reine Quellen-/SCXML-Check und `--prepare-only` benötigen keine DMN-Laufzeit.

