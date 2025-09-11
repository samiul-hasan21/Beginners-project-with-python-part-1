import random

history = []
while True:
    choice = input('Roll the dice by pressing Enter (y/n)?').lower()
    print()
    if choice=='y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        history.append((dice1, dice2))
        if dice1 == dice2:
            print(f'You rolled a double {dice1}!')
        else:
            print(f'You rolled {dice1} and {dice2}')  
    elif choice=='n':
        print('Goodbye')
        break
    else:
        print('Invalid input. Please enter y or n.')

historywant = input('Do you want to see your roll history (y/n)?').lower()
if historywant == 'y':
    print('Your roll history:')
    for i, (d1, d2) in enumerate(history, start=1):
        if d1 == d2:
            print(f'Roll {i}: Double {d1}')
        else:
            print(f'Roll {i}: {d1} and {d2}')

