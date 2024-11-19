#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 5, Task 2


string = input("Enter a string: ")
separator = input("Enter a separator: ")

result = [] #leere liste
current_part = "" #leerer string, hier buchstaben sammeln, bis trennzeichen kommt

for char in string: #geht durch jeden einzelnen buchstaben in 'Hallo,Welt', char ist 'H', dann 'a',...
    if char == separator: #wenn trennzeichen kommt, speicher alles bisherige in result
        result.append(current_part)  #wenn ja bei Komma, nimm alles was in currentpart ist und tue es in result
        current_part = ""    #mach current part wieder leer für nächsten teil
    else:
        current_part += char       #wenn nein füge buchstaben zu currentpart hinzu


result.append(current_part)


print(result)
