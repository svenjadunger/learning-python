#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 1


def flatten(my_list):
    result = []
    for item in my_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

test = [1, [2, 3], [4, [5, 6]]]
print(flatten(test))







# flatte2 = lambda l: [item for i in l for item in (flatten(i) if isinstance(i, list) else [i])]

# print(flatte2(test))  