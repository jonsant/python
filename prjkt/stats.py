import pygame

class Stats():
	def __init__(self, screen, settings):
		
		self.in_game = False
		self.in_settings = False
		self.someone_won = False
		self.current_commie = None
		self.commie_timer = settings.commie_time
		self.paused = False
		self.game_over = False

		# Player1
		#self.pl1_arming_timer = settings.arming_time

		# Player2
		#self.pl2_arming_timer = settings.arming_time
