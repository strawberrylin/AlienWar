#!/usr/bin/env python
# coding=utf-8

import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gamef

def run_game():
    # initialize the game and build a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien War")
    
    # make a ship
    ship = Ship(ai_settings,screen)

    # set the background
    screen.fill(ai_settings.bg_color)

    # start the loop
    while True:
        # watch the mouse and keyboard
        gamef.check_events(ship)
        # update the locating
        ship.update()
        # update the screen
        gamef.update_screen(ai_settings,screen,ship) 

run_game()
