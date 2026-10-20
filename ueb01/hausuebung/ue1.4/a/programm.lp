% Homework 1, Aufgabe 1.4 a: alle expliziten Grundregeln der Angabe.
canary(tweety).
penguin(tux).

% bird(X) :- canary(X).
bird(tweety) :- canary(tweety).
bird(tux) :- canary(tux).
% bird(X) :- penguin(X).
bird(tweety) :- penguin(tweety).
bird(tux) :- penguin(tux).

% walks(X) :- penguin(X).
walks(tweety) :- penguin(tweety).
walks(tux) :- penguin(tux).
% walks(X) :- bird(X), not flies(X).
walks(tweety) :- bird(tweety), not flies(tweety).
walks(tux) :- bird(tux), not flies(tux).

% flies(X) :- bird(X), not walks(X).
flies(tweety) :- bird(tweety), not walks(tweety).
flies(tux) :- bird(tux), not walks(tux).
