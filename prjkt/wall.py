import pygame
import funcs as funcs
from pygame.sprite import Sprite

class Wall(Sprite):
    def __init__(self, screen, settings, xpos, ypos):
        super(Wall, self).__init__()

        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load(funcs.find_data_file("wall3.png"))

        self.rect = self.image.get_rect()

        self.rect.centerx = xpos
        self.rect.centery = ypos

    def blitme(self):
        self.screen.blit(self.image, self.rect)

