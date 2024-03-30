#!/usr/bin/env python3
# TODO: error check, i.e. if word doesn't exist, word isn't 5 letters, multiple letters etc. 

import random 
import sys as sus
from termcolor import colored 
# everytime i do import i need to do 'pip install <import_name>'
# import nltk
# nltk.download('words')
# import nltk 
# from nltk.corpus import words 

def print_menu():
    print("Let's play Linguistica: ")
    print("Type a 5 letter word and hit enter (or return if you are a mac user..)!")

def get_random_word():
    with open("potential_words.txt", "r") as file:
        words = file.read().splitlines()
        return random.choice(words)

# nltk.data.path.append('/work/words')
# word_list = words.words()
# words_five = [word for word in word_list if len(word) == 5]

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
            print(f"{guess} is not a 5 letter word, try again")
            while (guess := input().lower()):
                continue
        
        with open('valid_words.txt', 'r') as valid_words_file:
            contents = valid_words_file.read()
            if str(guess) not in contents:
                print(f"{guess} is not in the linguistica dictionary, try again")
                continue

        valid_words_file.close()

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
        elif attempt == 6:
            print(f"Sorry the linguistica was {final_word}")
    
    play_again = input("Play again? if not type q to quit: ")