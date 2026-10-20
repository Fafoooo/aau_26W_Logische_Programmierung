# Exercise 1.3 a

**Aufgabe:** Alle Answer Sets des Programms aus Exercise 1.2 a bestimmen, ohne alle Interpretationen aufzuzählen. `programm.lp` enthält dieselben fünf Regeln noch einmal, damit dieser Ordner eigenständig ausführbar ist.

`e.` ist ein Fakt, daher gehört `e` zu jedem Answer Set. Die einzigen Regeln für `b,c` sind `b :- not c.` und `c :- not b.`.

- Fehlen beide Atome, werden beide Regeln im Redukt zu Fakten; die Ausgangsmenge wird nicht reproduziert.
- Sind beide enthalten, werden beide Regeln gelöscht; weder `b` noch `c` hat dann Unterstützung im kleinsten Modell.
- Daher ist in einem Answer Set **genau eines** der Atome `b,c` enthalten. Es bleiben zwei Fälle.

## Fall b enthalten, c nicht enthalten

- `b :- not c.` begründet `b`.
- `a :- b.` erzwingt `a`.
- `e.` erzwingt `e`.
- `d :- a,e.` erzwingt `d`.
- Der einzige mögliche Kandidat dieses Falls ist `{a,b,d,e}`.

Redukt:
```asp
a :- b.
b.
d :- a,e.
e.
```
Probe durch Fixpunkt: `{}` → `{b,e}` → `{a,b,e}` → `{a,b,d,e}` → unverändert. Der Kandidat ist stabil.

## Fall c enthalten, b nicht enthalten

- `c :- not b.` begründet `c`.
- `e.` begründet `e`.
- `a :- b.` kann ohne `b` kein `a` erzeugen; eine andere `a`-Regel existiert nicht.
- `d :- a,e.` kann ohne `a` kein `d` erzeugen; eine andere `d`-Regel existiert nicht.
- Der einzige mögliche Kandidat dieses Falls ist `{c,e}`.

Redukt:
```asp
a :- b.
c.
d :- a,e.
e.
```
Probe durch Fixpunkt: `{}` → `{c,e}` → unverändert. Der Kandidat ist stabil.

**Ergebnis:** Genau `{a,b,d,e}` und `{c,e}`. Die zwei Fälle decken jede mögliche stabile Belegung von `b,c` ab; in jedem Fall sind alle weiteren Atome festgelegt. □

Ausführen: `clingo programm.lp 0`. Zentrale Tests vergleichen dieses Programm mit 1.2 a und prüfen alle Modelle durch clingo und einen unabhängigen Reduktprüfer.
