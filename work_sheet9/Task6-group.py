
def musicians(inputfile_name: str) -> None:
    """
    Reads a file containing information about musicians (first name, surname, band)
    and prints each musician's information in the format:
    FirstName Surname (Band)

    Parameters:
    inputfile_name (str): The name of the file to read.

    Returns:
    None: The function prints the result instead of returning it.
    """
    #datei wird geöffnet zum lesen
    with open(inputfile_name, 'r') as file:
        while True:
            # Read the next three lines
            #readline liest zeile, strip entfernt leerzeichen, zeilenumbrüche
            first_name = file.readline().strip()
            surname = file.readline().strip()
            band = file.readline().strip()

#prüfen ob datie zu ende ist
            if not first_name or not surname or not band:
                break
#infos ausgeben
            print(f"{first_name} {surname} ({band})")


musicians('input_task6.txt')

#forschleife startet bei 0 geht zum ende der liste, in 3er sprüngne
#weil für jeden musiker 3 informationen
# Alternative with for:
# for i in range(0, len(lines), 3):
#     first_name = lines[i].strip() #erste zeile
#     last_name = lines[i + 1].strip() #zeite zeile
#     band = lines[i + 2].strip() #3. zeile
#     print(f"{first_name} {last_name} ({band})")