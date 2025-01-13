#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 10, Task 6

import re

def extract_sentence(filename):
    """
    Extracts words from CoNLL format file and combines them into a sentence.
    Each line contains: index word annotations... (tab separated)
    """
    #öffnet file, richtiges encoding f. sonderzeichen(utf-8)
    #with stellt sicher dass datei wieder geschlossen wird
    # list alles in einen string
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        # \d+: Eine oder mehrere Ziffern (für die Zeilennummer)
        # (\S+): Die Klammern fangen das Wort ein: \S: Bedeutet "nicht-Whitespace", +: "Ein oder mehrere davon"
# \t: Noch ein Tab-Zeichen danach
# re.findall : sucht alle vorkommen des patterns im text, gibt nur den teil in klammern zurück(die wörter), ignoriert annotationen nach zweiten tab
        words = re.findall(r'\d+\t(\S+)\t', text)
        #fügt liste der wörter mit leerzeichen zusammen und erstellt string
        return ' '.join(words)

# Test
#ruft funktion auf und vergleicht mit erwartetem satz, wenns nicht funkt. fehlermeldung
def test_extract_sentence():
    result = extract_sentence('conll.conll')
    
    # Expected output from the assignment
    expected = "Japanese investors nearly single-handedly bought up two new mortgage securities-based mutual funds totaling $ 701 million , the U.S. Federal National Mortgage Association said ."
    
    # Test exact match
    assert result == expected, "Output doesn't match expected sentence"
    print("Test passed! Extracted sentence:")
    print(result)

test_extract_sentence()