# Erklärung zu Homework 1: Grundprogramme, Redukte und Tests

Dieses Dokument behandelt ausschließlich `exercise01b.pdf`, Aufgaben
**1.1–1.4 mit jeweils a und b**. Alle Lösungen und Tests sind lokal;
es wird nichts auf Moodle abgegeben. Die acht `programm.lp`-Dateien sind
vollständig eigenständig ausführbar. Die Aufgaben 1.3 a/b enthalten echte
Kopien der Programme 1.2 a/b, keine Imports und keine bloßen Verweise.

## Orientierung

| Aufgabe | Programm | Ausführliche Lösung |
|---|---|---|
| 1.1 a | [ue1.1/a/programm.lp](ue1.1/a/programm.lp) | [antwort.md](ue1.1/a/antwort.md) |
| 1.1 b | [ue1.1/b/programm.lp](ue1.1/b/programm.lp) | [antwort.md](ue1.1/b/antwort.md) |
| 1.2 a | [ue1.2/a/programm.lp](ue1.2/a/programm.lp) | [antwort.md](ue1.2/a/antwort.md) |
| 1.2 b | [ue1.2/b/programm.lp](ue1.2/b/programm.lp) | [antwort.md](ue1.2/b/antwort.md) |
| 1.3 a | [ue1.3/a/programm.lp](ue1.3/a/programm.lp) | [antwort.md](ue1.3/a/antwort.md) |
| 1.3 b | [ue1.3/b/programm.lp](ue1.3/b/programm.lp) | [antwort.md](ue1.3/b/antwort.md) |
| 1.4 a | [ue1.4/a/programm.lp](ue1.4/a/programm.lp) | [antwort.md](ue1.4/a/antwort.md) |
| 1.4 b | [ue1.4/b/programm.lp](ue1.4/b/programm.lp) | [antwort.md](ue1.4/b/antwort.md) |

Zusätzlich existiert der gezielte, dateischreibfreie
[Reduktprüfer ue1.2/pruefe_redukte.py](ue1.2/pruefe_redukte.py).

## 1. Was der Code bedeutet

### Fakten, Regeln und Grundinstanzen

`d.` ist ein Fakt. `a :- b,d.` bedeutet: Sind **beide** Rumpfatome `b` und
`d` erfüllt, muss auch `a` erfüllt sein. Es bedeutet weder, dass `a` nur
auf diesem Weg gelten darf, noch dass man aus `a` rückwärts `b` oder `d`
folgern dürfte. Verschiedene Regeln mit demselben Kopf sind alternative
Ableitungswege.

`conn(amsterdam,brussels)` ist ein Atom mit zwei Konstanten. Alle
**ausführbaren** Regeln der acht Programme sind ground: Sie enthalten
keine Variablen. Allgemeine Regeln mit `X`, `Y`, `Z` bleiben dort, wo die
Angabe sie nennt, hinter `%` auskommentiert. Die Kandidatenblöcke in 1.2
und 1.3 stehen zwischen `%*` und `*%` und werden ebenfalls nicht ausgeführt.

Die Programme übernehmen die vorgegebenen Grundregeln. Es wurden keine
Ergebnisfakten, Constraint-Ersatzformulierungen, Choice-Regeln oder
`#show`-Projektionen eingebaut. Alle Modellatome werden ausgegeben.

### Kleinstes positives Modell

Für ein positives normales Grundprogramm beginnt die Herleitung bei der
leeren Menge. Der Operator `T_P` liefert die Köpfe derjenigen Regeln,
deren sämtliche Rumpfatome bereits in der vorherigen Stufe liegen. Fakten
haben einen leeren Rumpf und greifen daher sofort. Die synchrone Iteration
ab `{}` erreicht einen Fixpunkt, das **kleinste** Modell des Programms.
Dieses ist sein einziges Answer Set.

„Kleinstes“ bedeutet hier: Es ist bezüglich Mengeninklusion in jedem Modell
enthalten. Es geht nicht darum, irgendein Modell zu finden, das die Regeln
erfüllt, oder ein besonders kleines Modell zu erraten.

