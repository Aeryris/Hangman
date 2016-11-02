#!/usr/bin/python

# Import additional library called random
# This library contains functions like "choice".
# Choice function is used to randomly pick the word from the list which we define later in the code.
# 'import' below means that You are informing Your script about new things that it can do
# However You are not yet using it's functionality, You are just telling the program that You will
# It's like studying, You have read the book, got some new knowledge but you didn't have a chance to use it yet.
import random

import sys

# Prints number of guessed and not guessed letters to the screen
# Not yet guessed letters are represented by an underscore _
#
# This function will loop (go through) guessed characters list and print them.
def print_hangman_line(guessed):
    # Print clear line
    print("\r\n")

    # This is foreach loop
    # Basically assume 'guessed' is a list (array) and it looks like guessed=[a, b, c]
    # Foreach will go through each value and assign it to 'character'
    # So when the code below runs its something like that:
    # take first value from guessed list
    # assign that value to character variable and print it

    for character in guessed:
        print(character, end=' ')

    #Print clear line
    print("\r\n")
    return


# Check if letter is in the selected word
def check_letter(letter, word):
    # There is built in function called find
    # Word variable is any word we specify "teddy", "smerf", python automatically recogizes it and
    # knows that you can call find function on it
    return word.find(letter)

# Checks whether a letter was already guessed
def already_guessed(letter, guessed):
    # This checks if letter is already in guessed list
    if letter in guessed:
        return True
    else:
        return False

# Refresh the console window
def intro_screen(number_of_characters):
    print("    Hangman!")
    print("Word has " + str(number_of_characters) + " letters")
    return

# This opens a file with mode a (append) and writes text to it
def log_guess(file, text):
    with open(file, "a") as log:
        log.write(text + ", ")

# Read users letters
def read_character():
    return input("Please enter character: ")


# Print congratulations message
def congratulations():
    print()
    print("Congratulations!!!")
    return


# 1) List of predefined, hard-coded words
word_list = ["Haribo", "Cookies", "Nutella", "Dragon", "Wolf", "Me"]

# 1) Pick random word from the list
random_word = random.choice(word_list)

# 2) Computer tells the user the number of letters in the word
number_of_characters = len(random_word)

# This is a flag that will be marked
did_guess = False

# Guessed characters list
guessed_characters = []
for i in range(0, number_of_characters):
    guessed_characters.append('_')

# Number of guessed characters
number_guessed = 0

# Maximum number of failed guesses
max_failed_guesses = 4

# Number of failed guesses
guesses_failed = 0

# Bonus
# File name
file_name = 'hangman.txt'

# Intro game text
intro_screen(number_of_characters)

# Loop, repeat code until user guessed the word
while did_guess is False:

    #Print underscores or any guessed letters
    print_hangman_line(guessed_characters)

    # Ask user for the letter input
    input_character = read_character()

    # Write users guess to the file
    log_guess(file_name, input_character)


    # Check if letter was already guessed
    if already_guessed(input_character, guessed_characters):
        print("Letter already guessed")
    else: #otherwise
        # Check if letter is in the word
        find_character = check_letter(input_character, random_word)
        if find_character != -1: # result is not -1, means that letter was found in the word
            # Put the guessed character in the the correct position in the list
            # for instance assume we have word cat
            # to the user its displayed _ _ _
            # then user guessed a which is a position 2
            # then script replaces underscore _ as position 2 with the guessed letter
            guessed_characters[find_character] = input_character
            number_guessed += 1
        else:
            guesses_failed += 1
            print("Nope, try again")

        if guesses_failed == max_failed_guesses:
            print("You died! Sorry")
            sys.exit(0)


    if number_guessed == number_of_characters:
        # Stop the loop, user guessed the word
        did_guess = True
        if did_guess is True:
            congratulations()

