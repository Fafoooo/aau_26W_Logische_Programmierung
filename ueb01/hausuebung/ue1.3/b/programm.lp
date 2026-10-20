% Homework 1, Aufgabe 1.3 b: eigenstaendige Kopie von Aufgabe 1.2 b.
%*
X1 = {a,c,d,f}
X2 = {b,c,d,e}
X3 = {b,e}
*%
a :- not b.
b :- not c.
b :- not f.
c :- a.
c :- d.
d :- c, e.
d :- not b.
e :- not a, not f.
f :- not e.
