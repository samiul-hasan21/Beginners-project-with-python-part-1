import random

print("Welcome to Rock, Paper, Scissors game!")

while True:
    user_choice = input("Enter your choice (R,P,S): ").strip().lower()
    choices = ['r', 'p', 's']
    choices_full = {'r': 'Rock ✊', 'p': 'Paper ✋', 's': 'Scissors ✌️'}
    if user_choice in choices_full:
        print(f'You chose: {choices_full[user_choice]}')

    computer_choice = random.choice(choices)
    print(f"Computer chose: {choices_full[computer_choice]}")
    if user_choice not in choices:
        print("Invalid choice! Please choose R, P, or S.")
    elif user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
        (user_choice == 'p' and computer_choice == 'r') or \
        (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("Computer wins!")
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        break
    
print("Thanks for playing!")
