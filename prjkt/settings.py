import pygame

class Settings():
	def __init__(self):
		
		# Screen settings
		self.screen_width = 1280
		self.screen_height = 720
		self.bg_color = (0,0,0)
		
		self.bg = pygame.image.load("images/bg.jpg")
		
		self.player_speed = 1
