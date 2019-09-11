"""
File: tfl.py
Author: Jackson Bates
Created: 9/9/2019 1:01 PM 
"""

import nltk
import math
from enum import Enum


class TwoWayDict(dict):
    def __setitem__(self, key, value):
        # Remove any previous connections with these values
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

    def __len__(self):
        """Returns the number of connections"""
        return dict.__len__(self) // 2




class Connective:

    class Type(Enum):
        UNARY = 1
        BINARY = 2



class Negation(Connective):

    def __init__(self, item):
        self.negated = item
        self.type = Connective.Type.UNARY

    def __repr__(self):
        return "Negation({})".format(repr(self.negated))

    def __str__(self):
        if isinstance(self.negated,Connective):
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
        self.first = a1
        self.second = a2
        self.type = Connective.Type.BINARY

    def __repr__(self):
        return "Conjunction({} ^ {})".format(repr(self.first), repr(self.second))

    def __str__(self):
        first_is_connective = isinstance(self.first, Connective)
        second_is_connective = isinstance(self.second, Connective)
        if first_is_connective and second_is_connective:
            return "({}) ^ ({})".format(str(self.first), str(self.second))
        elif first_is_connective:
            return "({}) ^ {}".format(str(self.first), str(self.second))
        elif second_is_connective:
            return "{} ^ ({})".format(str(self.first), str(self.second))
        else:
            return "{} ^ {}".format(str(self.first), str(self.second))

    def to_english(self):
        print("{} and {}".format(self.first, self.second))


class Disjunction(Connective):

    def __init__(self, a1, a2):
        self.first = a1
        self.second = a2
        self.type = Connective.Type.BINARY

    def __repr__(self):
        return "Disjunction({} V {})".format(repr(self.first), repr(self.second))

    def __str__(self):
        first_is_connective = isinstance(self.first, Connective)
        second_is_connective = isinstance(self.second, Connective)
        if first_is_connective and second_is_connective:
            return "({}) V ({})".format(str(self.first), str(self.second))
        elif first_is_connective:
            return "({}) V {}".format(str(self.first), str(self.second))
        elif second_is_connective:
            return "{} V ({})".format(str(self.first), str(self.second))
        else:
            return "{} V {}".format(str(self.first), str(self.second))

    def to_english(self):
        print("{} or {}".format(self.first, self.second))


class Conditional(Connective):

    def __init__(self, a1, a2):
        self.antecedent = a1
        self.consequent = a2
        self.type = Connective.Type.BINARY

    def __repr__(self):
        return "Conditional({} -> {})".format(repr(self.antecedent),repr(self.consequent))

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
        self.first = a1
        self.second = a2
        self.type = Connective.Type.BINARY

    def __repr__(self):
        return "Biconditional({} <-> {})".format(repr(self.first),repr(self.second))

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
        print("{} if and only if {}".format(self.first,self.second))


class TruthTable:



    def __init__(self, atomics, statement):
        self.atomics = atomics
        self.statement = statement
        self.len = len(atomics)
        print("atomics: {}".format(self.atomics))
        print("statement: {}".format(self.statement))
        self.print_bar(self.len)
        self.print_list(self.atomics)
        for i in range(0,2**self.len):
            bin_str = "{}".format(bin(i)[2:].zfill(self.len))
            values = []
            for bit in bin_str:
                if bit is '0':
                    values.append("T")
                else:
                    values.append("F")
            self.print_bar(self.len)
            self.print_list(values)
        self.print_bar(self.len)


    def print_bar(self,len):
        spacer = '#'
        print(spacer * ((4 * len) + 1))

    def print_list(self, lst):
        spacer = '#'
        for el in lst:
            print("{} {} ".format(spacer, el), end="")
        print(spacer)



def get_atomics(statement, visited):
    if type(statement) is Atomic:
        return visited.append(statement)
    elif isinstance(statement, Connective):



if __name__ == '__main__':
    a = Atomic("A","Witches are from Salem")
    b = Atomic("B","Math professors are cool")
    c = Atomic("C","I will run")
    p = Atomic("P","Jean is in France")
    f = Atomic("F","Mary can jump high")
    q = Atomic("Q","Josh should be in 8th grade")
    neg1 = Negation(p)
    neg2 = Negation(f)
    neg3 = Negation(q)
    cond = Conditional(f,q)
    bi = Biconditional(p,f)
    cond2 = Conditional(b,a)
    cond3 = Conditional(a,cond2)
    cond4 = Biconditional(bi,cond3)
    conj = Conjunction(a,b)
    disj = Disjunction(a,b)
    print(p,repr(p))
    print(f,repr(f))
    print(q,repr(q))
    print(neg1, repr(neg1))
    print(cond, repr(cond))
    print(bi, repr(bi))
    print(conj, repr(conj))
    print(disj, repr(disj))
    neg1.to_english()
    neg2.to_english()
    neg3.to_english()
    bi.to_english()
    cond.to_english()
    print(cond4)
    cond4.to_english()
    lst = [a,b,c]
    statement = Conjunction(a,b)
    statement = Negation(statement)
    statement = Conditional(c,statement)
    print(statement)
    tt = TruthTable(lst, statement)


