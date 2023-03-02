import random

u_dead = False

random_choice = random.randint(0,2)

if random_choice == 0:
    bad_food = 'bread'
elif random_choice == 1:
    bad_food = 'milk'
else:
    bad_food = 'meat'

what_to_eat = ''
while (what_to_eat != 'bread' and
       what_to_eat != 'milk' and
       what_to_eat != 'meat'):
    what_to_eat = input('what should i eat in the fridge: bread, milk, or meat? ')

if bad_food == what_to_eat:
    u_dead = True
if u_dead == True:
    print("uh oh, that one had 2 flakes of fentanyl in it.")
    print('')
    print("*anonymous person asking what to eat is now perish*")
else:
    print("delicious " + what_to_eat + " for my bellie.")