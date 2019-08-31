import pygame.font
import os
import funcs as funcs

class Button():
	def __init__(self, screen, settings, stats, type_of_button):
		self.screen = screen
		self.stats = stats

		self.font = pygame.font.SysFont(None, 48)
		
		self.button_type = type_of_button
		
		self.image = pygame.image.load(funcs.find_data_file("%s_button.png" % str(self.button_type)))
		
		self.rect = self.image.get_rect()
		self.rect.center = (0,0)
	
		
	def draw_button(self, idx, num_of_buttons):
		sc_height = self.screen.get_rect().height
		space_each = (sc_height / num_of_buttons) - 60
		self.rect.center = (self.screen.get_rect().centerx, (space_each * idx))
		self.screen.blit(self.image, self.rect)
		
	def draw_quit_button(self):
		if self.stats.in_settings:
			self.rect.center = (self.screen.get_rect().left + 150, self.screen.get_rect().bottom - 80)
			self.screen.blit(self.image, self.rect)
		else:	
			self.rect.center = (self.screen.get_rect().centerx, self.screen.get_rect().centery)
			self.screen.blit(self.image, self.rect)

