import pygame
from pygame.sprite import Sprite
import funcs as funcs

def load_image(name):
	image = pygame.image.load(funcs.find_data_file(name))
	return image

class ExplosionSprite(Sprite):
	def __init__(self, screen, pos, expl_type="plane"):
		super().__init__()

		self.expl_type = expl_type

		self.images = []

		if self.expl_type == "plane":
			self.images.append(load_image('regularExplosion00.png'))
			self.images.append(load_image('regularExplosion01.png'))
			self.images.append(load_image('regularExplosion02.png'))
			self.images.append(load_image('regularExplosion03.png'))
			self.images.append(load_image('regularExplosion04.png'))
			self.images.append(load_image('regularExplosion05.png'))
			self.images.append(load_image('regularExplosion06.png'))
			self.images.append(load_image('regularExplosion07.png'))
			self.images.append(load_image('regularExplosion08.png'))

			self.rect = pygame.Rect(pos.centerx - 92, pos.centery - 92, 192, 192)
		else:
			pic0 = load_image('regularExplosion00.png')
			pic0 = pygame.transform.scale(pic0, (300, 300))
			self.images.append(pic0)

			pic1 = load_image('regularExplosion01.png')
			pic1 = pygame.transform.scale(pic1, (300, 300))
			self.images.append(pic1)

			pic2 = load_image('regularExplosion02.png')
			pic2 = pygame.transform.scale(pic2, (300, 300))
			self.images.append(pic2)

			pic3 = load_image('regularExplosion03.png')
			pic3 = pygame.transform.scale(pic3, (300, 300))
			self.images.append(pic3)

			pic4 = load_image('regularExplosion04.png')
			pic4 = pygame.transform.scale(pic4, (300, 300))
			self.images.append(pic4)

			pic5 = load_image('regularExplosion05.png')
			pic5 = pygame.transform.scale(pic5, (300, 300))
			self.images.append(pic5)

			pic6 = load_image('regularExplosion06.png')
			pic6 = pygame.transform.scale(pic6, (300, 300))
			self.images.append(pic6)

			pic7 = load_image('regularExplosion07.png')
			pic7 = pygame.transform.scale(pic7, (300, 300))
			self.images.append(pic7)

			pic8 = load_image('regularExplosion08.png')
			pic8 = pygame.transform.scale(pic8, (300, 300))
			self.images.append(pic8)

			self.rect = pygame.Rect(pos.centerx-150, pos.centery - 150, 300, 300)
		
		
		self.index = 0
		self.image = self.images[self.index]
		
		self.animation_time = 0.1
		self.current_time = 0
		self.animation_frames = 10
		self.current_frame = 0
		
	def update(self, dt):
		
		self.current_time += dt
		if self.current_time >= self.animation_time:
			self.index += 1
			if self.index >= len(self.images):
				self.index = 0
			self.image = self.images[self.index]
		
		""" self.current_frame += 1
		if self.current_frame >= self.animation_frames:
			self.current_frame = 0
			self.index = (self.index + 1) % len(self.images)
			self.image = self.images[self.index] """
	
