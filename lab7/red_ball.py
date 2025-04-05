import pygame

pygame.init()
widht,height=600,400
ball_radius=25
move_step=20

screen=pygame.display.set_mode((widht,height))
x=widht//2
y=height//2

running=True
clock=pygame.time.Clock()

while running:
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - ball_radius - move_step >= 0:
        y -= move_step
    if keys[pygame.K_DOWN] and y + ball_radius + move_step <= height:
        y += move_step
    if keys[pygame.K_LEFT] and x - ball_radius - move_step >= 0:
        x -= move_step
    if keys[pygame.K_RIGHT] and x + ball_radius + move_step <= widht:
        x += move_step
        
    pygame.draw.circle(screen,(255,0,0),(x,y),ball_radius)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()