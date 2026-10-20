# Blatt 01 – Erklärung zum Verstehen und Ändern

Dieses Blatt umfasst **zwei getrennte Angaben** mit jeweils denselben Aufgabennummern:
- [Exercise 1](Angabe/exercise01a.pdf): `uebung/`, inklusive Quiz.
- [Homework 1](Angabe/exercise01b.pdf): `hausuebung/`.
- [Beide Angaben zusammen](angabe_blatt01.pdf), zuerst Exercise, dann Homework.

Für jede Aufgabe gibt es `ue1.1/` bis `ue1.4/` und darin je `a/` und `b/`. Die `programm.lp` ist ausführbar; die unmittelbar daneben liegende `antwort.md` enthält Herleitung, Ergebnis und Probe. Die Bezeichnungen entsprechen der Angabe, nicht einer zusammengelegten Nummerierung.

**Dieser Leitfaden besteht aus zwei Teilen:** Unten werden sämtliche Übungs- und zentralen Testdateien erklärt. Die ebenso ausführliche [Datei-für-Datei-Erklärung der Hausübung](hausuebung/erklaerung.md) ist der zweite Teil; sie behandelt jede ihrer acht Programmdateien und den zusätzlichen Reduktprüfer. Die beiden Teile sind gemeinsam zu lesen.

## Grundlagen, die in allen Dateien gelten

- **Atom:** eine einzelne Aussage, z. B. `a` oder `bird(tux)`. Die Argumente von `likes(kate,soup)` gehören zum selben Atom.
- **Fakt:** `a.` gilt ohne Voraussetzung.
- **Regel:** `h :- b,c.` bedeutet: Sind `b` und `c` wahr, muss `h` wahr sein. Das Komma im Körper bedeutet UND. Zwei verschiedene Regeln mit Kopf `h` sind alternative Ableitungswege.
- **Defaultnegation:** `not a` bedeutet hier, dass `a` im geprüften Kandidaten fehlt. Es ist weder ein eigener Atomname noch ein Befehl, ein Atom nachträglich zu entfernen.
- **Grundprogramm / ground:** Die ausführbaren Regeln enthalten keine Variablen. Kleinbuchstaben wie `tux` sind Konstanten. Großbuchstaben in `%`-Kommentaren sind lediglich die allgemeine, nicht ausgeführte Form der Regel.
- **Klassisches Modell:** Jede Regel mit wahrem Körper hat einen wahren Kopf. Das allein reicht für ein Answer Set nicht aus.
- **Kleinstes Modell eines positiven Programms:** Bei `{}` beginnen und wiederholt alle Köpfe ableiten, deren Körper schon wahr ist. Positive Kreise ohne Startfakt erzeugen dabei nichts.
- **GL-Redukt für X:** Ganze Regeln mit einem `not a`, `a ∈ X`, löschen. Dann die übrigen negativen Literale entfernen. Positive Körper bleiben erhalten. `X` ist ein Answer Set genau dann, wenn das kleinste Modell dieses Redukts gleich `X` ist.

**Wichtige Arbeitsweise:** Beim positiven Fixpunkt wird jede Stufe vollständig aus der vorherigen berechnet. Ein gerade neu entstandenes Atom wird erst in der nächsten Stufe verwendet. Der Test und die niedergeschriebenen Stufen folgen derselben synchronen Konvention.

## Alle Programme starten

Vom Blattordner aus:
```sh
clingo uebung/ue1.1/a/programm.lp 0
clingo hausuebung/ue1.4/b/programm.lp 0
python3 checks.py
python3 hausuebung/ue1.2/pruefe_redukte.py
```

`0` fordert alle Answer Sets an. Ohne `0` würde eine einzelne gefundene Lösung keine vollständige Aufzählung belegen. Die Atomreihenfolge der Ausgabe ist unwichtig. Kein `#show` blendet Atome aus.

Erfolgreiche clingo-Läufe können Exitcodes `10` oder `30` haben; `20` bedeutet erwiesene Unerfüllbarkeit. Der Quiz-Gegenbeispieltest ohne Answer Set ist deshalb **kein** technischer Fehler. Die Python-Prüfprogramme liefern bei erfolgreicher Prüfung Exitcode `0`.

## Teil A – Jede Übungsdatei erklären

### `uebung/quiz/gegenbeispiel_1.lp`

