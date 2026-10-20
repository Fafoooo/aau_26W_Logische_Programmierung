% Homework 1, Aufgabe 1.1 a: unveraendertes positives Grundprogramm.
a :- b, d.
a :- c, e.
b :- d, m.
b :- e, f.
c :- d, e.
d.
e :- d.
f :- b, c.
g :- d, f.
g :- e, h.
h :- c, k.
k :- a, e.
