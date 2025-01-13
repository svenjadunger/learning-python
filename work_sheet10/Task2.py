#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 10, Task 2
import re

def to_pig_latin(word):
    """
    Converts word to Pig Latin:
    - Words starting with vowels (a,e,i,o,u): add 'way'
    - Words starting with consonants: move consonants until first vowel to end, add 'ay'
    
    Args:
        word (str): Word to convert (e.g., 'start', 'eat')
    Returns:
        str: Word in Pig Latin (e.g., 'artstay', 'eatway')
    """
    
    # ^ bedeutet am anfang des wortes
    # aeiou sind die vokabelliste
    # wort + way -> eat + way = eatway
    if re.match(r'^[aeiou]', word):
        return word + 'way'
    
    # re.search() findet ersten vokal 'a'
    # start() gibt die position 2 zurück, weil in start vokal a an postiion 2 ist
    vowel_pos = re.search(r'[aeiou]', word).start()
    #  word[vowel_pos:] = art, von posiion 2 bis ende
    # word[:vowel_pos] : st von anfang bis position 2
    # ay am ende
    #also: art + st + ay = artstay
    return word[vowel_pos:] + word[:vowel_pos] + 'ay'

# Tests
def test_pig_latin():
    # Words starting with vowels
    assert to_pig_latin("eat") == "eatway"     # e is a vowel

    assert to_pig_latin("ice") == "iceway"     # i is a vowel 
    
    # Words starting with consonants
    assert to_pig_latin("start") == "artstay"  # 'st' to end, add ay
    assert to_pig_latin("cat") == "atcay"      # move c to end add ay
    
    print("All tests passed!")

test_pig_latin()