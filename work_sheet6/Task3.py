#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 6, Task 3
#palindrom = text, der vorwärts und rückwarts gleich gelesen wird, zb "anna", "A man, a plan, a canal: Panama"
#char.isalnum(): prüft ob zeichen alphnum. ist(buchst. od. ziffern) A -> true, ' ' -> false, ',' -> false
#char.lower -> wandelt groß in kleinbuchst. um, damit groß/kleinschr. ignor. wird 'A' -> 'a'
#''.join(..) -> fügt bereinigte zeichen zu neuen string zsm : amanaplanacanalpanama
def is_palindrome(string):
    #groß,kleinschreibung wird ignoriert(lower())
    #sonderzeichen, leerzeichen,satzzeichen entfernt, isalnum()prüft nur buchstaben und zahlen
    #for char in string: itertiert d. jeden buchst. eingabe durchgänge: A, '', 'm',...
    cleaned = ''.join(char.lower() for char in string if char.isalnum())
    #cleaned[::-1] erstellt rückwärtsversion durch slicing: nimm ganzen string cleaned und lies ihn von hint. na. vorne
    #amanaplanacanalpanama wird zu amanaplanacanalpanama
    return cleaned == cleaned[::-1]
#prüft ob bereinigter string cleaned gleich mit rückwärsversion cleaned[::-1] ist, wenn ja palindrom


test_string_1 = "A man, a plan, a canal: Panama"
result_1 = is_palindrome(test_string_1)
print(result_1)  # Erwartet: True
