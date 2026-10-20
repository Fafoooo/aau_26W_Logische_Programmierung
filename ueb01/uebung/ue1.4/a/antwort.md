# Exercise 1.4 a

**Aufgabe:** Alle Answer Sets des Vogelprogramms in `programm.lp` bestimmen.

## Gemeinsamer Anteil

`canary(tweety).` und `penguin(tux).` sind Fakten. Die zwei positiven Vogelregeln liefern `bird(tweety)` bzw. `bird(tux)`. Daher ist in jedem Answer Set
```text
F={canary(tweety),penguin(tux),bird(tweety),bird(tux)}
```
enthalten.

## Gesundheitszustand

Für Tweety gelten die zwei Regeln:
```asp
injured(tweety) :- not ok(tweety), bird(tweety).
ok(tweety) :- not injured(tweety), bird(tweety).
```
- Fehlen beide Zustände, bleiben beide Regeln im Redukt ohne Negation und leiten nach `bird(tweety)` beide Zustände ab; der Kandidat ist nicht stabil.
- Sind beide Zustände enthalten, werden beide Regeln gelöscht; die Zustände fehlen im kleinsten Reduktmodell; der Kandidat ist nicht stabil.
- Ist nur `injured(tweety)` enthalten, bleibt die verletzte Regel als `injured(tweety) :- bird(tweety).`; die andere entfällt. Genau der gewählte Zustand wird reproduziert.
- Ist nur `ok(tweety)` enthalten, bleibt `ok(tweety) :- bird(tweety).`; die andere entfällt. Genau der gewählte Zustand wird reproduziert.

Für Tux gelten zwei eigene Regeln:
```asp
injured(tux) :- not ok(tux), bird(tux).
ok(tux) :- not injured(tux), bird(tux).
```
- Fehlen beide Zustände, leiten beide erhaltenen Reduktregeln nach `bird(tux)` beide Zustände ab; keine Stabilität.
- Sind beide enthalten, werden beide Regeln gelöscht; keine Unterstützung im Redukt.
- Ist nur `injured(tux)` enthalten, bleibt `injured(tux) :- bird(tux).`; die `ok`-Regel entfällt.
- Ist nur `ok(tux)` enthalten, bleibt `ok(tux) :- bird(tux).`; die Verletzungsregel entfällt.

Jeder Vogel hat daher genau einen Zustand. Zwischen den beiden Zustandsentscheidungen besteht keine Abhängigkeit.

## Fliegen

- `penguin(tweety)` hat keine definierende Regel und fehlt deshalb in jedem Answer Set. Die Flugregel für Tweety bleibt im Redukt als `flies(tweety) :- ok(tweety).`. Tweety fliegt genau bei Zustand `ok`.
- `penguin(tux)` ist ein Fakt. Die Flugregel für Tux wird bei jedem Kandidaten mit diesem Fakt gelöscht. `flies(tux)` kann deshalb nicht entstehen, auch wenn Tux `ok` ist.

## Ergebnis: genau vier Answer Sets

```text
M1=F ∪ {injured(tweety),injured(tux)}
M2=F ∪ {injured(tweety),ok(tux)}
M3=F ∪ {ok(tweety),injured(tux),flies(tweety)}
M4=F ∪ {ok(tweety),ok(tux),flies(tweety)}
```

## Reduktproben

Jeweils ab `{}`:
- M1: Fakten → Fakten plus beide Vögel → zusätzlich `injured(tweety),injured(tux)` → unverändert.
- M2: Fakten → Fakten plus beide Vögel → zusätzlich `injured(tweety),ok(tux)` → unverändert.
- M3: Fakten → Fakten plus beide Vögel → zusätzlich `ok(tweety),injured(tux)` → zusätzlich `flies(tweety)` → unverändert.
- M4: Fakten → Fakten plus beide Vögel → zusätzlich `ok(tweety),ok(tux)` → zusätzlich `flies(tweety)` → unverändert.

Die vier Fixpunkte sind genau die vier Kandidaten. Jede andere Gesundheitsbelegung wurde ausgeschlossen; die übrigen Atome sind durch Fakten, positive Regeln und die Flugbedingungen festgelegt. □

Ausführen: `clingo programm.lp 0`. Der zentrale Test vergleicht die vollständigen Atomlisten aller vier Modelle mit clingo und GL-Reduktprüfung.
