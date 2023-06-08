import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the game
pygame.display.set_caption("Bouncing Ball")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the ball
ball_radius = 20
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
ball_speed = 2
ball_dx = ball_speed
ball_dy = ball_speed

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy
    
    # Bounce the ball off the walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_dx *= -1
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_dy *= -1
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    screen.fill((0, 0, 0))
    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    
    # Update the screen
    pygame.display.flip()
    
    # Wait for a short time to control the frame rate
    pygame.time.wait(10)

# Clean up
pygame.quit()
