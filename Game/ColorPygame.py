import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
running = True
color = (255, 0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        color = (0, 255, 0)

    screen.fill(color)
    pygame.display.update()
