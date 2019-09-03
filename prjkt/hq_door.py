import pygame
from pygame.sprite import Sprite
import os
import funcs as funcs

class HQ_door(Sprite):
    def __init__(self, settings, screen, player, stats, xpos, ypos, wall):
        super(HQ_door, self).__init__()

        self.screen = screen
        self.stats = stats
        self.settings = settings
        self.player = player
        self.xpos = xpos
        self.ypos = ypos

        self.wall = wall

        self.init_door()

    def init_door(self):
        self.is_opening = False
        self.is_closing = False
        self.is_open = False
        self.is_closed = True
        self.ruined = False
        self.health = self.settings.door_health

        self.image = pygame.image.load(funcs.find_data_file("door.png"))
        self.rect = self.image.get_rect()

        self.rect.left = self.xpos
        self.rect.top = self.ypos

        self.door_trigger_rect = self.rect.copy()
        self.door_trigger_image = pygame.image.load(funcs.find_data_file("wall_trigger.png"))

    def open(self):
        self.is_opening = True
        self.is_closing = False
        self.is_open = False
        self.is_closed = True

    def close(self):
        self.is_opening = False
        self.is_closing = True
        self.is_open = False
        self.is_closed = False

    def explode_door(self):
        self.health -= 1
        if self.health >= 52:
            self.image = pygame.image.load(funcs.find_data_file("door_4.png"))
        elif self.health >= 39:
            self.image = pygame.image.load(funcs.find_data_file("door_3.png"))
        elif self.health >= 26:
            self.image = pygame.image.load(funcs.find_data_file("door_2.png"))
        elif self.health >= 13:
            self.image = pygame.image.load(funcs.find_data_file("door_1.png"))
        elif self.health <= 0:
            self.image = pygame.image.load(funcs.find_data_file("ruined_door.png"))
            self.ruined = True
            self.health = 0

    def destroy_door(self):
        self.ruined = True
        self.image = pygame.image.load(funcs.find_data_file("ruined_door.png"))
        self.rect.left = self.xpos
        self.rect.top = self.ypos


    def update(self):
        if self.player.player_num == 1:
            if self.is_opening:
                if self.rect.right >= self.screen.get_rect().left:
                    self.is_closed = False
                    self.is_open = False
                    self.rect.left -= self.settings.door_speed
                elif self.rect.right <= 0:
                    self.is_opening = False
                    self.is_open = True
                    
            elif self.is_closing:
                if not self.rect.right >= self.wall.rect.left:
                    self.rect.left += self.settings.door_speed
                    self.is_closed = False
                    self.is_open = False
                else:
                    self.is_closing = False
                    self.is_closed = True
        elif self.player.player_num == 2:
            if self.is_opening:
                if self.rect.left <= self.screen.get_rect().right:
                    self.is_closed = False
                    self.is_open = False
                    self.rect.left += self.settings.door_speed
                elif self.rect.left >= self.screen.get_rect().right:
                    self.is_opening = False
                    self.is_open = True
            elif self.is_closing:
                if self.rect.right > self.screen.get_rect().right:
                    self.is_closed = False
                    self.is_open = False
                    self.rect.left -= self.settings.door_speed
                elif self.rect.right <= self.screen.get_rect().right:
                    self.is_opening = False
                    self.is_open = False
                    self.is_closed = True
                    self.is_closing = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        #pygame.draw.rect(self.screen, (0,0,0), self.door_trigger_rect)
        self.screen.blit(self.door_trigger_image, self.door_trigger_rect)
