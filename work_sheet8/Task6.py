#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 8, Task 6

# N-Grams sind aufeinanderfolgende Sequenzen von n Elementen aus einem Text
# Bei n=2 (Bigrams) z.B. "I love" und "love coding" aus "I love coding"
# Sie werden häufig in der Textanalyse verwendet

def extract_contexts(text, stopwords):
    #teilt bei leerzeichen in liste v. wörtern
    words = text.split()
    result = {}
    
    #enumerate gibt uns paare v. indec u. wort: (0,"this")
    #i ist index(position)u. word aktuelles wort
    for i, word in enumerate(words):
        # prüft ob wort wichtig is(kein stopwort)
        #stopwörter wie this , is,.. werden übersprungen
        if word not in stopwords:
            # beim auftreten eines wichtigen worts: erstelle zwei leere sets i. einem tuple(linke_nachbarn, rechte_nachbarn)
            if word not in result:
                result[word] = (set(), set())  # Tuple mit zwei leeren Sets
            
            # Linken Nachbarn hinzufügen (wenn nicht am Anfang)
            #pruft ob es ein wort links gibt bedingung
            #words[i-1] greift auf li. nachbarwort zu, fügt es zu li. set(idx 0 hinzu)
            if i > 0:
                result[word][0].add(words[i-1])
                
            # Rechten Nachbarn hinzufügen (wenn nicht am Ende)
            #prüft ob es wort re. gibt bedingung
            # wwords [i+1] greift auf re, nachbarw. zu und fügt es zum re. set(idx1) hinzu
            if i < len(words)-1:
                result[word][1].add(words[i+1])
    
    return result #gibt dic zurück

# Test
text = "this is an example string and this example is very short"
stopwords = ['this', 'is', 'an', 'and', 'very']
print(extract_contexts(text, stopwords))
#{'example': ({'an', 'this'}, {'is', 'string'}), 'string': ({'example'}, {'and'}), 'short': ({'very'}, set())}