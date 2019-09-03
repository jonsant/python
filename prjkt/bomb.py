import pygame
from pygame.sprite import Sprite
import os
import funcs as funcs

class Bomb(Sprite):
    def __init__(self, screen, settings, xpos, ypos, player=None, activated=False):
        super().__init__()

        self.screen = screen
        self.settings = settings

        self.xpos = xpos
        self.ypos = ypos

        self.image = pygame.image.load(funcs.find_data_file("bomb.png"))

        self.rect = self.image.get_rect()
        self.rect.centerx = xpos
        self.rect.centery = ypos

        self.activated = activated

        if self.activated:
            self.my_creator = player
            self.timer = settings.bomb_time_to_explode

    def draw_item(self):
	    self.screen.blit(self.image, self.rect)