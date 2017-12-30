---

layout: post
title:  Alien War
date: 2017-12-30
tags:
	- 随笔
	- python
    - game

---

## Project Aim Introduction
I want to lenarn the Python by myself. After I read the << Python Crash course A hands-on ,Project-based Introduction to Programming >>, I want to strengthen my skill by the project.
[Click here to visit my Github repository](https://github.com/strawberrylin/AlienWar)

<!--more-->

---

## Project Background Introduction
After I read the << Python Crash course A hands-on , Project-based Introduction to Programming >>, there is a project in the book named Alien War, a 2-dimension game written with python using pygame. A suitable project that will help me to master the language, I think. 
So I spend one hour every day to write the source code in the direction of the book, wantting to master the language better and increase the experience in prgramming through the project. 

---

## Project Design Introduction
### **Function Description** :  
A space ship will stay at the bottom of the screen, only allowed to move rightwards or leftwards which is in the contorl of the payers. A group of aliens will move downwards from the top of the screen,  moving rightwards or leftwards. Players are  allowed to shot at the aliens. When bullets hit the alien, the alien will be killed and disappear from the screen. After killing all the aliens, there will come another group of aliens. Player will attain the score after every kill and level up while the alens be cleaned every time. If there is an alien hit the space or the bottom of the screen, Players will lose a space ship. Every player has three space ships. Game will over when there is no ship remains. The frequence of the aliens will increase with the level upping and the point of every kill will also increase. Players are requested to get as higher score as they can by their efforts.

### **Module**:
**alien_invasion**:The entrance of the game, call other  modules. Initialize the game and build the initial run environment of the game.
**setting**:The whole setings of the game, include ship, aliens, bullets, screen,  speed, points.
**game_function**:This module includes many functions run in the game to deal with many events. Such as keyboard down events, update events, create events, hit events, calculate events.
**alien**:This module is about the description of the alien.
**ship**:This module is about the dsescripton of the ship.
**bullet**:This module is about the description of the bullet.
**button**:This module is about the description of the button, to create a button of starting game.
**game_state**:To manage the state of the game.
**score_board**:This module will show the score atthe screen.
## Project Implement Introduction
**alien_invasion**: Import modules: settings, ship, game\_states, button, scoreboard. The entrance of the game, there is only one function named as run\_game(). Initialize the game and create the screen through pygame.  Then create the button, score_board, ship, aliens, bullets, game\_states instance. After that, there is a loop can only be ended by the exit() function. Check the keyboard down events, update the alien, ship, bullet and the screen.
***source code:***
``` python
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
        gamef.check_events(ai_settings,screen,games,score_board,play_button,ship,aliens,bullets)
        if games.game_active == 1:
            # update the locating
            ship.update()
            # update the bullets
            gamef.update_bullet(ai_settings,screen,games,score_board,ship,aliens,bullets)
            # update the aliens
            gamef.update_alien(ai_settings,games,screen,score_board,ship,aliens,bullets)
        # update the screen
        gamef.update_screen(ai_settings,screen,games,score_board,ship,aliens,bullets,play_button) 

run_game()

```

**game_function**: Define a largr of functions in the game. The function manu is as follows:
> check\_keydown_events(event,ai_settings,screen,ship,bullets):
    deal with keydown event
> check\_keyup_events(event,ship):
    deal with keyup
> check\_events(ai_settings,screen,states,score_board,play_button,ship,aliens,bullets):
    react to the mouse and keyboard
> update\_screen(ai_settings,screen,states,score_board,ship,aliens,bullets,play_button):
    update the screen
> update\_bullet(ai_settings,screen,states,score_board,ship,aliens,bullets):
    update the bullet and delete the old bullets
> update\_alien(ai_settings,states,screen,score_board,ship,aliens,bullets):
    check the site of the alien and update the site of the every alien
> get\_number\_aliens\_x(ai\_settings,alien_width):
    calculate how many a line a line can contain
> get\_number\_rows(ai\_settings,ship\_height,alien_height):
    calculate how many aliens the screen can contain
> create_alien(ai_settings,screen,aliens,alien_number,alien_rows):
    create an alien
> create_fleet(ai_settings,screen,ship,aliens):
    create the group of the aliens
> check_fleet_edges(ai_settings,aliens):
    what if the aliens hit the edges
> change_fleet_direction(ai_settings,aliens):
    change the direction of the alien
> check_collide_bullet_alien(ai_settings,screen,states,score_board,ship,aliens,bullets):
    react to the hit between aliens and bullets
> ship_hit(ai_settings,states,screen,score_board,ship,aliens,bullets):
    react to the hit between ship and aliens
> check_aliens_bottom(ai_settings,states,screen,score_board,ship,aliens,bullets):
    check if aliens arrive at the bottom of te screen
> check_play_button(ai_settings,screen,states,score_board,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    start the ame when click at the button
> check_highest_score(states, score_board):
    check if there is new score and update the score
   
 **setting**: Define the variable in the game and initialize the game, include: screen, bullet, alien, ship, speed.
**alien**:  Extends from Sprite, Initialize the alien and define the behavor of the alien: update, check edges.
**ship**:  Extends from Sprte, initialize the ship and define the behavor of the ship: update.
**bullet**: Extends fom Sprite, initialize the bullet and define the behavor of the bullet: update, draw_rect.
**button**: Define a button, render the "play" to an image and draw the button.
**game_state**: Initialize the game's state, add the reset behavor.
**score_board**: Initialize the score board,  render the score, level, highest score to an image and dislay the elft ship at he score.

----
## Project Summary
I spend one hour every dey almost half the month to write the project in the direction of the book, there are almost the whole source code in the book. I just fix some problems where I think exist some question in the logic. And I also add a start page to beauty the game. Above all, my skill in python has been promoted through the project.

