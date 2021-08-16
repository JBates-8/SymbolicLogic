"""
File: bnfparser.py
Author: Jackson Bates
Created: 11/16/2019 6:44 AM
"""



import re
import logging
logging.basicConfig()

class tokenizer:


    SYM = {
    "[A-Z]": "T_UCHAR",
    "[a-z]": "T_LCHAR",
    '<'    : "T_LTHAN",
    '>'    : "T_GTHAN",
    '\n'   : "T_NEWLINE",
    ' '    : "T_WHITESPACE",
    "\["   : "T_OPENBRACK",
    "\]"   : "T_CLOSEBRACK",
    "\="   : "T_EQUALS",
    "\:"   : "T_COLON",
    "\-"   : "T_SUB",
    "\+"   : "T_ADD",
    "\|"   : "T_VBAR"}



    def __init__(self, filename):
        self.filename = filename
        assert type(filename) is str
        with open(filename,'r') as file:
            self.chars = file.read()
            self.idx = 0
            
            end = len(self.chars)
            self.unclassified = []
            self.classified = []
            self.count = 0
            for i,c in enumerate(self.chars):
                self.classify(c,i)
            print("Percent classified: {:.2f}% ({}/{})".format(self.count*100/end,self.count, end))
            print(self.classified)
            print("Unclassified items: {}".format(self.unclassified))

    def verify_file(self):
        pass

    def classify(self, c, idx):
        for key,val in tokenizer.SYM.items():
            regex = re.compile(key)
            match = regex.match(c)
            if(match):
                print("Match found:",c,val,match)
                self.count += 1
                self.classified.append((val, idx))
                return
        print("No match found:","\'{}\'".format(c))
        self.unclassified.append(c)

class regexContainer:

    def __init__(self, rstring, desc):
        self.regex = rstring
        self.description = desc

    def __str__(self):
        return "regexContainer(\"{}\",\"{}\")".format(self.regex, self.description)

class literalRegex(regexContainer):

    def __init__(self, rstring):
        super().__init__(rstring, "String/Character literal regex")





REGEX_LIST = [
    r"<[a-z]+>$", #nonterminal
    r"::=$",      #replace symbol
    r"\[[A-Y]-[B-Z]\]$",
    r"\|$"
]
class alpharange:

    def __init__(self, ch1, ch2):
        self._ch1 = ch1
        self._ch2 = ch2
        self._ord1 = ord(ch1)
        self._ord2 = ord(ch2)
        assert self._ord1 < self._ord2
        self._alphalist = [chr(i) for i in range(self._ord1, self._ord2+1)]
        print()

    def __str__(self):
        return "[{},...,{}]".format(self._ch1, self._ch2)

    def __repr__(self):
        return "(alpharange [{},{}] {})".format(self._ch1, self._ch2, hex(id(self)))

class option:

    def __init__(self, choices):
        self.choices = choices
        self.size = len(self.choices)

    def __str__(self):
        s = ""
        for c in self.choices:
            s += c + " or "
        s = s[:-4]
        return s

    def __repr__(self):
        return str(self)


class bnfparser:

    def __init__(self, bnf_file):
        # parse grammar file and set terminals correctly
        self.filename = bnf_file
        with open(self.filename) as f:
            self.lines = f.readlines().copy()
            f.close()
        self.get_terminals()
        print(self.terminals)

    def get_terminals(self):
        self.terminals = {}
        for line in self.lines:
            regex = re.compile(r"<([a-z]+)>\s+::=\s+(.+)$")
            result = regex.search(line)
            k,v = result.group(1), result.group(2)
            optional = [el.strip() for el in v.split(" | ")]
            if len(optional) == 1:
                self.terminals[k] = v
            else:
                self.terminals[k] = option(optional)

    def convert(self, item):
        charsetregex = ""




    def getterminals(self):
        return self.terminals.keys()




bnf = bnfparser("grammar.txt")
print(alpharange("A","K"))
print(repr(alpharange("C","X")))
