from random import choice, randint


def can_breed(parent1, parent2):
    if parent1.sex != parent2.sex:
        return True
    else:
        return False


def breed_chance(parent1, parent2):
    if parent1.species == parent2.species:
        return 100
    else:
        return 50


def breed(parent1, parent2):
    if can_breed(parent1, parent2):
        print(f"These draconids have a {breed_chance(parent1, parent2)}% chance of a successful breeding")
    else:
        print("This 2 draconids can't breed together")


def baby_color(parent1, parent2):
    red_value = choice([parent1["color"][0], parent2["color"][0]])
    green_value = choice([parent1["color"][1], parent2["color"][1]])
    blue_value = choice([parent1["color"][2], parent2["color"][2]])
    adjusted_red = red_value + randint(-50, 50)
    adjusted_green = green_value + randint(-50, 50)
    adjusted_blue = blue_value + randint(-50, 50)
    color = [
        max(0, min(255, adjusted_red)),
        max(0, min(255, adjusted_green)),
        max(0, min(255, adjusted_blue))
    ]
    return color