- Die erste Zeile beginnt mit `%` und beschreibt die erwartete Bedeutung, ohne etwas auszuführen.
- `a :- a.` verlangt bei wahrem `a` wieder `a`. Diese Implikation ist sowohl in `{}` als auch in `{a}` erfüllt.
- Die Regel erzeugt ab der leeren Menge trotzdem kein `a`. Das einzige Answer Set ist `{}`. So zeigt eine Datei den Unterschied zwischen mehreren Modellen und einem einzigen kleinsten Modell.
- Zum Live-Ändern: Ersetze die Regel durch `a.`. Jetzt wird `a` zwingend abgeleitet; das bisherige Gegenbeispiel zu Quizfrage 1 funktioniert nicht mehr.

### `uebung/quiz/gegenbeispiel_4.lp`

- Der Kommentar kündigt fehlende Answer Sets an.
- `p :- not p.` ist eine negative Selbstabhängigkeit: Ohne angenommenes `p` wird es zum Fakt, mit angenommenem `p` verliert es seine einzige Regel.
- Der Test prüft beide Kandidaten und lässt zusätzlich clingo die Unerfüllbarkeit unter stabiler Semantik bestätigen.
- Zum Live-Ändern: Ein zusätzlicher Fakt `p.` würde `p` unabhängig begründen. Dann wäre `{p}` stabil. Das zeigt, warum fehlende Unterstützung und nicht ein allgemeines Verbot negativer Selbstbezüge entscheidend ist.

Die vier Quizantworten und die Begründung der Modell-Existenz normaler Programme ohne Constraints stehen in `uebung/quiz/antwort.md`.

### `uebung/ue1.1/a/programm.lp`

Nach dem Kommentar kommen die neun Originalregeln:
1. `a.` ist der erste Startfakt.
2. `b :- e.` kann erst mit einer Ableitung von `e` greifen.
3. `b :- f.` ist eine zweite Möglichkeit für `b`, aber keine zusätzliche Bedingung der vorherigen Regel.
4. `c :- b,f.` braucht beide Körperatome.
5. `c :- d,g.` ist der tatsächlich erfolgreiche Ableitungsweg für `c`.
6. `d.` ist der zweite Startfakt.
7. `e :- b,d.` braucht außer dem gegebenen `d` auch ein schon abgeleitetes `b`.
8. `g :- a,b.` würde `g` liefern, wenn `b` verfügbar wäre.
9. `g :- a,d.` liefert `g` aus den beiden Fakten ohne `b`.

Die Herleitung läuft von `a,d` über `g` zu `c`. Der Kreis zwischen `b,e` startet nicht, und `f` hat keinen Regelkopf. Die Datei darf nicht um einen vermeintlich vergessenen Fakt `f.` ergänzt werden. In `antwort.md` wird jede Originalregel mit dem gefundenen Ergebnis geprüft.

Zum Live-Ändern: Ergänze testweise `f.` in einer **Kopie**. Nun kann `b` über `f`, `e` über `b,d` und `c` über `b,f` entstehen. Vor dem Start für jede Stufe vorhersagen, was neu dazukommt. Die zentrale Sollprüfung soll eine geänderte Originaldatei als Abweichung melden.

### `uebung/ue1.1/b/programm.lp`

- Die ersten acht ausführbaren Zeilen sind acht unabhängige `likes`-Fakten: jeweils zwei Vorlieben für Kate, Mike, Paul und Tina.
- Der Kommentar `order(Z) :- ... X != Y` erklärt eine allgemeine Regel für gemeinsam bevorzugte Speisen. Er wird nicht ausgeführt.
- `order(beef)` wird aus Mikes und Tinas Rindfleischvorliebe abgeleitet.
- `order(soup)` wird aus Kates und Tinas Suppenvorliebe abgeleitet.
- Die allgemeine `happy(X)`-Regel ist erneut ein Kommentar; darunter stehen ihre konkreten acht Regeln.
- Kates Fischregel braucht `order(fish)`, aber dieses Atom wird nicht abgeleitet. Sie scheitert deshalb. Ihre Suppenregel kann greifen.
- Mikes Rindfleischregel kann greifen. Seine Kuchenregel scheitert am fehlenden `order(cake)`.
- Pauls Entenregel scheitert am fehlenden `order(duck)`. Seine Schweinefleischregel scheitert am fehlenden `order(pork)`.
- Tinas Rindfleischregel kann greifen. Ihre Suppenregel kann ebenfalls greifen. Beide erzeugen **dasselbe** Atom; Mengen zählen es nur einmal.

