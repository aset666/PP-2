import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 100
ENEMY_WIDTH, ENEMY_HEIGHT = 50, 100
COIN_RADIUS = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Load player image (replace with your image)
player_img = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_img.fill(BLUE)

# Enemy and coin setup
enemy_speed = 3
enemy_x = WIDTH // 2 - ENEMY_WIDTH // 2
enemy_y = -ENEMY_HEIGHT
coins = []
collected_coins = 0

# Player setup
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - PLAYER_HEIGHT - 10
player_speed = 5

# Font for displaying score and speed
font = pygame.font.Font(None, 36)

# Function to draw coins
def draw_coins():
    for coin in coins:
        pygame.draw.circle(screen, coin["color"], (coin["x"], coin["y"]), COIN_RADIUS)

# Function to check if the player collects a coin
def collect_coin():
    global collected_coins
    global coins
    for coin in coins[:]:
        if player_x < coin["x"] < player_x + PLAYER_WIDTH and player_y < coin["y"] < player_y + PLAYER_HEIGHT:
            collected_coins += coin["weight"]
            coins.remove(coin)  # Remove the collected coin
            # Increase enemy speed after collecting N coins
            if collected_coins >= 5:
                increase_enemy_speed()
                collected_coins = 0  # Reset coin collection for next speed increase

# Function to increase the speed of the enemy
def increase_enemy_speed():
    global enemy_speed
    enemy_speed += 1

# Function to randomly generate coins
def generate_coins():
    # Add new coins with random positions and weights
    if random.random() < 0.02:  # 2% chance to spawn a new coin each frame
        x = random.randint(0, WIDTH - COIN_RADIUS * 2)
        weight = random.randint(1, 3)  # Coin weight can be between 1 and 3
        coin = {"x": x, "y": -COIN_RADIUS, "weight": weight, "color": (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))}
        coins.append(coin)

# Main game loop
clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_WIDTH:
        player_x += player_speed

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -ENEMY_HEIGHT
        enemy_x = random.randint(0, WIDTH - ENEMY_WIDTH)

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw enemy
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT))

    # Generate and draw coins
    generate_coins()
    draw_coins()

    # Check if player collects coins
    collect_coin()

    # Draw score and speed
    score_text = font.render(f"Coins: {collected_coins}", True, BLACK)
    speed_text = font.render(f"Enemy Speed: {enemy_speed}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(speed_text, (10, 50))

    # Update screen
    pygame.display.update()

    # Set frame rate
    clock.tick(60)
