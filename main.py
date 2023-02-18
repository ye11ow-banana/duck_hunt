import pygame
from consts import ICON_WIDTH, ICON_HEIGHT
from images import icon, background, crosshair, bird_images

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((ICON_WIDTH, ICON_HEIGHT))
pygame.display.set_caption('Duck Hunt')

bg_sound = pygame.mixer.Sound("sounds/relax_music.mp3")
bg_sound.set_volume(0.1)

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(9)
