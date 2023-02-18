import pygame


def get_bird_images(
        bird_types: tuple[str, ...], directions: tuple[str, ...]
) -> dict[str, dict[str, list[pygame.Surface]]]:
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
