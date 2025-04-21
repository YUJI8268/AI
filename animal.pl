animal(lion) :- mammal, carnivore, has_mane.
animal(tiger) :- mammal, carnivore, has_stripes.
animal(cheetah) :- mammal, carnivore, has_spots.
animal(elephant) :- mammal, herbivore, has_trunk.
animal(zebra) :- mammal, herbivore, has_stripes.
animal(giraffe) :- mammal, herbivore, has_long_neck.
animal(crocodile) :- reptile, carnivore, has_sharp_teeth.
animal(tortoise) :- reptile, herbivore, has_shell.
animal(parrot) :- bird, herbivore, has_colored_feathers.
animal(eagle) :- bird, carnivore, has_sharp_beak.

mammal :- verify(has_fur), verify(gives_birth).
reptile :- verify(has_scales), verify(lays_eggs).
bird :- verify(has_feathers), verify(lays_eggs).
carnivore :- verify(eats_meat).
herbivore :- verify(eats_plants).
has_mane :- verify(has_mane).
has_stripes :- verify(has_stripes).
has_spots :- verify(has_spots).
has_trunk :- verify(has_trunk).
has_long_neck :- verify(has_long_neck).
has_sharp_teeth :- verify(has_sharp_teeth).
has_shell :- verify(has_shell).
has_colored_feathers :- verify(has_colored_feathers).
has_sharp_beak :- verify(has_sharp_beak).

:- dynamic(yes/1).
:- dynamic(no/1).

verify(Attribute) :-
    (yes(Attribute) -> true;
    no(Attribute) -> fail;
    ask(Attribute)).

ask(Attribute) :-
    format('Does the animal have the following attribute: ~w? (yes/no) ', [Attribute]),
    read(Response), nl,
    ((Response == yes ; Response == y) -> assertz(yes(Attribute));
    assertz(no(Attribute)), fail).

identify :-
    retractall(yes(_)),
    retractall(no(_)),
    animal(Animal),
    format('The animal is: ~w', [Animal]), nl, !.

identify :-
    write('No matching animal found!'), nl.

%identify.
