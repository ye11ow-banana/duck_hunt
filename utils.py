import pygame


def get_level():
    return 'medium'


def get_music(level):
    return pygame.mixer.Sound(f'sounds/{level}_music.mp3')
