import pygame
from pygame.sprite import Sprite
import os
import funcs as funcs
from pygame.sprite import Group

class Player(Sprite):
	def __init__(self, settings, stats, screen, plNum, player_start_pos=pygame.Rect(0,0,97,72)):
		super(Player, self).__init__()
		
		self.screen = screen
		
		self.player_num = plNum
		
		self.start_pos = player_start_pos

		self.screen_rect = screen.get_rect()
		
		self.settings = settings
		self.stats = stats

		self.initialize_player()
		

	def initialize_player(self):
		self.health = self.settings.player_health
		self.can_take_health = True
		self.aiming_up = False
		self.weapons = self.settings.starting_weapons
		self.selected_weapon = self.settings.available_weapons[0]
		self.ammo = self.settings.starting_ammo.copy()
		self.is_alive = True
		self.arming_bomb = False
		self.arming_timer = self.settings.arming_time
		self.hq_hearts = Group()

		if self.player_num == 1:
			self.direction = "up"
			self.image = pygame.image.load(funcs.find_data_file("tank%d.png" % self.player_num))
			self.img = pygame.transform.rotate(self.image, 180)
		elif self.player_num == 2:
			self.direction = "up"
			self.image = pygame.image.load(os.path.join(funcs.find_data_file("tank%d.png" % self.player_num)))
			self.img = pygame.transform.rotate(self.image, 180)
		elif self.player_num == 3:
			self.direction = "left"
			self.image = pygame.image.load(funcs.find_data_file("tank%d.png" % self.player_num))
			self.img = pygame.transform.rotate(self.image, 270)
			
			
		self.rect = self.image.get_rect()
		
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False
		
		
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
		if self.moving_left and self.moving_up:
			self.img = pygame.transform.rotate(self.image, 225)
			#self.rect = self.img.get_rect()
			self.direction = "upleft"
		elif self.moving_left and self.moving_down:
			self.img = pygame.transform.rotate(self.image, 315)
			#self.rect = self.img.get_rect()
			self.direction = "leftdown"
		elif self.moving_right and self.moving_up:
			self.img = pygame.transform.rotate(self.image, 135)
			#self.rect = self.img.get_rect()
			self.direction = "upright"
		elif self.moving_right and self.moving_down:
			self.img = pygame.transform.rotate(self.image, 45)
			#self.rect = self.img.get_rect()
			self.direction = "rightdown"
		elif self.moving_left:
			self.img = pygame.transform.rotate(self.image, 270)
			self.rect = self.img.get_rect()
			self.direction = "left"
		elif self.moving_right:
			self.direction = "right"
			self.img = pygame.transform.rotate(self.image, 90)
			self.rect = self.img.get_rect()
		elif self.moving_up:
			self.direction = "up"
			self.img = pygame.transform.rotate(self.image, 180)
		elif self.moving_down:
			self.direction = "down"
			self.img = self.image
			self.rect = self.img.get_rect()
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.img, self.rect)
		
