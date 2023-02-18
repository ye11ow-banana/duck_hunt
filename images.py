import pygame

from utils import get_bird_images

icon = pygame.image.load('images/icon.png')
background = pygame.image.load('images/background.webp')
crosshair = pygame.image.load('images/crosshair.jpg')

DIRECTIONS = 'top', 'top_right', 'right', 'bottom'
BIRD_TYPES = 'green', 'blue', 'red'
bird_images = get_bird_images(BIRD_TYPES, DIRECTIONS)
