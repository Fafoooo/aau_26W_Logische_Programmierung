# Homework 1 – Aufgabe 1.3 b

## Aufgabe und Ergebnis

Gesucht sind alle Answer Sets des Programms aus **Aufgabe 1.2 b**, mit einer
Begründung ohne Durchprobieren aller Interpretationen. Die Datei `programm.lp`
ist eine unabhängig ausführbare Kopie genau dieses Grundprogramms:

```prolog
a :- not b.
b :- not c.
b :- not f.
c :- a.
c :- d.
d :- c, e.
d :- not b.
e :- not a, not f.
f :- not e.
```

**Genau die folgenden drei Answer Sets existieren:**

```text
M1 = {a,c,d,f}
M2 = {b,f}
M3 = {b,e}
```

## Grundlage der strukturellen Herleitung

Ein Kandidat `M` ist stabil, wenn er genau das kleinste Modell seines
GL-Redukts ist. Eine Regel mit `not q`, `q ∈ M`, wird vollständig gelöscht;
alle übrigen negativen Rumpfliterale werden entfernt. Das kleinste Modell
des positiven Programms wird ab `{}` berechnet. Positive Kreise ohne
Startableitung dürfen daher nicht als frei wählbare Atome behandelt werden.

Die einzige globale Fallunterscheidung betrifft `b`. Im Fall mit `b` bleiben
anschließend nur die zwei Standardalternativen für `e` und `f` übrig.

## 1. Fall b ist nicht enthalten

Angenommen, `b ∉ M` in einem Answer Set `M`.

1. `a :- not b.` und `d :- not b.` werden zu Fakten `a.` und `d.`.
   Folglich `a,d ∈ M`.
2. `c :- a.` und `c :- d.` erzwingen `c ∈ M`.
3. Wegen `a ∈ M` wird die einzige `e`-Regel gelöscht. Deshalb `e ∉ M`.
4. `f :- not e.` wird dadurch zum Fakt; also `f ∈ M`.
5. Wegen `c,f ∈ M` werden beide Regeln für `b` gelöscht. Das angenommene
   Fehlen von `b` ist somit mit dem Redukt vereinbar.

Alle Atome sind festgelegt; einzig möglich ist `M1 = {a,c,d,f}`.

**Existenzprüfung:** Der vollständige Redukt ist

```prolog
a.
c :- a.
c :- d.
d :- c, e.
d.
f.
```

Seine Fixpunktstufen sind

```text
{} -> {a,d,f} -> {a,c,d,f} -> {a,c,d,f}.
```

Damit `LM(P^M1) = M1`; `M1` ist stabil.

## 2. Fall b ist enthalten: zuerst den positiven Kreis ausschließen

Angenommen, `b ∈ M`.

1. Die einzige `a`-Regel `a :- not b.` wird gelöscht. Also `a ∉ M`.
2. Auch `d :- not b.` wird gelöscht. Für `c` und `d` bleiben nur
   `c :- a.`, `c :- d.` und `d :- c,e.`.
3. Die erste dieser Regeln kann ohne ableitbares `a` kein `c` liefern.
   Die zweite braucht zunächst `d`, die dritte zunächst `c`.
   Es gibt keine andere Regel, die `c` oder `d` erstmalig erzeugen könnte.
   Daher enthält das kleinste Reduktmodell weder `c` noch `d`.
4. Das gilt auch dann, wenn `e` ableitbar ist: `e` allein erfüllt den Rumpf
   `c,e` nicht. Also gelten in diesem gesamten Fall `c,d ∉ M`.
5. Aus `c ∉ M` folgt, dass `b :- not c.` zum Fakt `b.` wird. Das enthaltene
   `b` besitzt also eine wirkliche Startableitung.

Nun werden die Möglichkeiten für `e` und `f` aus deren einzigen Kopfregeln
bestimmt. Da bereits `a ∉ M` gilt, sind sie die wechselseitigen
Standardalternativen `e :- not f.` und `f :- not e.`.

### 2a. e ist nicht enthalten

1. `f :- not e.` wird zum Fakt. Daher `f ∈ M`.
2. Wegen `f ∈ M` wird die einzige `e`-Regel gelöscht. Sie kann kein `e`
   erzeugen.
3. Alle Atome sind damit bestimmt: `M2 = {b,f}`.

