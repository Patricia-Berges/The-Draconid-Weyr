from data.db_handler import create_db, fetch_all_draconids_names, delete_all_draconids, fetch_all_draconids
import pygame
from screens.main_screen import gen_main_screen
from game_logic.ui import Button
import game_logic.screen_manager as screen_manager

# Initialize database and pygame
create_db()
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
WHITE = (255, 255, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draconid Game")


# ---- State Management ----
draconid_list = []


# ---- Functions ----
def delete_all():
    delete_all_draconids()
    print("Deleted all draconids")


# ---- Main Loop ----
running = True
screen_manager.screen_generator = gen_main_screen

while running:
    screen.fill(BLACK)

    if screen_manager.screen_generator:
        screen_manager.screen_generator(screen)

    pygame.display.flip()

pygame.quit()
