#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 5, Task 5


num = input("Enter a number: ") #13 wird als string '13'



if num.isdigit(): #prüft ob nur nr  (12a=false, 13 =true)
    n = int(num) # aus string zahl machen
    binary = '' #leerer string f. binärzahlen 0en und 1en
    while n: #solange n nicht 0 ist.. 
        binary = str(n % 2) + binary #n%2 rest bei division durch 2 , rest vorne anfügen
        n //= 2
    print(binary if binary else '0') #if binary nicht leer print binary, else wenns leer ist print 0
else:
    print("Invalid Input!")