Der vollständige Redukt zu `M2` lautet:

```prolog
b.             % aus b :- not c.
c :- a.
c :- d.
d :- c, e.
f.
```

Die Regel `b :- not f.` ist gelöscht, ebenso die `a`- und die
Standard-`d`-Regel sowie die `e`-Regel.

```text
{} -> {b,f} -> {b,f}.
```

Der positive `c/d`-Kreis bleibt ohne Start; damit `LM(P^M2) = M2`.

### 2b. e ist enthalten

1. Wegen `e ∈ M` wird die einzige `f`-Regel gelöscht. Also `f ∉ M`.
2. Da `a,f ∉ M`, wird `e :- not a,not f.` zum Fakt `e.`.
3. Auch `b :- not f.` wird zum Fakt. Alle Atome sind damit festgelegt:
   `M3 = {b,e}`.

Der vollständige Redukt zu `M3`, mit beiden Herkunftsvorkommen von `b.`, ist:

```prolog
b.             % aus b :- not c.
b.             % aus b :- not f.
c :- a.
c :- d.
d :- c, e.
e.
```

```text
{} -> {b,e} -> {b,e}.
```

Auch mit dem Fakt `e` können `c` und `d` nicht erstmalig entstehen.
Somit `LM(P^M3) = M3`.

## 3. Vollständigkeit ohne Brute Force

Jedes Answer Set liegt entweder im Fall ohne `b` oder im Fall mit `b`.
Ohne `b` war nur `M1` möglich. Mit `b` waren `a,c,d` ausgeschlossen, und die
erschöpfenden Unterfälle `e ∉ M` und `e ∈ M` erzwingen jeweils `f` bzw.
das Fehlen von `f`. Sie liefern nur `M2` und `M3`.

Insbesondere können weder beide Atome `e,f` fehlen (dann würden beide
Standardregeln aktiv und zumindest `f` als Fakt erzeugt) noch beide enthalten
sein (dann wäre die einzige `f`-Regel gelöscht). Jeder der drei verbleibenden
Kandidaten wurde durch seinen vollständigen Redukt bestätigt. Die Liste
ist daher vollständig, ohne die Gesamtheit aller Interpretationen aufzuzählen.

Der Kandidat `{b,c,d,e}` aus Aufgabe 1.2 ist gerade **kein** zusätzlicher
Fall: `c` und `d` stützen sich dort nur gegenseitig. Sein Redukt hat das
kleinere Modell `{b,e}`.

## Erklärung der Programmdatei und tatsächliche Tests

Die neun Regeln in `programm.lp` sind dieselben ausführbaren Regeln wie
in `../../ue1.2/b/programm.lp`; kein Import ist zum Ausführen erforderlich.

- Die `not b`-Regeln für `a` und `d` begründen die Hauptfallunterscheidung.
- Die beiden Regeln für `b` sind Alternativen, keine gemeinsame Konjunktion.
- `c :- a.` bietet eine äußere Startableitung für `c`, wenn `a` entsteht.
- `c :- d.` und `d :- c,e.` können ohne diese äußere Ableitung keinen
  positiven Kreis von selbst starten.
- `e :- not a,not f.` verlangt das Fehlen beider Atome; `f :- not e.`
  liefert die dazugehörige Standardalternative.
- Der Kandidatenkommentar aus Aufgabe 1.2 ist semantisch wirkungslos.
  Es gibt keine Ergebnisfakten, Choice-Regeln oder Ausgabefilter.

Tatsächlich ausgeführt mit `/usr/bin/clingo` **5.6.2**:

```sh
clingo --outf=2 0 programm.lp
```

```text
Result: SATISFIABLE
Models.Number: 3
Models.More: no
Alle Atomemengen: {a,c,d,f}; {b,f}; {b,e}
Prozess-Exitcode: 30
```

Zusätzlich wurde ausgeführt:

```sh
python3 ../../ue1.2/pruefe_redukte.py
```

Der Prüfer bestätigte die genaue Struktur und die kleinsten Modelle aller
hier verwendeten Redukte unabhängig über Fixpunktbildung und clingo.
Er endete mit Exitcode `0`. Die vollständige Enumeration dient als Probe;
das Vollständigkeitsargument steht in den strukturellen Fällen oben.
