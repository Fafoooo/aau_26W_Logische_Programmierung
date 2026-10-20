# Homework 1 – Aufgabe 1.1 b

## Aufgabe und Ergebnis

Für das positive Grundprogramm aus der PDF ist das Answer Set zu bestimmen.
Die Variablenregeln aus den PDF-Kommentaren bleiben in `programm.lp`
**Kommentare**. Ausgeführt werden ausschließlich die angegebenen Grundregeln.

Das einzige Answer Set lautet vollständig:

```text
{
  conn(amsterdam,brussels),
  conn(brussels,cologne),
  conn(cologne,amsterdam),
  tour(amsterdam,cologne),
  tour(brussels,amsterdam),
  tour(cologne,brussels),
  finish(brussels)
}
```

## Fixpunktberechnung

Wir berechnen das kleinste Modell ab der leeren Menge. In jeder Stufe werden
nur Regeln ausgewertet, deren Rumpf in der vorherigen Stufe erfüllt ist.

1. `I0 = {}`.
2. `I1` enthält genau die drei `conn`-Fakten:
   `conn(amsterdam,brussels)`, `conn(brussels,cologne)` und
   `conn(cologne,amsterdam)`.
3. In `I2` kommen genau die drei `tour`-Atome hinzu:
   - `tour(amsterdam,cologne)` folgt aus den Verbindungen Amsterdam–Brüssel
     und Brüssel–Köln.
   - `tour(brussels,amsterdam)` folgt aus Brüssel–Köln und Köln–Amsterdam.
   - `tour(cologne,brussels)` folgt aus Köln–Amsterdam und Amsterdam–Brüssel.
4. In `I3` kommt `finish(brussels)` hinzu: Sowohl `tour(cologne,brussels)`
   als auch `conn(cologne,amsterdam)` sind nun vorhanden.
5. `I4 = I3`: Es gibt keine weitere anwendbare Regel mit neuem Kopf.

Damit ist die angegebene Menge ein Fixpunkt. Jede ihrer Ableitungen beginnt
bei den Fakten; sie ist deshalb in jedem Modell enthalten. Sie ist somit
das kleinste Modell und das einzige Answer Set des positiven Programms.

## Warum nur `finish(brussels)`?

Die drei konkreten Regeln prüfen unterschiedliche zusätzliche Verbindungen:

| Kopf | Bereits ableitbare Tour | Zusätzlich benötigte Verbindung | Ergebnis |
|---|---|---|---|
| `finish(cologne)` | `tour(amsterdam,cologne)` | `conn(amsterdam,amsterdam)` | Verbindung fehlt; keine Ableitung. |
| `finish(amsterdam)` | `tour(brussels,amsterdam)` | `conn(brussels,amsterdam)` | Verbindung fehlt; keine Ableitung. |
| `finish(brussels)` | `tour(cologne,brussels)` | `conn(cologne,amsterdam)` | Verbindung ist Fakt; Ableitung gelingt. |

Ein `tour`-Atom erzeugt kein neues `conn`-Atom. Die Regeln definieren auch
keine ungerichteten Kanten und keine beliebig langen Wege. Insbesondere ist
`tour(brussels,amsterdam)` **kein** Ersatz für `conn(brussels,amsterdam)`.

## Erklärung der Programmdatei

- Die drei `conn`-Fakten sind die gesamte Ausgangsdatenbasis.
- Jede der drei expliziten `tour`-Regeln kombiniert genau zwei bestimmte
  `conn`-Fakten. Konstanten wie `amsterdam` sind keine Variablen.
- Jede der drei `finish`-Regeln kombiniert eine bestimmte Tour mit einer
  direkten Verbindung vom Start dieser Tour nach Amsterdam.
- `% tour(X,Z) ...` und `% finish(Y) ...` zeigen nur die verallgemeinerte
  Idee aus der Angabe. Das `%` verhindert ihre Ausführung. Es wurden keine
  weiteren Grundinstanzen hinzuerfunden.
- Alle Atome bleiben sichtbar; es gibt keine Ergebnisfakten und kein `#show`.

## Tatsächlich ausgeführter Test

Im Ordner dieser Datei:

```sh
clingo --outf=2 0 programm.lp
```

Getestet mit `/usr/bin/clingo` **5.6.2**:

```text
Result: SATISFIABLE
Models.Number: 1
Models.More: no
Answer Set: genau die oben vollständig angegebene Menge
Prozess-Exitcode: 30
```

Die Reihenfolge der Atome im JSON ist für den Mengenvergleich unerheblich.
`0` und `Models.More: no` belegen, dass die Enumeration nicht beim ersten
von möglicherweise mehreren Modellen abgebrochen wurde. Exitcode `30`
kennzeichnet hier den erfolgreichen, vollständigen SAT-Lauf.
