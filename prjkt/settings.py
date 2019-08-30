import pygame
import pygame.font
import os
import funcs as funcs

folder = os.path.dirname(os.path.realpath(__file__))

class Settings():
	def __init__(self, joysticks):
		
		# Screen settings
		self.screen_width = 1280
		self.screen_height = 720
		self.bg_color = (0,0,0)
		
		self.in_game_bg = pygame.image.load(funcs.find_data_file("images/bg.jpg"))
		self.menu_bg = pygame.image.load(funcs.find_data_file("images/menu_bg.png"))
		self.settings_bg = pygame.image.load(os.path.join(funcs.find_data_file("images/settings_bg.png")))
		
		# Timer settings
		self.commie_time = 5

		# Bullet:
			# Standard
		self.bullet_speed_factor = 30
		self.bullet_damage = 5
		
			# Big
		self.big_bullet_speed = 40
		self.big_bullet_damage = 30
		
		# Heart:
		self.heart_healing = 5

		# Plane:
		self.plane_speed_factor = 15
		self.plane_health = 1

		# Player settings
		
			# Both
		self.player_health = 100
		self.player_speed = 5
		self.player_health_color = (40,255,50)
		
			# Player1
		self.player1_start_pos = pygame.Rect(300, 300,97,72)
		self.player1_joystick_id = 0
		
			# Player2
		self.player2_start_pos = pygame.Rect(800, 300, 97,72)
		
		# Controller
		self.joystick_xaxis = None
		self.joystick_yaxis = None
		self.joystick_select = None
		self.joystick_start = None
		self.joystick_b = None
		self.joystick_a = None

		# Load existing joystick config if exists
		if joysticks:
			try:
				with open(funcs.find_data_file("controller.txt"), "r") as controller_settings:
					for idx, line in enumerate(controller_settings):
						if idx == 0:
							self.joystick_xaxis = int(line)
						elif idx == 1:
							self.joystick_yaxis = int(line)
						elif idx == 2:
							self.joystick_select = int(line)
						elif idx == 3:
							self.joystick_start = int(line)
						elif idx == 4:
							self.joystick_b = int(line)
						elif idx == 5:
							self.joystick_a = int(line)
			except FileNotFoundError:
				pass
		self.buttons_left = 6
		self.controller_used = False
		
		self.show_main_msg = False
