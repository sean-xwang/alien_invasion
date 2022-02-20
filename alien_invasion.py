import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initiate a game and generate an object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Generate a ship
    ship = Ship(ai_settings,screen)
    # Generate a group to store all bullets
    bullets = Group()

    # set background color
    bg_color = (230,230,230)

    # Start main game loop
    while True:

        # Monitor mouse and keyboard
        gf.check_events(ai_settings, screen, ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship,bullets)

run_game()