### Defaultnegation und Gelfond–Lifschitz-Redukt

`not q` ist Defaultnegation, keine klassische Negation und kein neues Atom.
Für einen Kandidaten `X` bilden wir den GL-Redukt `P^X`:

1. Jede Regel löschen, die ein `not q` mit `q ∈ X` enthält.
2. Aus den verbliebenen Regeln alle negativen Rumpfliterale entfernen.
3. Die positiven Rumpfatome bleiben dabei unverändert stehen.
4. Das kleinste Modell des so entstandenen positiven Programms berechnen.
5. Genau bei `LM(P^X) = X` ist der Kandidat ein Answer Set.

Die in 1.2 geforderten **exakten**, nicht zusätzlich vereinfachten Redukte
stehen jeweils in `antwort.md`. Regeln mit später unerfüllbaren positiven
Rümpfen werden dort ausdrücklich nicht vorzeitig gelöscht. In 1.2 b wird
auch das zweimal entstehende Faktvorkommen `b.` nachvollziehbar notiert.

### Warum positive Kreise keine freie Wahl sind

Bei `b :- e.` und `e :- b.` ohne äußere Startableitung entsteht ab `{}`
weder `b` noch `e`. Die Menge `{b,e}` könnte zwar ein Modell sein und jedes
Atom würde vom anderen gestützt, sie ist aber nicht das kleinste Modell.
Das ist der entscheidende Unterschied zwischen bloßer Regelerfüllung,
Unterstützung und stabiler Semantik.

Dieses Problem tritt konkret in 1.1 a zwischen `b` und `f`, in 1.2 a beim
Kandidaten `{a,b,e}` zwischen `b` und `e` sowie in 1.2 b beim Kandidaten
`{b,c,d,e}` zwischen `c` und `d` auf. Der Fakt `e` im letzten Redukt liefert
noch keinen Start für den `c/d`-Kreis.

## 2. Erklärung jeder Programmdatei

### `ue1.1/a/programm.lp`

Das Programm ist rein positiv. Die Regeln haben folgende Funktionen:

| Regel(n) | Bedeutung im Ableitungsprozess |
|---|---|
| `d.` | Einziger Ausgangsfakt. |
| `e :- d.` | Liefert aus dem Fakt das erste zusätzliche Atom. |
| `c :- d,e.` | Verlangt beide bereits abgeleiteten Atome. |
| `a :- b,d.` / `a :- c,e.` | Zwei Alternativen für `a`; die zweite ist erfolgreich. |
| `b :- d,m.` / `b :- e,f.` | Für `b` fehlen entweder `m` oder eine Startableitung für `f`. |
| `f :- b,c.` | Kann ohne bereits vorhandenes `b` nicht starten. |
| `k :- a,e.` | Erweitert die erfolgreiche Kette nach `a`. |
| `h :- c,k.` | Verwendet das neu erzeugte `k`. |
| `g :- d,f.` / `g :- e,h.` | Die zweite Regel liefert `g`, obwohl `f` fehlt. |

`m` kommt ausschließlich im Rumpf vor. Dafür darf kein Fakt nachgetragen
werden. Das Modell ist `{a,c,d,e,g,h,k}`. Die vollständigen synchronen
Stufen stehen in der Antwort und wurden vom Reduktprüfer berechnet.

### `ue1.1/b/programm.lp`

Die drei `conn`-Fakten bilden einen gerichteten Kreis. Die drei expliziten
`tour`-Regeln kombinieren jeweils genau zwei Kanten dieses Kreises. Sie
berechnen keine transitive Hülle und machen die Kanten nicht ungerichtet.
Die drei `finish`-Regeln testen jeweils eine Tour und eine weitere direkte
Verbindung vom Tourstart nach Amsterdam.

