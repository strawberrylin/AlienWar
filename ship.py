#!/usr/bin/env python
# coding=utf-8

import pygame

class Ship():
    
    def __init__(self,ai_settings,screen):
        """
        initialize the ship and set the location
        """
        self.ai_settings = ai_settings
        self.screen = screen

        # load the ship image 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # locate the ship at the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store the float number
        self.center = float(self.rect.centerx)

        # set the label with moving
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """
        test the label and set the location
        """
        if self.moving_right == True :
            self.center += self.ai_settings.ship_speed_factor
            if self.center >= self.screen_rect.right - 20.0:
                self.center = self.screen_rect.right - 20.0
        if self.moving_left ==True:
            self.center -= self.ai_settings.ship_speed_factor
            if self.center <= self.screen_rect.left + 20.0:
                self.center = self.screen_rect.left + 20.0
        
        # update the location
        self.rect.centerx = self.center

    def blitme(self):
        """
        draw the ship at the sit
        """
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """
        set the ship at the center-bottom of the screen
        """
        self.center = self.screen_rect.centerx
