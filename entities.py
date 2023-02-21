from random import randint

import pygame

from consts import WINDOW_WIDTH, WINDOW_HEIGHT, LEVELS
from data_structures import BirdImages, NonSpawnedBorder, BirdPosition


class Bird:
    def __init__(self, level):
        self.is_killed = False
        self.level = level
        self.speed = self._get_speed()
        self.images = self._get_bird_images()
        self.non_spawned_border = NonSpawnedBorder(left=250, top=500, right=300, bottom=100)
        self.position = self._get_random_position()
        self._move()

    def _move(self) -> None:
        return

    def _get_speed(self) -> int:
        level_speeds = {LEVELS[0]: [5], LEVELS[1]: [5, 7], LEVELS[2]: [5, 7, 9]}
        possible_speeds = level_speeds.get(self.level, [5])
        return possible_speeds[randint(0, len(possible_speeds) - 1)]

    def _get_bird_images(self) -> BirdImages:
        bird_directions = {}
        for direction in 'top', 'top_right', 'right', 'bottom':
            images = []
            for _ in range(1, 4):
                image_path = f'images/birds/{self.level}/{direction}_{_}.png'
                try:
                    images.append(pygame.image.load(image_path))
                except FileNotFoundError:
                    pass
            bird_directions[direction] = images
        return BirdImages(
            top=bird_directions['top'],
            top_right=bird_directions['top_right'],
            right=bird_directions['right'],
            bottom=bird_directions['bottom']
        )

    def _get_random_position(self) -> BirdPosition:
        x = randint(self.non_spawned_border.left, WINDOW_WIDTH - self.non_spawned_border.right)
        y = randint(self.non_spawned_border.top, WINDOW_HEIGHT - self.non_spawned_border.bottom)
        return BirdPosition(x=x, y=y)