Nur `finish(brussels)` hat beide Rumpfatome: `tour(cologne,brussels)` und
`conn(cologne,amsterdam)`. Für die anderen beiden `finish`-Köpfe fehlen
`conn(amsterdam,amsterdam)` bzw. `conn(brussels,amsterdam)`. Eine Tour darf
nicht als Verbindung mit demselben Argumentpaar verwendet werden.

Die allgemeine `tour`-Regel und die allgemeine `finish`-Regel bleiben reine
Kommentare. Auch die inaktive Grundregel für `finish(amsterdam)` bleibt
wörtlich im ausführbaren Originalprogramm erhalten.

### `ue1.2/a/programm.lp`

Die acht Regeln werden unverändert ausgeführt:

- `a :- not d.` erzeugt im Redukt einen Fakt, wenn `d` im Kandidaten fehlt.
- `b :- not a.` ist eine unabhängige Standardableitung von `b`.
- `b :- e,not d.` benötigt nach dem Entfernen des zulässigen `not d`
  weiterhin eine echte Ableitung von `e`.
- `c :- a,not e.` und `c :- b,not e.` erlauben `c` nur ohne angenommenes `e`.
- `d :- not a,not e.` wird nur dann zum Fakt, wenn beide Atome fehlen.
- `e :- a,d.` bleibt als positive Regel in jedem Redukt unverändert stehen.
- `e :- b,not c.` benötigt eine Ableitung von `b`, sofern `c` fehlt.

Die kommentierten Kandidaten sind keine Fakten und keine Einschränkung
der Solver-Suche. Der Originalprogramm-Lauf liefert `{a,c}` und `{b,c,d}`.
Für die vorgegebenen Kandidaten lauten die kleinsten Reduktmodelle:

| Kandidat | `LM(P^X)` | Stabil? |
|---|---|---|
| `{}` | `{a,b,c,d,e}` | Nein |
| `{a,c}` | `{a,c}` | Ja |
| `{a,b,e}` | `{a}` | Nein |

### `ue1.2/b/programm.lp`

- `a :- not b.` und `d :- not b.` sorgen ohne `b` gemeinsam für `a` und `d`.
- `b :- not c.` und `b :- not f.` sind getrennte Alternativen für `b`.
- `c :- a.` ist ein äußerer positiver Ableitungsweg für `c`.
- `c :- d.` und `d :- c,e.` bilden einen positiven Kreis; `e` allein ist
  noch keine Startableitung für diesen Kreis.
- `e :- not a,not f.` wird nur ohne **beide** Atome zum Fakt `e.`.
- `f :- not e.` ist die Standardalternative ohne `e`.

Insbesondere steht in der Originaldatei kein Fakt `f.`. Dieser entsteht
nur in passenden Redukten. Die vollständige Enumeration des Originals ist
`{a,c,d,f}`, `{b,e}`, `{b,f}`. Für die vorgegebenen Kandidaten gilt:

| Kandidat | `LM(P^X)` | Stabil? |
|---|---|---|
| `{a,c,d,f}` | `{a,c,d,f}` | Ja |
| `{b,c,d,e}` | `{b,e}` | Nein |
| `{b,e}` | `{b,e}` | Ja |

### `ue1.3/a/programm.lp`

Die Datei enthält dieselben acht ausführbaren Regeln wie 1.2 a, aber liegt
hier als eigenständige Kopie. Die nichtausführbare Aufgabenbeschreibung im
Kommentar unterscheidet sich. Der Befehl `clingo --outf=2 0 programm.lp`
braucht keine andere Programmdatei.

Für die vollständige Herleitung wird zuerst `e` ausgeschlossen: Ein
angenommenes `e` entfernt alle `c`- und `d`-Regeln; anschließend bleibt
für `b/e` nur ein positiver Kreis ohne Startableitung. Ohne `e` bestimmen
die Fälle mit bzw. ohne `a` alle anderen Atome und liefern nur `{a,c}`
bzw. `{b,c,d}`. Beide Mengen werden zusätzlich über ihre genauen Redukte
bestätigt. Der ausführliche Beweis steht neben der Datei in `antwort.md`;
er verwendet keine vollständige Interpretationstabelle.

