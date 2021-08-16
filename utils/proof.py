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