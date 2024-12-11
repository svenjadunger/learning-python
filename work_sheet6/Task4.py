#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 4

def is_anagram(string1, string2):
    list1 = list(string1.replace(" ", ""))  
    list2 = list(string2.replace(" ", ""))
    for i_elem in list1:
        if i_elem in list2:
            list2.remove(i_elem)
    if len(list2) == 0:
        return True
    else:
        return False


string1 = input('Enter the first string: ')
string2 = input('Enter the second string: ')
print(is_anagram(string1, string2))

# Test: Dormitory, Dirty room
