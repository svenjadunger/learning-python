# #! /usr/bin/python3
# # -*- coding: utf-8 -*-
# # Group I
# # Matriculation numbers: [827575, 826703, 828610]
# # Sheet 4, Task 2


sentence = input('Enter text: ')

for char in ".,!?":
    sentence = sentence.replace(char, " ")

words = sentence.split()
cleaned_sentence = ""

for word in words:
    word = word.strip("'\"")
    
    if "'" in word[1:-1]:
        cleaned_word = word
    else:
        cleaned_word = word.strip("'\"")
        
    if cleaned_word:
        cleaned_sentence += cleaned_word + " "

if cleaned_sentence:
    print(cleaned_sentence)
else:
    print('Token not found')