#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 6
#nimmt dateinamen als parameter
def musicians(inputfile_name):
    """
    Read musician data from file and print formatted output.
    Each three lines contain: first name, last name, band name.
    """
    #datei öffnen zum lesen, speichert alle zeilen in der liste lines
    with open(inputfile_name, 'r') as file:
        lines = file.readlines()
        #geht in 3er schritten durch die liste
        for i in range(0, len(lines), 3):
            #prüft ob noch 3 zeilen verfügbar sind
            if i + 2 < len(lines):
                #daten extrahieren: (strip entfernt leerzeichen)
                first_name = lines[i].strip()#erste zeile (vorname)
                last_name = lines[i + 1].strip()#zweite zeile(nachname)
                band = lines[i + 2].strip()#dritte zweile (band)
                print(f"{first_name} {last_name} ({band})")
                
# test
with open('input_task6.txt', 'w') as f:
    f.write('Justin\nTimberlake\n*NSYNC\nFreddie\nMercury\nQueen')

musicians('input_task6.txt')