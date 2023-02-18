import pygame
from consts import ICON_WIDTH, ICON_HEIGHT
from images import icon, background, crosshair, bird_images

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((ICON_WIDTH, ICON_HEIGHT))
pygame.display.set_caption('Duck Hunt')

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(9)
