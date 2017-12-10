#!/usr/bin/env python
# coding=utf-8

import sys
import pygame

from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """
    deal with keydown event
    """
    if event.key == pygame.K_RIGHT:
        # move right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # create a bulet and add it to the group
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """
    deal with keyup
    """
    if event.key == pygame.K_RIGHT:
        # stop move right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # stop move left
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """
    react to the mouse and keyboard
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    # overdraw the screen
    screen.fill(ai_settings.bg_color)
    # overdraw all teh bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # enable recent draw
    pygame.display.flip()

def update_bullet(bullets):
    """
    update the bullet and delete the old bullets
    """
    # update the bullets
    bullets.update()
    # delete the bullet outside the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 
