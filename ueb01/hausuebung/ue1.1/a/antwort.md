# Homework 1 – Aufgabe 1.1 a

## Aufgabe und Ergebnis

Gesucht ist das Answer Set des positiven Grundprogramms aus `programm.lp`.
Alle Regeln der PDF sind unverändert enthalten; insbesondere stehen dort
`c :- d, e.` und `b :- d, m.`. Für `m` gibt es **keine** definierende Regel.

Das einzige Answer Set ist

```text
{a,c,d,e,g,h,k}
```

## Herleitung als kleinstes Modell

Für ein positives normales Programm ist das Answer Set sein **kleinstes**
Herbrand-Modell. Wir starten bei `I0 = {}` und bilden synchron
`I(n+1) = T_P(I(n))`: Ein Regelkopf kommt genau dann hinzu, wenn sämtliche
positiven Rumpfatome bereits in `I(n)` stehen. Die Iteration beginnt nicht bei
einem geratenen Modell.

| Stufe | Gesamte Atomemenge | Neue Ableitung mit Begründung |
|---|---|---|
| `I0` | `{}` | Start ohne Annahmen |
| `I1` | `{d}` | `d.` ist ein Fakt. |
| `I2` | `{d,e}` | `e :- d.` |
| `I3` | `{c,d,e}` | `c :- d,e.` |
| `I4` | `{a,c,d,e}` | `a :- c,e.` |
| `I5` | `{a,c,d,e,k}` | `k :- a,e.` |
| `I6` | `{a,c,d,e,h,k}` | `h :- c,k.` |
| `I7` | `{a,c,d,e,g,h,k}` | `g :- e,h.` |
| `I8` | `{a,c,d,e,g,h,k}` | Keine neue Ableitung: Fixpunkt. |

Die Fixpunktstufen wurden zusätzlich durch `../../ue1.2/pruefe_redukte.py`
berechnet; der Pfad ist relativ zu diesem Ordner.

## Warum fehlen `b`, `f` und `m`?

- `m` steht in keinem Regelkopf und ist kein Fakt. Es kann deshalb nicht
  erstmalig abgeleitet werden. `b :- d,m.` liefert trotz des Fakts `d` kein `b`.
- Die andere Regel für `b` ist `b :- e,f.`. Sie benötigt zuerst `f`.
- Die einzige Regel für `f` ist `f :- b,c.`. Sie benötigt zuerst `b`.
- Der positive Kreis zwischen `b` und `f` hat somit keine Anfangsableitung.
  Dass `e` und `c` vorhanden sind, ersetzt weder `f` noch `b`.

Eine größere, unter den Regeln abgeschlossene Atomemenge könnte beide
Kreisatome enthalten. Sie wäre aber nicht das **kleinste** Modell und daher
kein Answer Set. Positives gegenseitiges Stützen reicht nicht aus.

`g` fehlt dagegen nicht: Seine erste Regel `g :- d,f.` bleibt zwar ohne
Ableitung, die zweite Regel `g :- e,h.` greift in Stufe `I7`.

## Erklärung der Programmdatei

- `a :- b,d.` und `a :- c,e.` sind alternative Wege zu `a`.
- `b :- d,m.` und `b :- e,f.` sind alternative Wege zu `b`, die beide im
  kleinsten Modell blockiert bleiben.
- `c :- d,e.`, `d.` und `e :- d.` liefern den Start der Ableitungskette.
- `f :- b,c.` bildet den beschriebenen unbegründeten Kreis mit `b`.
- Die zwei `g`-Regeln sind Alternativen; nur `g :- e,h.` wird benötigt.
- `h :- c,k.` und `k :- a,e.` schließen die erfolgreiche Ableitungskette.

Kommas im Rumpf bedeuten **und**, verschiedene Regeln mit gleichem Kopf
liefern **alternative** Begründungen. Es wurden keine Fakten für das
Ergebnis ergänzt und keine Ausgabeatome mit `#show` versteckt.

## Tatsächlich ausgeführter Test

Im Ordner dieser Datei:

```sh
clingo --outf=2 0 programm.lp
```

Mit `/usr/bin/clingo` **5.6.2** wurde ausgegeben:

```text
Result: SATISFIABLE
Models.Number: 1
Models.More: no
Answer Sets, als Mengen: {a,c,d,e,g,h,k}
Prozess-Exitcode: 30
```

`0` fordert alle Answer Sets an. Die Meldung, dass `m` in keinem Regelkopf
vorkommt, ist erwartete Information zur Originalangabe, kein Syntaxfehler.
Der SAT-Exitcode `30` ist bei diesem vollständigen clingo-Lauf erfolgreich;
er darf nicht wie ein gewöhnlicher Shell-Fehler interpretiert werden.
