import pygame
from pygame.sprite import Sprite

class Player(Sprite):
	def __init__(self, settings, screen, plNum):
		super(Player, self).__init__()
		
		self.screen = screen
		
		self.player_num = plNum
		
		self.image = pygame.image.load("images/tank%d_right.png" % self.player_num)
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False
		
		
		
		self.settings = settings
		
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		# Store a decimal value for the ship's center
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
	def update(self, dt=1):
		
		if self.moving_left:
			self.image = pygame.image.load("images/tank%d_left.png" % self.player_num)
			if self.rect.left > self.screen_rect.left:
				self.centerx -= self.settings.player_speed * dt
		if self.moving_right:
			self.image = pygame.image.load("images/tank1_right.png")
			if self.rect.right < self.screen_rect.right:
				self.centerx += self.settings.player_speed * dt
		if self.moving_up:
			self.image = pygame.image.load("images/tank1_up.png")
			if self.rect.top > self.screen_rect.top:
				self.centery -= self.settings.player_speed * dt
		if self.moving_down:
			self.image = pygame.image.load("images/tank1_down.png")
			if self.rect.bottom < self.screen_rect.bottom:
				self.centery += self.settings.player_speed * dt
		
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)
		
