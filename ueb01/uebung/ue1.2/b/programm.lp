% Exercise 1.2 b; candidates X1={a,b,d,e}, X2={b,e}.
a :- not b.
a :- d.
b :- not c.
c :- a, not b.
d :- a.
d :- not c, not e.
e :- b, not a.
e :- d.
