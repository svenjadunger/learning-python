#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 2

#erstellt funkt. mit zwei parametern: ein und ausgabedateinamen
def find_token_frequency(inputfile_name, outputfile_name):
    """
    Count token frequencies in input file and write results to output file.
    
    Args:
        inputfile_name (str): Name of input text file
        outputfile_name (str): Name of output file for frequencies
    """
    # leeres dict. f. speichern von worthäufigkeiten
    # jedes wort wird schlüssel, die häufigkeit sein wert
    frequencies = {}
    
    # öffnet eingabedatei zum lesen mit r
    # liest den gesamten text
    # teilt text in einzelne wörter (tokens)
    with open(inputfile_name, 'r') as infile:
        text = infile.read()
        tokens = text.split()
        
        # geht durch jedes wort, wenn wort schon im dic ist: erhöhe zähler um 1
        # wenn nicht: füge es neu mit zähler 1 hinzu
        for token in tokens:
            if token in frequencies:
                frequencies[token] += 1
            else:
                frequencies[token] = 1
    
    # ergebnsise schreiben
    # öffnet ausgabedatei zum schreiben mit w
    # geht durch die wörter in ursprüngl. reihenfolge
    # schreibt wort und häufigkeit in neue zeile
    # entfernt mit pop geschriebene wörter aus dict. (verhindert duplikate)
    with open(outputfile_name, 'w') as outfile:
        for token in tokens:
            if token in frequencies:
                outfile.write(f"{token} {frequencies[token]}\n")
                frequencies.pop(token)  # Avoid duplicates
    
    return "Successfully created file."

# Test
#with open öffnet eine neue datei namens inputtask2
# mit w schreibmodus, testinputwrite schreibt den testtext in die datei; nach dem with block wird datei automat. geschlossen
with open("input_task2.txt", "w") as test_input:
    test_input.write("Hello world! Hello Python. Hello world!")

#ruft funktion auf mit den zwei dateinamen
#wird ausgegeben succesffuly created file
print(find_token_frequency("input_task2.txt", "output_task2.txt"))

#öffnet die erstellte ausgabedaatei im lesemodus r
#testourput.read liest gesamten inhalt und printed aus
with open("output_task2.txt", "r") as test_output:
    print(test_output.read())
