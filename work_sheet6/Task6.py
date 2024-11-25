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
        # string.split: der text (der reihe von zahlen enthält, die durch leerzeichen getrennt) wird in liste v. einzelnen zahlen geteilt
        #int(num)+96: jede wird wird in ganzzahl gewandelt, u. wir addieren 96, um richtigen asci wert des buchst. zu haben
        #zb int("8") #96 = 104, asci wert für h
        #chr() wandelt asci wert zurückk in buchstaben um, zb chr(104) ergibt 'h'
        #join: alle buchstaben werden zu einzigen string zusammengef. ohne leerzeichen
        #zb: 'h','e',.. wird zu 'hello'
        return ''.join(chr(int(num) + 96) for num in string.split())
    else: # wenn decoding falsch:
        # string.lower: text in kleinbuchst. gewandelt, damit großbuch auch kodiert werden, HeLLo -> hello
        #if char.isalpha() schauen dass nur buchstab(keine zahlen oder zeichen kodiert werden)
        #ord(char) -96: für jeden buchstaben wird asci wert berechnet, und wir subtrah 96, um zahl zu erhalten
        #zb ord('h') = 104, also 104-96 = 8
        #str: zahl wird in str verwandelt
        #join: alle zahlen werden durch leerzeichen getrennt u zu einem einzigen string zusammengef.
        #zb '8', '5','12',.. wird zu '8 5 12,..'
        return ' '.join(str(ord(char) - 96) for char in string.lower() if char.isalpha())


# Test 1: Kodierung von "hello"
encoded = encode("hello")
print("Encoded:", encoded)  # Erwartet: "8 5 12 12 15"

# Test 2: Dekodierung von "8 5 12 12 15"
decoded = encode("8 5 12 12 15", decoding=True)
print("Decoded:", decoded)  # Erwartet: "hello"
