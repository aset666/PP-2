import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up the game window and clock
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game with Shapes")
clock = pygame.time.Clock()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)

# Snake settings
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Functions to display text
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [window_width / 6, window_height / 3])

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    game_window.blit(value, [0, 0])

# Snake body
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, black, [x[0], x[1], snake_block, snake_block])

# Generate food
def generate_food():
    return random.randint(0, window_width - snake_block), random.randint(0, window_height - snake_block)

# Draw shapes
def draw_square(x, y, size):
    pygame.draw.rect(game_window, green, [x, y, size, size])

def draw_right_triangle(x, y, size):
    points = [(x, y), (x + size, y), (x, y + size)]
    pygame.draw.polygon(game_window, red, points)

def draw_equilateral_triangle(x, y, size):
    points = [(x, y), (x + size, y), (x + size / 2, y - (size * (3 ** 0.5) / 2))]
    pygame.draw.polygon(game_window, blue, points)

def draw_rhombus(x, y, size):
    points = [(x, y), (x + size / 2, y - size), (x + size, y), (x + size / 2, y + size)]
    pygame.draw.polygon(game_window, yellow, points)

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    x1 = window_width / 2
    y1 = window_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = generate_food()

    while not game_over:
        while game_close:
            game_window.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_window.fill(blue)

        # Draw shapes on the screen
        draw_square(50, 50, 50)  # Draw a green square at position (50, 50)
        draw_right_triangle(150, 150, 60)  # Draw a red right triangle
        draw_equilateral_triangle(300, 300, 80)  # Draw a blue equilateral triangle
        draw_rhombus(500, 500, 60)  # Draw a yellow rhombus

        # Check for food collision
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()
            Length_of_snake += 1

        # Draw snake and food
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.draw.rect(game_window, green, [foodx, foody, snake_block, snake_block])

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
