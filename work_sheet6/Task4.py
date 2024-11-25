#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 4

#Anagramm = wort oder zeichenkette, die durch Umstellen der Buchstaben eines anderen wortes entsteht
#listen und silent sind Anagramme

def is_anagram(string1, string2):
    # for char in string1 und string2: nimmt jedes zeichen der eingaben einzeln zb 'a gentleman' -> 'A', '', 'g'
    # if char.isalnum() filtert alle n.alphanum. Zeichen(leerzeichen,satzzeichen), entf. leerzeichen,!,.
    # char.lower() wandelt großbuchs. in klein um A -> a
    # ''.join() fügt verbleibende zeichen zu neuen bereinigten string zsm a gentleman -> agentleman
    cleaned1 = ''.join(char.lower() for char in string1 if char.isalnum())
    cleaned2 = ''.join(char.lower() for char in string2 if char.isalnum())
    # sorted(cleaned1) zerlegt bereinigten string in liste v. buchstab., sortiert alphabetisch : agentleman: a,a,e,e,g
    #wenn sortierte zeichenlisten identisch sind ['a', 'a', 'e', 'e', 'g', = ['a', 'a', 'e', 'e', 'g', -> True
    return sorted(cleaned1) == sorted(cleaned2)


string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
print(result)  # Erwartet: True
