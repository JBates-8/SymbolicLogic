"""
File: tfl.py
Author: Jackson Bates
Created: 9/9/2019 1:01 PM 
"""

import nltk
import math



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


def statement_list(statement, lst):
    # note for the initial call it should be statement_list(statement, [])
    t = type(statement)
    lst.append(statement)
    if t is Atomic:
        return lst
    elif t is Negation:
        return statement(statement.negated,lst)
    elif t is Conditional:
        return lst




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


