# Exercise 1.2 b

**Aufgabe:** Für das zweite normale Programm `X1={a,b,d,e}` und `X2={b,e}` auf Stabilität prüfen.

## X1={a,b,d,e}

Regeln in Reihenfolge der Angabe:
1. `a :- not b.` löschen, weil `b ∈ X1`.
2. `a :- d.` behalten.
3. `b :- not c.` wird `b.`, weil `c ∉ X1`.
4. `c :- a,not b.` löschen, weil `b ∈ X1`.
5. `d :- a.` behalten.
6. `d :- not c,not e.` löschen, weil `e ∈ X1`; ein verletztes negatives Literal reicht zum Löschen der ganzen Regel.
7. `e :- b,not a.` löschen, weil `a ∈ X1`.
8. `e :- d.` behalten.

Redukt:
```asp
a :- d.
b.
d :- a.
e :- d.
```

Fixpunkt:
```text
I0={}
I1={b}
I2={b}=I1
```

`a` und `d` hängen nur voneinander ab. Ohne Fakt in diesem Kreis wird keines von beiden abgeleitet. Damit fehlt auch die Voraussetzung für `e`.

`LM(P^X1)={b} ≠ X1`. **X1 ist kein Answer Set**, obwohl es ein klassisches Modell ist. Ein Modelltest allein genügt nicht.

## X2={b,e}

1. `a :- not b.` löschen, weil `b ∈ X2`.
2. `a :- d.` behalten.
3. `b :- not c.` wird `b.`, weil `c ∉ X2`.
4. `c :- a,not b.` löschen, weil `b ∈ X2`.
5. `d :- a.` behalten.
6. `d :- not c,not e.` löschen, weil `e ∈ X2`.
7. `e :- b,not a.` wird `e :- b.`, weil `a ∉ X2`.
8. `e :- d.` behalten.

Redukt:
```asp
a :- d.
b.
d :- a.
e :- b.
e :- d.
```

Fixpunkt:
```text
I0={}
I1={b}
I2={b,e}         (e :- b.)
I3={b,e}=I2
```

`LM(P^X2)={b,e}=X2`. **X2 ist ein Answer Set.** Die zyklischen Atome `a,d` bleiben draußen, `c` hat im Redukt keine Regel, und `b,e` sind vollständig begründet.

**Ergebnis:** X1 nein, X2 ja. Zentrale Tests bestätigen die Reduktfixpunkte und die Entscheidungen.

Ausführen: `clingo programm.lp 0`; prüfen: `python3 ../../../checks.py`.
