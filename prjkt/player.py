import pygame
from pygame.sprite import Sprite

class Player(Sprite):
	def __init__(self, settings, screen, plNum, player_start_pos=pygame.Rect(0,0,97,72)):
		super(Player, self).__init__()
		
		self.screen = screen
		
		self.player_num = plNum
		
		self.start_pos = player_start_pos
		
		self.health = 100
		
		
		if self.player_num == 1:
			self.direction = "right"
			self.image = pygame.image.load("images/tank%d.png" % self.player_num)
			self.img = pygame.transform.rotate(self.image, 90)
		else:
			self.direction = "left"
			self.image = pygame.image.load("images/tank%d.png" % self.player_num)
			self.img = pygame.transform.rotate(self.image, 270)
			
			
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False
		
		self.settings = settings
		
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.start_pos.centerx
		self.rect.bottom = self.start_pos.bottom
		
		# Store a decimal value for the ship's center
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
	def update(self):
		
		if self.moving_left:
			if self.rect.left > self.screen_rect.left:
				self.centerx -= self.settings.player_speed
		if self.moving_right:
			if self.rect.right < self.screen_rect.right:
				self.centerx += self.settings.player_speed
		if self.moving_up:
			if self.rect.top > self.screen_rect.top:
				self.centery -= self.settings.player_speed
		if self.moving_down:
			if self.rect.bottom < self.screen_rect.bottom:
				self.centery += self.settings.player_speed
				
		self.update_image()
		
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
	
	def update_image(self):
		if self.moving_left:
			self.headed_left = True
			self.headed_up = False
			self.headed_right = False
			self.headed_down = False
			self.img = pygame.transform.rotate(self.image, 270)
		elif self.moving_right:
			self.headed_left = False
			self.headed_up = False
			self.headed_right = True
			self.headed_down = False
			self.img = pygame.transform.rotate(self.image, 90)
		elif self.moving_up:
			self.headed_left = False
			self.headed_up = True
			self.headed_right = False
			self.headed_down = False
			self.img = pygame.transform.rotate(self.image, 180)
		elif self.moving_down:
			self.headed_left = False
			self.headed_up = False
			self.headed_right = False
			self.headed_down = True
			self.img = self.image
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.img, self.rect)
		
