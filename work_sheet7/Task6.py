#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 6


def list_depth(lst):
    depth = 1
    if not lst:
        return 1 #return tiefe, so ist hardgecoded
    for i_elem in lst:
        if isinstance(i_elem, list):
            depth = max(depth, list_depth(i_elem) + 1)
    return depth


my_list = [['ich', 'lege', 'tief'], ['ich', [['lege', 'tiefer']]], 'ich', 'lege', 'oben']
print(list_depth(my_list))