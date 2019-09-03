import pygame
import funcs as funcs
from pygame.sprite import Sprite

class Wall(Sprite):
    def __init__(self, screen, settings, xpos, ypos):
        super(Wall, self).__init__()

        self.screen = screen
        self.settings = settings

        self.ruined = False

        self.image = pygame.image.load(funcs.find_data_file("wall3_5.png"))

        self.rect = self.image.get_rect()

        self.rect.centerx = xpos
        self.rect.bottom = ypos

        self.init_wall()

    def init_wall(self):
        self.health = self.settings.wall_health
        self.ruined = False
        self.image = pygame.image.load(funcs.find_data_file("wall3_5.png"))

    def explode_wall(self):
        self.health -= 1
        if self.health >= 52:
            self.image = pygame.image.load(funcs.find_data_file("wall3_4.png"))
        elif self.health >= 39:
            self.image = pygame.image.load(funcs.find_data_file("wall3_3.png"))
        elif self.health >= 26:
            self.image = pygame.image.load(funcs.find_data_file("wall3_2.png"))
        elif self.health >= 13:
            self.image = pygame.image.load(funcs.find_data_file("wall3_1.png"))
        elif self.health <= 0:
            self.image = pygame.image.load(funcs.find_data_file("ruined_wall.png"))
            self.ruined = True
            self.health = 0
        

    def blitme(self):
        self.screen.blit(self.image, self.rect)

