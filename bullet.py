#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    a class to manage the bullet
    """
    def __init__(self,ai_settings,screen,ship):
        """
        create a Bullet intence at the ship
        """
        super(Bullet,self).__init__()
        self.screen = screen

        # create a rect of bullet and set the correct location
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the site of the bullet
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """
        upward the bullet
        """
        # updae the nunber on behalf of the site
        self.y -= self.speed_factor
        # update the rect 
        self.rect.y = self.y

    def draw_bullet(self):
        """
        draw the bullet at the screen
        """
        pygame.draw.rect(self.screen,self.color,self.rect)
