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

        # ship setting
        self.ship_number = 2

        # the factor to speed up the game
        self.speedup_scale = 1.2

        # the factor to add the point of aliens
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        initialize the game speed
        """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.2
        self.alien_speed_factor = 1

        # right: 1 left: -1
        self.fleet_direction = 1

        # score
        self.alien_points = 50

    def speedup_game(self):
        """
        speedup
        """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale 
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

