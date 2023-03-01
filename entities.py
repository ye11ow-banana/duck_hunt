import math
from random import randint
from typing import Callable, Literal

import pygame

from consts import WINDOW_WIDTH, WINDOW_HEIGHT, LEVELS
from data_structures import BirdImages, NonSpawnedBorder, BirdPosition


class Bird:
    __slots__ = (
        'is_killed', '_level', '_images', '_non_spawned_border',
        'current_position', 'initial_position', '_previous_y',
        '_serial_image_indexes', '_math_subfunction', 'current_image'
    )

    def __init__(self, level: Literal['easy'] | Literal['medium'] | Literal['hard']):
        self.is_killed = False
        self._level = level
        self._images = self._get_bird_images()
        self._non_spawned_border = NonSpawnedBorder(left=200, top=500, right=500, bottom=100)
        self.current_position = self._get_random_position()
        self.initial_position = BirdPosition(self.current_position.x, self.current_position.y)
        self._previous_y = self.current_position.y
        self._serial_image_indexes: dict[
            Literal['top'] | Literal['right'] | Literal['top_right'], float
        ] = {}
        self._math_subfunction = self._get_math_subfunction()
        self.current_image = self.get_current_image()

    def move(self) -> None:
        self._previous_y = self.current_position.y
        self.current_position.x += 1
        if self.is_killed:
            self._math_subfunction = self._down_function
        self.current_position.y = self._math_function(self.current_position.x)

    def get_current_image(self) -> pygame.Surface:
        if self.is_killed:
            return self._images.bottom[0]
        if self._previous_y - self.current_position.y < 0.5:
            current_image = self._get_serial_image_by_direction('right')
        elif self._previous_y - self.current_position.y == 1 and \
                self.initial_position.x - self.current_position.x == 0:
            current_image = self._get_serial_image_by_direction('top')
        else:
            current_image = self._get_serial_image_by_direction('top_right')
        self.current_image = current_image
        return current_image

    def _get_serial_image_by_direction(
            self, direction: Literal['top'] | Literal['right'] | Literal['top_right']
    ) -> pygame.Surface:
        index = self._serial_image_indexes.get(direction, 0) + 0.25
        index = index if index < len(getattr(self._images, direction)) else 0
        image = getattr(self._images, direction)[int(index)]
        self._serial_image_indexes = {direction: index}
        return image

    def _math_function(self, x: float) -> float:
        return self.initial_position.y - self._math_subfunction(x - self.initial_position.x)

    def _down_function(self, x: float) -> float:
        self.current_position.x -= 1
        return self.initial_position.y - self.current_position.y - 5

    def _up_function(self, x: float) -> float:
        self.current_position.x -= 1
        return self.initial_position.y - self.current_position.y + 1

    @staticmethod
    def _linear_function(x: float) -> float:
        return 0.5 * x

    @staticmethod
    def _root_function(x: float) -> float:
        return 15 * math.sqrt(x)

    @staticmethod
    def _in_power_function(x: float) -> float:
        return 0.002 * x ** 2

    def _get_math_subfunction(self) -> Callable[[float], float]:
        math_function_by_level = {
            LEVELS[0]: [self._up_function, self._linear_function],
            LEVELS[1]: [self._up_function, self._linear_function, self._root_function],
            LEVELS[2]: [
                self._up_function, self._linear_function,
                self._root_function, self._in_power_function
            ]
        }
        _list = math_function_by_level[self._level]
        return _list[randint(0, len(_list) - 1)]

    def _get_speed(self) -> int:
        level_speeds = {LEVELS[0]: [5], LEVELS[1]: [5, 7], LEVELS[2]: [5, 7, 9]}
        possible_speeds = level_speeds.get(self._level, [5])
        return possible_speeds[randint(0, len(possible_speeds) - 1)]

    def _get_bird_images(self) -> BirdImages:
        bird_directions = {}
        for direction in 'top', 'top_right', 'right', 'bottom':
            images = []
            for _ in range(1, 4):
                image_path = f'images/birds/{self._level}/{direction}_{_}.png'
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
        x = randint(self._non_spawned_border.left, WINDOW_WIDTH - self._non_spawned_border.right)
        y = randint(self._non_spawned_border.top, WINDOW_HEIGHT - self._non_spawned_border.bottom)
        return BirdPosition(x, y)
