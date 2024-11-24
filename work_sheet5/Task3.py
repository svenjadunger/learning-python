#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 5, Task 3

def cleaning(sentence):
    for char in ".,:;!?":
        sentence = sentence.replace(char, " ")

    words = sentence.split()
    cleaned_sentence = ''

    for word in words:
        cleaned_word = word.strip("'\"")
        if cleaned_word:
            cleaned_sentence += cleaned_word + " "
    if cleaned_sentence:
        print(cleaned_sentence)
        return cleaned_sentence
    else:
        print('Token not found')


sentence = input('Enter a string: ')
cleaned_sentence = cleaning(sentence)
words_count = len(cleaned_sentence.split())
letters_count = 0

for i_elem in cleaned_sentence:
    if i_elem.isalpha():
        letters_count += len(i_elem)

average_word_len = round(letters_count / words_count, 2)
result = (words_count, average_word_len)
print(result)
