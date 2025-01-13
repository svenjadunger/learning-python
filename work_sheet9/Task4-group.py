def join_names(inputfile_name: str, outputfile_name: str):
    """
    Combines first and last names from an input file and writes them to an output file.

    Args:
        inputfile_name (str): The name of the input file containing alternating first and last names.
        outputfile_name (str): The name of the output file where combined names will be written.

    Returns:
        None
    """
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