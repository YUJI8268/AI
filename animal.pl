% Animal Recognition Expert System
% Knowledge Base with rules for animals

% Facts
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

% Classification Rules
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

% Dynamic fact storage for user responses
:- dynamic(yes/1).
:- dynamic(no/1).

% Asking user for verification
verify(Attribute) :-
    (yes(Attribute) -> true;
    no(Attribute) -> fail;
    ask(Attribute)).

% Asking the user and storing the response
ask(Attribute) :-
    format('Does the animal have the following attribute: ~w? (yes/no) ', [Attribute]),
    read(Response), nl,
    ((Response == yes ; Response == y) -> assertz(yes(Attribute));
    assertz(no(Attribute)), fail).

% Identify the animal based on attributes
identify :-
    retractall(yes(_)), % Reset previous answers
    retractall(no(_)),
    animal(Animal),
    format('The animal is: ~w', [Animal]), nl, !.

% If no match is found
identify :-
    write('No matching animal found!'), nl.
