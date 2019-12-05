"""
File: bnfparser.py
Author: Jackson Bates
Created: 11/16/2019 6:44 AM 
"""



import re


class regexContainer:

    def __init__(self, rstring, desc):
        self.regex = rstring
        self.description = desc

    def __str__(self):
        return "regexContainer(\"{}\",\"{}\")".format(self.regex, self.description)


class literalRegex(regexContainer):

    def __init__(self, rstring):
        super().__init__(rstring, "String/Character literal regex")




def alpharange(ch1, ch2):
    i1, i2 = ord(ch1), ord(ch2)
    assert i1 < i2
    cur = i1
    while cur <= i2:
        yield chr(cur)
        cur += 1

REGEX_LIST = [
    r"<[a-z]+>$", #nonterminal
    r"::=$",      #replace symbol
    r"\[[A-Y]-[B-Z]\]$",
    r"\|$"
]


class bnfparser:

    def __init__(self, bnf_file):
        # parse grammar file and set terminals correctly
        self.filename = bnf_file
        with open(self.filename) as f:
            self.lines = f.readlines().copy()
            f.close()
        self.get_terminals()

    def get_terminals(self):
        self.terminals = {}
        for line in self.lines:
            line = [part.split() for part in line.split(" ::= ")]
            if len(line[1]) == 1:
                line[1] = line[1][0]
                regex = re.compile(r"\[[A-Y]-[B-Z]\]$")
                if regex.match(line[1]): # convert to list of chars
                    line[1] = list(alpharange(line[1][1],line[1][3]))
            self.terminals[line[0][0]] = line[1]


    def getterminals(self):
        return self.terminals.keys()



p = bnfparser("grammar.txt")
print(p.getterminals())

r = literalRegex(r"'.'")
print(r)
print([r])