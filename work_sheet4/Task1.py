#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Group I
# Matriculation numbers: [827575, 826703, 828610]
# Sheet 4, Task 1


import random

# create needed variables
options = ["scissors", "paper", "rock"]

print("Let's play rock, paper, scissors!")

player_b = input(f"Please input one of the following: " + ", ".join(options) + "\n")

# an element from the list 'options' is selected randomly
player_a = random.choice(options)



# validate user input
if player_b not in options:
    print("Please choose one of the given options!")
else:
    print("vs.\n" + player_a)
    print("-"*25)
    if player_a == player_b:
        print("There is no winner!")
    elif player_b == "scissors" and player_a == "paper":
        print("You won!")
    elif player_b == "paper" and player_a == "rock":
        print("You won!")
    elif player_b == "rock" and player_a == "scissors":
        print("You won!")
    else:
        print("You lost!")
        
        #cattpucchin