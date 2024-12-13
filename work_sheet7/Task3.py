#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 3


def list_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + list_sum(lst[1:])


numbers = [1, 2, 3, 4]
print(list_sum(numbers))