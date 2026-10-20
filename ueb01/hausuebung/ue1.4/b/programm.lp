% Homework 1, Aufgabe 1.4 b: die Grundregeln inklusive der drei p-Regeln.
num(1). num(2). num(3).

% lucky(X) :- num(X), not unlucky(X).
lucky(1) :- num(1), not unlucky(1).
lucky(2) :- num(2), not unlucky(2).
lucky(3) :- num(3), not unlucky(3).

% unlucky(X) :- num(X), not lucky(X).
unlucky(1) :- num(1), not lucky(1).
unlucky(2) :- num(2), not lucky(2).
unlucky(3) :- num(3), not lucky(3).

% p :- lucky(X), lucky(Y), X != Y, not p.
p :- lucky(1), lucky(2), not p.
p :- lucky(1), lucky(3), not p.
p :- lucky(2), lucky(3), not p.
