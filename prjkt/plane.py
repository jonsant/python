import pygame
from pygame.sprite import Sprite
import os
import random

folder = os.path.dirname(os.path.realpath(__file__))

class Plane(Sprite):
	def __init__(self, settings, screen):
		super(Plane, self).__init__()
		
		self.screen = screen

		self.sr = screen.get_rect()
		
		self.settings = settings

		self.initialize_plane()
		

	def initialize_plane(self):
		self.health = self.settings.player_health

		self.image = pygame.image.load(os.path.join(folder, "images/plane.png"))
		
		self.moving_left = False
		self.moving_right = False
		self.moving_up = False
		self.moving_down = False

		self.xdir = 0
		self.ydir = 0
		while self.xdir == 0 and self.ydir == 0:
			self.xdir = random.randint(-1, 1)
			self.ydir = random.randint(-1, 1)

		if self.ydir == -1 and self.xdir == -1:
			self.moving_left = True
			self.moving_up = True
			self.start_pos = pygame.Rect(random.randint(self.sr.left + 30, self.sr.right), self.sr.bottom-100, 97, 201)
		elif self.ydir == -1 and self.xdir == 0:
			self.moving_up = True
			self.start_pos = pygame.Rect(random.randint(self.sr.left + 30, self.sr.right - 30), self.sr.bottom-100, 97, 201)
		elif self.ydir == -1 and self.xdir == 1:
			self.moving_right = True
			self.moving_up = True
			self.start_pos = pygame.Rect(random.randint(self.sr.left, self.sr.right - 30), self.sr.bottom-100, 97, 201)
		elif self.ydir == 1 and self.xdir == -1:
			self.moving_down = True
			self.moving_left = True
			self.start_pos = pygame.Rect(random.randint(self.sr.left + 30, self.sr.right), self.sr.top-250, 97, 201)
		elif self.ydir == 1 and self.xdir == 0:
			self.moving_down = True
			self.start_pos = pygame.Rect(random.randint(self.sr.left + 30, self.sr.right - 30), self.sr.top-250, 97, 201)
		elif self.ydir == 1 and self.xdir == 1:
			self.moving_down = True
			self.moving_right = True
			self.start_pos = pygame.Rect(random.randint(self.sr.left, self.sr.right - 30), self.sr.top-250, 97, 201)
		elif self.ydir == 0 and self.xdir == 1:
			self.moving_right = True
			self.start_pos = pygame.Rect(self.sr.left-100, random.randint(self.sr.top, self.sr.bottom), 97, 201)
		elif self.ydir == 0 and self.xdir == -1:
			self.moving_left = True
			self.start_pos = pygame.Rect(self.sr.right, random.randint(self.sr.top, self.sr.bottom-200), 97, 201)

		
		


		#self.img = pygame.transform.rotate(self.image, 90)
		
			
			
		self.rect = self.image.get_rect()
		
		
		
		
		# Start plane at random position.
		self.rect.centerx = self.start_pos.centerx
		self.rect.bottom = self.start_pos.bottom
		
		# Store a decimal value for the ship's center
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

	def update(self):
		if self.moving_up and self.moving_left:
			self.centerx -= self.settings.plane_speed_factor
			self.centery -= self.settings.plane_speed_factor
		elif self.moving_up and self.moving_right:
			self.centerx += self.settings.plane_speed_factor
			self.centery -= self.settings.plane_speed_factor
		elif self.moving_down and self.moving_left:
			self.centerx -= self.settings.plane_speed_factor
			self.centery += self.settings.plane_speed_factor
		elif self.moving_down and self.moving_right:
			self.centerx += self.settings.plane_speed_factor
			self.centery += self.settings.plane_speed_factor
		elif self.moving_left:
			#if self.rect.left > self.sr.left:
			self.centerx -= self.settings.plane_speed_factor
		elif self.moving_right:
			#if self.rect.right < self.sr.right:
			self.centerx += self.settings.plane_speed_factor
		elif self.moving_up:
			#if self.rect.top > self.sr.top:
			self.centery -= self.settings.plane_speed_factor
		elif self.moving_down:
			#if self.rect.bottom < self.sr.bottom:
			self.centery += self.settings.plane_speed_factor
				
		self.update_image()
		
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
	
	def update_image(self):
		if self.moving_left and self.moving_up:
			self.img = pygame.transform.rotate(self.image, -45)
			self.direction = "upleft"
		elif self.moving_left and self.moving_down:
			self.img = pygame.transform.rotate(self.image, 45)
			self.direction = "leftdown"
		elif self.moving_right and self.moving_up:
			self.img = pygame.transform.rotate(self.image, -45)
			self.img = pygame.transform.flip(self.img, True, False)
			self.direction = "upright"
		elif self.moving_right and self.moving_down:
			self.img = pygame.transform.rotate(self.image, 45)
			self.img = pygame.transform.flip(self.img, True, False)
			self.direction = "rightdown"
		elif self.moving_left:
			self.img = self.image
			self.direction = "left"
			self.headed_left = True
			self.headed_up = False
			self.headed_right = False
			self.headed_down = False
		elif self.moving_right:
			self.direction = "right"
			self.img = pygame.transform.flip(self.image, True, False)
			self.headed_left = False
			self.headed_up = False
			self.headed_right = True
			self.headed_down = False
		elif self.moving_up:
			self.direction = "up"
			self.headed_left = False
			self.headed_up = True
			self.headed_right = False
			self.headed_down = False
			self.img = pygame.transform.rotate(self.image, -90)
			self.img = pygame.transform.flip(self.img,True,False)
		elif self.moving_down:
			self.direction = "down"
			self.headed_left = False
			self.headed_up = False
			self.headed_right = False
			self.headed_down = True
			self.img = pygame.transform.rotate(self.image, 90)
		
	def draw_item(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.img, self.rect)
		
