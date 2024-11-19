#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 5, Task 3

text = input("Enter a sentence ") #Hallo, wie gehts
words = text.split() #teilt text bei leerzeichen -> ['Hallo',',','wie','gehts']

word_count = 0
total_length = 0

for word in words:
    if word[-1].isalpha() or word[-1] in ',.!?:"-': #ist letzter buchstabe ein buchstabe oder letzter buchstabe ein satzzeichen
        word_count += 1 #wenn ja gültiges wort
        total_length += sum(1 for c in word if c.isalpha()) #geht durch alle char in word, zählt 1 f. buchstabe, ignoriert zeichen

result = (word_count, round(total_length/word_count, 2) if word_count else 0) 
#erstellt tupel mit anzahl der wörter, durchschnittl. länge auf 2 gerundet, if .. else 0 wenn keine wörter, dann 0
#wenn word_count größer als 0 ist (gibt wörter) wird round(total_length/word_count,2) berechnet
#else 0: wenn word_count 0 ist (gibt keine wörter) wird der wert 0 zurückgegeben
print(result)