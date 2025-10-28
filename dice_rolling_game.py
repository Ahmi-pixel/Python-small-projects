"""A simple dice rolling game that allows users to roll two dice and see their results."""

import random

while True:
    roll = input("Roll the dice? (y/n): ").lower()
    if roll == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"You rolled a {dice1} and a {dice2}. Total: {dice1 + dice2}")
    elif roll == 'n':
        print("Maybe next time!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
