#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 3

def list_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + list_sum(lst[1:]) #1. wert der liste + funktion wird rekursiv m. restl. Liste aufgerufen
    #summe wird berechnet 1. wert zur summe der restl. liste addiert wird
    
    