### `ue1.3/b/programm.lp`

Die neun Regeln sind eine selbstständig ausführbare Kopie von 1.2 b.
Sie werden nicht durch eine Kodierung der bereits gefundenen Modelle
ersetzt. Die beiden `not b`-Regeln erzwingen ohne `b` den Fall `{a,c,d,f}`.
Mit `b` fehlt jede äußere Startableitung für `c/d`; beide Atome fallen weg.
Die verbleibenden `e/f`-Standardalternativen liefern nur `{b,e}` und `{b,f}`.

Das Beweisziel in 1.3 ist nicht bloß, einige stabile Kandidaten zu prüfen:
Die Antwort zeigt, warum **jedes** Answer Set in einen dieser strukturell
erzwungenen Fälle fällt, und prüft anschließend die Existenz aller Fälle
an ihren kleinsten Reduktmodellen.

### `ue1.4/a/programm.lp`

- `canary(tweety).` und `penguin(tux).` sind die beiden Fakten.
- Vier Grundregeln für `bird` übertragen Kanarien- oder Pinguinstatus auf
  den Vogelstatus, jeweils für beide Konstanten aus der PDF.
- Zwei positive Grundregeln für `walks` übertragen Pinguinstatus auf Gehen.
- Zwei weitere `walks`-Regeln gelten standardmäßig ohne entsprechendes
  `flies`-Atom.
- Zwei `flies`-Regeln gelten standardmäßig ohne entsprechendes `walks`-Atom.

Tux geht unabhängig von der Defaultwahl; damit ist seine `flies`-Regel
in jedem stabilen Redukt gelöscht. Für Tweety gibt es keine positive
Pinguinableitung, sodass genau die beiden Standardalternativen verbleiben.
Weder beide noch keine von `walks(tweety)` und `flies(tweety)` ist stabil.
Es wird kein naturkundliches Zusatzwissen über Kanarienvögel eingebaut.
Auch die Grundregeln mit unerfüllbaren Rümpfen bleiben in der Datei stehen.

### `ue1.4/b/programm.lp`

Die drei Zahlenfakten werden gefolgt von je einer positiven oder negativen
Defaultalternative: Für jede Zahl erzeugen die zwei wechselseitigen
Standardregeln genau eines der Atome `lucky(i)` und `unlucky(i)`.
Die drei ausdrücklich vorgegebenen `p`-Regeln prüfen die Paare `1/2`,
`1/3`, `2/3`; ihre allgemeine Variablenform bleibt ein Kommentar.

`p` kann in keinem Answer Set vorkommen, weil sein Vorkommen sämtliche
`p`-Regeln aus dem eigenen Redukt löschen würde. Ohne `p` werden diese
Regeln positiv. Zwei glückliche Zahlen würden dann `p` erzwingen und so
Stabilität verhindern. Daher bleiben genau die vier Möglichkeiten mit
keiner oder einer glücklichen Zahl. Die Originalregeln werden nicht durch
Constraints ersetzt; ihre Wirkung wird aus der stabilen Semantik erklärt.

## 3. Erklärung des zusätzlichen Prüfprogramms

### `ue1.2/pruefe_redukte.py`

Der Prüfer benötigt nur Python-Standardbibliothek und `/usr/bin/clingo`.
Er schreibt keine Dateien. Er liest die beiden 1.2-Programme und das
positive Programm 1.1 a relativ zu seinem eigenen Speicherort; der Aufruf
ist dadurch unabhängig vom Arbeitsverzeichnis.