Zum Live-Ändern: Ergänze `order(duck).` nur in einer Kopie. Danach wird auch `happy(paul)` abgeleitet. Eine zusätzliche Vorliebe allein reicht nicht, wenn sie keine der ausführbaren Bestellregeln verändert. Kommentierte allgemeine Regeln sind nicht automatisch aktiv.

### `uebung/ue1.2/a/programm.lp`

- Der erste Kommentar nennt die zwei Kandidaten. Er trägt keine Kandidatenatome als Fakten ein und schränkt clingo nicht auf diese Kandidaten ein.
- `a :- b.` bleibt in jedem Redukt stehen.
- `b :- not c.` wird zum Fakt, wenn der Kandidat `c` nicht enthält; mit enthaltenem `c` entfällt die ganze Regel.
- `c :- not b.` stellt den entgegengesetzten Standardfall bereit.
- `d :- a,e.` bleibt positiv und braucht beide Atome.
- `e.` gilt in jedem Modell.

`antwort.md` bildet für **beide** Kandidaten den vollständigen Redukt. Weil beide Kandidaten `b` enthalten und `c` nicht, haben sie denselben Redukt. Dessen kleinstes Modell ist `{a,b,d,e}`. Deshalb ist nur der erste Kandidat stabil.

Zum Live-Ändern: Entferne in einer Kopie den Fakt `e.`. Überlege, ob `d` dann überhaupt eine erfolgreiche Ableitung erhalten kann. Prüfe nicht nur, ob die bisherige Menge noch Modell ist, sondern berechne ihren neuen Reduktfixpunkt.

### `uebung/ue1.2/b/programm.lp`

- Der Kandidatenkommentar ist wieder nicht ausführbar.
- `a :- not b.` gibt `a` einen äußeren Startweg, aber nur ohne angenommenes `b`.
- `a :- d.` verbindet `a` positiv mit `d`.
- `b :- not c.` ist der einzige Ableitungsweg für `b`.
- `c :- a,not b.` braucht nach einem erlaubten `not b` weiterhin ein ableitbares `a`.
- `d :- a.` schließt mit `a :- d.` einen positiven Kreis.
- `d :- not c,not e.` ist ein anderer Startweg für `d`, aber **beide** negativen Bedingungen müssen erfüllt sein.
- `e :- b,not a.` erzeugt `e` aus `b`, falls `a` fehlt.
- `e :- d.` ist die positive Alternative für `e`.

Bei Kandidat `{a,b,d,e}` entfallen die äußeren Startwege für `a,d`; der Kreis darf nicht aus der Kandidatenmenge selbst starten. Im Redukt entsteht nur `b`. Beim Kandidaten `{b,e}` bleibt zusätzlich `e :- b.` erhalten; so entstehen genau `b,e`.

Zum Live-Ändern: Wenn ein positiver Fakt `d.` ergänzt wird, hat der `a/d`-Kreis einen äußeren Einstieg. Erst den Redukt prüfen, dann die neue stabile Menge bestimmen; eine frühere Ausschlussbegründung wegen fehlenden Starts gilt dann nicht mehr.

### `uebung/ue1.3/a/programm.lp`

- Diese fünf Regeln sind bewusst eine eigenständige Kopie von 1.2 a. Jede Regel hat exakt die oben erklärte Funktion.
- Nur der Kommentar nennt das neue Ziel: nicht zwei vorgegebene Kandidaten prüfen, sondern **alle** Answer Sets finden.
- Die Antwort zerlegt anhand der wechselseitigen Defaultregeln in `b` oder `c`. Weder beide noch keines ist stabil. In jedem der beiden Fälle sind `a,d,e` festgelegt.
- Der zentrale Test vergleicht die Regeln dieser Datei mit 1.2 a. Werden sie für Experimente geändert, müssen beide Dateien nicht dauerhaft parallel gepflegt werden: besser eine gesonderte Kopie verwenden.

### `uebung/ue1.3/b/programm.lp`

