#!/usr/bin/env python
# coding=utf-8

import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group

import game_functions as gamef

def run_game():
    # initialize the game and build a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien War")
    
    # create a ship
    ship = Ship(ai_settings,screen)
    # create a group to store the bullets
    bullets = Group()
    # create a group to store te aliens
    aliens = Group()
    gamef.create_fleet(ai_settings,screen,ship,aliens)

    # set the background
    screen.fill(ai_settings.bg_color)

    # start the main loop
    while True:
        # watch the mouse and keyboard
        gamef.check_events(ai_settings,screen,ship,bullets)
        # update the locating
        ship.update()
        # update the bullets
        gamef.update_bullet(ai_settings,screen,ship,aliens,bullets)
        # update the aliens
        gamef.update_alien(ai_settings,aliens)
        # update the screen
        gamef.update_screen(ai_settings,screen,ship,aliens,bullets) 

run_game()