| Bestandteil | Zweck und wichtige Grenze |
|---|---|
| `Regel` | Unveränderliche Darstellung von Kopf, positiven und negativen Rumpfatomen. Die Reihenfolge der Regeln und doppelte Fakten bleiben für den exakten Vergleich erhalten. |
| `lesen` | Entfernt Block- und Zeilenkommentare und zerlegt die aussagenlogischen Regeln. Der Parser ist absichtlich nur für die nullstelligen Atome aus 1.1 a und 1.2 ausgelegt, nicht für die Stadt- oder Vogelprogramme. |
| `redukt` | Löscht zunächst jede Regel mit einem negierten Kandidatenatom; die übrigen Regeln behalten nur ihre positiven Rumpfatome. Positive Literale werden nicht anhand des Kandidaten vereinfacht. |
| `fixpunkt` | Startet bei der leeren Menge und berechnet synchron die nächste `T_P`-Stufe. Die Folge wird auf Monotonie geprüft und beim ersten Fixpunkt beendet. Die doppelte Schlussstufe wird nur nicht erneut ausgegeben. |
| `ausgabe` | Schreibt einen positiven Regelsatz als clingo-Eingabetext; es entstehen keine Dateien. |
| `clingo_modelle` | Übergibt den Text über stdin, startet `clingo --outf=2 0 -`, akzeptiert erfolgreiche SAT-Codes `10`/`30`, liest JSON und verlangt `Models.More == "no"`. Atomreihenfolgen werden durch Mengenbildung bedeutungslos. |
| `menge` / `anzeigen` | Wandeln die im Test kurz notierten nullstelligen Atomnamen in Mengen um bzw. formatieren Mengen sortiert. Sie werden nicht auf Atome mit Argumenten angewendet. |
| `main` | Vergleicht die Originalmodellmengen, dann die Reduktstrukturen mit unabhängig notierten Sollregeln und die Fixpunkte mit Sollmengen. Anschließend prüft clingo jeden positiven Redukt unabhängig und es werden zusätzlich die Stufen von 1.1 a bestätigt. |

Geprüft werden alle sechs Kandidaten aus 1.2 sowie die dort noch nicht
vorkommenden Lösungen `{b,c,d}` aus 1.3 a und `{b,f}` aus 1.3 b. Zusammen
sind damit auch sämtliche in 1.3 verwendeten Kandidatenredukte abgedeckt.
Der Prüfer enumeriert nicht alle möglichen Interpretationen und ist kein
Ersatz für die textlichen Vollständigkeitsbeweise.

Aufruf aus diesem `hausuebung`-Ordner:

```sh
python3 ue1.2/pruefe_redukte.py
```

Tatsächliches Ergebnis:

```text
1.2 a: alle clingo-Modelle korrekt: {a,c}, {b,c,d}
  X1: Kandidat={}, LM={a,b,c,d,e}, stabil=False
  X2: Kandidat={a,c}, LM={a,c}, stabil=True
  X3: Kandidat={a,b,e}, LM={a}, stabil=False
  1.3: M2: Kandidat={b,c,d}, LM={b,c,d}, stabil=True
1.2 b: alle clingo-Modelle korrekt: {a,c,d,f}, {b,e}, {b,f}
  X1: Kandidat={a,c,d,f}, LM={a,c,d,f}, stabil=True
  X2: Kandidat={b,c,d,e}, LM={b,e}, stabil=False
  X3: Kandidat={b,e}, LM={b,e}, stabil=True
  1.3: M2: Kandidat={b,f}, LM={b,f}, stabil=True
OK: alle Reduktstrukturen, Fixpunkte und clingo-Gegenprüfungen bestanden.
```

Der echte Lauf gibt zwischen diesen Statuszeilen zusätzlich alle
Fixpunktstufen aus. Exitcode des Python-Prüfers: **0**.

## 4. Alle acht Solverläufe und erwartete Atomemengen

Verwendet wurde die lokal installierte CLI **clingo 5.6.2**. Jedes der acht
Programme wurde separat mit sämtlichen Answer Sets ausgeführt. Die
tatsächlich verwendeten Befehle, relativ zu diesem Ordner, waren:

