# Exercise 1.4 b

**Aufgabe:** Alle Answer Sets des Programms mit drei Zahlen, `lucky`, `unlucky` und `p` bestimmen.

Die drei Fakten erzwingen `N={num(1),num(2),num(3)}`.

## Genau ein Glückszustand pro Zahl

Für Zahl 1:
- Fehlen `lucky(1)` und `unlucky(1)`, bleiben beide Regeln erhalten und leiten über `num(1)` beide ab: nicht stabil.
- Sind beide enthalten, entfallen beide Regeln: nicht unterstützt.
- Nur `lucky(1)` wird durch den Redukt `lucky(1) :- num(1).` reproduziert.
- Nur `unlucky(1)` wird durch `unlucky(1) :- num(1).` reproduziert.

Für Zahl 2:
- Fehlen `lucky(2)` und `unlucky(2)`, bleiben beide Regeln erhalten und leiten über `num(2)` beide ab: nicht stabil.
- Sind beide enthalten, entfallen beide Regeln: nicht unterstützt.
- Nur `lucky(2)` wird durch `lucky(2) :- num(2).` reproduziert.
- Nur `unlucky(2)` wird durch `unlucky(2) :- num(2).` reproduziert.

Für Zahl 3:
- Fehlen `lucky(3)` und `unlucky(3)`, bleiben beide Regeln erhalten und leiten über `num(3)` beide ab: nicht stabil.
- Sind beide enthalten, entfallen beide Regeln: nicht unterstützt.
- Nur `lucky(3)` wird durch `lucky(3) :- num(3).` reproduziert.
- Nur `unlucky(3)` wird durch `unlucky(3) :- num(3).` reproduziert.

## Wirkung der drei p-Regeln

1. Angenommen `p ∈ M`. Alle drei `p`-Regeln enthalten `not p` und werden im Redukt gelöscht. Keine andere Regel hat Kopf `p`. Damit fehlt `p` im kleinsten Reduktmodell: Widerspruch zur Stabilität.
2. Also muss `p ∉ M` gelten.
3. Dann lauten die drei Regeln im Redukt `p :- unlucky(1).`, `p :- unlucky(2).`, `p :- unlucky(3).`.
4. Enthielte `M` `unlucky(1)`, würde dessen eigene Reduktregel es ableiten; danach würde die erste `p`-Regel `p` ableiten: Widerspruch.
5. Enthielte `M` `unlucky(2)`, würde dessen eigene Reduktregel es ableiten; danach würde die zweite `p`-Regel `p` ableiten: Widerspruch.
6. Enthielte `M` `unlucky(3)`, würde dessen eigene Reduktregel es ableiten; danach würde die dritte `p`-Regel `p` ableiten: Widerspruch.
7. Keine Zahl ist daher `unlucky`. Nach der vorherigen Zustandsanalyse müssen alle drei Zahlen `lucky` sein.

## Ergebnis und Probe

Das einzige mögliche Answer Set ist
```text
M={num(1),num(2),num(3),lucky(1),lucky(2),lucky(3)}.
```

Vollständiger Redukt:
```asp
num(1). num(2). num(3).
lucky(1) :- num(1).
lucky(2) :- num(2).
lucky(3) :- num(3).
p :- unlucky(1).
p :- unlucky(2).
p :- unlucky(3).
```

Die `unlucky`-Regeln entfallen, weil die jeweiligen `lucky`-Atome in `M` liegen. Fixpunkt: `{}` → `N` → `M` → unverändert. Keine `unlucky`-Regel ist übrig; deshalb kann keine der `p`-Regeln auslösen. Der Fixpunkt ist gleich dem Kandidaten, der somit stabil ist. Die vorherigen Ausschlüsse beweisen Vollständigkeit. □

Ausführen: `clingo programm.lp 0`; prüfen: `python3 ../../../checks.py`.
