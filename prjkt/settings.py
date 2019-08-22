import pygame

class Settings():
	def __init__(self):
		
		# Screen settings
		self.screen_width = 1280
		self.screen_height = 720
		self.bg_color = (0,0,0)
		
		self.bg = pygame.image.load("images/bg.jpg")
		
		# Player settings
		
			# Both
		self.player_speed = 5
		
			# Player1
		self.player1_start_pos = pygame.Rect(300, 300,97,72)
		
			# Player2
		self.player2_start_pos = pygame.Rect(800, 300, 97,72)
