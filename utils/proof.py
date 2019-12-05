"""
File: proof.py
Author: Jackson Bates
Created: 11/4/2019 12:18 PM 
"""

from inspect import stack, trace

from enum import Enum
import logging
from logging import Formatter, critical, error, warning, info, debug

# Source: https://stackoverflow.com/questions/14844970/modifying-logging-message-format-based-on-message-logging-level-in-python3
class CustomFormatter(Formatter):

    err_fmt = "ERROR: %(msg)s"
    dbg_fmt = "DBG: %(module)s: %(lineno)d: %(msg)s"
    info_fmt = "%(msg)s"

    def __init__(self):
        super().__init__(fmt="%(levelno)d: %(msg)s", datefmt=None, style='%')

    def format(self, record):

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._style._fmt

        # Replace the original format with one customized by logging level
        if record.levelno == logging.DEBUG:
            self._style._fmt = CustomFormatter.dbg_fmt

        elif record.levelno == logging.INFO:
            self._style._fmt = CustomFormatter.info_fmt

        elif record.levelno == logging.ERROR:
            self._style._fmt = CustomFormatter.err_fmt

        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)

        # Restore the original format configured by the user
        self._style._fmt = format_orig

        return result

LOGGER_FORMAT = "[%(levelname)5s] (%(asctime)s) - %(message)s"
logging.basicConfig(format = LOGGER_FORMAT, level = logging.DEBUG)
logger = logging.getLogger("proof.py")
info("Logger created")


def reprs(*args):
    s = ""
    for arg in args:
        s += str(repr(arg))+" "
    debug(s)

class Atomic:

    def __init__(self, character):
        self.character = character

    def __repr__(self):
        return "<Atomic> {}".format(self.character)

    def __str__(self):
        return self.character

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



S = {'^':"Conjunction",
     'v':"Disjunction",
     "->":"Conditional",
     "<->":"Biconditional",
     '(':"Open Sub-Statement",
     ')':"Close Sub-Statement"}

debug("Symbol Dictionary (S): {}".format(S))


def parenloc(text):
    istart = []  # stack of indices of opening parentheses
    d = {}
    for i, c in enumerate(text):
        if c == '(':
             istart.append(i)
        if c == ')':
            try:
                d[istart.pop()] = i
            except IndexError:
                print('Too many closing parentheses')
    if istart:  # check if stack is empty afterwards
        print('Too many opening parentheses')
    return d

def count(symb, statement):
    if symb not in statement:
        return (False, 0)
    else:
        c = 1
        idx = statement.find(symb)
        tmp = statement[idx+2:]
        reprs(tmp, idx, c)
        idx = tmp.find(symb)
        while idx > 0:
            c += 1
            tmp = tmp[idx+2:]
            idx = tmp.find(symb)
            reprs(tmp, idx, c)
        return (True, c)


def get_symbols(statement):
    debug(statement)
    debug(S.keys())
    symbols = {}
    for symb in S.keys():
        isin = count(symb, statement)
        if isin[0]:
            symbols[symb] = isin[1]
        debug( "{} in {} : {}".format( symb, statement, isin))
    debug(symbols)
    parens = parenloc(statement)
    debug(parens)



def statement_from_str(statement):
    if len(statement)==1 and statement.isalpha() and statement.isupper():
        debug("Atomic: {}".format(statement))
    else:
        sym = get_symbols(statement)
        info(sym)


def proof_solve(assumptions, conclusion):
    info("Assumptions: ")
    for i,a in enumerate(assumptions):
        info("\t({}) {}".format(i+1,a))
    info("Conclusion: ")
    info("\t\t{}".format(conclusion))
    for a in assumptions:
        statement_from_str(a)




assumpts = ["A","(A->B)->(C->D)"]
conc = "B"

proof_solve(assumpts, conc)