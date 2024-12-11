#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 6


def encode(string, decoding=False):
    if decoding:
        return ''.join(chr(int(num) + 96) for num in string.split())
    else: 
        return ' '.join(str(ord(char) - 96) for char in string.lower() if char.isalpha())


# Test 1: Kodierung von "hello"
encoded = encode("hello")
print("Encoded:", encoded)  #"8 5 12 12 15"

# Test 2: Dekodierung von "8 5 12 12 15"
decoded = encode("8 5 12 12 15", decoding=True)
print("Decoded:", decoded)  #"hello"

decoded = encode("1 2 3", decoding=True)
print("Decoded:", decoded) 

encoded = encode("x y z")
print("Encoded:", encoded) 

decoded = encode("24 25 26" , decoding=True)
print("Decoded:", decoded)