- Hier sind die acht Originalregeln aus 1.2 b wiederholt. Keine Modellliste ersetzt die Originalregeln.
- Die Antwort prüft zuerst den Fall ohne `b`; dann werden `a,c,d,e` hergeleitet.
- Im Fall mit `b` wird weiter nach `a` unterschieden. Ohne `a` entsteht `{b,e}`. Mit `a` entsteht ein klassisches Modell, dessen Redukt aber nur `b` liefert.
- Genau dieser letzte Ausschluss zeigt, warum eine vollständige Antwort mehr als eine Liste plausibel erfüllter Regeln benötigt.

### `uebung/ue1.4/a/programm.lp`

- `canary(tweety).` und `penguin(tux).` sind die Artenfakten.
- `bird(tweety) :- canary(tweety).` macht Tweety zum Vogel.
- `bird(tux) :- penguin(tux).` macht Tux zum Vogel.
- Die zwei Regeln mit `injured(tweety)` und `ok(tweety)` bilden eine Defaultwahl. Jeweils eine Alternative hat im passenden Redukt die positive Bedingung `bird(tweety)`.
- Die zwei eigenen Regeln für Tux bilden eine zweite, unabhängige Defaultwahl. Die Verwendung desselben Prädikatnamens koppelt die unterschiedlichen Grundatome nicht aneinander.
- `flies(tweety) :- ok(tweety),not penguin(tweety).` kann bei gesundem Tweety greifen, weil kein `penguin(tweety)` ableitbar ist.
- `flies(tux) :- ok(tux),not penguin(tux).` entfällt in jedem stabilen Redukt wegen des Pinguinfakts, auch bei gesundem Tux.

Keine Gesundheitsbelegung darf beide oder keinen der zwei Zustände pro Vogel enthalten. Die Antwort prüft für jeden Vogel beide fehlerhaften Belegungen und beide gültigen Einzelzustände. Die Flugatome folgen danach ohne weitere Wahl.

Zum Live-Ändern: Ein zusätzlicher Fakt `penguin(tweety).` würde auch Tweetys Flugregel ausschalten, aber die Gesundheitsregeln nicht entfernen. Nicht aus außerlogischem Wissen folgern, dass ein Kanarienvogel kein Pinguin sein könne; nur die Regeln zählen.

### `uebung/ue1.4/b/programm.lp`

- Drei Fakten `num(1). num(2). num(3).` legen den Zahlenbereich fest.
- Für Zahl 1 erlaubt `lucky(1) :- num(1),not unlucky(1).` die glückliche Alternative; die nächste Regel erlaubt die unglückliche Alternative.
- Für Zahl 2 stehen zwei eigene Regeln mit denselben Funktionen und Argument 2.
- Für Zahl 3 stehen zwei eigene Regeln mit denselben Funktionen und Argument 3.
- Die drei letzten Regeln `p :- unlucky(i),not p.` sind negative Selbstschleifen, die durch jede unglückliche Zahl aktiviert würden.
- Enthielte ein Kandidat `p`, wären alle drei Regeln gelöscht und `p` unbegründet. Ohne `p` würde jedes abgeleitete `unlucky(i)` sofort `p` erzwingen. Deshalb ist keine unglückliche Zahl zulässig.

Die Antwort schreibt diese Prüfung für die drei Zahlen einzeln aus und kontrolliert den vollständigen Redukt des einzig verbleibenden Kandidaten mit drei glücklichen Zahlen.

Zum Live-Ändern: Entferne in einer Kopie nur die letzte `p`-Regel. Dann ist nur Zahl 3 nicht mehr auf diese Weise eingeschränkt; die erste und zweite Regel bleiben aktiv. Erst alle Zustandsmöglichkeiten aufschreiben, dann mit `clingo ... 0` kontrollieren.

## Teil B – Jede Hausübungsdatei erklären

