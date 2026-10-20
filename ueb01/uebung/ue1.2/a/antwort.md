# Exercise 1.2 a

**Aufgabe:** Sind `X1={a,b,d,e}` und `X2={b,e}` Answer Sets des Programms in `programm.lp`?

**GL-Redukt:** Zuerst jede Regel löschen, die ein `not q` mit `q ∈ X` enthält. Danach aus den übrigen Regeln alle negativen Literale entfernen. Eine Menge `X` ist genau dann stabil, wenn sie gleich dem kleinsten Modell dieses positiven Redukts ist.

## X1={a,b,d,e}

- `a :- b.` bleibt unverändert.
- `b :- not c.` bleibt, weil `c ∉ X1`; nach Entfernen des negativen Literals entsteht `b.`.
- `c :- not b.` wird gelöscht, weil `b ∈ X1`.
- `d :- a,e.` bleibt unverändert.
- `e.` bleibt unverändert.

Redukt:
```asp
a :- b.
b.
d :- a,e.
e.
```

Synchroner Fixpunkt:
```text
I0={}
I1={b,e}          (Fakten)
I2={a,b,e}        (a :- b.)
I3={a,b,d,e}      (d :- a,e.)
I4=I3
```

`LM(P^X1)=X1`. **X1 ist ein Answer Set.**

## X2={b,e}

- `a :- b.` bleibt unverändert.
- `b :- not c.` wird zu `b.`, weil `c ∉ X2`.
- `c :- not b.` wird gelöscht, weil `b ∈ X2`.
- `d :- a,e.` bleibt unverändert.
- `e.` bleibt unverändert.

Redukt:
```asp
a :- b.
b.
d :- a,e.
e.
```

Synchroner Fixpunkt:
```text
I0={}
I1={b,e}
I2={a,b,e}
I3={a,b,d,e}
I4=I3
```

`LM(P^X2)={a,b,d,e} ≠ {b,e}`. **X2 ist kein Answer Set.** Schon im ursprünglichen Programm verletzt `X2` die Regel `a :- b.`, weil `b` wahr ist und `a` fehlt.

**Ergebnis:** X1 ja, X2 nein. Die Menge aller Answer Sets wird in Exercise 1.3 a bestimmt. Der zentrale Test überprüft die Reduktfixpunkte und beide Entscheidungen.

Ausführen: `clingo programm.lp 0`; prüfen: `python3 ../../../checks.py`.
