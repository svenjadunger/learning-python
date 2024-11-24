#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 5, Task 2


user_string = input('Enter a text with separators: ')
separator = input('Enter separator: ')

current_part = ''
result = []

for i_elem in user_string:
    if i_elem == separator:
        result.append(current_part)
        current_part = ''
    else:
        current_part += i_elem
result.append(current_part)

print(f'The split result is: {result}')

