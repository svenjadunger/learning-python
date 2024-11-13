# #! /usr/bin/python3
# # -*- coding: utf-8 -*-
# # Group I
# # Matriculation numbers: [827575, 826703, 828610]
# # Sheet 4, Task 2


# zuerst input enter von Benutzer
sentence = input("Enter a sentence: ")

# Liste für die gereinigten Tokens erstellen
cleaned_tokens = []

# Jedes Satzzeichen wird hier erstmal von einem Leerzeichen umgeben
# zb "Hello,world" wird zu "Hello , world"
# wieso?: damit wir Satzzeichen als eigene Tokens erkennen können, hilft später beim Aufteilen in Tokens, braucht man für split() später
for char in ",.!?":
    sentence = sentence.replace(char, f" {char} ")

# split teilt Satz bei Leerzeichen in einzelne Wörter
# die Wörter kommen dann in die Liste "words" z.B. Hello! wird zu ["Hello", "!"]
words = sentence.split()

# Schleife läuft, jedes Wort wird einzeln bearbeitet
for word in words:
    word = word.strip()
    
    # Wenn nichts übrig bleibt oder nur Satzzeichen -> No token found
    if not word or word in ",.!?":
        cleaned_tokens.append("No token found.")
    
    # Prüft ob ein Apostroph ' in der Mitte ist (nicht am Ende oder Anfang) zb let's, can't
    elif "'" in word and not (word.startswith("'") or word.endswith("'")):
        cleaned_tokens.append(word)
    
    # Für alle anderen Fälle: Anführungszeichen entfernen
    else:
        word = word.strip('"').strip("'")
        if word:
            cleaned_tokens.append(word)
        else:
            cleaned_tokens.append("No token found.")

# Am Ende alle gereinigten Tokens ausgeben
for token in cleaned_tokens:
    print(token)
    