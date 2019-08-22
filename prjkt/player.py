import pygame
from pygame.sprite import Sprite

class Player(Sprite):
	def __init__(self, settings, screen):
		super(Player, self).__init__()
		
		self.screen = screen
		
		self.image = pygame.image.load("images/tank1.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.moving_left = False
		self.moving_right = False
		
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# Store a decimal value for the ship's center
		self.center = float(self.rect.centerx)
		
	def update(self):
		
		if self.moving_left and self.rect.right < self.screen_rect.right:
			self.center += self.settings.player_speed
		if self.moving_right and self.rect.right < self.screen_rect.left:
			self.center += self.settings.player_speed
		
		self.rect.centerx = self.center
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
		
