#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 5, Task 3

text = input("Enter a sentence ")
words = text.split()  # teilt text bei leerzeichen
print(words)
word_count = 0
total_length = 0
for word in words:
    # Entferne alle Satzzeichen am Anfang und Ende des Wortes
    cleaned_word = word.strip('\',.!?:"-')
    if cleaned_word:  # Prüft ob das Wort nach Entfernung der Satzzeichen nicht leer ist
        word_count += 1
        # Zählt nur alphabetische Zeichen für die Länge
        total_length += sum(1 for c in cleaned_word if c.isalpha())
result = (word_count, round(total_length/word_count, 2) if word_count else 0)
print(total_length)
print(result)