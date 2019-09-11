"""
File: Atomic.py
Author: Jackson Bates
Created: 9/10/2019 10:05 PM 
"""

class AtomicBase:

    def __init__(self, letter, statement, cur_value = None):
        self.letter = letter
        self.statement = statement
        self.cur_value = cur_value

    def __repr__(self):
        return "Atomic({}, {})".format(self.letter,self.statement)

    def __str__(self):
        return self.letter

    def sentence(self):
        return self.statement

clas