Der verbindliche zweite Teil ist [hausuebung/erklaerung.md](hausuebung/erklaerung.md). Dort werden in getrennten Abschnitten erklärt:
- `hausuebung/ue1.1/a/programm.lp`: Kette ab `d`, fehlendes `m`, ungestarteter `b/f`-Kreis.
- `hausuebung/ue1.1/b/programm.lp`: drei Verbindungskanten, drei Zweischritttouren, genau eine erfolgreiche `finish`-Regel.
- `hausuebung/ue1.2/a/programm.lp`: alle acht Regeln, drei Kandidaten, vollständige Redukte.
- `hausuebung/ue1.2/b/programm.lp`: alle neun Regeln, drei Kandidaten, nicht gestarteter `c/d`-Kreis.
- `hausuebung/ue1.3/a/programm.lp`: dieselben Regeln wie 1.2 a; struktureller Ausschluss von `e`, dann Fallaufteilung nach `a`.
- `hausuebung/ue1.3/b/programm.lp`: dieselben Regeln wie 1.2 b; Fallaufteilung nach `b`, dann `e/f`.
- `hausuebung/ue1.4/a/programm.lp`: jede Vogel-, Geh- und Flugregel; Tux geht positiv, Tweety hat zwei Defaultalternativen.
- `hausuebung/ue1.4/b/programm.lp`: jede Glücksregel und jedes Paar in den `p`-Regeln; höchstens eine glückliche Zahl.
- `hausuebung/ue1.2/pruefe_redukte.py`: alle Funktionen des zusätzlichen Python-Prüfers, seine Grenzen, Sollredukte und tatsächliche Tests.

Die `antwort.md` neben jeder dieser Dateien enthält außerdem den vollständigen Beweis und die konkrete Reduktprobe, nicht nur einen Verweis auf den Solver.

## Zentrale Datei `checks.py`: Schritt für Schritt

### Imports und Dateiauflösung

- Der Kommentarblock erklärt Aufruf und Voraussetzungen. Es werden keine Python-Pakete installiert.
- `from __future__ import annotations` verzögert die Auswertung von Typangaben. Die Angaben beschreiben Datenformen, ohne Daten zu berechnen.
- `dataclass` erzeugt eine Datenklasse; `product` liefert Kombinationen; `json` liest clingo-Ausgaben; `Path` behandelt Dateinamen; `re` prüft Textformen; `shutil` sucht clingo; `subprocess` startet den externen Solver.
- `ROOT = Path(__file__).resolve().parent` wählt den Ordner der Testdatei, nicht das aktuelle Arbeitsverzeichnis. Deshalb funktionieren absolute Aufrufe von anderswo.

### `Rule`

`@dataclass(frozen=True)` verhindert nachträgliches Ändern einer Regel. `head` ist ein einzelner Atomtext. `positive` und `negative` sind unveränderliche Mengen von Körperatomen; die leeren Standardwerte beschreiben einen Fakt. Die Reihenfolge der Literale beeinflusst die Bedeutung nicht. Dieser allgemeine Prüfer vergleicht Modelle; der zusätzliche Hausübungsprüfer bewahrt bei seinen exakten Strukturprüfungen außerdem die Regelreihenfolge und doppelte Fakten.

### `split_body`

1. Eine leere Ergebnisliste und der Klammerzähler `depth=0` werden angelegt.
2. Jedes Zeichen wird mit seinem Index durchlaufen.
3. `(` erhöht die Tiefe; `)` senkt sie. Eine negative Tiefe wird abgelehnt.
4. Nur ein Komma bei Tiefe 0 beendet ein Körperliteral.
5. Kommas innerhalb von `likes(kate,soup)` bleiben deshalb Bestandteil desselben Atoms.
6. Nach der Schleife muss die Tiefe wieder 0 sein. Das letzte Literal wird angehängt; leere Literale werden abgelehnt.

Ein bloßes `split(',')` wäre für Atome mit mehreren Argumenten falsch. Diese Funktion verhindert genau diesen typischen Parserfehler.

### `atom` und `parse`

- `atom` entfernt Leerraum und verlangt mit einem vollständigen regulären Ausdruck einen kleinen Prädikatnamen mit optionalen Konstantenargumenten. Variablen, Choice-Regeln, Ausgabedirektiven und Constraints sind absichtlich nicht unterstützt: Es ist ein Prüfer für **dieses** Grundblatt, kein vollständiger ASP-Parser.
- `parse` entfernt zuerst `%* ... *%`-Blockkommentare, dann `%`-Zeilenkommentare. Die Reihenfolge ist wichtig, weil sonst aus Blockkommentaren scheinbar ausführbarer Resttext übrig bliebe.
- Die übrigen Aussagen werden am Punkt getrennt. Leere Zwischenstücke werden übersprungen.
- Ein optionales `:-` trennt Kopf und Körper. Mehr als eine solche Trennung wird abgelehnt.
- Körper werden durch `split_body` zerlegt. Nur ein vorn stehendes `not ` schiebt das Atom in die negative Menge; alle anderen Körperatome kommen in die positive Menge.
- `Rule(...)` speichert die fertig geprüfte Regel. Die Liste bleibt in Eingabereihenfolge.

