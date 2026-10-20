# Homework 1 – Aufgabe 1.2 a

## Aufgabe und unverändertes Programm

Für die Kandidaten `X1 = {}`, `X2 = {a,c}` und `X3 = {a,b,e}` sollen die
Gelfond–Lifschitz-Redukte bestimmt und die Answer-Set-Eigenschaft geprüft werden.
`programm.lp` enthält die Originalregeln, hier zur Zuordnung nummeriert:

| Nummer | Originalregel |
|---|---|
| r1 | `a :- not d.` |
| r2 | `b :- not a.` |
| r3 | `b :- e, not d.` |
| r4 | `c :- a, not e.` |
| r5 | `c :- b, not e.` |
| r6 | `d :- not a, not e.` |
| r7 | `e :- a, d.` |
| r8 | `e :- b, not c.` |

Insbesondere ist `not e` in r6 eine Negation im Rumpf und **kein** Fakt `e`.
Der Block mit `X1`, `X2`, `X3` ist ein mehrzeiliger Kommentar, kein ASP-Code.

## Verwendete Definition

Für einen festen Kandidaten `X` entsteht `P^X` in zwei Schritten:

1. Eine Regel vollständig löschen, wenn sie ein Rumpfliteral `not q` mit
   `q ∈ X` enthält.
2. Aus jeder verbleibenden Regel alle `not`-Literale entfernen.

Positive Rumpfatome werden dabei **nicht** anhand des Kandidaten ersetzt oder
vereinfacht. Danach wird das kleinste Modell `LM(P^X)` des positiven Redukts
ab `{}` berechnet. Genau dann, wenn **`LM(P^X) = X`**, ist `X` ein Answer Set.
Nur Modellsein oder gegenseitige Unterstützung im Kandidaten reicht nicht.

## Kandidat X1 = {}

Keine Regel wird gelöscht, weil kein negiertes Atom im Kandidaten liegt.
Der **vollständige, nicht weiter vereinfachte** Redukt lautet:

```prolog
a.             % r1
b.             % r2
b :- e.        % r3
c :- a.        % r4
c :- b.        % r5
d.             % r6
e :- a, d.     % r7
e :- b.        % r8
```

Insbesondere wird r6 zum Fakt `d.`: Beide negativen Rumpfliterale entfallen.
Die Berechnung mit synchronem unmittelbarem Folgerungsoperator liefert:

```text
I0 = {}
I1 = {a,b,d}        -- Fakten r1, r2, r6
I2 = {a,b,c,d,e}    -- c durch r4/r5, e durch r7/r8
I3 = I2            -- Fixpunkt
```

Damit ist `LM(P^X1) = {a,b,c,d,e} ≠ {}`.
**X1 ist kein Answer Set.**

## Kandidat X2 = {a,c}

Gelöscht werden r2 und r6 wegen `not a` sowie r8 wegen `not c`.
Die übrigen negierten Atome `d` und `e` liegen nicht in `X2`.
Der genaue Redukt ist:

```prolog
a.             % r1
b :- e.        % r3
c :- a.        % r4
c :- b.        % r5
e :- a, d.     % r7
```

Die positiven Regeln r3, r5 und r7 bleiben im Redukt, obwohl einige ihrer
Rumpfatome später nicht ableitbar sein werden. Solches Vereinfachen gehört
nicht zur GL-Reduktbildung.

```text
I0 = {}
I1 = {a}       -- Fakt r1
I2 = {a,c}     -- r4
I3 = I2       -- weder d noch e oder b kann neu abgeleitet werden
```

`d` hat im Redukt keine definierende Regel. Deshalb greift r7 nicht; ohne
`e` greift r3 nicht. Es bleibt beim Fixpunkt `{a,c}`.
**X2 ist ein Answer Set**, da `LM(P^X2) = X2`.

## Kandidat X3 = {a,b,e}

Gelöscht werden r2 wegen `not a`, r4 und r5 wegen `not e`, sowie r6 wegen
`not a` und `not e`. r8 bleibt erhalten: `c` liegt nicht in `X3`.
Der genaue Redukt lautet:

```prolog
a.             % r1
b :- e.        % r3
e :- a, d.     % r7
e :- b.        % r8
```

```text
I0 = {}
I1 = {a}       -- Fakt r1
I2 = I1       -- Fixpunkt
```

`d` kann nicht abgeleitet werden. Daher liefert `e :- a,d.` kein `e`.
Die verbleibenden Regeln `b :- e.` und `e :- b.` bilden einen **unbegründeten
positiven Kreis**: Keine der beiden Regeln kann das erste Kreisatom liefern.

`X3` erfüllt zwar die Regeln des Redukts und beide Kreisatome haben darin
gegenseitige Unterstützung. Dennoch besitzt der Redukt das kleinere Modell
`{a}`. Es gilt `LM(P^X3) = {a} ≠ {a,b,e}`.
**X3 ist kein Answer Set.**

## Zusammenfassung

| Kandidat X | Kleinstes Modell des genauen Redukts | Answer Set? |
|---|---|---|
| `{}` | `{a,b,c,d,e}` | Nein |
| `{a,c}` | `{a,c}` | Ja |
| `{a,b,e}` | `{a}` | Nein |

## Erklärung und Ausführung der Programmdatei

`programm.lp` berechnet die Answer Sets des **Originalprogramms**, nicht nur
die vorgegebenen Kandidaten. r1/r2 geben Standardableitungen für `a`/`b`,
r3 kann `b` zusätzlich aus `e` gewinnen, r4/r5 liefern `c`, sofern `e` nicht
gilt, r6 liefert `d` nur ohne `a` und `e`, r7/r8 sind die zwei Wege zu `e`.
Die Negation ist Defaultnegation: `not q` wird relativ zum Kandidaten
geprüft und ist kein neu erzeugtes Atom. Es gibt keine klassischen
Negationsatome, Choice-Regeln, Zusatzfakten oder Ausgabefilter.

Tatsächlich ausgeführter Test mit `/usr/bin/clingo` **5.6.2**, in diesem Ordner:

```sh
clingo --outf=2 0 programm.lp
```

```text
Result: SATISFIABLE
Models.Number: 2
Models.More: no
Alle Answer Sets: {a,c}; {b,c,d}
Prozess-Exitcode: 30
```

Die Vollständigkeitsbegründung für diese beiden Mengen steht zusätzlich
selbstständig in `../../ue1.3/a/antwort.md`. Die Menge `{b,c,d}` ist nicht
unter den drei in Aufgabe 1.2 vorgegebenen Kandidaten.

Die **exakten Reduktregeln und ihre kleinsten Modelle** wurden außerdem
maschinell geprüft:

```sh
python3 ../pruefe_redukte.py
```

Der Prüfer vergleicht die Regelstruktur mit unabhängigen Solltexten,
berechnet die Fixpunkte und lässt clingo alle Modelle jedes positiven
Redukts über stdin aufzählen. Ergebnis: alle Prüfungen bestanden, Exitcode `0`.
