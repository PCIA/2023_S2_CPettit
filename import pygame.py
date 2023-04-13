import pygame
import random

# initialize pygame
pygame.init()

# set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Oregon Trail')

# define game variables
distance_traveled = 0
food = 500
health = 100
weather = 'sunny'

# define game functions
def update_weather():
    global weather
    weather_options = ['sunny', 'rainy', 'stormy', 'snowy']
    weather = random.choice(weather_options)

def hunt():
    global food
    food_gained = random.randint(50, 100)
    food += food_gained
    print(f"You went hunting and gained {food_gained} pounds of food.")

def rest():
    global health
    health += 20
    if health > 100:
        health = 100
    print("You decided to rest and regain some health.")

def travel():
    global distance_traveled, food, health
    distance_traveled += 100
    food_needed = 50
    if weather == 'rainy':
        food_needed *= 1.2
        health -= 10
        print("It's raining and the trail is muddy. Your progress is slowed and your health is suffering.")
    elif weather == 'stormy':
        food_needed *= 1.5
        health -= 20
        print("There's a terrible storm and you have to hunker down for a while. You're low on food and your health is suffering.")
    elif weather == 'snowy':
        food_needed *= 2
        health -= 30
        print("It's snowing heavily and the trail is difficult to traverse. You're burning through your food and your health is suffering.")
    else:
        print("You continue on the trail.")
    food -= food_needed
    if food < 0:
        food = 0
        health -= 10
        print("You're running out of food and your health is suffering.")
    if health <= 0:
        print("You died of starvation and exposure.")
        pygame.quit()
        quit()

# main game loop
game_running = True
while game_running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                hunt()
            elif event.key == pygame.K_r:
                rest()
            elif event.key == pygame.K_t:
                travel()

    # update game state
    update_weather()

    # draw game window
    game_window.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render(f"Distance Traveled: {distance_traveled} miles", True, (0, 0, 0))
    game_window.blit(text, (10, 10))
    text = font.render(f"Food: {food} pounds", True, (0, 0, 0))
    game_window.blit(text, (10, 50))
    text = font.render(f"Health: {health}%", True, (0, 0, 0))
    game_window.blit(text, (10, 90))
    text = font.render(f"Weather: {weather}", True, (0, 0, 0))
    game_window.blit(text, (10, 130))
    pygame.display.update
