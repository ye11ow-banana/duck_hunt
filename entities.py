import math
from random import randint

import pygame

from consts import WINDOW_WIDTH, WINDOW_HEIGHT, LEVELS
from data_structures import BirdImages, NonSpawnedBorder, BirdPosition


class Bird:
    def __init__(self, level):
        self.is_killed = False
        self.level = level
        self.speed = 5
        self.images = self._get_bird_images()
        self.non_spawned_border = NonSpawnedBorder(left=250, top=500, right=300, bottom=100)
        self.math_function = self._get_math_function()
        self.position = self._get_random_position()
        self.function_position = BirdPosition(0, self.position.y)

    def move(self) -> None:
        self.position.y = self.math_function(self.function_position.x, self.function_position.y)
        self.position.x += 1
        self.function_position.x += 1

    @staticmethod
    def _linear_function(x, y):
        return y - 0.25 * x

    @staticmethod
    def _root_function(x, y):
        return y - 10 * math.sqrt(x)

    @staticmethod
    def _in_power_function(x, y):
        return y - 0.002 * x ** 2

    def _get_math_function(self):
        math_function_by_level = {
            LEVELS[0]: [self._root_function],
            LEVELS[1]: [self._root_function],
            LEVELS[2]: [self._root_function]
        }
        return math_function_by_level[self.level][0]

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

    def _get_random_position(self):
        x = randint(self.non_spawned_border.left, WINDOW_WIDTH - self.non_spawned_border.right)
        y = self.math_function(x, WINDOW_HEIGHT)
        return BirdPosition(x, y)
