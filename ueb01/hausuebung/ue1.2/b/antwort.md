# Homework 1 – Aufgabe 1.2 b

## Aufgabe und Originalregeln

Zu prüfen sind `X1 = {a,c,d,f}`, `X2 = {b,c,d,e}` und `X3 = {b,e}`.
Die Nummern beziehen sich auf das unveränderte Programm in `programm.lp`:

| Nummer | Originalregel |
|---|---|
| r1 | `a :- not b.` |
| r2 | `b :- not c.` |
| r3 | `b :- not f.` |
| r4 | `c :- a.` |
| r5 | `c :- d.` |
| r6 | `d :- c, e.` |
| r7 | `d :- not b.` |
| r8 | `e :- not a, not f.` |
| r9 | `f :- not e.` |

r8 enthält zwei negative Rumpfliterale. Insbesondere steht in der Angabe
**kein** Fakt `f.`. Die Kandidaten im Blockkommentar sind keine Eingabefakten.

## GL-Redukt und Stabilitätskriterium

Für `P^X` wird jede Regel gelöscht, die `not q` mit `q ∈ X` enthält.
Aus den verbleibenden Regeln entfernt man ausschließlich die negativen
Literale. Die positiven Rumpfatome bleiben stehen. Ein Kandidat ist genau
dann ein Answer Set, wenn er mit dem **kleinsten** Modell dieses positiven
Redukts übereinstimmt. Dieses Modell wird ohne Vorannahmen ab `{}` hergeleitet.

## Kandidat X1 = {a,c,d,f}

Gelöscht werden r2 wegen `not c`, r3 wegen `not f` und r8 wegen `not a`
und `not f`. Da `b` und `e` nicht in `X1` liegen, bleiben r1, r7 und r9.
Der genaue Redukt lautet:

```prolog
a.             % r1
c :- a.        % r4
c :- d.        % r5
d :- c, e.     % r6
d.             % r7
f.             % r9
```

Auch `d :- c,e.` bleibt Teil des Redukts. Dass `e` nicht ableitbar ist,
rechtfertigt keine zusätzliche Löschung bei der Reduktbildung.

```text
I0 = {}
I1 = {a,d,f}      -- Fakten r1, r7, r9
I2 = {a,c,d,f}    -- c durch r4 und r5
I3 = I2          -- Fixpunkt
```

Daher `LM(P^X1) = X1`.
**X1 ist ein Answer Set.**

## Kandidat X2 = {b,c,d,e}

Gelöscht werden r1 und r7 wegen `not b`, r2 wegen `not c` sowie r9 wegen
`not e`. `a` und `f` fehlen im Kandidaten; r8 wird deshalb zu `e.`.
Der genaue Redukt ist:

```prolog
b.             % r3
c :- a.        % r4
c :- d.        % r5
d :- c, e.     % r6
e.             % r8
```

```text
I0 = {}
I1 = {b,e}     -- Fakten r3 und r8
I2 = I1       -- Fixpunkt
```

`a` hat keine definierende Regel. Für `c` bleibt deshalb nur `c :- d.`;
für `d` bleibt nur `d :- c,e.`. Der Fakt `e` erfüllt zwar einen Teil des
zweiten Rumpfs, liefert aber weder das erste `c` noch das erste `d`.
Der positive Kreis `{c,d}` ist unbegründet.

Der Kandidat `{b,c,d,e}` ist ein Modell des Redukts, aber nicht dessen
kleinstes Modell: `{b,e}` erfüllt bereits alle Regeln. Also
`LM(P^X2) = {b,e} ≠ X2`.
**X2 ist kein Answer Set.**

## Kandidat X3 = {b,e}

Gelöscht werden r1 und r7 wegen `not b` und r9 wegen `not e`.
`c`, `f` und `a` fehlen im Kandidaten, daher bleiben sowohl r2 als auch r3
als Fakten und r8 wird ebenfalls ein Fakt. Der genaue Redukt einschließlich
der beiden aus verschiedenen Regeln entstandenen `b.`-Vorkommen ist:

```prolog
b.             % r2
b.             % r3
c :- a.        % r4
c :- d.        % r5
d :- c, e.     % r6
e.             % r8
```

Als mathematische Regelmenge könnte man das doppelte `b.` einmal notieren;
hier bleiben zur exakten Herkunft beide Vorkommen sichtbar. Die Semantik
ist in beiden Schreibweisen dieselbe.

```text
I0 = {}
I1 = {b,e}     -- Fakten r2, r3 und r8
I2 = I1       -- a fehlt; der positive c/d-Kreis hat keinen Start
```

Damit `LM(P^X3) = X3`.
**X3 ist ein Answer Set.**

## Zusammenfassung

| Kandidat X | Kleinstes Modell des genauen Redukts | Answer Set? |
|---|---|---|
| `{a,c,d,f}` | `{a,c,d,f}` | Ja |
| `{b,c,d,e}` | `{b,e}` | Nein |
| `{b,e}` | `{b,e}` | Ja |

Die fehlende Minimalität von `X2` darf nicht mit bloßer Regelerfüllung
verwechselt werden. Gerade positive Kreise können sich innerhalb eines
zu großen Kandidaten gegenseitig stützen, ohne aus Fakten ableitbar zu sein.

## Erklärung und Ausführung der Programmdatei

- r1 und r7 schalten ohne `b` gemeinsam `a` und `d` frei.
- r2 und r3 sind zwei alternative Standardableitungen von `b`.
- r4/r5 geben zwei positive Ableitungswege für `c`; r6 benötigt `c` **und** `e`.
- r8 liefert `e`, wenn sowohl `a` als auch `f` fehlen; r9 liefert `f` ohne `e`.
- Großgeschriebene Kandidatenbezeichnungen befinden sich ausschließlich im
  `%* ... *%`-Kommentar. Der ausführbare Teil ist vollständig ground.
- Es werden weder Modelle als Fakten vorgegeben noch Atome mit `#show`
  ausgeblendet. Die Originalregeln werden nicht durch vereinfachte ersetzt.

Tatsächlich ausgeführter Test mit `/usr/bin/clingo` **5.6.2**:

```sh
clingo --outf=2 0 programm.lp
```

```text
Result: SATISFIABLE
Models.Number: 3
Models.More: no
Alle Answer Sets: {a,c,d,f}; {b,e}; {b,f}
Prozess-Exitcode: 30
```

Die Vollständigkeit wird in `../../ue1.3/b/antwort.md` begründet. `{b,f}`
liegt nicht unter den drei hier vorgegebenen Kandidaten.

Zusätzlich wurde ausgeführt:

```sh
python3 ../pruefe_redukte.py
```

Die drei genauen Redukte, ihre Fixpunkte und clingo-Gegenprüfungen waren
korrekt; der gesamte Prüfer endete mit Exitcode `0`.
