from dataclasses import dataclass

import pygame


@dataclass
class BirdImages:
    """
    Class to storing images of a bird in
    different directions for moving it.
    """
    top: list[pygame.Surface]
    top_right: list[pygame.Surface]
    right: list[pygame.Surface]
    bottom: list[pygame.Surface]


@dataclass
class NonSpawnedBorder:
    """
    Class to limit bird spawn space.

    E.g. left is the non spawn length
    from left border of the window.
    """
    left: int
    top: int
    right: int
    bottom: int


@dataclass
class BirdPosition:
    """
    Class to limit bird spawn space.

    E.g. left is the non spawn length
    from left border of the window.
    """
    x: int
    y: int
