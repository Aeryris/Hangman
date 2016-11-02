#!/usr/bin/python

import random
import os


# Prints number of guessed and not guessed letters to the screen
# Not yet guessed letters are represented by an underscore _
def print_hangman_line(number, guessed=''):
    for i in range(0, number):
        print("_", end=" ")
    return


# Check if letter is in the selected word
def check_letter(letter, word):
    return


# Refresh the console window
def refresh_screen(number_of_characters):
    # Clear console window - http://stackoverflow.com/a/2084628
    os.system('cls' if os.name == 'nt' else 'clear')
    print("    Hangman!")
    print("Word has " + str(number_of_characters) + " letters")
    return


# Print congratulations message
def congratulations():
    return


# 1) List of predefined, hard-coded words
word_list = ["Haribo", "Cookies", "Nutella", "Dragon", "Wolf", "Me"]

# 1) Pick random word from the list
random_word = random.choice(word_list)

# 2) Computer tells the user the number of letters in the word
number_of_characters = len(random_word)

# This is a flag that will be marked
did_guess = False

# Loop, repeat code until user guessed the word
while (did_guess == False):

    # Clear screen window and print content again.
    refresh_screen(number_of_characters)

    print_hangman_line(number_of_characters)

    # Stop the loop, user guessed the word
    did_guess = True

    if did_guess == True:
        congratulations()
