import pygame
import sys
from pygame.locals import *

# Constants
FPS = 60
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60
PADDLE_BUFFER = 20
PADDLE_SPEED = 6
PUCK_RADIUS = 15
PUCK_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
fpsClock = pygame.time.Clock()

# Set up the display
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Air Hockey')

# Paddle and Puck Setup
def paddle(x, y):
    pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

def puck(x, y):
    pygame.draw.circle(DISPLAYSURF, WHITE, (x, y), PUCK_RADIUS)

# Initial positions
paddle1_y = paddle2_y = (WINDOW_HEIGHT - PADDLE_HEIGHT) / 2
puck_x, puck_y = WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2
puck_dx, puck_dy = PUCK_SPEED, PUCK_SPEED

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Movement logic for paddles
    keys = pygame.key.get_pressed()
    if keys[K_w] and paddle1_y > 0:
        paddle1_y -= PADDLE_SPEED
    if keys[K_s] and paddle1_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle1_y += PADDLE_SPEED
    if keys[K_UP] and paddle2_y > 0:
        paddle2_y -= PADDLE_SPEED
    if keys[K_DOWN] and paddle2_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        paddle2_y += PADDLE_SPEED

    # Update puck position
    puck_x += puck_dx
    puck_y += puck_dy

    # Collision with top/bottom
    if puck_y - PUCK_RADIUS <= 0 or puck_y + PUCK_RADIUS >= WINDOW_HEIGHT:
        puck_dy *= -1

    # Check if puck goes out of bounds
    if puck_x - PUCK_RADIUS <= 0 or puck_x + PUCK_RADIUS >= WINDOW_WIDTH:
        running = False  # Stop the game if the puck goes out of bounds

    # Collision with paddles
    if puck_x - PUCK_RADIUS <= PADDLE_WIDTH + PADDLE_BUFFER and paddle1_y <= puck_y <= paddle1_y + PADDLE_HEIGHT:
        puck_dx *= -1
    if puck_x + PUCK_RADIUS >= WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER and paddle2_y <= puck_y <= paddle2_y + PADDLE_HEIGHT:
        puck_dx *= -1

    # Clear screen
    DISPLAYSURF.fill(BLACK)

    # Draw paddles and puck
    paddle(PADDLE_BUFFER, paddle1_y)
    paddle(WINDOW_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER, paddle2_y)
    puck(int(puck_x), int(puck_y))

    # Update display and tick
    pygame.display.update()
    fpsClock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
