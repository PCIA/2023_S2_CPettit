<<<<<<< HEAD
import pygame, sys
from temp import *
# Pygame setup
pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    pygame.display.update()
    clock.tick(60)
=======
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
while (user_choice != 'rock' and
       user_choice != 'paper' and
       user_choice != 'scissors'):
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
>>>>>>> 72d39f9bd903ac8f788c803d9cc845538d228fd1
