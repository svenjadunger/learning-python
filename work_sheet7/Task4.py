#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 4

def flatten(my_list):
    result = []  
    for item in my_list:
        if isinstance(item, list):  
            result.extend(flatten(item))  
        else:
            result.append(item)  
    return result

print(flatten([1, [2, [3, 4], 5], 6]))  #[1, 2, 3, 4, 5, 6]