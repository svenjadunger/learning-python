#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 7
#funktion nimmt dateinamen als parameter
def random_line(inputfile_name):
    """
    Return a random line from the given file.
    """
    import random
    #öffnet datei, liest alle zeilen in eine liste
    with open(inputfile_name, 'r') as file:
        lines = file.readlines()
        #zufällige auswähl: wählt zufallig eine zeile aus
        #strip entfernt leerzeichen
        #gibt zeile zurück
        return random.choice(lines).strip()


# test
print(random_line('input_task6.txt'))  # zb justin