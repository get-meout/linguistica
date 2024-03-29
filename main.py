#!/usr/bin/env python3

import random 
import sys as sus
from termcolor import colored 

def print_menu():
    print("Let's play Linguistica: ")
    print("Type a 5 letter word and hit enter (or return if you are a mac user..)!")

def get_random_word():
    with open("potential_words.txt", "r") as file:
        words = file.read().splitlines()
        return random.choice(words)

print_menu()
final_word = get_random_word()

# print(final_word) # debugging REMOVE LATER

for attempt in range(0, 6):
    guess = input().lower()

    if len(guess) != 5:
        while (guess := input().lower()):
            continue

    for i in range( min(len(guess), 5) ):
        if guess[i] == final_word[i]: 
            print(colored(guess[i], 'green'), end = "") 
        elif guess[i] in final_word:
            print(colored(guess[i], 'yellow'), end = "") 
        else:
            print(colored(guess[i], 'grey'), end = "") 

        if i == 4:
            print()

    if guess == final_word:
        print(colored(f"Congrats! You got solved today's linguistica in {attempt+1}", 'red'))
        break