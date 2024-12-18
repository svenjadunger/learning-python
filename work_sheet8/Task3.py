#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 8, Task 3

def map_languages(dict1, dict2):
    """returns a dictonary mapping language1 to language3 and takes two dictonaries as arguments"""
    return {key: dict2[value] for key, value in dict1.items() if value in dict2}



#durchläuft alle schlüssel-wert-paare in dict1: dict1.items()
#prüft ob wert aus dict1 in dict2 vorkommt: if value in dict2
#dict2[value]: holt den wert aus dict2, falls der schlüssel vorh. ist
#erstellt das ergebnis-dict. mit urspr. schlüssel aus dict 1 und wert aus dic2: {key: dict2[value]}


#Test
dict1 = {'red': 'rot', 'green': 'grün'}
dict2 = {'rot': 'kırmızı', 'gelb': 'sarı', 'blau': 'mavi'}

result = map_languages(dict1, dict2)
print(result)  #{'red': 'kırmızı'}
