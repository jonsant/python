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
		
		self.in_game_bg = pygame.image.load(funcs.find_data_file("bg.jpg"))
		self.menu_bg = pygame.image.load(funcs.find_data_file("menu_bg.png"))
		self.settings_bg = pygame.image.load(os.path.join(funcs.find_data_file("settings_bg.png")))
		self.in_game_commie_bg = pygame.image.load(funcs.find_data_file("commie_bg.jpg"))
		
		# Timer settings
		self.commie_time = 20

		# Walls & Doors

		self.door_speed = 3

		# Bullet:
			# Standard
		self.bullet_speed_factor = 35
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
		self.player_speed = 8
		self.player_health_color = (40,255,50)
		self.available_weapons = ["bullet", "missile", "grenade"]
		self.starting_ammo = {"bullets": 1000000, "missiles": 1000000, "grenades": 2}
		
			# Player1
		self.player1_start_pos = pygame.Rect(10, 600,97,72)
		self.player1_joystick_id = 0
		
			# Player2
		self.player2_start_pos = pygame.Rect(1175, 595, 97,72)
		
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
