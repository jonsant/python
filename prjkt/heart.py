import pygame
from pygame.sprite import Sprite
import os
import random

folder = os.path.dirname(os.path.realpath(__file__))

class Heart(Sprite):
    def __init__(self, screen, settings):
        super().__init__()

        self.screen = screen
        self.settings = settings

        xpos = random.randint(screen.get_rect().left + 10, screen.get_rect().right - 10)
        ypos = random.randint(screen.get_rect().top + 10, screen.get_rect().bottom - 10)

        self.image = pygame.image.load(os.path.join(folder, "images/heart.png"))

        self.rect = self.image.get_rect()
        self.rect.centerx = xpos
        self.rect.centery = ypos

    def draw_heart(self):
	    self.screen.blit(self.image, self.rect)