# Exercise 1.1 a

**Aufgabe:** Das Answer Set des positiven Programms in `programm.lp` bestimmen. Die neun ausführbaren Regeln sind wörtlich aus der Angabe übernommen.

Für ein positives Programm ist das Answer Set das kleinste Modell. Wir starten bei `I0={}` und wenden alle Regeln synchron an: Körper werden immer in der vorherigen Stufe geprüft.

1. `I0={}`.
2. `I1={a,d}`: Die beiden Fakten `a.` und `d.` haben leeren Körper und gelten ohne Voraussetzung.
3. `I2={a,d,g}`: `g :- a,d.` ist nun anwendbar. Fakten bleiben erhalten. `b` braucht `e` oder `f`; beides fehlt. `e` braucht `b`; es fehlt. Die Regel für `c` mit `d,g` wartet noch auf das neue `g`.
4. `I3={a,c,d,g}`: `c :- d,g.` ist nun anwendbar.
5. `I4=I3`: Kein weiterer Körper wird wahr. Der Fixpunkt ist erreicht.

`f` hat keine definierende Regel. Daher kann es in keiner Stufe entstehen. Die Regeln `b :- e.` und `e :- b,d.` liefern ohne anfängliches `b` oder `e` keinen Startpunkt. `b`, `e` und `f` gehören nicht zum kleinsten Modell.

**Ergebnis:** `{a,c,d,g}` ist das einzige Answer Set.

**Probe jeder Regel:**
- `a.`: `a` ist enthalten.
- `b :- e.`: `e` fehlt, also verlangt die Regel kein `b`.
- `b :- f.`: `f` fehlt.
- `c :- b,f.`: `b` und `f` fehlen.
- `c :- d,g.`: Beide Körperatome und der Kopf `c` sind enthalten.
- `d.`: `d` ist enthalten.
- `e :- b,d.`: `b` fehlt.
- `g :- a,b.`: `b` fehlt.
- `g :- a,d.`: Beide Körperatome und `g` sind enthalten.

Damit ist die Menge ein Modell. Die Fixpunktberechnung bestätigt zusätzlich ihre Minimalität; allein die Regelprobe würde dafür nicht ausreichen.

Ausführen: `clingo programm.lp 0`. Alle Modelle werden auch durch `../../../checks.py` kontrolliert.
