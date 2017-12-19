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
        self.game_active = 0
        self.reset_states()
        # the highest score
        self.highest_score = 0


    def reset_states(self):
        """
        initialize the value
        """
        self.ships_left = self.ai_settings.ship_number
        self.score = 0
        self.level = 1


