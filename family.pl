male(jack).
male(oliver).
male(ali).
male(james).
male(simon).
male(harry).

female(helen).
female(sophie).
female(jess).
female(lily).

parent_of(jack, jess).
parent_of(jack, lily).
parent_of(helen, jess).
parent_of(helen, lily).
parent_of(oliver, james).
parent_of(sophie, james).
parent_of(jess, simon).
parent_of(ali, simon).
parent_of(lily, harry).
parent_of(james, harry).

father_of(X, Y) :-
    male(X),
    parent_of(X, Y).

mother_of(X, Y) :-
    female(X),
    parent_of(X, Y).

grandfather_of(X, Y) :-
    male(X),
    parent_of(X, Z),
    parent_of(Z, Y).

grandmother_of(X, Y) :-
    female(X),
    parent_of(X, Z),
    parent_of(Z, Y).

sister_of(X, Y) :-
    female(X),
    parent_of(F, Y),
    parent_of(F, X),
    X \= Y.

brother_of(X, Y) :-
    male(X),
    parent_of(F, Y),
    parent_of(F, X),
    X \= Y.

aunt_of(X, Y) :-
    female(X),
    parent_of(Z, Y),
    sister_of(X, Z).

uncle_of(X, Y) :-
    male(X),
    parent_of(Z, Y),
    brother_of(X, Z).

ancestor_of(X, Y) :-
    parent_of(X, Y).

ancestor_of(X, Y) :-
    parent_of(X, Z),
    ancestor_of(Z, Y).

print_family_tree(Person) :-
    write('Family tree for '), write(Person), write(':'), nl,
    print_family_tree_helper(Person, 0).

print_family_tree_helper(Person, Tabs) :-
    Tabs >= 0,
    format('~*c', [Tabs, 32]),
    write(Person), nl,
    (father_of(Person, Child); mother_of(Person, Child)),
    NextTabs is Tabs + 4,
    print_family_tree_helper(Child, NextTabs).
    
% grandmother_of(X, harry).
