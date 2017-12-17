#!/usr/bin/env python
# coding=utf-8

import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_states import Game_states
from button import Button
from scoreboard import Scoreboard

import game_functions as gamef

def run_game():
    # initialize the game and build a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien War")

    # create a button
    play_button = Button(ai_settings, screen, "Play")
    
    # create a intence of Game_states
    games = Game_states(ai_settings)

    # create the score board
    score_board = Scoreboard(ai_settings, screen, games)

    # set the background
    screen.fill(ai_settings.bg_color)

    # create a ship
    ship = Ship(ai_settings,screen)

    # create a group to store the bullets
    bullets = Group()

    # create a group to store te aliens
    aliens = Group()

    if games.game_active == 1:
        gamef.create_fleet(ai_settings,screen,ship,aliens)

    # start the main loop
    while True:
        # watch the mouse and keyboard
        gamef.check_events(ai_settings,screen,games,play_button,ship,aliens,bullets)
        if games.game_active == 1:
            # update the locating
            ship.update()
            # update the bullets
            gamef.update_bullet(ai_settings,screen,ship,aliens,bullets)
            # update the aliens
            gamef.update_alien(ai_settings,games,screen,ship,aliens,bullets)
        # update the screen
        gamef.update_screen(ai_settings,screen,games,score_board,ship,aliens,bullets,play_button) 

run_game()

