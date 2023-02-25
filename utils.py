import argparse

import pygame

from consts import LEVELS


def get_level():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--level', default=LEVELS[1], choices=[*LEVELS],
        type=str, help='Difficulty level of the game'
    )
    args = parser.parse_args()
    return args.level


def get_music(level):
    return pygame.mixer.Sound(f'sounds/{level}_music.mp3')
