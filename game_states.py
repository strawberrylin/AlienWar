#!/usr/bin/env python
# coding=utf-8

class Game_states():
    """
    trace the game and count the information
    """
    def __init__(self,ai_settings):
        """
        initialize the value
        """
        self.ai_settings = ai_settings
        self.game_active = True
        self.reset_states()

    def reset_states(self):
        """
        initialize the value
        """
        self.ships_left = self.ai_settings.ship_number
