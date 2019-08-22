import pygame
from pygame.sprite import Sprite

def load_image(name):
	image = pygame.image.load(name)
	return image

class ExplosionSprite(Sprite):
	def __init__(self, screen, pos):
		super().__init__()
		self.images = []
		self.images.append(load_image('images/regularExplosion00.png'))
		self.images.append(load_image('images/regularExplosion01.png'))
		self.images.append(load_image('images/regularExplosion02.png'))
		self.images.append(load_image('images/regularExplosion03.png'))
		self.images.append(load_image('images/regularExplosion04.png'))
		self.images.append(load_image('images/regularExplosion05.png'))
		self.images.append(load_image('images/regularExplosion06.png'))
		self.images.append(load_image('images/regularExplosion07.png'))
		self.images.append(load_image('images/regularExplosion08.png'))
		
		
		self.index = 0
		self.image = self.images[self.index]
		self.rect = pygame.Rect(pos.centerx - 96, pos.centery - 96, 192, 192)
		self.animation_time = 0.1
		self.current_time = 0
		self.animation_frames = 10
		self.current_frame = 0
		
	def update(self):
		
		#self.current_time += dt
		#if self.current_time >= self.animation_time:
		#	self.index += 1
		#	if self.index >= len(self.images):
		#		self.index = 0
		#	self.image = self.images[self.index]
		
		self.current_frame += 1
		if self.current_frame >= self.animation_frames:
			self.current_frame = 0
			self.index = (self.index + 1) % len(self.images)
			self.image = self.images[self.index]
	
