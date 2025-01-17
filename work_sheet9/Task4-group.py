from pathlib import Path

def join_names(inputfile_name: str | Path , outputfile_name: str):
    """
    Combines first and last names from an input file and writes them to an output file.

    Args:
        inputfile_name (str): The name of the input file containing alternating first and last names.
        outputfile_name (str): The name of the output file where combined names will be written.

    Returns:
        None
    """
    if isinstance(inputfile_name, str): inputfile_name = Path(inputfile_name)
    assert isinstance(inputfile_name, Path) and inputfile_name.is_file()
    with open(inputfile_name, 'r') as inputfile, open(outputfile_name, 'w') as outfile:
        while True:
            first_name = inputfile.readline().strip()
            last_name = inputfile.readline().strip()

            if not first_name or not last_name:  # If the end of the file is reached, exit the loop.
                break

            outfile.write(f"{first_name} {last_name}\n")


join_names('names.txt', 'names_and_surnames.txt')

# Alternative with for:
# for i in range(0, len(lines), 2):
#     first_name = lines[i].strip()
#     last_name = lines[i + 1].strip()
#     outputfile.write(f"{first_name} {last_name}\n")