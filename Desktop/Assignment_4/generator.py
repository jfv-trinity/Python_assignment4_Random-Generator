#!/usr/bin/env python3
"""
Program: generator.py
Author: Joseph Volpe
SN: 301118010
File generates and displays sentences using simple grammar
and vocabulary. Words are chosen at random from stored variables and imported datafiles that are converted to tuples.
"""

import random
"""Adjective and conjunctions used"""
adjective = ("TIRED", "ANGRY")
conjunction = ("AND", "FOR", "BUT")

def convert(list): 
    """Takes a list and converts it to a tuple"""
    return tuple(list) 

def sentence():
    """Builds and returns a sentence depending on value."""
    x = random.randint(1,100)
    if(x%2 < 1):
        return nounPhrase() + " " + verbPhrase()
    else:
        return nounPhrase() + " " + verbPhrase() + " "  + random.choice(conjunction) + " " +nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase depending on value."""
    x = random.randint(1,100)
    if(x%2 < 1):
        return random.choice(articles) + " " + random.choice(adjective) + " " + random.choice(nouns)
    else:
        return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase depending on value."""
    x = random.randint(1,100)
    if(x%2 < 1):
        return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()
    else:
        return random.choice(verbs) + " " + nounPhrase()
    
def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def getWords(filename):
    """Takes a argument and opens the argument and reads line by line. Each line is put into a list then converted to a tuple"""
    with open(filename) as f:
        tempList = list()
        for line in f:
            line = line.strip()
            tempList.append(line)   
    words = tuple(tempList)
    f.close()
    return(words)


def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
        
        
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")
main()

