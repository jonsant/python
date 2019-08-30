import pygame
from pygame.sprite import Sprite
import os
import random

folder = os.path.dirname(os.path.realpath(__file__))

class Commie(Sprite):
    def __init__(self, screen, settings, xpos, ypos):
        super().__init__()

        self.screen = screen
        self.settings = settings

        self.xpos = xpos
        self.ypos = ypos

        #xpos = random.randint(screen.get_rect().left + 10, screen.get_rect().right - 10)
        #ypos = random.randint(screen.get_rect().top + 10, screen.get_rect().bottom - 10)

        self.image = pygame.image.load(os.path.join(folder, "images/commie.png"))

        self.rect = self.image.get_rect()
        self.rect.centerx = xpos
        self.rect.centery = ypos

    def draw_item(self):
	    self.screen.blit(self.image, self.rect)