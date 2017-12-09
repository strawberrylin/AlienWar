#!/usr/bin/env python
# coding=utf-8

import sys
import pygame

def check_keydown_events(event,ship):
    """
    deal with keydown event
    """
    if event.key == pygame.K_RIGHT:
        # move right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # move left
        ship.moving_left = True

def check_keyup_events(event,ship):
    """
    deal with keyup
    """
    if event.key == pygame.K_RIGHT:
        # stop move right
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # stop move left
        ship.moving_left = False

def check_events(ship):
    """
    react to the mouse and keyboard
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship):
    # overdraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # enable recent draw
    pygame.display.flip()

