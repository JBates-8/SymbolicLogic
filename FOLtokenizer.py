"""
File: FOLtokenizer.py
Author: Jackson Bates
Created: 4/23/2020 12:27 AM
"""

TOKENS = {
    "^":"AND",
    "v":"OR",
    "<":"CONOPEN",
    "-":"CONMID",
    ">":"CONEND",
    "(":"PAROPEN",
    ")":"PARCLOSE"
}

class FOLtokenizer:

    def __init__(self, statement_string):
        assert type(statement_string) is str
        self.num_tokens = len(statement_string)
