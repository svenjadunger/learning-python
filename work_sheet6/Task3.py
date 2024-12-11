#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 3

#palindrom = text, der vorwärts und rückwarts gleich gelesen wird, zb "anna", "A man, a plan, a canal: Panama"

def is_palindrome(string):
    cleaned = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned == cleaned[::-1]



test_string_1 = "A man, a plan, a canal: Panama"
result_1 = is_palindrome(test_string_1)
print(result_1)  # True
