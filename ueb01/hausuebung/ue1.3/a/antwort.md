# Homework 1 – Aufgabe 1.3 a

## Aufgabe und vollständiges Ergebnis

Alle Answer Sets des Programms aus **Aufgabe 1.2 a** sind zu bestimmen, ohne
alle Interpretationen durchzuprobieren. Dieser Ordner enthält dafür eine
eigenständig ausführbare Kopie des vollständigen Grundprogramms:

```prolog
a :- not d.
b :- not a.
b :- e, not d.
c :- a, not e.
c :- b, not e.
d :- not a, not e.
e :- a, d.
e :- b, not c.
```

**Genau diese beiden Answer Sets existieren:**

```text
M1 = {a,c}
M2 = {b,c,d}
```

Die Kandidaten im Blockkommentar der Programmdatei stammen aus Aufgabe 1.2.
Sie schränken die Berechnung nicht ein.

## Semantische Grundlage

Für ein Answer Set `M` muss `M = LM(P^M)` gelten. Beim GL-Redukt werden
Regeln mit einem in `M` verletzten `not`-Literal gelöscht; aus allen übrigen
Regeln entfernt man die Defaultnegation. Das positive Resultat hat ein
kleinstes Modell, das ab `{}` durch Regelanwendung entsteht. Ein Atom ohne
mögliche Anfangsableitung kann dabei nicht allein durch einen positiven
Kreis entstehen.

Wir nutzen diese Eigenschaft für strukturelle Fallunterscheidungen. Wir
zählen **nicht** alle Teilmengen der Atome auf.

## 1. In keinem Answer Set kann e enthalten sein

Angenommen, `e ∈ M` für ein Answer Set `M`.

1. Beide Regeln mit Kopf `c` enthalten `not e` und werden aus `P^M` gelöscht.
   Daher ist `c ∉ LM(P^M)` und wegen Stabilität auch `c ∉ M`.
2. Die einzige Regel mit Kopf `d` enthält ebenfalls `not e` und wird gelöscht.
   Deshalb `d ∉ M`.
3. Weil `d ∉ M`, wird `a :- not d.` zum Fakt `a.`. Also `a ∈ M`.
4. Weil `a ∈ M`, wird `b :- not a.` gelöscht. Die zweite `b`-Regel wird
   wegen `d ∉ M` zu `b :- e.`.
5. Wegen `c ∉ M` wird `e :- b,not c.` zu `e :- b.`. Die andere `e`-Regel
   `e :- a,d.` bleibt zwar stehen, kann aber ohne ableitbares `d` nicht greifen.
6. Die einzigen verbleibenden Möglichkeiten für `b` und `e` sind somit
   `b :- e.` und `e :- b.`. Es gibt weder ein Faktatom in diesem Kreis noch
   eine erfolgreiche Ableitung von außerhalb. Ab `{}` wird nur `a` erzeugt.

Folglich wäre `LM(P^M) = {a}`, im Widerspruch zu `e ∈ M`. Also gilt in
**jedem** Answer Set `e ∉ M`. Der Ausschluss beruht auf kleinsten Modellen,
nicht bloß darauf, dass sich zwei Atome gegenseitig begründen.

## 2. Fall a ist enthalten

Nun gilt bereits `e ∉ M`. Nehmen wir zusätzlich `a ∈ M` an.

1. `d :- not a,not e.` wird wegen `a ∈ M` gelöscht. Es gibt keinen anderen
   Kopf `d`; daher `d ∉ M`.
2. `a :- not d.` wird damit zum Fakt `a.` und begründet das angenommene `a`.
3. `b :- not a.` wird gelöscht. `b :- e,not d.` kann kein `b` liefern,
   weil `e` nach dem ersten Beweisschritt nicht ableitbar ist. Also `b ∉ M`.
4. Weil `e ∉ M`, bleibt `c :- a.` im Redukt; aus `a` folgt `c ∈ M`.
5. Alle Köpfe des Programms sind damit festgelegt. Einzig möglicher Kandidat
   dieses Falls ist `M1 = {a,c}`.

