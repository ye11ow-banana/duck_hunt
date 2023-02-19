import pygame
from consts import ICON_WIDTH, ICON_HEIGHT


icon = pygame.image.load('images/icon.png')
background = pygame.image.load('images/background.webp')
crosshair = pygame.image.load('images/crosshair.jpg')

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((ICON_WIDTH, ICON_HEIGHT))
pygame.display.set_caption('Duck Hunt')

music = pygame.mixer.Sound('sounds/music.mp3')
music.set_volume(0.1)

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(9)
