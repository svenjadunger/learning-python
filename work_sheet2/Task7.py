#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 2, Task 7


word = input("Enter a word ")

print(word.lower().count('a'))
reverse_word = ''.join(reversed(word))
print(reverse_word)

print(word[::2])
print(word[-3:])

replaced_word = word.replace(' ', '***')
print(replaced_word)