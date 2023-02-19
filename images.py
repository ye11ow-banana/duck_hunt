import pygame

from utils import get_bird_images
from consts import BIRD_TYPES, DIRECTIONS

icon = pygame.image.load('images/icon.png')
background = pygame.image.load('images/background.webp')
crosshair = pygame.image.load('images/crosshair.jpg')

bird_images = get_bird_images(BIRD_TYPES, DIRECTIONS)
