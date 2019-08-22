import pygame
from pygame.sprite import Sprite
from bullet import Bullet

class VBullet(Bullet, Sprite):
	"""A class to manage bullets fired from the ship"""
	
	def __init__(self, my_settings, screen, ship):
		"""Create a bullet object at the ship's current position."""
		super().__init__(my_settings, screen, ship)
		self.screen = screen
		
		# Create a bullet rect at (0,0) and then set correct position.
		#self.rect = pygame.Rect(0,0, my_settings.vBullet_width,
		#	my_settings.vBullet_height)
		#self.rect.centerx = ship.rect.centerx
		#self.rect.top = ship.rect.top
		
		# Load the bullet image and get its rect.
		self.image = pygame.image.load("images/svbullet.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# Store the bullet's position as a decimal value.
		self.y = float(self.rect.y)
		
		self.color = my_settings.vBullet_color
		self.speed_factor = my_settings.vBullet_speed_factor
		

