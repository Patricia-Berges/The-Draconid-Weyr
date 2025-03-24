import pygame
from game_logic.ui import Button
from game_logic.sprite_generation import render_sprite, randomize_dragon_colors
from game_logic.draconid_generator import gen_draconid
import game_logic.screen_manager as screen_manager

sprite = render_sprite()


def new_draconid():
    draconid = gen_draconid()
    print(f"Generated draconid: {draconid.name}, {draconid.species}, {draconid.sex}, {draconid.age}")


def update_sprite(new_sprite):
    global sprite
    sprite = new_sprite


def gen_main_screen(screen):
    global sprite
    # ---- Variables ----
    GRAY = (100, 100, 100)
    DARK_GRAY = (50, 50, 50)
    BLACK = (0, 0, 0)

    def handle_randomize_dragon():
        new_sprite = randomize_dragon_colors()  # Randomize and update sprite
        update_sprite(new_sprite)

    def go_to_list_screen():
        from screens.draco_list_screen import gen_draco_list_screen  # ⚠️ Delayed import to avoid circular import
        screen_manager.screen_generator = gen_draco_list_screen

    # ---- Buttons ----
    buttons_main = [
        Button(250, 250, 350, 50, "Generate Draconid", GRAY, DARK_GRAY, lambda: new_draconid()),
        Button(250, 350, 350, 50, "Print all names", GRAY, DARK_GRAY, lambda: go_to_list_screen()),
        Button(250, 450, 350, 50, "Delete all", GRAY, DARK_GRAY, lambda: delete_all()),
        Button(250, 150, 350, 50, "Randomize Dragon", GRAY, DARK_GRAY, handle_randomize_dragon)
    ]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        for button in buttons_main:
            button.handle_event(event)

    screen.fill(BLACK)
    screen.blit(sprite, (100, 100))  # Draw the sprite
    for button in buttons_main:
        button.draw(screen)
