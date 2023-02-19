import pygame

from consts import WINDOW_WIDTH, WINDOW_HEIGHT, background_colors
from utils import get_level, get_music

icon = pygame.image.load('images/icon.png')
background = pygame.image.load('images/background.webp')
crosshair = pygame.image.load('images/crosshair.jpg')

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Duck Hunt')

level = get_level()

music = get_music(level)
music.set_volume(0.1)

screen.fill(background_colors[level])

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(9)
