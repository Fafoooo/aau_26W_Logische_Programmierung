% Homework 1, Aufgabe 1.2 a: Originalprogramm, keine Kandidaten als Fakten.
%*
X1 = {}
X2 = {a,c}
X3 = {a,b,e}
*%
a :- not d.
b :- not a.
b :- e, not d.
c :- a, not e.
c :- b, not e.
d :- not a, not e.
e :- a, d.
e :- b, not c.
