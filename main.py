"""
File: main.py
Author: Jackson Bates
Created: 8/28/2019 2:11 PM 
"""

import nltk

phrase = "Paris is in France. France is in Europe. Therefore Paris is in Europe."

sentances = nltk.sent_tokenize(phrase)

for s in sentances:
    tokens = nltk.word_tokenize(s)
    tags = nltk.pos_tag(tokens)
    print(tags)

