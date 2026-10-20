# Verifikation – Blatt 01

## Ausgeführte Prüfungen

Die folgenden Befehle wurden im Blattordner tatsächlich ausgeführt und liefen erfolgreich durch:

```sh
python3 checks.py
python3 hausuebung/ue1.2/pruefe_redukte.py
```

Beide Python-Prozesse endeten mit **Exitcode 0**. Verwendeter externer Solver: **clingo 5.6.2**.

## Befunde des zentralen Tests

Jede unten angegebene Modellfamilie wurde als **vollständige Menge von Atomemengen** mit zwei Verfahren geprüft:
- clingo mit `--outf=2 --warn=none 0 -`, einschließlich `Models.More == no` und konsistenter Modellzählung;
- unabhängiger Python-Prüfer: GL-Redukt für Kandidaten, kleinster positiver Fixpunkt ab `{}`, Vergleich mit den vorgegebenen Sollmodellen.

Bestätigte Anzahlen, jeweils a / b:
- Exercise 1.1: **1 / 1**.
- Exercise 1.2: **2 / 2**.
- Exercise 1.3: **2 / 2**.
- Exercise 1.4: **4 / 1**.
- Homework 1.1: **1 / 1**.
- Homework 1.2: **2 / 3**.
- Homework 1.3: **2 / 3**.
- Homework 1.4: **2 / 4**.

Das sind **16 Aufgabenprogramme**, nicht bloß 16 einzelne Modelle. Die Atomlisten aller Ergebnisse erscheinen bei jedem Lauf von `checks.py` und stehen in den jeweiligen Antworten.

Zusätzlich bestätigt:
- Alle vier Kandidatenentscheidungen und kleinsten Reduktmodelle von Exercise 1.2.
- Alle sechs vorgegebenen Kandidaten aus Homework 1.2 sowie die zusätzlichen Lösungskandidaten `{b,c,d}` und `{b,f}` aus Homework 1.3: exakte Reduktstrukturen, Fixpunkte, Gegenprüfung der Redukte durch clingo.
- Positive Fixpunktstufen von Homework 1.1 a.
- Für beide Angaben ist der ausführbare Regelinhalt von 1.3 a/b mit 1.2 a/b identisch.
- Quizgegenbeispiel `a :- a.`: zwei klassische Modelle `{}` und `{a}`, aber nur Answer Set `{}`.
- Quizgegenbeispiel `p :- not p.`: kein Answer Set; `{p}` ist trotzdem ein klassisches Modell.
- Selbsttests für ein Atom mit innerem Komma, einen positiven Kreis ohne Start, wechselseitige Defaultnegation und eine positive Faktenkette.

Die Original-PDFs wurden zusätzlich als Seitenbilder und mit `pdftotext -layout` gelesen; die zusammengeführte Angabe wurde mit `pdfinfo` als **6 Seiten** bestätigt. Aufgabennummern und ursprüngliche Regelkörper wurden beibehalten.

## Unabhängige Prüfung

Nach Fertigstellung wurden Exercise 1 samt zentralem Prüfer und Homework 1 in zwei getrennten, schreibgeschützten Prüfkontexten gegen die jeweilige Originalangabe geprüft. Beide Prüfungen meldeten keine fachlichen Fehler und keine fehlenden Teilaufgaben. Geprüft wurden Originalregeln, Quiz, schriftliche Redukte, Fixpunktstufen, Modelllisten, Vollständigkeitsbeweise und Erklärungen. Der zentrale Prüfer wurde dabei erneut erfolgreich ausgeführt; der zweite Prüfer führte zusätzlich sämtliche acht Hausübungsprogramme und den Hausübungs-Reduktprüfer neu aus.

## Reproduzierbarkeit und Grenzen

Keine Python-Zusatzpakete, keine Netzverbindung und kein Moodle-Zugang sind zum Wiederholen der Tests nötig. Python nicht mit `-O` starten, weil die Prüfer Assertions verwenden. Die eigenen Parser unterstützen bewusst nur die Grundprogramme des Blatts; für beliebige ASP-Syntax ist clingo selbst zuständig.

Der vollständige maschinelle Kandidatenvergleich ist eine Gegenprobe. Die Lösungen zu Aufgabe 1.3 erfüllen die Aufgabenforderung durch eigene strukturelle Fallbeweise; sie verweisen nicht nur auf Enumeration.

Es wurde nichts in Moodle eingereicht.
