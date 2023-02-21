import pygame

from consts import WINDOW_WIDTH, WINDOW_HEIGHT, background_colors
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

screen.fill(background_colors[level])

birds = []
bird_timer = pygame.USEREVENT + 1
pygame.time.set_timer(bird_timer, 2500)

running = True
while running:
    screen.blit(background, (0, 0))

    for bird in birds:
        screen.blit(bird.images.top[0], (bird.position.x, bird.position.y))

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
        if event.type == bird_timer:
            birds.append(Bird(level))

    clock.tick(9)
