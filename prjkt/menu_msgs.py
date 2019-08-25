import pygame
import pygame.font

class Menu_Msgs():
	def __init__(self, settings, screen):
		
		self.settings = settings
		self.screen = screen
		
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)
	
		self.prep_main_msg()
		self.prep_joystick_setup_msg()
	
	def prep_main_msg(self, msg="No joystick found"):
		self.no_joystick_msg = msg
		self.no_joystick_msg_img = self.font.render(self.no_joystick_msg, True, self.text_color)
		
		self.no_joystick_msg_rect = self.no_joystick_msg_img.get_rect()
		self.no_joystick_msg_rect.centerx = self.screen.get_rect().centerx
		self.no_joystick_msg_rect.bottom = self.screen.get_rect().bottom - 10
		
	def show_main_menu_msgs(self):
		if self.settings.show_main_msg:
			self.screen.blit(self.no_joystick_msg_img, self.no_joystick_msg_rect)
			
	def prep_joystick_setup_msg(self, button="Left Control Pad"):
		if not button == "Done":
			self.joystick_setup_msg = "Press the " + button + " button."
		else:
			self.joystick_setup_msg = "Done!"
		self.joystick_setup_msg_img = self.font.render(self.joystick_setup_msg, True, self.text_color)
		
		self.joystick_setup_msg_rect = self.joystick_setup_msg_img.get_rect()
		self.joystick_setup_msg_rect.centerx = self.screen.get_rect().centerx
		self.joystick_setup_msg_rect.bottom = self.screen.get_rect().bottom - 10
		
	def show_settings_msgs(self):
		self.screen.blit(self.joystick_setup_msg_img, self.joystick_setup_msg_rect)
		