```sh
clingo --outf=2 0 ue1.1/a/programm.lp
clingo --outf=2 0 ue1.1/b/programm.lp
clingo --outf=2 0 ue1.2/a/programm.lp
clingo --outf=2 0 ue1.2/b/programm.lp
clingo --outf=2 0 ue1.3/a/programm.lp
clingo --outf=2 0 ue1.3/b/programm.lp
clingo --outf=2 0 ue1.4/a/programm.lp
clingo --outf=2 0 ue1.4/b/programm.lp
```

Im tatsächlichen Toolaufruf wurden jeweils der absolute Programmpfad und
`/usr/bin/clingo` verwendet. Alle Läufe lieferten `Result: SATISFIABLE`,
`Models.More: no` und Prozess-Exitcode **30**.

### Erwartungswerte und beobachtete Ergebnisse

Für die langen Modelle seien die folgenden gemeinsamen Teilmengen definiert:

```text
C = {conn(amsterdam,brussels),conn(brussels,cologne),conn(cologne,amsterdam)}
T = {tour(amsterdam,cologne),tour(brussels,amsterdam),tour(cologne,brussels)}
B = {canary(tweety),penguin(tux),bird(tweety),bird(tux),walks(tux)}
N = {num(1),num(2),num(3)}
```

`C`, `T`, `B`, `N` sind hier nur Schreibabkürzungen in der Erklärung;
es sind keine Programmatome. `∪` bezeichnet Mengenvereinigung.

| Programm | Vollständige Modellfamilie, Soll = beobachtet | `Models.Number` |
|---|---|---|
| 1.1 a | `{a,c,d,e,g,h,k}` | 1 |
| 1.1 b | `C ∪ T ∪ {finish(brussels)}` | 1 |
| 1.2 a | `{a,c}`; `{b,c,d}` | 2 |
| 1.2 b | `{a,c,d,f}`; `{b,e}`; `{b,f}` | 3 |
| 1.3 a | `{a,c}`; `{b,c,d}` | 2 |
| 1.3 b | `{a,c,d,f}`; `{b,e}`; `{b,f}` | 3 |
| 1.4 a | `B ∪ {flies(tweety)}`; `B ∪ {walks(tweety)}` | 2 |
| 1.4 b | `N ∪ {unlucky(1),unlucky(2),unlucky(3)}`; `N ∪ {lucky(1),unlucky(2),unlucky(3)}`; `N ∪ {unlucky(1),lucky(2),unlucky(3)}`; `N ∪ {unlucky(1),unlucky(2),lucky(3)}` | 4 |

Die langen Mengen sind in den jeweiligen `antwort.md` zusätzlich vollständig
ohne diese Abkürzungen ausgeschrieben. Die JSON-Reihenfolge von Modellen
und Atomen ist semantisch unerheblich.

`0` bedeutet hier **alle Modelle**, nicht null Modelle. Erfolgreiche clingo-
Prozesse dürfen die von allgemeinen Shellkonventionen abweichenden SAT-Codes
`10` oder `30` zurückgeben. Bei diesen acht vollständigen Läufen war es
stets `30`. Die Informationsmeldung über das nicht im Kopf vorkommende `m`
bei 1.1 a ist erwartet und darf nicht durch einen zusätzlichen Fakt
„repariert“ werden.

## 5. Selbstkontrolle beim Nachvollziehen

- Kann jeder neu abgeleitete Kopf auf eine tatsächlich anwendbare Regel
  zurückgeführt werden?
- Wurde der Redukt nur mit den negativen Literalen gebildet und erst danach
  das positive Programm ausgewertet?
- Wird wirklich das kleinste Modell ab `{}` berechnet, statt den Kandidaten
  als Ausgangsmenge zu nehmen?
- Wurden positive Kreise ohne Startableitung ausgeschlossen?
- Deckt der Beweis in 1.3 jeden möglichen stabilen Fall ab, und wurde jeder
  verbleibende Kandidat zusätzlich durch seinen Redukt bestätigt?
- Wurde bei der Solverprobe die vollständige Enumeration geprüft, statt nur
  ein einzelnes passendes Modell zu betrachten?
