
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
    with open(inputfile_name, 'r') as file:
        while True:
            # Read the next three lines
            first_name = file.readline().strip()
            surname = file.readline().strip()
            band = file.readline().strip()

            # Check if we reached the end of the file
            if not first_name or not surname or not band:
                break

            print(f"{first_name} {surname} ({band})")


musicians('input_task6.txt')

# Alternative with for:
# for i in range(0, len(lines), 3):
#     first_name = lines[i].strip()
#     last_name = lines[i + 1].strip()
#     band = lines[i + 2].strip()
#     print(f"{first_name} {last_name} ({band})")