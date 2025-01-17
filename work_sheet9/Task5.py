#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 5
#nimmt dateinamen als parameter
def parse_file(inputfile_name):
    """
    Parse a CSV file to create a dictionary with country data.

    Args:
        inputfile_name (str): Name of the input CSV file.

    Returns:
        dict: Dictionary with country as key and a tuple of (Population, Area, MGS, Langs) as value.
    """
    #erstellt leered dict. f. länderdaten
    country_dict = {}
#öffnet und liest csv datei
    with open(inputfile_name, 'r') as infile:
        lines = infile.readlines()
#verarbeitung jeder zeile
#enumerate gilt zeilennr (idx )und inhalt
#strip entfernet whitespace, split teilt an kommas
    for idx, line in enumerate(lines, start=1):
        parts = line.strip().split(',')
        #prüfe ob alle 5 felder vorh. sind, bei fehlen: warnung ausgeben und zeile überspringen
        if len(parts) != 5:
            print(f"Line {idx} was ignored due to missing information.")
            continue
#konvertiert die werte in richtige datentypen
        # fängt fehler bei ungültigen zahlen ab
        try:
            country = parts[0]
            population = float(parts[1])
            area = float(parts[2])
            mgs = float(parts[3])
            langs = int(parts[4])
            country_dict[country] = (population, area, mgs, langs)
        except ValueError:
            print(f"Line {idx} was ignored due to invalid data.")

    return country_dict

# TestdATEI ertellen
with open("country_info.csv", "w") as csv_file:
    csv_file.write(
        "USA,331002.0,9833520.0,78.9,1\nCanada,37742.0,9984670.0,82.3,2\nMexico,128932.0,1964375.0,75.1,1\nInvalidLine,1000,,70.0,1\n"
    )
#funktion testen
result = parse_file("country_info.csv")
print(result)
