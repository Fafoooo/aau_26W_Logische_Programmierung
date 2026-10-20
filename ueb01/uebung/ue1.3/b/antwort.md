# Exercise 1.3 b

**Aufgabe:** Alle Answer Sets des zweiten Programms aus Exercise 1.2 bestimmen. Die acht Regeln sind in diesem Ordner als `programm.lp` wiederholt.

Die einzige Regel mit Kopf `b` ist `b :- not c.`.
- Wenn `c` fehlt, wird diese Regel im Redukt zum Fakt `b.`; ein stabiler Kandidat muss dann `b` enthalten.
- Wenn `c` enthalten ist, wird diese Regel gelöscht; ein stabiler Kandidat kann dann kein `b` enthalten.
Damit bleiben genau die Fälle `b` fehlt / `b` enthalten.

## Fall 1: b fehlt

1. Wegen `a :- not b.` muss `a` enthalten sein.
2. Wegen `c :- a,not b.` muss `c` enthalten sein.
3. Wegen `d :- a.` muss `d` enthalten sein.
4. Wegen `e :- d.` muss `e` enthalten sein.
5. Der Kandidat ist zwingend `M1={a,c,d,e}`.

Redukt:
```asp
a.
a :- d.
c :- a.
d :- a.
e :- d.
```
Die Regel für `b` entfällt wegen `c`; die doppelt negative `d`-Regel entfällt wegen `c` und `e`; die `e`-Regel mit `not a` entfällt wegen `a`.

Fixpunktprobe:
```text
{} → {a} → {a,c,d} → {a,c,d,e} → unverändert
```
Also ist `M1` stabil.

## Fall 2: b enthalten

Dann muss `c` fehlen: Die einzige `c`-Regel enthält `not b` und entfällt im Redukt.

### Fall 2.1: a fehlt

- `d` muss fehlen, weil `a :- d.` sonst `a` erzwingen würde.
- `e :- b,not a.` erzwingt `e`.
- Der Kandidat ist zwingend `M2={b,e}`.

Redukt:
```asp
a :- d.
b.
d :- a.
e :- b.
e :- d.
```
Die doppelt negative `d`-Regel entfällt wegen `e`. Der Fixpunkt ist `{}` → `{b}` → `{b,e}` → unverändert. `a,d` haben keinen Anfangsfakt. Also ist `M2` stabil.

### Fall 2.2: a enthalten

- `d :- a.` erzwingt `d`.
- `e :- d.` erzwingt `e`.
- Der einzige Kandidat ist `{a,b,d,e}`.
- Wegen `b` entfällt `a :- not b.`.
- Wegen `e` entfällt `d :- not c,not e.`.
- Wegen `a` entfällt `e :- b,not a.`.

Der Redukt lautet:
```asp
a :- d.
b.
d :- a.
e :- d.
```
Sein Fixpunkt ist `{}` → `{b}` → unverändert. Damit werden `a,d,e` nicht reproduziert; dieser Fall liefert kein Answer Set.

**Ergebnis:** Genau `{a,c,d,e}` und `{b,e}`. Die Fallunterscheidung legt jedes Atom fest und schließt den einzigen verbleibenden Kandidaten durch seine fehlende Reduktunterstützung aus. □

Ausführen: `clingo programm.lp 0`; zentrale Prüfung: `python3 ../../../checks.py`.
