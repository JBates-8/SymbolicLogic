"""
Class for theorems in mathematics
"""

wildcard = '*'

class Definition:

    def __init__(self, statement_str):
        self.statement = statement_str
        self.find_keywords()

    def find_keywords(self):
        self.keywords = []
        for word in self.statement.split(" "):
            if word.startswith(wildcard) and word.endswith(wildcard):
                self.keywords.append(word)


thms = []
with open("defs.txt","r") as f:
    for line in [l.strip() for l in f.readlines()]:
        print(line)
        thm = Definition(line)
        print(thm.keywords)