**Existenzprüfung:** Der vollständige Redukt zu `M1` ist

```prolog
a.
b :- e.
c :- a.
c :- b.
e :- a, d.
```

Sein Fixpunkt entsteht durch

```text
{} -> {a} -> {a,c} -> {a,c}.
```

Also `LM(P^M1) = M1`; der Kandidat ist tatsächlich ein Answer Set.

## 3. Fall a ist nicht enthalten

Es gilt weiterhin `e ∉ M`; nun nehmen wir `a ∉ M` an.

1. `d :- not a,not e.` wird zum Fakt `d.`. Also `d ∈ M`.
2. Daher wird `a :- not d.` gelöscht; das Fehlen von `a` ist mit dem
   Redukt vereinbar.
3. `b :- not a.` wird zum Fakt `b.`. Also `b ∈ M`.
4. Wegen `e ∉ M` wird `c :- b,not e.` zu `c :- b.`. Somit `c ∈ M`.
5. `e :- a,d.` kann ohne `a` nicht greifen; `e :- b,not c.` wird wegen
   `c ∈ M` gelöscht. Es wird kein `e` erzeugt.
6. Einzig möglicher Kandidat dieses Falls ist daher `M2 = {b,c,d}`.

**Existenzprüfung:** Der vollständige Redukt zu `M2` ist

```prolog
b.
c :- a.
c :- b.
d.
e :- a, d.
```

Sein Fixpunkt entsteht durch

```text
{} -> {b,d} -> {b,c,d} -> {b,c,d}.
```

Also `LM(P^M2) = M2`; auch dieser Kandidat ist ein Answer Set.

## 4. Warum ist die Liste vollständig?

Der erste Beweisschritt schließt sämtliche Kandidaten mit `e` aus. Für
Kandidaten ohne `e` sind die beiden Fälle `a ∈ M` und `a ∉ M` erschöpfend.
In jedem Fall bestimmen die Regeln alle übrigen Atome eindeutig. Beide
verbleibenden Mengen haben ihre Reduktprüfung bestanden. Weitere Atome
können in einem kleinsten Reduktmodell nicht ohne Regelkopf entstehen.
Damit gibt es **genau** `{a,c}` und `{b,c,d}`.

## Erklärung der Programmdatei und Tests

`programm.lp` enthält dieselben acht ausführbaren Regeln wie
`../../ue1.2/a/programm.lp`; nur die Aufgabenbeschreibung im Kommentar ist
angepasst. Die Datei braucht beim Ausführen keine weitere `.lp`-Datei.

- Die beiden Standardregeln für `a` und `b` steuern die Fallaufteilung.
- `b :- e,not d.` und `e :- b,not c.` können nach der Reduktbildung einen
  positiven Kreis bilden; dieser erzeugt ohne Startableitung keine Atome.
- Die zwei `c`-Regeln gelten nur ohne `e`.
- Die einzige `d`-Regel verlangt gleichzeitig das Fehlen von `a` und `e`.
- `e :- a,d.` ist positiv und bleibt bei jedem GL-Redukt stehen; ihre
  Anwendbarkeit ist erst bei der Fixpunktberechnung zu entscheiden.
- Kein Ergebnis wurde als Fakt ergänzt, keine globale Modellliste erraten
  oder mittels `#show` auf eine Teilmenge projiziert.

Tatsächlich ausgeführt mit `/usr/bin/clingo` **5.6.2**, in diesem Ordner:

```sh
clingo --outf=2 0 programm.lp
```

```text
Result: SATISFIABLE
Models.Number: 2
Models.More: no
Alle Atomemengen: {a,c}; {b,c,d}
Prozess-Exitcode: 30
```

Zusätzlich prüft der ausgeführte Befehl

```sh
python3 ../../ue1.2/pruefe_redukte.py
```

beide hier angegebenen positiven Redukte einschließlich ihres Fixpunkts
und ihrer clingo-Modelle. Der Prüfer endete erfolgreich mit Exitcode `0`.
Die Solver-Enumeration bestätigt die Herleitung; sie ersetzt nicht die
obige Vollständigkeitsbegründung.
