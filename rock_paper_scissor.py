import random

emojis = {
    'r': '✊',  # Rock
    'p': '✋',  # Paper
    's': '✌️'   # Scissors
}
choices = ('r', 'p', 's')
while True:
    user_choice = input("Enter rock, paper, scissors (r/s/p): ").lower()
    if user_choice not in choices:
        print("Invalid input. Please enter 'r', 'p', or 's'.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {emojis[computer_choice]}")
    print(f"You chose: {emojis[user_choice]}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif ((user_choice == 'r' and computer_choice == 's') or
          (user_choice == 'p' and computer_choice == 'r') or
          (user_choice == 's' and computer_choice == 'p')):
        print("You win!")
    else:
        print("Computer wins!")
    should_continue = input("Continue playing? (y/n): ").lower()
    if should_continue != 'y':
        print("Thanks for playing!")
        break
