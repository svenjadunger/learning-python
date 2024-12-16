#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 8, Task 2



def letter_frequency(text):
    # Entferne Leerzeichen und Satzzeichen aus d. Text
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())

    # create empty dictory for buchstabenhäufigkeit
    frequency = {}

    # Zähle die Buchstaben in cleaded text
    for char in cleaned_text:
        if char in frequency:
            frequency[char] += 1 #wenn buchst. bereits im dict. ist, wird zähler um 1 erhöht
        else:
            frequency[char] = 1 #andernfalls wird buchst. m. zähler v. 1 hinzugef.

    return frequency


text = "Hallo Welt!"
result = letter_frequency(text)
print(result)  #{'h': 1, 'a': 1, 'l': 3, 'o': 1, 'w': 1, 'e': 1, 't': 1}
