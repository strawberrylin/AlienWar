#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    class for alien
    """
    def __init__(self,ai_settings,screen):
        """
        initialize the alien ane the setting
        """
        super(Alien,self).__init__()
        self.screen = screen
        self.settings = ai_settings

        # load the alien and set the rect 
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # the first location of the alien is at left-top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the acurate location of the alien
        self.x = float(self.rect.x)

    def blitme(self):
        """
        draw the alien at the setted site
        """
        self.screen.blit(self.image,self.rect)

    def update(self):
        """
        move the alien towards right or left
        """
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """
        check if alien hit the edge of the screen
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

