import pygame # type: ignore
import math
from datetime import datetime

pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CENTER = (WIDTH // 2, HEIGHT // 2)

def draw_hand(length, angle_deg, color, width):
    angle_rad = math.radians(angle_deg - 90)
    end_x = CENTER[0] + length * math.cos(angle_rad)
    end_y = CENTER[1] + length * math.sin(angle_rad)
    pygame.draw.line(screen, color, CENTER, (end_x, end_y), width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, CENTER, 100, 4)

    now = datetime.now()
    minute = now.minute
    second = now.second

    minute_angle = (minute / 60) * 360
    second_angle = (second / 60) * 360

    draw_hand(60, minute_angle, RED, 6)    # Right hand – minutes
    draw_hand(80, second_angle, BLACK, 4)  # Left hand – seconds

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
