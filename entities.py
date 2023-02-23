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
        self.non_spawned_border = NonSpawnedBorder(left=200, top=500, right=500, bottom=100)
        self.current_position = self._get_random_position()
        self.initial_position = BirdPosition(self.current_position.x, self.current_position.y)
        self.previous_y = self.current_position.y
        self.serial_image_indexes = {}
        self.math_subfunction = self._get_math_subfunction()

    def __getattribute__(self, item):
        if item == 'get_current_image':
            self._move()
        return super().__getattribute__(item)

    def get_current_image(self):
        if self.previous_y - self.current_position.y < 0.5:
            return self._get_serial_image_by_direction('right')
        elif self.previous_y - self.current_position.y == 1 and \
                self.initial_position.x - self.current_position.x == 0:
            return self._get_serial_image_by_direction('top')
        else:
            return self._get_serial_image_by_direction('top_right')

    def _get_serial_image_by_direction(self, direction):
        index = self.serial_image_indexes.get(direction, 0) + 0.25
        index = index if index < len(getattr(self.images, direction)) else 0
        image = getattr(self.images, direction)[int(index)]
        self.serial_image_indexes = {direction: index}
        return image

    def _move(self) -> None:
        self.previous_y = self.current_position.y
        self.current_position.x += 1
        self.current_position.y = self._math_function(self.current_position.x)

    def _math_function(self, x):
        return self.initial_position.y - self.math_subfunction(x - self.initial_position.x)

    def _up_function(self, x):
        self.current_position.x -= 1
        return self.initial_position.y - self.current_position.y + 1

    @staticmethod
    def _linear_function(x):
        return 0.5 * x

    @staticmethod
    def _root_function(x):
        return 15 * math.sqrt(x)

    @staticmethod
    def _in_power_function(x):
        return 0.002 * x ** 2

    def _get_math_subfunction(self):
        math_function_by_level = {
            LEVELS[0]: [self._up_function, self._linear_function],
            LEVELS[1]: [self._up_function, self._linear_function, self._root_function],
            LEVELS[2]: [
                self._up_function, self._linear_function,
                self._root_function, self._in_power_function
            ]
        }
        _list = math_function_by_level[self.level]
        return _list[randint(0, len(_list) - 1)]

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
        y = randint(self.non_spawned_border.top, WINDOW_HEIGHT - self.non_spawned_border.bottom)
        return BirdPosition(x, y)
