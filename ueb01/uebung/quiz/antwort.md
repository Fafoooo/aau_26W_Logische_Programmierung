# Quiz – Exercise 1

Es gelten die auf dem Blatt verwendeten **normalen Regeln mit genau einem Atom im Kopf**, ohne Integritätsbedingungen. Ein klassisches Modell erfüllt jede Implikation; ein Answer Set ist das kleinste Modell des eigenen GL-Redukts. Diese Begriffe sind verschieden.

## 1. Each positive logic program has at most one model: **false**

Gegenbeispiel in `gegenbeispiel_1.lp`: `a :- a.`
- Interpretation `{}`: Der Körper `a` ist falsch, daher ist die Regel erfüllt.
- Interpretation `{a}`: Körper und Kopf sind wahr, daher ist die Regel erfüllt.
- Somit hat dasselbe positive Programm zwei klassische Modelle. Sein einziges Answer Set ist trotzdem `{}`.

## 2. Each positive logic program has at most one answer set: **true**

- Es gibt keine negativen Literale. Jeder GL-Redukt ist deshalb das unveränderte Programm.
- Der positive Konsequenzoperator wird ab `{}` bis zum Fixpunkt angewandt.
- Dieser Fixpunkt ist das eindeutige kleinste Modell.
- Ein Answer Set muss genau dieses kleinste Modell sein. Zwei verschiedene Answer Sets sind daher ausgeschlossen.

## 3. Each normal logic program has at least one model: **true**

- Sei `H` die Menge aller Grundatome des Programms.
- In der Interpretation `H` ist jeder Regelkopf wahr.
- Ist der Körper einer Regel wahr, ist auch ihr Kopf wahr; die Implikation ist erfüllt.
- Ist der Körper falsch, ist die Implikation ebenfalls erfüllt.
- Folglich ist `H` ein klassisches Modell. Es muss kein Answer Set sein.

**Abgrenzung:** Erlaubt man zusätzlich kopflose Integritätsbedingungen, gilt die Aussage nicht mehr; etwa die leere Bedingung `:- .` ist unerfüllbar. Solche Bedingungen sind nicht Teil der hier betrachteten normalen Programme.

## 4. Each normal logic program has at least one answer set: **false**

Gegenbeispiel in `gegenbeispiel_4.lp`: `p :- not p.`
- Für `X={}` bleibt `p.` im Redukt. Dessen kleinstes Modell ist `{p}`, also nicht `X`.
- Für `X={p}` wird die einzige Regel gelöscht. Das leere Redukt hat kleinstes Modell `{}`, also nicht `X`.
- Es gibt keine weitere Interpretation über `{p}`. Das Programm hat kein Answer Set.

**Ergebnis:** false, true, true, false.

Test: `python3 ../../checks.py` vom Ordner `uebung/quiz` aus. Der zentrale Test prüft beide klassischen Modelle des ersten Beispiels und die fehlenden Answer Sets des zweiten Beispiels mit Redukt und clingo.
