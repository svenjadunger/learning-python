#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 2

def node_count(tree):
    if isinstance(tree[1], str):  # ist zweites element tree[1] ein string? wenn ja: Blattknoten, zb the oder cat
        return 0 # ...wenn ja dann 0 zurückgeb, da blattknoten keine nicht-blattknoten sind
    return 1 + sum(node_count(child) for child in tree[1])  #falls 2. element eine liste,
#ist es ein Nicht-blattknoten (zb S oder NP), +1 um aktuellen knoten zu zählen
#f. jeden teilbaum(child) i.d. liste tree[1] wird funkt. node.c. rekurisv aufgerufen, ergebnisse summiert

# tree ergänzen