### `reduct`

Für jede Regel wird die negative Menge mit dem Kandidaten verglichen. Ist der Schnitt nicht leer, wird die **ganze** Regel ausgelassen. Andernfalls wird eine neue Regel mit gleichem Kopf und gleichem positivem Körper erzeugt; ihr negativer Körper ist leer. Ein positives Körperatom wird nicht entfernt, nur weil es im Kandidaten fehlt.

### `least_steps`

1. Die Funktion verlangt ein positives Programm.
2. Die Stufenliste startet mit der leeren Menge.
3. In jeder Runde werden genau die Köpfe gesammelt, deren positiver Körper in der letzten Stufe liegt. Fakten haben leeren Körper; die leere Menge ist Teilmenge jeder Stufe.
4. Eine Assertion kontrolliert, dass bei der Iteration ab `{}` kein schon hergeleitetes Atom verloren geht.
5. Ist die neue Menge gleich der letzten, ist der Fixpunkt erreicht; sonst wird sie angehängt.

Die letzte Menge ist das kleinste Modell. Die Wiederholung der identischen Schlussstufe wird nur nicht noch einmal gespeichert.

### `stable_models`

- Ein positives Programm benötigt nur seine eine Fixpunktberechnung; es gibt keine Kandidatenkombinationen zu prüfen.
- Bei normalen Programmen werden Kombinationen der **Kopfatome** erzeugt. Atome, die nur im Körper vorkommen, können niemals Teil eines kleinsten Reduktmodells sein und müssen deshalb nicht als wahr geraten werden.
- Für jeden Kandidaten wird erst `reduct`, danach `least_steps` ausgeführt.
- Nur Gleichheit zwischen Kandidat und letztem Fixpunkt nimmt den Kandidaten in die Ergebnisfamilie auf.

Das vollständige Durchtesten ist hier eine unabhängige maschinelle Gegenprobe für kleine endliche Programme. Die schriftlichen Lösungen zu 1.3 verwenden stattdessen die ausdrücklich verlangten strukturellen Fallbeweise.

### `classical_model`

Die Funktion prüft die Implikation jeder Regel: Entweder ist ihr Körper nicht vollständig wahr oder ihr Kopf ist enthalten. Der Körper gilt genau dann, wenn alle positiven Atome enthalten und alle negativen Atome abwesend sind. Diese Funktion erklärt den Unterschied zu Stabilität, ersetzt aber nie die Reduktprüfung.

### `solve_clingo`

1. `shutil.which` sucht das echte ausführbare `clingo`. Fehlt es, scheitert der Test mit einer verständlichen Voraussetzungsmeldung.
2. `subprocess.run` startet ohne Shell und sendet die Originalquelle über stdin an `clingo --outf=2 --warn=none 0 -`.
3. JSON-Ausgabe, sämtliche Modelle und maximal 30 Sekunden Laufzeit werden ausdrücklich angefordert. `--warn=none` unterdrückt nur erwartete Hinweise über reine Körperatome, keine Syntaxfehler.
4. Es werden ausschließlich die dokumentierten SAT-/UNSAT-Rückgabecodes angenommen.
5. Die JSON-Antwort muss einen abgeschlossenen SAT- oder UNSAT-Lauf melden; `Models.More` muss `no` sein.
6. Alle Zeugen aller Aufrufblöcke werden als Mengen gelesen. Gemeldete Anzahl und tatsächliche Zeugenanzahl müssen übereinstimmen; doppelte Modelle werden ausgeschlossen.
7. Eine weitere Prüfung verbindet den SAT-Status mit dem Vorhandensein von Modellen. Ein fehlender Zeuge wird nicht stillschweigend als Erfolg akzeptiert.

### `letters`, `show` und `expectations`

