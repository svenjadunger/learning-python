#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 1

def to_left_recursive(lst):
    if len(lst) <= 1:
        return lst
    return [to_left_recursive(lst[:-1]), lst[-1]]


print(to_left_recursive([]))          # []
print(to_left_recursive([1, 2, 3, 4]))  # [[[1], 2], 3], 4]

# lst[:-1]: Dies nimmt alle Elemente außer dem letzten (eine Teil-Liste).
# lst[-1]: Dies holt das letzte Element der Liste.
# Die Funktion wird dann rekursiv mit der Teil-Liste lst[:-1] aufgerufen. Das Ergebnis dieses Aufrufs wird zusammen mit lst[-1] in eine neue Liste gepackt.


# 1, 2, 3, 4]

#     Rekursion 1:
#     lst = [1, 2, 3, 4]
#     -> [to_left_recursive([1, 2, 3]), 4]

#     Rekursion 2:
#     lst = [1, 2, 3]
#     -> [to_left_recursive([1, 2]), 3]