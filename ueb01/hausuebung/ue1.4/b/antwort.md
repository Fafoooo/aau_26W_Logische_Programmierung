# Homework 1 – Aufgabe 1.4 b

## Aufgabe und vollständiges Ergebnis

Zu bestimmen sind alle Answer Sets des normalen Grundprogramms mit
`num(1)`, `num(2)`, `num(3)`, den `lucky`/`unlucky`-Standardalternativen
und den drei Originalregeln für `p`.

Es gibt **genau vier** Answer Sets:

```text
M0 = {
  num(1),num(2),num(3),
  unlucky(1),unlucky(2),unlucky(3)
}

M1 = {
  num(1),num(2),num(3),
  lucky(1),unlucky(2),unlucky(3)
}

M2 = {
  num(1),num(2),num(3),
  unlucky(1),lucky(2),unlucky(3)
}

M3 = {
  num(1),num(2),num(3),
  unlucky(1),unlucky(2),lucky(3)
}
```

In keinem Answer Set ist `p` enthalten. Die Bezeichnungen `M0` bis `M3`
kennzeichnen hier die Zahl, die als einzige glücklich ist; bei `M0` ist
keine Zahl glücklich.

## 1. Für jede Zahl genau eine Alternative

Alle drei `num`-Atome sind Fakten. Für jede der Zahlen enthält das Programm
zwei wechselseitige Standardregeln, beispielsweise für `1`:

```prolog
lucky(1) :- num(1), not unlucky(1).
unlucky(1) :- num(1), not lucky(1).
```

- Fehlen beide Atome im Kandidaten, bleiben beide Regeln mit Rumpf `num(1)`
  im Redukt. Beide Köpfe werden dann aus dem Fakt abgeleitet; Stabilität
  scheitert.
- Sind beide Atome enthalten, werden beide Regeln gelöscht. Es gibt keine
  weitere definierende Regel für diese Köpfe; das kleinste Modell enthält
  keines der beiden Atome. Stabilität scheitert erneut.
- Ist genau eines enthalten, bleibt dessen Regel als positive Regel mit
  Rumpf `num(1)` erhalten, während die andere gelöscht wird. Genau diese
  Alternative wird dann abgeleitet.

Diese Argumentation gilt für jede Zahl, weil für `2` und `3` dieselben
beiden Regeltypen mit ihren jeweiligen Konstanten vorhanden sind. Somit
gehört für jede Zahl **genau eines** von `lucky(i)` und `unlucky(i)` zu
einem Answer Set.

## 2. p kann nicht in einem Answer Set liegen

Die einzigen Regeln mit Kopf `p` sind genau diese drei Grundregeln:

```prolog
p :- lucky(1), lucky(2), not p.
p :- lucky(1), lucky(3), not p.
p :- lucky(2), lucky(3), not p.
```

Angenommen, `p ∈ M`. Dann werden wegen `not p` **alle drei** Regeln aus
`P^M` gelöscht. Es gibt kein anderes Vorkommen von `p` als definierenden
Kopf. Daher wäre `p ∉ LM(P^M)`, im Widerspruch zur Stabilität. Also gilt
notwendig `p ∉ M`.

Es wäre falsch, `p` bei zwei glücklichen Zahlen einfach zusätzlich in die
Antwort aufzunehmen: Gerade dadurch verschwinden seine eigenen Regeln
bei der Reduktbildung.

## 3. Höchstens eine Zahl kann glücklich sein

Für einen möglichen stabilen Kandidaten gilt jetzt `p ∉ M`. Die drei
`p`-Regeln bleiben dann im Redukt und verlieren nur `not p`:

```prolog
p :- lucky(1), lucky(2).
p :- lucky(1), lucky(3).
p :- lucky(2), lucky(3).
```

Sind zwei verschiedene `lucky`-Atome enthalten und im kleinsten Modell
ableitbar, greift die passende dieser drei Regeln und leitet `p` ab. Das
widerspricht `p ∉ M = LM(P^M)`. Daher ist höchstens eine Zahl glücklich.

