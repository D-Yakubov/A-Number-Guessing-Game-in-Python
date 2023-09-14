"""
builder: Dastonbek Yakubov
date: 13/09/2023
project: A number guessing game 
"""

import random

def find_num(x=10):
    random_num = random.randint(1,x)
    print(f"I thought between 1 and {x}. Can you find it?", end="")
    guesses = 0
    while True:
        guesses += 1
        guessed_num = int(input(">>>"))
        if guessed_num < random_num:
            print(f"Incorrect! I thought number is greater than {guessed_num}. Try again.", end="")
        elif guessed_num > random_num:
            print(f"Incorrect! I thought number is less than {guessed_num}. Try again.", end="")
        else:
            break
    print(f"Congratulations! You find {guessed_num} with {guesses} guesses!")
    return guesses
        