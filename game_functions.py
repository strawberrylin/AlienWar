#!/usr/bin/env python
# coding=utf-8

import sys
import pygame

from bullet import Bullet
from alien import Alien
from time import sleep

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

def check_events(ai_settings,screen,states,score_board,play_button,ship,aliens,bullets):
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, states, score_board, play_button, ship, aliens,bullets,  mouse_x, mouse_y)

def update_screen(ai_settings,screen,states,score_board,ship,aliens,bullets,play_button):
    # overdraw the screen
    screen.fill(ai_settings.bg_color)
    # overdraw all the bullets
    # sprite() return a list
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # if game is not started, draw the play_button
    if states.game_active == 0:
        play_button.draw_button()
    elif states.game_active == 1:
        # overdraw the screen
        screen.fill(ai_settings.bg_color)
        # overdraw all the bullets
        # sprite() return a list
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        # show the score 
        score_board.show_score()
    elif states.game_active == -1:
        sys.exit()

    # enable recent draw
    pygame.display.flip()

def update_bullet(ai_settings,screen,states,score_board,ship,aliens,bullets):
    """
    update the bullet and delete the old bullets
    """
    # update the bullets
    bullets.update()
    # delete the bullet outside the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 
    # Check if bullet hit the alien.If then,delete the bullet and alien.
    # group.sprite.collide() return a dictionary <bullet,alien>
    # compare the bullet's rect with alien's rect,if equal,delete the alien.
    
    check_collide_bullet_alien(ai_settings,screen,states,score_board,ship,aliens,bullets)

def update_alien(ai_settings,states,screen,score_board,ship,aliens,bullets):
    """
    check the site of the alien and update the site of the every alien
    """
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    # check the hit between aliens and ship
    # sprite.spritecollideany() return bool value if hit
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,states,screen,score_board,ship,aliens,bullets)

    # check if aliens arrive at the bottom of the screen
    check_aliens_bottom(ai_settings,states,screen,score_board,ship,aliens,bullets)

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

def check_collide_bullet_alien(ai_settings,screen,states,score_board,ship,aliens,bullets):
    """
    react to the hit between aliens and bullets
    """
    # delete the bullets and aliens if they hit
    collide_alien_bullet = pygame.sprite.groupcollide(bullets,aliens,True,True)

    # if hit, add the score
    if collide_alien_bullet :
        for aliens in collide_alien_bullet.values():
            states.score += ai_settings.alien_points * len(aliens)
            score_board.prep_score()
        check_highest_score(states, score_board)
    # check the list of the aliens and create a new group of aliens
    if len(aliens) == 0 :
        bullets.empty()
        ai_settings.speedup_game()

        # level up
        states.level += 1
        score_board.prep_level()

        # create a group of aliens
        create_fleet(ai_settings,screen,ship,aliens)

def ship_hit(ai_settings,states,screen,score_board,ship,aliens,bullets):
    """
    react to the hit between ship and aliens
    """
    if states.ships_left > 0:
        # ship_left -1
        states.ships_left -= 1
        states.score = 0
        states.level = 1
        ai_settings.initialize_dynamic_settings()

        # update the score_board 
        score_board.prep_ship()
        score_board.prep_score()
        score_board.prep_level()
        
        # empty the bullets and aliens list
        aliens.empty()
        bullets.empty()
        
        # create new group of aliens and set the ship at the center-bottom of the screen
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
        # pause
        sleep(0.5)
    else:
        states.game_active = -1
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,states,screen,score_board,ship,aliens,bullets):
    """
    check if aliens arrive at the bottom of te screen
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
        # deal like the ship hit
            ship_hit(ai_settings,states,screen,score_board,ship,aliens,bullets)
            break

def check_play_button(ai_settings,screen,states,score_board,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """
    start the ame when click at the button
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and states.game_active == 0:
        # initialize the settings
        ai_settings.initialize_dynamic_settings()
        # make mouse invisible
        pygame.mouse.set_visible(False)
        # reset the information
        states.reset_states()
        states.game_active = 1
        
        # reset the score board and level
        score_board.prep_score()
        score_board.prep_highest_score()
        score_board.prep_level()

        # empty the bullets and aliens list
        aliens.empty()
        bullets.empty()

        # create a new group of aliens
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def check_highest_score(states, score_board):
    """
    check if there is new score and update the score
    """
    if states.score > states.highest_score:
        states.highest_score = states.score
        score_board.prep_highest_score()


