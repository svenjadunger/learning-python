#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 3

def create_dictionary(input_name1, input_name2, output_name):
    """
    Create a translation dictionary file from two input files.

    Args:
        input_name1 (str): File with words in the first language.
        input_name2 (str): File with words in the second language.
        output_name (str): File to write the translation pairs.

    Returns:
        str: Success or error message.
    """
    # öffnet beide eingabedateien und liest alle zeilen in listen, readlines() behält die zeilenumbrüche
    with open(input_name1, 'r') as file1, open(input_name2, 'r') as file2:
        lang1_words = file1.readlines()
        lang2_words = file2.readlines()

#prüft ob beide daten gleich viele zeilen haben, wenn nicht fehlermeldung zurückgeben
    if len(lang1_words) != len(lang2_words):
        return "The input files are not compatible."

#öffnet ausgabedatei und kombiniert mit zip beide wortlisten, strip entfernt leerzeichen und zeilenumbrüche und es werden
#wortpaare mit - dazwischen geschreben
    with open(output_name, 'w') as outfile:
        for word1, word2 in zip(lang1_words, lang2_words):
            outfile.write(f"{word1.strip()} - {word2.strip()}\n")

    return "Successfully created file."

# Testdateine erstellen
with open("lang1.txt", "w") as lang1:
    lang1.write("hello\nworld\n")

with open("lang2.txt", "w") as lang2:
    lang2.write("hola\nmundo\n")

#funktion testen
print(create_dictionary("lang1.txt", "lang2.txt", "dictionary.txt"))

#ergenis prüfen
with open("dictionary.txt", "r") as dictionary:
    print(dictionary.read())
