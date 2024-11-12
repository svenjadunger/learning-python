#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 4, Task 2

contaminated_token = input("Enter a token: ")
contaminated_token = contaminated_token.strip()

if contaminated_token == "":
    print("No token found.")
elif (contaminated_token.startswith('"') and contaminated_token.endswith('"')) or \
     (contaminated_token.startswith("'") and contaminated_token.endswith("'") and not "'s" in contaminated_token):
    cleaned_token = contaminated_token[1:-1] #removes last and first Zeichen
    print(cleaned_token)
elif "'s" in contaminated_token:
    print(contaminated_token)
elif contaminated_token in [".", ",", "!", "?"]:
    print("No token found.")
else:
    cleaned_token = contaminated_token.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    print(cleaned_token)
