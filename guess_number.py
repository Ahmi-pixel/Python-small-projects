

import random


num = random.randint(1, 100)
print("Guess the number between 1 and 100: ")
while True:
    try:
        guess = int(input("Enter the number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer between 1 and 100.")
        continue
    if guess < 1 or guess > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    if guess == num:
        print("Congratulations! You've guessed the correct number.")
        break
    elif guess < num:
        print("Too low! Try higher.")
    else:
        print("Too high! Try a lower number.")
