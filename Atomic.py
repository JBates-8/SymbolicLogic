"""
File: Atomic.py
Author: Jackson Bates
Created: 11/4/2019 12:34 PM 
"""


class Atomic:

    def __init__(self, character):
        self.character = character

    def __repr__(self):
        return "<Atomic> {}".format(self.character)

    def __str__(self):
        return self.character


class Connective:

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2


class Negation:

    def __init__(self, item):
        self.negated = item

    def __repr__(self):
        return "Negation({})".format(repr(self.negated))

    def __str__(self):
        if isinstance(self.negated, Connective):
            return "~({})".format(str(self.negated))
        else:
            return "~{}".format(str(self.negated))

    def to_english(self):
        # TODO Update this to allow for non atomic things to be converted
        print("It is not the case that {}".format(self.negated.sentence()))

    def eval_truth(self):
        return not (self.negated.eval_truth())


class Conjunction(Connective):

    def __init__(self, a1, a2):
        super(Conjunction, self).__init__(a1, a2)

    def __repr__(self):
        return "{}({} ^ {})".format(self.__class__.__name__, repr(self.a1), repr(self.a2))

    def __str__(self):
        first_is_connective = isinstance(self.a1, Connective)
        second_is_connective = isinstance(self.a2, Connective)
        if first_is_connective and second_is_connective:
            return "({}) ^ ({})".format(str(self.a1), str(self.a2))
        elif first_is_connective:
            return "({}) ^ {}".format(str(self.a1), str(self.a2))
        elif second_is_connective:
            return "{} ^ ({})".format(str(self.a1), str(self.a2))
        else:
            return "{} ^ {}".format(str(self.a1), str(self.a2))

    def to_english(self):
        print("{} and {}".format(self.a1, self.a2))


class Disjunction(Connective):

    def __init__(self, a1, a2):
        super().__init__(a1, a2)
        self.first = a1
        self.second = a2
        self.type = Connective.Type.BINARY

    def __repr__(self):
        return "Disjunction({} v {})".format(repr(self.first), repr(self.second))

    def __str__(self):
        first_is_connective = isinstance(self.first, Connective)
        second_is_connective = isinstance(self.second, Connective)
        if first_is_connective and second_is_connective:
            return "({}) v ({})".format(str(self.first), str(self.second))
        elif first_is_connective:
            return "({}) v {}".format(str(self.first), str(self.second))
        elif second_is_connective:
            return "{} v ({})".format(str(self.first), str(self.second))
        else:
            return "{} v {}".format(str(self.first), str(self.second))

    def to_english(self):
        print("{} or {}".format(self.first, self.second))


class Conditional(Connective):

    def __init__(self, a1, a2):
        super().__init__(a1, a2)
        self.antecedent = a1
        self.consequent = a2
        self.type = Connective.Type.BINARY

    def __repr__(self):
        return "Conditional({} -> {})".format(repr(self.antecedent), repr(self.consequent))

    def __str__(self):
        antecedent_is_connective = isinstance(self.antecedent, Connective)
        consequent_is_connective = isinstance(self.consequent, Connective)
        if antecedent_is_connective and consequent_is_connective:
            return "({}) -> ({})".format(str(self.antecedent), str(self.consequent))
        elif antecedent_is_connective:
            return "({}) -> {}".format(str(self.antecedent), str(self.consequent))
        elif consequent_is_connective:
            return "{} -> ({})".format(str(self.antecedent), str(self.consequent))
        else:
            return "{} -> {}".format(str(self.antecedent), str(self.consequent))

    def to_english(self):
        print("If {} then {}".format(self.antecedent, self.consequent))


class Biconditional(Connective):

    def __init__(self, a1, a2):
        super().__init__(a1, a2)
        self.first = a1
        self.second = a2
        self.type = Connective.Type.BINARY

    def __repr__(self):
        return "Biconditional({} <-> {})".format(repr(self.first), repr(self.second))

    def __str__(self):
        first_is_connective = isinstance(self.first, Connective)
        second_is_connective = isinstance(self.second, Connective)
        if first_is_connective and second_is_connective:
            return "({}) <-> ({})".format(str(self.first), str(self.second))
        elif first_is_connective:
            return "({}) <-> {}".format(str(self.first), str(self.second))
        elif second_is_connective:
            return "{} <-> ({})".format(str(self.first), str(self.second))
        else:
            return "{} <-> {}".format(str(self.first), str(self.second))

    def to_english(self):
        print("{} if and only if {}".format(self.first, self.second))
