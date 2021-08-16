"""
File: FirstOrderLogic.py
Author: Jackson Bates
Created: 4/5/2020 4:02 PM

First Order Logic in Python

Constants:           TODO
Variables:           TODO
Predicates:          TODO
Functions/Relations: TODO
Connectives:         TODO
Equality:            TODO
Quantifiers:         TODO
Atomic Sentences:    TODO

2 parts:
 - Statement processing / nlp
 - Symbolic representation of statements
"""

import logging

class Atomic:

    def __init__(self, character):
        self.character = character

    def __repr__(self):
        return "<Atomic> {}".format(self.character)

    def __str__(self):
        return self.character


class Negation:

    def __init__(self, a1):
        self.a1 = a1

    def __repr__(self):
        return "Negation({})".format(repr(self.a1))

    def __str__(self):
        if isinstance(self.a1,Connective):
            return "~({})".format(str(self.a1))
        else:
            return "~{}".format(str(self.a1))


class Connective:

    def __init__(self, a1 = "A", a2 = "B", symbol = "*"):
        self.a1 = a1
        self.a2 = a2
        self.symbol = symbol

    def __repr__(self):
        return "{}({} {} {})".format(self.__class__.__name__, repr(self.a1), self.symbol, repr(self.a2))

    def __str__(self):
        if isinstance(self.a1, Connective) and isinstance(self.a2, Connective):
            return "({}) {} ({})".format(str(self.a1), self.symbol, str(self.a2))
        elif isinstance(self.a1, Connective):
            return "({}) {} {}".format(str(self.a1), self.symbol, str(self.a2))
        elif isinstance(self.a2, Connective):
            return "{} {} ({})".format(str(self.a1), self.symbol, str(self.a2))
        else:
            return "{} {} {}".format(str(self.a1), self.symbol, str(self.a2))


class Conjunction(Connective):

    def __init__(self, a1, a2):
        super(Conjunction, self).__init__(a1, a2, "^")


class Disjunction(Connective):

    def __init__(self, a1, a2):
        super(Disjunction, self).__init__(a1, a2, "v")


class Conditional(Connective):

    def __init__(self, a1, a2):
        super(Conditional, self).__init__(a1, a2, "->")


class Biconditional(Connective):

    def __init__(self, a1, a2):
        super(Biconditional, self).__init__(a1, a2, "<->")


baseCon = Connective("A", "B")
print(baseCon)
print(repr(baseCon))
conj = Conjunction("A", "B")
print(conj)
print(repr(conj))
print(Disjunction("A","B"))
print(Conditional("A","B"))
print(Biconditional("A","B"))





