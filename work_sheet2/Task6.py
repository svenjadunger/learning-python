#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 2, Task 6



user_input = input().split()

length = len(user_input)

input_as_tuple = tuple(user_input)

contains_python = ('Python' in user_input or 'python' in user_input)

copy_input = user_input
copy_input.reverse()

same_element = (user_input[0] == input_as_tuple[0])