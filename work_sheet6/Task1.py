#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 1

def flatten(user_list):
    result = []
    for i_elem in user_list:
        if isinstance(i_elem, list):  
            nested_result = flatten(i_elem) 
            for nested_elem in nested_result:
                result.append(nested_elem)
        else:
            result.append(i_elem)  
    return result


my_list = [['ich', 'lege', 'tief'], ['ich', [['lege', 'tiefer']]], 'ich', 'lege', 'oben']
result = flatten(my_list)
print(f"Flattened list: {' '.join(result)}")




