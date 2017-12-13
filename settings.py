#!/usr/bin/env python
# coding=utf-8

class Settings():
    """
    store the all class of the game
    """
    def __init__(self):
        """
        initialize the settings of the game
        """
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

        # bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
 
        # alien setting
        self.alien_speed_factor = 1
        # after knocking at the edge of the screen,drop down
        self.fleet_drop_speed = 10
        # 1:right,-1:left
        self.fleet_direction = 1
