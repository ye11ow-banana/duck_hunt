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

headshot_sound = pygame.mixer.Sound(f'sounds/headshot.mp3')
headshot_sound.set_volume(0.5)
headshot_is_played = False

birds: list[Bird] = []
spawn_timer = 0

crosshair_rect = crosshair.get_rect()

label = pygame.font.Font('fonts/Roboto-Black.ttf', 30)
big_label = pygame.font.Font('fonts/Roboto-Black.ttf', 100)
score = 0

upset_smile_label = big_label.render(':(', True, 'white')
lose_label = label.render('You lost', True, 'white')
restart_label = label.render('Play again', True, 'white')
restart_label_rect = restart_label.get_rect(topleft=(200, 275))
donate_label = label.render('Donate us please we want to eat:', True, 'white')
card_label = label.render('Mono: 1234 1234 1234 1234', True, 'white')

is_button_pressed_once = True

time_to_spawn = 21

gameplay = True

running = True
while running:
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
        if pygame.mouse.get_pressed()[0] and is_button_pressed_once:
            for bird in birds:
                image = bird.current_image
                bird_rect = image.get_rect()
                bird_rect.center = bird.current_position.x, bird.current_position.y
                if bird_rect.collidepoint(mouse):
                    bird.is_killed = True
                    score += 1
                    headshot_is_played = False
                    is_button_pressed_once = False
        if event.type == pygame.MOUSEBUTTONUP:
            is_button_pressed_once = True

    if not gameplay:
        pygame.mouse.set_visible(True)
        screen.fill((0, 120, 215))
        screen.blit(upset_smile_label, (200, 50))
        screen.blit(lose_label, (200, 200))
        screen.blit(restart_label, restart_label_rect)
        screen.blit(donate_label, (200, 350))
        screen.blit(card_label, (200, 425))

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            birds.clear()
            music.stop()
            score = 0
        continue

    screen.fill(BACKGROUND_COLORS[level])

    pygame.mouse.set_visible(False)
    for bird in birds:
        bird_image = bird.get_current_image()
        bird.move()
        bird_rect = bird_image.get_rect()
        bird_rect.center = bird.current_position.x, bird.current_position.y
        screen.blit(bird_image, bird_rect)
        if bird.current_position.y > bird.initial_position.y:
            birds.remove(bird)
        if bird.current_position.x > WINDOW_WIDTH + 20 or bird.current_position.y < -20:
            gameplay = False

    screen.blit(background, (0, 0))
    if spawn_timer == time_to_spawn:
        birds.append(Bird(level))
        spawn_timer = 0
    spawn_timer += 1
    screen.blit(crosshair, crosshair_rect)
    crosshair_rect.center = pygame.mouse.get_pos()

    if score % 50 == 0 and score != 0 and not headshot_is_played:
        headshot_sound.play()
        headshot_is_played = True
        if time_to_spawn > 5:
            time_to_spawn -= 5
            spawn_timer = 0

    score_label = label.render(f'Killed: {score}', True, 'white')
    screen.blit(score_label, (WINDOW_WIDTH - 200, 50))

    clock.tick(SPEEDS[level])
