import pygame
import sys
import random
import math
import os

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Snake Game")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Clock and speed
clock = pygame.time.Clock()
speed = 10
snake_block = 20

# Fonts
font = pygame.font.SysFont("arial", 25)
big_font = pygame.font.SysFont("arial", 45)

# Sounds
def load_sound(filename):
    try:
        return pygame.mixer.Sound(filename)
    except:
        return None

eat_sound = load_sound(os.path.join("assets", "eat.wav"))
gameover_sound = load_sound(os.path.join("assets", "gameover.wav"))

# Draw Pac-Man head
def draw_pacman(x, y, direction, mouth_open):
    angle_map = {"RIGHT": (30, 330), "LEFT": (210, 150), "UP": (120, 420), "DOWN": (300, 600)}
    start, end = angle_map[direction]
    if mouth_open:
        pygame.draw.arc(screen, YELLOW, (x, y, 20, 20), math.radians(start), math.radians(end), 10)
    else:
        pygame.draw.circle(screen, YELLOW, (x + 10, y + 10), 10)

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over_screen(score, restart_callback):
    if gameover_sound: gameover_sound.play()
    screen.fill(BLACK)
    msg = big_font.render("GAME OVER", True, RED)
    score_text = font.render(f"Final Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(msg, (180, 120))
    screen.blit(score_text, (220, 180))
    screen.blit(restart_text, (120, 230))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    restart_callback()

def start_game(username, update_score_func):
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = dy = 0
    snake = []
    length = 1
    score = 0
    mouth_open = True
    mouth_timer = 0
    direction = "RIGHT"

    food_x = random.randrange(0, WIDTH - snake_block, snake_block)
    food_y = random.randrange(0, HEIGHT - snake_block, snake_block)

    def restart():
        update_score_func(username, score)
        start_game(username, update_score_func)

    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                update_score_func(username, score)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -snake_block; direction="UP"
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, snake_block; direction="DOWN"
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -snake_block, 0; direction="LEFT"
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = snake_block, 0; direction="RIGHT"

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over_screen(score, restart)

        snake_head = [x, y]_
