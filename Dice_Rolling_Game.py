import random

count=0
history = []
while True:
    choice = input('Roll the dice by pressing Enter (y/n)?').strip().lower()
    print()
    count+=1
    if choice=='y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        history.append((dice1, dice2))
        if dice1 == dice2:
            print(f'You rolled a double {dice1}!')
        else:
            print(f'You rolled {dice1} and {dice2}')  
    elif choice=='n':
        historywant = input('Do you want to see your roll history (y/n)?').strip().lower()   
        break
    else:
        print('Invalid input. Please enter y or n.')


if historywant == 'y':
    print('Your roll history:')
    for i, (d1, d2) in enumerate(history, start=1):
        if d1 == d2:
            print(f'Roll {i}: Double {d1}')
        else:
            print(f'Roll {i}: {d1} and {d2}')
elif historywant == 'n':
    print('Then no history for you!')
else:
    print('Invalid input. Please enter y or n.')
print()
countwant = input('Do you want to see how many times you rolled the dice (y/n)?').strip().lower()
if countwant == 'y':
    print(f'You rolled the dice {count} times.')
elif countwant == 'n':
    print('Goodbye')
