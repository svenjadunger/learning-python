#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 7, Task 2

tree = ("S",[("NP", [("DET", "the"), ("N", "cat")]),("VP", [("V", "chases"),("NP", [("DET", "the"), ("N", "birds")])])])

def node_count(tree_tuple):
    counter = 0

    # Base case: check if the element is a string (terminal)
    if isinstance(tree_tuple, str):
        return 0

    parent_node, child = tree_tuple
    counter += 1
    for child_tree in child:
        counter += node_count(child_tree)
#return counter besser
    return counter


print(f"Non-terminal nodes in the tree: {node_count(tree)}")
