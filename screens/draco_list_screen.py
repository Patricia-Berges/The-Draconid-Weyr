import pygame
from game_logic.ui import Button
import game_logic.screen_manager as screen_manager
from data.db_handler import fetch_all_draconids


GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def gen_draco_list_screen(screen):
    def go_to_main_screen():
        from screens.main_screen import gen_main_screen
        screen_manager.screen_generator = gen_main_screen

    draconid_list = fetch_all_draconids()

    buttons = [
        Button(250, 500, 300, 50, "Back", GRAY, DARK_GRAY, lambda: go_to_main_screen()),
    ]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        for button in buttons:
            button.handle_event(event)

    screen.fill(BLACK)  # First the functions, then paint the screen, then add the elements to it!!

    font = pygame.font.Font(None, 36)
    y_offset = 50
    for draconid in draconid_list:
        text_surface = font.render(f"{draconid['name']} ({draconid['species']})", True, WHITE)
        screen.blit(text_surface, (50, y_offset))
        y_offset += 40

    for button in buttons:
        button.draw(screen)
