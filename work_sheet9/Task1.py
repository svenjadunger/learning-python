#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 1
#wor4=none ist ein optionaler parameter, wenn er nicht angegeben wird, ist sein wert none
def mad_libs(word1: str, word2: str, word3: str, word4 : str =None):
    """
    Fills a Mad Libs style text with given words.
    Args:
        word1 (str): A noun
        word2 (str): A verb in past tense
        word3 (str): An adjective
        word4 (str): Another adjective
    Returns:
        str: The completed text
    """
    #prüft ob word4 einen wert hat, also nicht none ist
    if word4:
        text = f"I saw an {word1} that {word2} very {word3} and {word4}."
    else: #wenn word4=none
        text = f"I saw an {word1} that {word2} very {word3}."
    return text

# Test mit 3 Argumenten
print(mad_libs("bear", "smiled", "gracefully"))
# Test mit 4 Argumenten
print(mad_libs("bear", "smiled", "gracefully", "happily"))
