import pygame

from consts import WINDOW_WIDTH, WINDOW_HEIGHT, SPEEDS, BACKGROUND_COLORS
from entities import Bird
from utils import get_level, get_music

icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('images/background.webp')
crosshair = pygame.image.load('images/crosshair.jpg')

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Duck Hunt')

level = get_level()

music = get_music(level)
music.set_volume(0.05)

birds = []
spawn_timer = 0

running = True
while running:
    screen.fill(BACKGROUND_COLORS[level])
    for bird in birds:
        screen.blit(bird.get_current_image(), (bird.current_position.x, bird.current_position.y))
    screen.blit(background, (0, 0))
    if spawn_timer == 20:
        birds.append(Bird(level))
        spawn_timer = 0
    spawn_timer += 1

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                music.play()
            elif event.key == pygame.K_2:
                music.stop()

    clock.tick(SPEEDS[level])
