#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 8, Task 1

def lists_to_dict(keys, values):
    """Converts two lists into a dictonary"""
    #prüfe ob länge der beiden listen gleich sind
    if len(keys) != len(values):
        raise ValueError("Lists must have the same length.") #fehler werfen, wenn nicht gleich lang
    #die funktion zip verbindet beide listen zu paaren(key, value)
    #zb ['a', 'b'] und [1, 2] ergeben ('a', 1) und ('b', 2)
    #dict erstellt daraus ein dictonary
    return dict(zip(keys, values))


keys = ["name", "age", "city"]
values = ["Alice", 30, "Berlin"]
result = lists_to_dict(keys, values)
print(result)  # {'name': 'Alice', 'age': 30, 'city': 'Berlin'}