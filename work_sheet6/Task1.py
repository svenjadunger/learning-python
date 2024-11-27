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

test = [1, [2, 3], [4, [5, 6]]] #[1, 2, 3, 4, 5, 6]
print(flatten(test))

test2 = [1, [2, [3, [4, [5, [6]]]]]]
print(flatten(test2)) #[1, 2, 3, 4, 5, 6]




# def flatten(my_list):
#     result = []
#     stack = list(my_list)  
    
#     while stack:
#         item = stack.pop()  
#         if isinstance(item, list):
#             stack.extend(item[::-1]) 
#         else:
#             result.append(item)
    
#     return result[::-1]  





