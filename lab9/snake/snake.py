import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game with Timed Foods")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# Block size and initial speed
block_size = 20
initial_snake_speed = 15  # Initial speed value
snake_speed = initial_snake_speed  # Initialize snake speed

# Fonts for displaying text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])

# Function to display the level
def Your_level(level):
    value = score_font.render("Level: " + str(level), True, WHITE)
    screen.blit(value, [screen_width - 150, 0])

# Main game logic
def gameLoop():
    global snake_speed  # Add global statement to modify the global snake_speed variable
    game_over = False
    game_close = False

    # Initial snake position
    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_body = []
    length_of_snake = 1

    # List to hold foods
    foods = []

    # Score and level variables
    score = 0
    level = 1

    clock = pygame.time.Clock()

    food_timer = 0  # Timer for food expiration

    while not game_over:
        while game_close:
            screen.fill(BLUE)
            message = font_style.render("You Lost! Press Q-Quit or C-Play Again", True, RED)
            screen.blit(message, [screen_width / 6, screen_height / 3])
            Your_score(score)
            Your_level(level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Snake control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for border collision
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        # Move the snake
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLUE)

        # Generate random food every 5 seconds
        if food_timer == 0 or time.time() - food_timer > 5:  # Food appears every 5 seconds
            foodx = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0
            food_weight = random.randint(1, 5)  # Random food weight between 1 and 5
            food_timer = time.time()  # Reset the food timer

            # Add food to the list with its position and weight
            foods.append({"x": foodx, "y": foody, "weight": food_weight, "time": time.time()})

        # Check if the food has expired and remove it
        for food in foods[:]:
            if time.time() - food["time"] > 3:  # If the food has been on screen for more than 3 seconds, remove it
                foods.remove(food)

        # Draw food
        for food in foods:
            pygame.draw.rect(screen, GREEN, [food["x"], food["y"], block_size, block_size])  # Food

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_body.append(snake_head)

        # Remove the last element to keep the snake's length consistent
        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Check if snake collides with itself
        for block in snake_body[:-1]:
            if block == snake_head:
                game_close = True

        # Draw the snake
        for block in snake_body:
            pygame.draw.rect(screen, WHITE, [block[0], block[1], block_size, block_size])

        # Check if the snake eats food
        for food in foods[:]:
            if x1 == food["x"] and y1 == food["y"]:
                foods.remove(food)  # Remove the eaten food
                length_of_snake += 1
                score += food["weight"]  # Add food's weight to the score

                # Increase level and speed as the snake eats food
                if score % 30 == 0:
                    level += 1
                    snake_speed += 2  # Increase snake speed

        Your_score(score)
        Your_level(level)

        pygame.display.update()

        clock.tick(snake_speed)  # Ensure the snake's speed is controlled

    pygame.quit()
    quit()

# Start the game
gameLoop()
