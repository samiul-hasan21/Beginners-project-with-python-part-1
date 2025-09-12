import random

print("Welcome to the Number Guessing Game!")
print("In This game, you will guess a number within a range you choose.")
h=input("Do you want to read the instructions (y)?").strip().lower()
if h=='y':
    print("Instructions:")
    print("1. Choose a range by entering the first and second number.")
    print("2. Choose a mode: Hard mode (3 attempts) or Easy mode (unlimited attempts).")
    print("3. Try to guess the randomly selected number within the chosen range.")
    print("4. After each guess, you'll be told if your guess is too high, too low, or correct.")
    print("5. In Easy mode, you can choose to stop playing after every 3 attempts incorrect guess.")
    print("6. In Hard mode, you have a maximum of 3 attempts to guess the number.")
    print("Good luck and have fun!")
    print()
else:
    print("Let's get started then!")
    print()

F= int(input('Enter the first number of the range: '))
S= int(input('Enter the second number of the range: '))
K = max(F, S)
L= min(F, S)

    
while True:
    mode = input("Do you want to play in hard mode(y/n) or do you want to quit(q)?").strip().lower()
    count = 0
    if mode == 'y':
        print(f"You have chosen hard mode. You have 3 attempts to guess the number between {L} and {K}.")
        number = random.randint(L, K)
        attempts = 3
        while attempts > 0:
            try:
                guess = int(input(f"You have {attempts} attempts left. Make a guess: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue
            count += 1
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
            else:
                print(f"Congratulations! You've guessed the number {number} in {count} attempts.")
                break
            attempts -= 1
            if attempts == 0:
                print(f'Sorry you have run out of attempts. The number was {number}.')
    elif mode == 'n':
        number = random.randint(L, K)
        attempts = 0
        print(f"You have chosen easy mode. You have to guess the number between {L} and {K} with no limit of attempts.")
        while True:
            try:
                guess = int(input(f"Make a guess: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue
            count += 1
            attempts += 1
            if guess < number:
                print("Too low.")  
            elif guess > number:
                print("Too high.")  
            else:
                print(f"Congratulations! You've guessed the number {number} in {count} attempts.")
                break
            if attempts==3:
                ask = input("Do you want to continue (y/n)?").strip().lower()
                attempts=0
                if ask =='n':
                    print(f'The number was {number}. Goodbye!')
                    break
    elif mode == 'q':
        print("Thank you for playing! Goodbye!")
        break

    else:
        print("Invalid input. Please enter y or n.")
    
