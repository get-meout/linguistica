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

# print_menu()
# final_word = get_random_word()
play_again = ""
while play_again != "q":

    print_menu()
    final_word = get_random_word()
    print(final_word) # debugging REMOVE LATER

    for attempt in range(0, 6):
        guess = input().lower()

        sus.stdout.write('\x1b[1A') # moves cursor up one line
        sus.stdout.write('\x1b[2K') # clears uncoloured user's guess

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

        print()

        if guess == final_word:
            print(colored(f"Congrats! You got solved today's linguistica in {attempt+1}", 'red'))
            break
        
    play_again = input("Play again? if not type q to quit: ")