#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 6

#zwei eingabewerte: string, der text, den wir kodieren od. dekodieren wollen
#decoding: ein optionaler wert, wenn er true ist, wird text dekodiert, ansonsten kodiert
def encode(string, decoding=False):
    #wenn decoding wahr ist:
    if decoding:
        # addieren 96, um den entsprechenden ASCII-Wert des Buchstabens zu haben
        # wenn Zahl 8 ist, berechnen wir 8 + 96 = 104, asciiwert von 104 ist h, durch chr() Ascii-Zeichen 'h'
        return ''.join(chr(int(num) + 96) for num in string.split())
    else: # wenn decoding falsch:
        # für jeden buchst. ascii wert berechnet mit ord(char), ord('a')-96 = 97-96 = 1, gibt numerische Darstellung an
        return ' '.join(str(ord(char) - 96) for char in string.lower() if char.isalpha())


# Test 1: Kodierung von "hello"
encoded = encode("hello")
print("Encoded:", encoded)  #"8 5 12 12 15"

# Test 2: Dekodierung von "8 5 12 12 15"
decoded = encode("8 5 12 12 15", decoding=True)
print("Decoded:", decoded)  #"hello"

decoded = encode("1 2 3", decoding=True)
print("Decoded:", decoded) 