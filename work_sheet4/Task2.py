# #! /usr/bin/python3
# # -*- coding: utf-8 -*-
# # Group I
# # Matriculation numbers: [827575, 826703, 828610]
# # Sheet 4, Task 2


# zuerst input enter von Benutzer
sentence = input("Enter a sentence: ")

# Jedes Satzzeichen wird hier erstmal von einem Leerzeichen umgeben
# zb "Hello,world" wird zu "Hello , world"
# wieso?: damit wir Satzzeichen als eigene Tokens erkennen können, hilft später beim Aufteilen in Tokens, braucht man für split() später


sentence = sentence.replace(",", " , ")
sentence = sentence.replace(".", " . ")
sentence = sentence.replace("!", " ! ")
sentence = sentence.replace("?", " ? ")

# split teilt Satz bei Leerzeichen in einzelne Wörter
# die Wörter kommen dann in die Liste "words" z.B. Hello! wird zu ["Hello", "!""]
words = sentence.split()

# Schleife läuft, jedes Wort wird einzeln bearbeitet, strip() entfernt Leerzeichen am Anfang u. Ende
for contaminated_token in words:
    
    contaminated_token = contaminated_token.strip()
    
    # Wenn nichts übrig bleibt -> No token found
    if contaminated_token == "":
        print("No token found.")
        
    # Wenn Token nur Satzzeichen ist -> No token found
    elif contaminated_token in [".", ",", "!", "?"]:
        print("No token found.")
        
    # Prüft ob ein Apostroph ' in der Mitte ist (nicht am Ende oder Anfang) zb let's , can't
    elif "'" in contaminated_token and not (contaminated_token.startswith("'") or contaminated_token.endswith("'")):
        print(contaminated_token)
        
    # prüft ob wort von Anführungszeichen umgeben ist, wenn ja löscht es erstes u. letztes Zeichen, "word" -> word
    elif (contaminated_token.startswith('"') and contaminated_token.endswith('"')) or \
         (contaminated_token.startswith("'") and contaminated_token.endswith("'")):
        cleaned = contaminated_token[1:-1]
        print(cleaned)
        
    # für alle anderen fälle (normale fälle): Satzzeichen und Anführungszeichen entfernen
    else:
        cleaned_token = contaminated_token
        # Anführungszeichen entfernen
        cleaned_token = cleaned_token.replace('"', '')
        # Satzzeichen entfernen
        cleaned_token = cleaned_token.replace(",", "")
        cleaned_token = cleaned_token.replace(".", "")
        cleaned_token = cleaned_token.replace("!", "")
        cleaned_token = cleaned_token.replace("?", "")
        
        
        # wenn leer -> no token found printen oder das gereinigte word printen
        if cleaned_token == "":
            print("No token found.")
        else:
            print(cleaned_token)