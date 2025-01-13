#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 10, Task 4

import re

def find_sorted_words(filename):
    """
    Finds words with letters in alphabetical order from a text file.
    Words must be longer than 2 letters.
    
    Args:
        filename (str): Path to text file
    Returns:
        list: Words with letters in alphabetical order
    """
    # datei einlesen, schaut dass sonderzeichen correct gelesen werden(utf-8), lower konvertiert alles zu kleinbuchstaben f. einheitl. verarbeitung
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    
    # findall() findet alle übereinstimmenden wörter
    # \b = wortgrenze (kein teil eines größeren wortes)
    # [a-z] = nur kleinbuchstaben
    # {3, } = mind. 3 zeichen
    # \b wieder wortgrenze
    words = re.findall(r'\b[a-z]{3,}\b', text)
    
    # list(word) = macht eine liste der buchstaben a, c , t
    # sorted(word) = sortiert die buchstaben alphabet.
    return [word for word in words if list(word) == sorted(word)]

# Test
def test_sorted_words():
    
    result = find_sorted_words('pride_and_prejudice.txt')
    
    # Test some known words that should be in the results
    assert 'act' in result
    assert len(result) > 0
    
    print("Found words:", result[:10])  # Print first 10 words
    print(f"Total words found: {len(result)}")

test_sorted_words()