#!/usr/bin/python

# Import additional library called random
# This library contains functions like "choice".
# Choice function is used to randomly pick the word from the list which we define later in the code.
# 'import' below means that You are informing Your script about new things that it can do
# However You are not yet using it's functionality, You are just telling the program that You will
# It's like studying, You have read the book, got some new knowledge but you didn't have a chance to use it yet.
import random

# Import additional library called os
# It allows the program to manipulate the system.
# In this program it is used to clear the screen from anything that we print
# For instance if there is print("Hello")
# it will print to the screen  Hello
# then if we use os.system('cls')
# That Hello text will be removed from the screen
import os
import sys

# Prints number of guessed and not guessed letters to the screen
# Not yet guessed letters are represented by an underscore _
# This function has two parameters number and guessed
# Number will represent the number of characters in the word
# Guessed will contain list of guessed words
# As You can see guessed is written as guessed = ''
# What this means it that this parameter is optional.
# So we have two options of how we can use this function
# We can call/invoke/run/execute (they all mean the same) the function in the following way
# print_hangman_line(10) - as You can see we only provided one parameter 10,
#       that means second parameter which is 'guessed' will automatically be set to '' (empty value)
# or
# print_hangman_line(10, guessed=['a', 'b', 'c']) -
#       In here we have provided 2 parameters, 10 and guessed=['a', 'b', 'c']
#
# Lets assume that the function would look like this
#   print_hangman_line(number, guessed='abc'):
# This means that default value for parameter guessed is abc
def print_hangman_line(guessed, guessed_old=''):
    # for i in range(0, number):
    #     print("_", end=" ")

    for character in guessed:
        print(character, end=' ')

    print("\r\n")
    return


# Check if letter is in the selected word
def check_letter(letter, word):
    return word.find(letter)

def already_guessed(letter, guessed):
    if letter in guessed:
        return True
    else:
        return False

# Refresh the console window
def refresh_screen(number_of_characters):
    # Clear console window - http://stackoverflow.com/a/2084628
    os.system('cls' if os.name == 'nt' else 'clear')
    print("    Hangman!")
    print("Word has " + str(number_of_characters) + " letters")
    return

def log_guess(file, text):
    with open(file, "a") as log:
        log.write(text + ", ")

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

# Clear screen window and print content again.
refresh_screen(number_of_characters)

# Loop, repeat code until user guessed the word
while did_guess is False:

    print_hangman_line(guessed_characters)

    input_character = read_character()

    log_guess(file_name, input_character)

    print("Checking: " + input_character)

    if already_guessed(input_character, guessed_characters):
        print("Letter already guessed")
    else:
        find_character = check_letter(input_character, random_word)
        if find_character != -1:
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

