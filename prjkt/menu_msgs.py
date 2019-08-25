import pygame
import pygame.font

class Menu_Msgs():
	def __init__(self, settings, screen):
		
		self.settings = settings
		self.screen = screen
		
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)
	
		self.prep_no_joystick_msg()
	
	def prep_no_joystick_msg(self):
		self.no_joystick_msg = "No joystick found"
		self.no_joystick_msg_img = self.font.render(self.no_joystick_msg, True, self.text_color)
		
		self.no_joystick_msg_rect = self.no_joystick_msg_img.get_rect()
		self.no_joystick_msg_rect.centerx = self.screen.get_rect().centerx
		self.no_joystick_msg_rect.bottom = self.screen.get_rect().bottom - 10
		
	def show_main_menu_msgs(self):
		if self.settings.show_no_joystick_msg:
			self.screen.blit(self.no_joystick_msg_img, self.no_joystick_msg_rect)
