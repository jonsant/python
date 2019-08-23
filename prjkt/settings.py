import pygame

class Settings():
	def __init__(self):
		
		# Screen settings
		self.screen_width = 1280
		self.screen_height = 720
		self.bg_color = (0,0,0)
		
		self.in_game_bg = pygame.image.load("images/bg.jpg")
		self.menu_bg = pygame.image.load("images/menu_bg.png")
		self.settings_bg = pygame.image.load("images/settings_bg.png")
		
		# Bullet:
			# Standard
		self.bullet_speed_factor = 20
		self.bullet_damage = 10
		
			# Big
		self.big_bullet_speed = 30
		self.big_bullet_damage = 30
		
		# Player settings
		
			# Both
		self.player_speed = 5
		
			# Player1
		self.player1_start_pos = pygame.Rect(300, 300,97,72)
		self.player1_joystick_id = 0
		
			# Player2
		self.player2_start_pos = pygame.Rect(800, 300, 97,72)
		
		self.joystick_xaxis = None
		self.joystick_yaxis = None
		self.joystick_select = None
		self.joystick_start = None
		self.joystick_b = None
		self.joystick_a = None
		self.buttons_left = 6