- `letters('ac')` ist nur eine Kurzschreibweise für die nullstelligen Atome `{a,c}`. Für Atome mit Argumenten werden ausdrückliche Zeichenkettenmengen benutzt.
- `show` sortiert Atomnamen für reproduzierbare, lesbare Protokolle.
- `expectations` enthält die aus den schriftlichen Lösungen vorgegebenen Sollmodelle. Sie werden **nicht** aus clingo übernommen.
- Für 1.3 werden die Sollmengen aus 1.2 wiederverwendet, weil dieselben Programme gefragt sind.
- Der gemeinsame Vogelanteil wird mit jeder begründeten Zustandskombination vereinigt; `flies(tweety)` kommt bei der Übung genau im gesunden Zustand hinzu.
- Die Hausübungs-Vogelmodelle enthalten immer `walks(tux)` und genau eine von Tweetys Alternativen.
- Bei den Zahlen enthalten alle Modelle die drei Fakten. Die Übung erwartet drei glückliche Zahlen; die Hausübung erwartet keine oder genau eine glückliche Zahl.

### `test_helpers`

Die Selbsttests kontrollieren zuerst den Parser an einem Atom mit innerem Komma. Danach werden ein positiver Kreis ohne Start, ein wechselseitiger Defaultfall, eine negative Selbstschleife und eine positive Faktenkette geprüft. Drei dieser kleinen Programme werden zusätzlich an clingo übergeben. So wird nicht bloß angenommen, dass der eigene Reduktprüfer korrekt implementiert ist.

### `test_candidates`

Die vier Prüfungen aus Exercise 1.2 werden mit vorgegebenen kleinsten Reduktmodellen verglichen: erster Kandidat bei a ja, zweiter nein; erster bei b nein, zweiter ja. Jede Prüfung kontrolliert sowohl die berechnete Menge als auch den Wahrheitswert der Stabilitätsentscheidung.

### `main` und Startblock

1. Zuerst laufen die Selbsttests.
2. Danach werden alle vorhandenen Aufgabenprogramme gesucht. Die tatsächlich vorhandenen Pfade müssen **genau** der Sollpfadmenge entsprechen; kein Programm darf fehlen oder unbemerkt zusätzlich bleiben.
3. Jedes Programm wird gelesen und geparst. Der unabhängige Reduktprüfer und clingo müssen jeweils exakt die Sollmodellfamilie liefern.
4. Zusätzlich wird geprüft, dass alle Sollmodelle klassische Modelle sind und eine `antwort.md` neben dem Programm existiert.
5. Ausgabezeilen nennen die bestätigten Atomlisten. Die Modellreihenfolge spielt beim Vergleich keine Rolle.
6. Für beide Angaben wird der Regelinhalt von 1.3 gegen 1.2 verglichen.
7. Die speziellen Kandidatenprüfungen und Quiz-Gegenbeispiele laufen ebenfalls.
8. Nur wenn jede Assertion erfolgreich war, erscheint die abschließende OK-Meldung.
9. `if __name__ == '__main__': main()` startet die Tests bei direkter Ausführung, nicht beim Import der Funktionen.

**Nicht mit `python3 -O` starten:** Optimierung würde Assertions abschalten und damit Prüfungen umgehen. Bei einer Änderung müssen die Tests erneut normal laufen. Eine Abweichung ist kein Grund, die Sollmodelle ungeprüft an die neue Ausgabe anzupassen.

## Übrige Dateien

- `README.md`: Einstieg, Befehle, Aufgabenübersicht, Hinweis auf KI-Unterstützung. Keine ausführbaren ASP-Regeln.
- Jede `antwort.md`: Aufgabenfrage, Herleitung, Ergebnis und Probe. Gedankliche Abkürzungen `F`, `N`, `M` sind Mengenbezeichnungen in der Erklärung, keine neuen Programmatome.
- `Angabe/exercise01a.pdf`, `Angabe/exercise01b.pdf`: unveränderte Originale.
- `angabe_blatt01.pdf`: beide Originale hintereinander; keine Umformulierung oder neu gesetzte Angabe.
- `TESTS.md`: kurze Zusammenfassung der real ausgeführten Prüfungen.
- `.gitignore`: hält automatisch erzeugte Python-Caches und LaTeX-Hilfsdateien aus dem Blattcommit heraus.

Es wird nichts in Moodle eingereicht. Vor einer Präsentation die Herleitungen selbst durchgehen und die vorgeschlagenen Änderungen in separaten Kopien testen.
