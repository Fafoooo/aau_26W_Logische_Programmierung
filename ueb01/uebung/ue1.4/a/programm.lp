% Exercise 1.4 a: birds, health and flying.
canary(tweety).
penguin(tux).

bird(tweety) :- canary(tweety).
bird(tux) :- penguin(tux).

injured(tweety) :- not ok(tweety), bird(tweety).
ok(tweety) :- not injured(tweety), bird(tweety).
injured(tux) :- not ok(tux), bird(tux).
ok(tux) :- not injured(tux), bird(tux).

flies(tweety) :- ok(tweety), not penguin(tweety).
flies(tux) :- ok(tux), not penguin(tux).
