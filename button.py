#!/usr/bin/env python
# coding=utf-8

import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
        """
        initialize the button
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.start_image = pygame.image.load('images/start.bmp')


        # set the size and other factor
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # set the default font and size 48
        self.font = pygame.font.SysFont(None, 48)

        # create the rect intence 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.bottom += 185

        # render the text as image
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """
        render the text as image and set at center
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        draw the button at the screen
        """
        self.screen.blit(self.start_image,self.screen_rect)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
