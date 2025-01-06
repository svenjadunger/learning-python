#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 6

def musicians(inputfile_name):
    """
    Read musician data from file and print formatted output.
    Each three lines contain: first name, last name, band name.
    """
    with open(inputfile_name, 'r') as file:
        lines = file.readlines()
        
        for i in range(0, len(lines), 3):
            if i + 2 < len(lines):
                first_name = lines[i].strip()
                last_name = lines[i + 1].strip()
                band = lines[i + 2].strip()
                print(f"{first_name} {last_name} ({band})")
                
# test
with open('input_task6.txt', 'w') as f:
    f.write('Justin\nTimberlake\n*NSYNC\nFreddie\nMercury\nQueen')

musicians('input_task6.txt')