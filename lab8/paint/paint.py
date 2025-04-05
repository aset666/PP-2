import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up drawing variables
color = BLACK
drawing = False
shape = "pen"  # Default shape (pen)
last_pos = None

# Set up the font for text
font = pygame.font.Font(None, 36)

# Create a button to change color (for simplicity, just a red button here)
color_button_rect = pygame.Rect(10, 10, 50, 50)

# Function to draw the selected shape
def draw_shape(screen, shape, color, start_pos, end_pos):
    if shape == "pen":
        pygame.draw.line(screen, color, start_pos, end_pos, 5)
    elif shape == "rectangle":
        pygame.draw.rect(screen, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 5)
    elif shape == "circle":
        radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, start_pos, radius, 5)

# Main game loop
screen.fill(WHITE)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse button events (for drawing and selecting color)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                last_pos = event.pos
            elif event.button == 3:  # Right mouse button (to erase)
                shape = "eraser"
                drawing = True
                last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 or event.button == 3:
                drawing = False
                last_pos = None

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                if shape == "eraser":
                    pygame.draw.rect(screen, WHITE, pygame.Rect(last_pos, (event.pos[0] - last_pos[0], event.pos[1] - last_pos[1])), 10)
                else:
                    draw_shape(screen, shape, color, last_pos, event.pos)
                last_pos = event.pos

        # Color button click (simple color selection)
        if event.type == pygame.MOUSEBUTTONDOWN and color_button_rect.collidepoint(event.pos):
            color = RED  # Change to red (can add more buttons for other colors)

    # Draw color selection button
    pygame.draw.rect(screen, RED, color_button_rect)

    # Draw text showing the current tool
    text = font.render(f"Current tool: {shape}", True, BLACK)
    screen.blit(text, (WIDTH - 200, 10))

    pygame.display.update()
