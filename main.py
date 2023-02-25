import pygame

from consts import WINDOW_WIDTH, WINDOW_HEIGHT, SPEEDS, BACKGROUND_COLORS
from entities import Bird
from utils import get_level, get_music

icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('images/background.webp')
crosshair = pygame.image.load('images/crosshair.png')
crosshair = pygame.transform.scale(
    crosshair, (crosshair.get_width() // 3, crosshair.get_height() // 3)
)

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Duck Hunt')

level = get_level()

music = get_music(level)
music.set_volume(0.05)

birds = []
spawn_timer = 0

pygame.mouse.set_visible(False)
crosshair_rect = crosshair.get_rect()

running = True
while running:
    screen.fill(BACKGROUND_COLORS[level])
    for bird in birds:
        bird_image = bird.get_current_image()
        bird.move()
        bird_rect = bird_image.get_rect()
        bird_rect.center = bird.current_position.x, bird.current_position.y
        screen.blit(bird_image, bird_rect)
        if bird.current_position.y > bird.initial_position.y:
            birds.remove(bird)

    screen.blit(background, (0, 0))
    if spawn_timer == 20:
        birds.append(Bird(level))
        spawn_timer = 0
    spawn_timer += 1

    screen.blit(crosshair, crosshair_rect)
    crosshair_rect.center = pygame.mouse.get_pos()

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
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            for bird in birds:
                image = bird.current_image
                bird_rect = image.get_rect()
                bird_rect.center = bird.current_position.x, bird.current_position.y
                if bird_rect.collidepoint(mouse):
                    bird.is_killed = True

    clock.tick(SPEEDS[level])
