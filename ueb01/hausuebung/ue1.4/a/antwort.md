# Homework 1 – Aufgabe 1.4 a

## Aufgabe und vollständige Answer Sets

Das normale Grundprogramm beschreibt Tweety als Kanarienvogel und Tux als
Pinguin. Gesucht sind alle Answer Sets. `programm.lp` übernimmt sämtliche
expliziten Grundregeln der PDF; die verallgemeinerten Variablenregeln sind
nur Kommentare.

Es gibt **genau zwei** Answer Sets:

```text
M1 = {
  canary(tweety),
  penguin(tux),
  bird(tweety),
  bird(tux),
  walks(tux),
  flies(tweety)
}

M2 = {
  canary(tweety),
  penguin(tux),
  bird(tweety),
  bird(tux),
  walks(tux),
  walks(tweety)
}
```

## 1. In beiden Modellen feststehende Atome

Die Fakten `canary(tweety).` und `penguin(tux).` gehören zu jedem kleinsten
Reduktmodell. Daraus folgen positiv:

- `bird(tweety)` durch `bird(tweety) :- canary(tweety).`;
- `bird(tux)` durch `bird(tux) :- penguin(tux).`;
- `walks(tux)` durch `walks(tux) :- penguin(tux).`.

Die Atome `canary(tux)` und `penguin(tweety)` sind weder Fakten noch Köpfe
einer definierenden Regel. Sie werden nicht erzeugt. Die Regeln, die sie
als Rumpfatome verwenden, bleiben im Originalprogramm dennoch vorhanden.

## 2. Tux kann in keinem Answer Set fliegen

`walks(tux)` ist unabhängig von Defaultnegation bereits positiv erzwungen.
Für jeden stabilen Kandidaten wird deshalb

```prolog
flies(tux) :- bird(tux), not walks(tux).
```

gelöscht. Es gibt keine weitere Regel mit Kopf `flies(tux)`. Deshalb ist
`flies(tux)` in jedem Answer Set abwesend. Die zusätzliche Standardregel
für `walks(tux)` widerspricht der positiven Ableitung nicht.

## 3. Tweety muss genau eine der beiden Alternativen erhalten

Für Tweety gibt es keine erfolgreiche positive `walks`-Ableitung aus einem
Pinguinfakt. Es bleiben die Standardregeln

```prolog
walks(tweety) :- bird(tweety), not flies(tweety).
flies(tweety) :- bird(tweety), not walks(tweety).
```

- **Beide Atome fehlen:** Dann bleiben beide Regeln im Redukt, jeweils mit
  Rumpf `bird(tweety)`. Weil dieser Vogelstatus positiv ableitbar ist,
  würden beide Atome entstehen. Ein solcher Kandidat ist nicht stabil.
- **Beide Atome sind enthalten:** Dann werden beide Regeln gelöscht. Die
  weitere `walks(tweety)`-Regel braucht das nicht ableitbare `penguin(tweety)`.
  Somit entsteht keines der beiden Atome im kleinsten Reduktmodell. Auch
  dieser Kandidat ist nicht stabil.
- **Nur `flies(tweety)` ist enthalten:** Die `walks`-Standardregel wird
  gelöscht, die `flies`-Standardregel wird zu `flies(tweety) :- bird(tweety).`.
  Dadurch entsteht genau die Flug-Alternative `M1`.
- **Nur `walks(tweety)` ist enthalten:** Die `flies`-Regel wird gelöscht,
  die `walks`-Standardregel wird zu `walks(tweety) :- bird(tweety).`.
  Dadurch entsteht genau die Geh-Alternative `M2`.

Es gibt hier **keine** Zusatzregel „Kanarienvögel fliegen“. Der Kanarienfakt
begründet nur den Vogelstatus. Deshalb ist auch das Answer Set mit gehendem
Tweety korrekt; es darf nicht aufgrund von Alltagswissen gestrichen werden.

## 4. Fixpunktprüfung und Vollständigkeit

Sei

```text
B = {canary(tweety),penguin(tux),bird(tweety),bird(tux),walks(tux)}.
```

Für den Redukt zu `M1` werden genau die folgenden negativen Regeln entfernt:
`walks(tweety) :- bird(tweety),not flies(tweety).` und
`flies(tux) :- bird(tux),not walks(tux).`.
In den übrigen negativen Regeln entfällt `not`; alle positiven Regeln
bleiben unverändert. Die synchronen Ableitungsstufen sind:

```text
{} -> {canary(tweety),penguin(tux)}
   -> B
   -> B ∪ {flies(tweety)}
   -> B ∪ {flies(tweety)}.
```

Für den Redukt zu `M2` werden die beiden `flies`-Regeln entfernt. Die beiden
`walks`-Standardregeln verlieren ihr `not`; alle positiven Regeln bleiben:

```text
{} -> {canary(tweety),penguin(tux)}
   -> B
   -> B ∪ {walks(tweety)}
   -> B ∪ {walks(tweety)}.
```

Jeder Kandidat ist damit gleich dem kleinsten Modell seines Redukts.
Die festen Atome, der Ausschluss von `flies(tux)` und die erschöpfende
Tweety-Fallunterscheidung lassen keine weiteren Answer Sets zu.

## Erklärung der Programmdatei

1. Die beiden Fakten sind die gesamte Ausgangsbasis.
2. Vier `bird`-Regeln sind die ausdrücklich vorgegebenen Grundinstanzen
   der beiden allgemeinen Vogelregeln. Sie werden nicht auf die zwei
   tatsächlich erfolgreichen Ableitungen verkürzt.
3. Zwei positive `walks`-Regeln übertragen den Pinguinstatus auf das Gehen.
4. Zwei weitere `walks`-Regeln verwenden `not flies(...)` als Defaultbedingung.
5. Die beiden `flies`-Regeln verwenden `not walks(...)` als Defaultbedingung.
6. Die verallgemeinerten Regeln hinter `%` werden nicht ausgeführt. Es gibt
   weder Variablen im ausführbaren Teil noch Choice-Regeln oder `#show`.

`not` ist keine klassische Negation und keine Behauptung über die reale
Flugfähigkeit eines Vogels; es ist eine Bedingung relativ zum Kandidaten.

## Tatsächlich ausgeführter Test

Mit `/usr/bin/clingo` **5.6.2** wurde in diesem Ordner ausgeführt:

```sh
clingo --outf=2 0 programm.lp
```

```text
Result: SATISFIABLE
Models.Number: 2
Models.More: no
Modelle: genau M1 und M2, vollständig oben ausgeschrieben
Prozess-Exitcode: 30
```

Die Reihenfolge von Modellen und Atomen darf variieren. Entscheidend sind
die beiden vollständigen Mengen und die bestätigte vollständige Enumeration.
