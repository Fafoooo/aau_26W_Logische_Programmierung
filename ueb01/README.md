# Exercise + Homework 1 – Logische Programmierung

Vollständig bearbeitet: **Exercise 1 samt Quiz** und **Homework 1**, jeweils Aufgaben 1.1–1.4 a/b. Die gleichlautenden Nummern der zwei PDFs sind getrennt abgelegt.

## Einstieg

- [Erklärung zum Verstehen und Live-Ändern](erklaerung_blatt01.md)
- [Detaillierter zweiter Erklärungsteil: Hausübung](hausuebung/erklaerung.md)
- [Originalangabe Exercise](Angabe/exercise01a.pdf)
- [Originalangabe Homework](Angabe/exercise01b.pdf)
- [Beide Originale in einer PDF](angabe_blatt01.pdf)
- [Tatsächliche Testbefunde](TESTS.md)

## Lösungen

**Exercise 1**
- [Quiz](uebung/quiz/antwort.md)
- 1.1: [a](uebung/ue1.1/a/antwort.md), [b](uebung/ue1.1/b/antwort.md)
- 1.2: [a](uebung/ue1.2/a/antwort.md), [b](uebung/ue1.2/b/antwort.md)
- 1.3: [a](uebung/ue1.3/a/antwort.md), [b](uebung/ue1.3/b/antwort.md)
- 1.4: [a](uebung/ue1.4/a/antwort.md), [b](uebung/ue1.4/b/antwort.md)

**Homework 1**
- 1.1: [a](hausuebung/ue1.1/a/antwort.md), [b](hausuebung/ue1.1/b/antwort.md)
- 1.2: [a](hausuebung/ue1.2/a/antwort.md), [b](hausuebung/ue1.2/b/antwort.md)
- 1.3: [a](hausuebung/ue1.3/a/antwort.md), [b](hausuebung/ue1.3/b/antwort.md)
- 1.4: [a](hausuebung/ue1.4/a/antwort.md), [b](hausuebung/ue1.4/b/antwort.md)

Jede Teilaufgabe hat eine eigenständig ausführbare `programm.lp` unmittelbar neben ihrer `antwort.md`. 1.3 wiederholt absichtlich die Programme aus 1.2; Tests verlangen identische ausführbare Regeln. Keine Ergebnisfakten ersetzen die Aufgabenprogramme.

## Lokal ausführen

Voraussetzungen: Python ab 3.10, [clingo](https://potassco.org/clingo/). Getestet mit clingo 5.6.2. Keine Python-Zusatzpakete nötig.

Vom Ordner `ueb01` aus:
```sh
clingo uebung/ue1.4/a/programm.lp 0
clingo hausuebung/ue1.4/b/programm.lp 0
python3 checks.py
python3 hausuebung/ue1.2/pruefe_redukte.py
```

`0` lässt alle Answer Sets ausgeben. Die Prüfer kontrollieren auch `Models.More == no` und vergleichen vollständige Atomlisten, nicht deren Reihenfolge. Die zentralen Prüfungen kombinieren clingo mit einem unabhängig implementierten GL-Redukt-/Fixpunktprüfer. Die schriftlichen Lösungen zu 1.3 enthalten strukturelle Vollständigkeitsbeweise statt Interpretationstabellen.

## Hinweise

- `not` ist Defaultnegation. Ein klassisches Modell ist nicht automatisch ein Answer Set.
- Undefinierte Körperatome wie `f` in Exercise 1.1 a und `m` in Homework 1.1 a sind Absicht der Vorlage. Solverhinweise dazu dürfen nicht durch erfundene Fakten beseitigt werden.
- **KI-Unterstützung:** Ausarbeitung mit einem KI-Assistenten, automatisierten Solver-/Redukttests und unabhängiger Prüfung. Keine Eigenleistung von Fabio wird behauptet. Vor einer Präsentation die Schritte selbst nachvollziehen; dafür sind die ausführlichen Erklärungen gedacht. Die bestehende Kurszusammenfassung im Repo dokumentiert KI als Unterstützung/Inspiration.
- Dies ist eine lokale Übungsausarbeitung. Es wurde nichts auf Moodle abgegeben.
