import pygame
from pygame.sprite import Sprite
import os

folder = os.path.dirname(os.path.realpath(__file__))

class Bullet(Sprite):
	def __init__(self, settings, screen, player):
		super(Bullet, self).__init__()
		
		self.screen = screen
		
		self.settings = settings
		
		self.player_centerx = player.centerx
		
		self.image = pygame.image.load(os.path.join(folder, "images/standard_bullet.png"))
		
		self.rect = self.image.get_rect()
		self.rect.centerx = player.centerx
		self.rect.centery = player.centery
		
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False
		
		self.player_direction = player.direction
		
		if self.player_direction == "left":
			self.img = pygame.transform.rotate(self.image, 90)
		elif self.player_direction == "right":
			self.img = pygame.transform.rotate(self.image, 270)
		elif self.player_direction == "down":
			self.img = pygame.transform.rotate(self.image, 180)
		else:
			self.img = self.image
		
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
	def update(self):
		if self.player_direction == "left":
			self.centerx -= self.settings.bullet_speed_factor
		elif self.player_direction == "right":
			self.centerx += self.settings.bullet_speed_factor
		elif self.player_direction == "up":
			self.centery -= self.settings.bullet_speed_factor
		elif self.player_direction == "down":
			self.centery += self.settings.bullet_speed_factor
		
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery	
			
	def blitme(self):
		self.screen.blit(self.img, self.rect)
