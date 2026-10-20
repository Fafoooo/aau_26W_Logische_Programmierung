# Exercise 1.1 b

**Aufgabe:** Das Answer Set des positiven Programms über Essensvorlieben bestimmen. Alle acht `likes`-Fakten und zehn ground Regeln stehen in `programm.lp`; Zeilen mit `%` sind nur Kommentare.

Sei
```text
F = {likes(kate,fish), likes(kate,soup),
     likes(mike,beef), likes(mike,cake),
     likes(paul,duck), likes(paul,pork),
     likes(tina,beef), likes(tina,soup)}.
```

## Fixpunkt

1. `I0={}`.
2. `I1=F`: Genau die acht Fakten werden abgeleitet.
3. `I2=F ∪ {order(beef),order(soup)}`:
   - `likes(mike,beef)` und `likes(tina,beef)` gelten, daher entsteht `order(beef)`.
   - `likes(kate,soup)` und `likes(tina,soup)` gelten, daher entsteht `order(soup)`.
4. `I3=I2 ∪ {happy(kate),happy(mike),happy(tina)}`:
   - Kate mag Suppe, und Suppe wird bestellt: `happy(kate)`.
   - Mike mag Rindfleisch, und Rindfleisch wird bestellt: `happy(mike)`.
   - Tina mag Rindfleisch, und Rindfleisch wird bestellt: `happy(tina)`.
   - Tina mag Suppe, und Suppe wird bestellt: dieselbe Aussage `happy(tina)` wird ein zweites Mal begründet, aber nicht ein zweites Mal in die Menge aufgenommen.
5. `I4=I3`: Kein zusätzliches Atom wird abgeleitet.

**Ergebnis:**
```text
{likes(kate,fish), likes(kate,soup),
 likes(mike,beef), likes(mike,cake),
 likes(paul,duck), likes(paul,pork),
 likes(tina,beef), likes(tina,soup),
 order(beef), order(soup),
 happy(kate), happy(mike), happy(tina)}
```

## Probe und ausgeschlossene Atome

- Alle acht Fakten sind im Ergebnis enthalten.
- Beide `order`-Regeln haben wahren Körper und ihren Kopf im Ergebnis.
- `happy(kate)` über Fisch hat falschen Körper, weil `order(fish)` fehlt.
- `happy(kate)` über Suppe hat wahren Körper und enthaltenen Kopf.
- `happy(mike)` über Rindfleisch hat wahren Körper und enthaltenen Kopf.
- `happy(mike)` über Kuchen hat falschen Körper, weil `order(cake)` fehlt.
- Pauls Regel über Ente hat falschen Körper, weil `order(duck)` fehlt.
- Pauls Regel über Schweinefleisch hat falschen Körper, weil `order(pork)` fehlt.
- Tinas Regel über Rindfleisch hat wahren Körper und enthaltenen Kopf.
- Tinas Regel über Suppe hat wahren Körper und enthaltenen Kopf.

`order(fish)`, `order(cake)`, `order(duck)` und `order(pork)` haben keine definierende Regel. Sie können im kleinsten Modell nicht entstehen. Deshalb gehört `happy(paul)` nicht zum Answer Set.

Die allgemeine `order(Z)`-Regel im Kommentar ist keine zusätzliche ausführbare Regel. Wir verwenden genau die expliziten ground Regeln der Angabe.

Ausführen: `clingo programm.lp 0`. Gegenprüfung: `python3 ../../../checks.py`.
