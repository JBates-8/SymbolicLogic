"""
File: main.py
Author: Jackson Bates
Created: 8/28/2019 2:11 PM 
"""

atomics = ['A','B','C','D']
statements = [
    "A",
    "~B",
    "A->C",
    "B<->C",
]

def parse_statement(statement_str, atomic_lst):
    print("Atomics list: {}".format(atomic_lst))
    print(statement_str)
    character_set = set(filter(str.isalpha,statement_str))
    print("Statement character set: {}".format(sorted(list(character_set))))
    # check that the character_set is a subset of the atomic_lst as a set
    is_subset = character_set.issubset(set(atomic_lst))
    print("Check for valid subset: {}".format(is_subset))



    print()

for st in statements:
    parse_statement(st,atomics)



