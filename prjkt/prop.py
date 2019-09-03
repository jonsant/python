import pygame
from pygame.sprite import Sprite
import os
import funcs as funcs

class Property(Sprite):
    def __init__(self, screen, settings, player):
        super().__init__()

        self.screen = screen
        self.settings = settings

        self.player = player

        self.init_prop()

    def init_prop(self):

        self.taken = False
        
        self.xpos = self.player.centerx
        self.ypos = self.player.centery + 70

        self.image = pygame.image.load(funcs.find_data_file("diamond.png"))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.xpos
        self.rect.centery = self.ypos

    def draw(self):
        if not self.taken:
	        self.screen.blit(self.image, self.rect)