#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 2


#nicht nur wörter sondern auch alle zeichen

#erstellt funkt. mit zwei parametern: ein und ausgabedateinamen
def find_token_frequency(inputfile_name, outputfile_name):
    """
    Count token frequencies in input file and write results to output file.
    Args:
    inputfile_name (str): Name of input text file
    outputfile_name (str): Name of output file for frequencies
    """
    # leeres dict. f. speichern von worthäufigkeiten
    # schlüssel: das token(wort oder satzzeichen), wert: wie oft es vorkommt
    frequencies = {}
    
    # Satzzeichen die als eigene Tokens zählen sollen
    satzzeichen = ".,!?;:-~@#$%^&*()"

    # öffnet eingabedatei zum lesen mit r
    # liest den gesamten text
    # teilt text in einzelne wörter (tokens)
    with open(inputfile_name, 'r') as infile:
        text = infile.read()
        words = text.split()
        
#geht durch jedes wort, current_token ist temporärer string zum aufbauen des aktuellen tokens
        for word in words:
            current_token = ""
            
            #geht durch jeden buchstaben im wort, prüft ob es satzzeichen ist
            for char in word:
                if char in satzzeichen:
                    # wenn vor satzzeichen ein token gebaut wurde: prüft ob es schon im dic. ist, wenn ja: erhöhe zähler um 1, 
                    #wenn nein: fügt es neu mit zähler 1 hinzu
                    #leert den temporären token
                    if current_token:
                        if current_token in frequencies:
                            frequencies[current_token] += 1
                        else:
                            frequencies[current_token] = 1
                        current_token = ""
                    
                    # Speichert das satzzeuchen selbst als token: wenn schon vorh: erhöht zähler, wenn neu: fügt es m. zähler 1 hinzu
                    if char in frequencies:
                        frequencies[char] += 1
                    else:
                        frequencies[char] = 1
                        #wenn kein satzzeichen: fügt buchstaben zum aktuellen token hinzu
                else:
                    current_token += char
            
            # am ende des wortes: speichert den letzten token falls vorhanden
            if current_token:
                if current_token in frequencies:
                    frequencies[current_token] += 1
                else:
                    frequencies[current_token] = 1

    # ergebnsise schreiben
    # öffnet ausgabedatei zum schreiben mit w
    # geht durch die wörter zum schreiben der ergebnisse
    
    # entfernt mit pop geschriebene wörter aus dict. (verhindert duplikate)
    with open(outputfile_name, 'w') as outfile:
        for token in words:
            current = ""
            #teilt wieder in tokens und satzzeichenm schreibt token und häufigkeit in datei
            # entfernt mit pop geschriebene wörter aus dict. (verhindert duplikate)
            for char in token:
                if char in satzzeichen:
                    if current in frequencies:
                        outfile.write(f"{current} {frequencies.pop(current)}\n")
                    if char in frequencies:
                        outfile.write(f"{char} {frequencies.pop(char)}\n")
                    current = ""
                else:
                    current += char
                    #schreibt letzten token des wortes falls vorhanden
            if current in frequencies:
                outfile.write(f"{current} {frequencies.pop(current)}\n")

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