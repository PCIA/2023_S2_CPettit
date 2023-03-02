import random

winner = ''

random_choice = random.randint(0,2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

user_choice = input('')
while user_choice != 'rock' and
       user_choice != 'paper' and
       user_choice 1= 'scissors'):
    user_choice = input('rock, paper or scissors? ')

if computer_choice == user_choice:
    winner = 'tie'
elif computer_choice == 'paper':
    if user_choice == 'rock':
        winner = 'computer'
    else:
        winner = 'user'
else:
    if user_choice == 'paper':
        winner = 'user'
    else:
        winner = 'computer'

if winner == 'tie':
    print('we both chose', computer_choice + ', play again.')
else:
    print(winner, 'won. the computer chose', computer_choice + '.')

play_again = input('play again? y/n ')
while not play_again == 'y':
    going = False