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
		self.rect = pygame.Rect(5, 5, 60, 60)
		
	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]
