#!/usr/bin/env python
# coding=utf-8

import sys
import pygame

from bullet import Bullet
from alien import Alien

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
    elif event.key == pygame.K_q:
        sys.exit()
    
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

def update_screen(ai_settings,screen,ship,aliens,bullets):
    # overdraw the screen
    screen.fill(ai_settings.bg_color)
    # overdraw all teh bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

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

def update_alien(ai_settings,aliens):
    """
    check the site of the alien and update the site of the every alien
    """
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def get_number_aliens_x(ai_settings,alien_width):
    """
    calculate how many a line a line can contain
    """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x
    
def get_number_rows(ai_settings,ship_height,alien_height):
    """
    calculate how many aliens the screen can contain
    """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) -ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,alien_rows):
    """
    create an alien
    """
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * alien_rows
    aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
    """
    create the group of the aliens
    """
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    
    # create the group of alien
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def check_fleet_edges(ai_settings,aliens):
    """
    what if the aliens hit the edges
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens) 
            break

def change_fleet_direction(ai_settings,aliens):
    """
    change the direction of the alien
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

