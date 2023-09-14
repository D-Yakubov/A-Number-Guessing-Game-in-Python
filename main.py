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

def find_num_pc(x=10):
    input(f"Think a number between 1 and {x}, then press any keyboard. I find it")
    low = 1
    high = x
    guesses =   0
    while True:
        guesses += 1
        if low != high:
            guessed_num = random.randint(low, high)
        else:
            guessed_num = low
        answer = input(
            f"You thought {guessed_num} this number?: (if right press 't')"
            f"I thought number is greater than (+), or less than (-)".lower()
        )
        if answer == "-":
            high = guessed_num - 1
        elif answer == "+":
            low = guessed_num + 1
        else:
            break
        print(f"I found it with {guesses} guesses!")
        return guesses

def play(x=10):
    again = True
    while again:
        guesses_user = find_num(x)
        guesses_pc = find_num_pc(x)

        if guesses_user > guesses_pc:
            print(f"I found it with {guesses_pc} guesses and I won!")
        elif guesses_user < guesses_pc:
            print(f"You found it with {guesses_pc} guesses and You won! Congratulations!")
        else:
            print("Draw!")
        again = int(input("Do you wanna play again? Yes(1)/No(0):"))

play()
         