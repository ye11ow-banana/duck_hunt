import pygame

from data_structures import BirdImages, NonSpawnedBorder, BirdPosition


class Bird:
    def __init__(self, level):
        self.is_killed = False
        self.level = level
        self.speed = self._get_speed()
        self.images = self._get_bird_images()
        self.non_spawned_border = NonSpawnedBorder(left=100, top=500, right=200, bottom=50)
        self.position = self._get_random_position()
        self._move()

    def _move(self) -> None:
        return

    def _get_speed(self) -> None:
        return

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

    def _get_random_position(self) -> None:
        return
