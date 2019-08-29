import pygame

class Stats():
	def __init__(self, screen, settings):
		
		self.in_game = False
		self.in_settings = False
		self.someone_won = False
		self.current_commie = None
