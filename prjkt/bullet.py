import pygame
from pygame.sprite import Sprite
import os
import funcs as funcs

class Bullet(Sprite):
	def __init__(self, settings, screen, player):
		super(Bullet, self).__init__()
		
		self.screen = screen
		
		self.settings = settings
		
		self.my_creator = player
		self.player_centerx = player.centerx

		if self.my_creator.aiming_up:
			funcs.play_sound("missile.wav")
		else:
			funcs.play_sound("shoot.wav")
		
		self.image = pygame.image.load(funcs.find_data_file("standard_bullet.png"))
		
		self.rect = self.image.get_rect()
		
		
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False
		
		self.player_direction = player.direction

		self.rect.centerx = player.centerx
		self.rect.centery = player.centery
		
		if self.player_direction == "upleft":
			self.img = pygame.transform.rotate(self.image, 225)
		elif self.player_direction == "leftdown":
			self.img = pygame.transform.rotate(self.image, 315)
			self.rect.centerx += 25
		elif self.player_direction == "upright":
			self.img = pygame.transform.rotate(self.image, 135)
			self.rect.centerx += 10
			self.rect.centery += 20
		elif self.player_direction == "rightdown":
			self.img = pygame.transform.rotate(self.image, 45)
		elif self.player_direction == "left":
			self.img = pygame.transform.rotate(self.image, 270)
		elif self.player_direction == "right":
			self.img = pygame.transform.rotate(self.image, 90)
		elif self.player_direction == "up":
			self.img = pygame.transform.rotate(self.image, 180)
		else:
			self.img = self.image
		
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
	def update(self):
		if self.player_direction == "upleft":
			self.centerx -= self.settings.bullet_speed_factor
			self.centery -= self.settings.bullet_speed_factor
		elif self.player_direction == "upright":
			self.centerx += self.settings.bullet_speed_factor
			self.centery -= self.settings.bullet_speed_factor
		elif self.player_direction == "rightdown":
			self.centerx += self.settings.bullet_speed_factor
			self.centery += self.settings.bullet_speed_factor
		elif self.player_direction == "leftdown":
			self.centerx -= self.settings.bullet_speed_factor
			self.centery += self.settings.bullet_speed_factor
		elif self.player_direction == "left":
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
