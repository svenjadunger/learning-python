#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 4
#nimmt eingabe und ausgabedatei als parameter
def join_names(inputfile_name, outputfile_name):
    """
    Combine first and last names from input file into full names in output file.

    Args:
        inputfile_name (str): File with alternating first and last names.
        outputfile_name (str): File to write full names.

    Returns:
        str: Confirmation message after writing the file.
    """
    #öffnet eingabedatei zum lesen, liest alle zeilen in eine liste names
    with open(inputfile_name, 'r') as infile:
        names = infile.readlines()
#prüfe ob anzahl der zeilen gerade ist für vor und nachnamen
#wenn ungerade: fehlermeldung ausgeben
    if len(names) % 2 != 0:
        return "The input file has an uneven number of lines."
#öffnet ausgabedatei
#range(0, len(names), 2) springt in 2er schritten durch die liste
#schreibt vor und nachname mit leerzeichen dazwischen
    with open(outputfile_name, 'w') as outfile:
        for i in range(0, len(names), 2):
            outfile.write(f"{names[i].strip()} {names[i+1].strip()}\n")

    return "Successfully created file."

# Testdatei erstellen
with open("names.txt", "w") as names:
    names.write("Fred\nMiller\nEve\nTurner\nSteve\nBaker\n")
#funktion testesb
print(join_names("names.txt", "full_names.txt"))
#ergebnis prüfen
with open("full_names.txt", "r") as full_names:
    print(full_names.read())
