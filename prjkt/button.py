import pygame.font

class Button():
	def __init__(self, screen, settings, type_of_button):
		self.screen = screen
		
		self.font = pygame.font.SysFont(None, 48)
		
		self.button_type = type_of_button
		
		self.image = pygame.image.load("images/%s_button.png" % str(self.button_type))
		
		self.rect = self.image.get_rect()
		self.rect.center = (0,0)
	
		
	def draw_button(self, idx, num_of_buttons):
		self.rect.center = (self.screen.get_rect().centerx, (self.screen.get_rect().centery * idx) / num_of_buttons)
		self.screen.blit(self.image, self.rect)

