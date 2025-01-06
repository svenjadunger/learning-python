#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 9, Task 2


def find_token_frequency(inputfile_name, outputfile_name):
    """
    Count token frequencies in input file and write results to output file.
    
    Args:
        inputfile_name (str): Name of input text file
        outputfile_name (str): Name of output file for frequencies
    """
    # Dictionary to store frequencies
    frequencies = {}
    
    # Read input file and count frequencies
    with open(inputfile_name, 'r') as infile:
        text = infile.read()
        tokens = text.split()
        
        for token in tokens:
            if token in frequencies:
                frequencies[token] += 1
            else:
                frequencies[token] = 1
    
    # Write results to output file
    with open(outputfile_name, 'w') as outfile:
        for token in tokens:
            if token in frequencies:
                outfile.write(f"{token} {frequencies[token]}\n")
                frequencies.pop(token)  # Avoid duplicates
    
    return "Successfully created file."

# Test
with open("input_task2.txt", "w") as test_input:
    test_input.write("Hello world! Hello Python. Hello world!")

print(find_token_frequency("input_task2.txt", "output_task2.txt"))

with open("output_task2.txt", "r") as test_output:
    print(test_output.read())