Zusammen mit genau einer Alternative je Zahl bleiben nur die vier oben
aufgeführten Möglichkeiten: keine glückliche Zahl, nur `1`, nur `2` oder
nur `3`. Die Originalregeln wirken unter stabiler Semantik wie ein Verbot
von zwei glücklichen Zahlen. Im Code werden sie trotzdem **nicht** durch
Constraints ersetzt, weil die wörtliche Angabe erhalten bleiben soll.

## 4. Existenz aller vier Mengen durch ihre Redukte

Für jeden der Kandidaten bleiben die drei `num`-Fakten und die drei eben
angegebenen positiven `p`-Regeln erhalten. Die jeweils gewählten
Alternativen werden genau durch folgende verbleibende Regeln erzeugt:

| Kandidat | Positive Alternativregeln im Redukt |
|---|---|
| `M0` | `unlucky(1) :- num(1).` / `unlucky(2) :- num(2).` / `unlucky(3) :- num(3).` |
| `M1` | `lucky(1) :- num(1).` / `unlucky(2) :- num(2).` / `unlucky(3) :- num(3).` |
| `M2` | `unlucky(1) :- num(1).` / `lucky(2) :- num(2).` / `unlucky(3) :- num(3).` |
| `M3` | `unlucky(1) :- num(1).` / `unlucky(2) :- num(2).` / `lucky(3) :- num(3).` |

Die drei entgegengesetzten Alternativregeln sind jeweils gelöscht.
Sei `N = {num(1),num(2),num(3)}`. Für jeden einzelnen Kandidaten verlaufen
die Fixpunktstufen so:

```text
Redukt zu M0: {} -> N -> M0 -> M0
Redukt zu M1: {} -> N -> M1 -> M1
Redukt zu M2: {} -> N -> M2 -> M2
Redukt zu M3: {} -> N -> M3 -> M3
```

In keinem dieser Fälle ist ein Rumpf der positiven `p`-Regeln erfüllt,
da jeweils höchstens ein `lucky`-Atom vorliegt. Also bleibt `p` abwesend.
Damit ist jeder Kandidat gleich dem kleinsten Modell seines Redukts.
Die vorangegangenen notwendigen Bedingungen schließen jede andere
Interpretation aus; die Ergebnisliste ist vollständig.

## Erklärung der Programmdatei

- `num(1). num(2). num(3).` setzt die drei Zahlen als Fakten.
- Die drei `lucky`-Regeln geben die glückliche Standardalternative je Zahl.
- Die drei `unlucky`-Regeln geben die gegenteilige Standardalternative je Zahl.
- Die drei `p`-Regeln bilden die drei ausdrücklich vorgegebenen Paare
  verschiedener Zahlen. Es sind weder Selbstpaare noch weitere Regeln
  ergänzt worden.
- Die allgemeine Regel mit `X != Y` ist wie in der PDF **auskommentiert**.
  Der ausführbare Teil ist vollständig ground und enthält keine Variablen.
- Die `p`-Regeln wurden weder entfernt noch durch Constraints oder
  Kardinalitätsregeln ersetzt. Es gibt kein `#show`, das `p` verbergen könnte.

Der eigentliche Widerspruch bei zwei glücklichen Zahlen entsteht aus
**Defaultnegation plus kleinstem Reduktmodell**, nicht aus einer speziellen
Syntaxbedeutung des Atoms `p`.

## Tatsächlich ausgeführter Test

Im Ordner dieser Datei wurde mit `/usr/bin/clingo` **5.6.2** ausgeführt:

```sh
clingo --outf=2 0 programm.lp
```

```text
Result: SATISFIABLE
Models.Number: 4
Models.More: no
Alle Atomemengen: genau M0, M1, M2, M3 wie oben vollständig ausgeschrieben
Prozess-Exitcode: 30
```

`0` fordert die vollständige Enumeration an. `Models.More: no` bestätigt,
dass nicht nur eine echte Teilmenge der Answer Sets angezeigt wurde.
