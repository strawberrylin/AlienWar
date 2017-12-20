#!/usr/bin/env python
# coding=utf-8

import pygame.font

from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """
    show the score
    """
    def __init__(self, ai_settings, screen, states):
        """
        initialize the score
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.states = states
        
        # set the font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initial score image
        self.prep_score()
        self.prep_highest_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """
        render thr score to a image
        """
        # round() function acurate the float, second format -1 make the nearest 10, 100, 1000
        rounded_score = int(round(self.states.score, -1))
        # cat string function to insert ',' in the string
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        pygame.image.save(self.score_image,'score.bmp')
        
        # lay the score at the right-top of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """
        show the score
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_highest_score(self):
        """
        render the highest score to a image
        """
        highest_score = int(round(self.states.highest_score, -1))
        highest_score_str = "{:,}".format(highest_score)
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.ai_settings.bg_color)

        # set the location at the bottom-center at the screen
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """
        render the level to a image
        """
        self.level_image = self.font.render(str(self.states.level), True, self.text_color, self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        """
        show the left ships
        """
        self.ships = Group()
        for ship_number in range(self.states.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
