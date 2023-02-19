import pygame


class Bird:
    def __init__(self, level):
        self.is_killed = False
        self.level = level
        self.speed = None
        self.images = None
        self.non_spawned_border = None
        self.position = None

    def _get_bird_images(self, bird_types, directions):
        bird_images = {}
        for bird_type in bird_types:
            bird_directions = {}
            for direction in directions:
                images = []
                for _ in range(1, 4):
                    image_path = f'images/birds/{bird_type}/{direction}_{_}.png'
                    try:
                        images.append(pygame.image.load(image_path))
                    except FileNotFoundError:
                        pass
                bird_directions[direction] = images
            bird_images[bird_type] = bird_directions
        return bird_images
