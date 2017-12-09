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
