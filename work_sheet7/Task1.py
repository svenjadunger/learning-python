#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 1

#macht linkslastige Struktur


def to_left_recursive(lst):
    if len(lst) <= 1: 
        return lst #dann stoppe Rekursion
    return [to_left_recursive(lst[:-1]), lst[-1]] 


print(to_left_recursive([]))          # []
print(to_left_recursive([1, 2, 3, 4]))  # [[[1], 2], 3], 4]
print(to_left_recursive([1])) 



