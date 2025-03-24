import pygame
import random


# Load all the parts of the sprite
lineart = pygame.image.load("sprites/dragon_lineart.png")
base_color = pygame.image.load("sprites/dragon_base_color.png")
skin = pygame.image.load("sprites/dragon_skin.png")
horns = pygame.image.load("sprites/dragon_horns.png")
stripes = pygame.image.load("sprites/dragon_stripes.png")


def render_sprite():
    sprite = pygame.Surface(lineart.get_size(), pygame.SRCALPHA)
    sprite.blit(base_color, (0, 0))
    sprite.blit(skin, (0, 0))
    sprite.blit(horns, (0, 0))
    sprite.blit(stripes, (0, 0))
    sprite.blit(lineart, (0, 0))
    return sprite


final_sprite = render_sprite()


def change_color(image, red, green, blue):
    """Randomizes the base color of the image by changing its RGB values."""
    image = image.copy()  # Create a copy to avoid modifying the original
    width, height = image.get_size()

    # Generate random RGB values for the new base color
    new_color = pygame.Color(red, green, blue)

    for x in range(width):
        for y in range(height):
            current_color = image.get_at((x, y))  # Get the pixel color

            if current_color[3] > 0:  # Ignore transparent pixels
                # Change the color of non-transparent pixels to the new random color
                image.set_at((x, y), new_color)

    return image


def random_color_value():
    return random.randint(0, 255)


def randomize_all_parts(line, base, skin_color, horn_color, marking):
    """Randomize the colors of each part."""
    # Randomize each part
    randomized_base = change_color(base, random_color_value(), random_color_value(), random_color_value())
    randomized_skin = change_color(skin_color, random_color_value(), random_color_value(), random_color_value())
    randomized_stripes = change_color(marking, random_color_value(), random_color_value(), random_color_value())

    # Re-render the dragon sprite with the randomized parts
    new_sprite = pygame.Surface(line.get_size(), pygame.SRCALPHA)

    # Combine each part with the lineart
    new_sprite.blit(randomized_base, (0, 0))
    new_sprite.blit(randomized_skin, (0, 0))
    new_sprite.blit(horn_color, (0, 0))
    new_sprite.blit(randomized_stripes, (0, 0))
    new_sprite.blit(line, (0, 0))

    return new_sprite


def randomize_dragon_colors():
    sprite = randomize_all_parts(lineart, base_color, skin, horns, stripes)
    print("Dragon parts have been randomized!")
    return sprite
