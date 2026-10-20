% Homework 1, Aufgabe 1.1 b: ausschliesslich die Grundregeln der Angabe.
conn(amsterdam,brussels).
conn(brussels,cologne).
conn(cologne,amsterdam).

% tour(X,Z) :- conn(X,Y), conn(Y,Z).
tour(amsterdam,cologne) :- conn(amsterdam,brussels),
                           conn(brussels,cologne).
tour(brussels,amsterdam) :- conn(brussels,cologne),
                           conn(cologne,amsterdam).
tour(cologne,brussels) :- conn(cologne,amsterdam),
                         conn(amsterdam,brussels).

% finish(Y) :- tour(X,Y), conn(X,amsterdam).
finish(cologne) :- tour(amsterdam,cologne),
                   conn(amsterdam,amsterdam).
finish(amsterdam) :- tour(brussels,amsterdam),
                     conn(brussels,amsterdam).
finish(brussels) :- tour(cologne,brussels),
                    conn(cologne,amsterdam).
