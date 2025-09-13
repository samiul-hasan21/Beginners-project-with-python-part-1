import random

print("Welcome to Rock, Paper, Scissors game!")


play = input("Do you want to play with the computer or with a friend?(c/f): ").strip().lower()
if play == 'c':
    print("You are playing against the computer.")
    p_wins=0
    c_wins=0
    ties=0
    while True:
        user_choice = input("Enter your choice (R,P,S): ").strip().lower()
        choices = ['r', 'p', 's']
        choices_full = {'r': 'Rock ✊', 'p': 'Paper ✋', 's': 'Scissors ✌️'}
        win_map = {'r': 's', 'p': 'r', 's': 'p'}
        if user_choice in choices_full:
            print(f'You chose: {choices_full[user_choice]}')

        computer_choice = random.choice(choices)
        print(f"Computer chose: {choices_full[computer_choice]}")
        if user_choice not in choices:
            print("Invalid choice! Please choose R, P, or S.")
        elif user_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif win_map[user_choice] == computer_choice:
            print("You win!")
            p_wins += 1
        else:
            print("Computer wins!")
            c_wins += 1
        print(f"Score: You - {p_wins}, Computer - {c_wins} And Ties - {ties}")
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break
elif play == 'f':
    print("You are playing against a friend.")
    p1_wins = 0
    p2_wins = 0
    ties = 0
    while True:
        player1_choice = input("Player 1, enter your choice (R,P,S): ").strip().lower()
        player2_choice = input("Player 2, enter your choice (R,P,S): ").strip().lower()
        choices = ['r', 'p', 's']
        choices_full = {'r': 'Rock ✊', 'p': 'Paper ✋', 's': 'Scissors ✌️'}
        win_map = {'r': 's', 'p': 'r', 's': 'p'}
        if player1_choice in choices_full:
            print(f'Player 1 chose: {choices_full[player1_choice]}')
        if player1_choice not in choices:
            print("Invalid choice player 1! Please choose R, P, or S.")
        if player2_choice in choices_full:
            print(f'Player 2 chose: {choices_full[player2_choice]}')
        if player2_choice not in choices:
            print("Invalid choice player 2! Please choose R, P, or S.")
        elif player1_choice == player2_choice:
            print("It's a tie!")
            ties += 1
        elif win_map[player1_choice] == player2_choice:
            print("Player 1 wins!")
            p1_wins += 1
        else:
            print("Player 2 wins!")
            p2_wins += 1
        print(f"Score: Player 1 - {p1_wins}, Player 2 - {p2_wins} And Ties - {ties}")
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break    
print("Thanks for playing!")
