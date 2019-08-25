from pygame.sprite import Group
import pygame.font

class Scoreboard():
	def __init__(self, screen, settings, players):
		
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None, 48)
		
		self.screen = screen
		self.settings = settings
		self.players = players
		self.prep_info_text()
		
	def prep_info_text(self, msg=""):
		self.scoreboard_msg = msg
		self.scoreboard_msg_img = self.font.render(self.scoreboard_msg, True, self.text_color)
		
		self.scoreboard_msg_rect = self.scoreboard_msg_img.get_rect()
		self.scoreboard_msg_rect.centerx = self.screen.get_rect().centerx
		self.scoreboard_msg_rect.bottom = self.screen.get_rect().bottom - 10
		
	def draw_scores(self):
		for player in self.players:
			if player.player_num == 1:
				pos = (20,10, player.health, 25)
			if player.player_num == 2:
				pos = (self.screen.get_rect().right - 120, 10, player.health, 25)
			
			pygame.draw.rect(self.screen, self.settings.player_health_color, pos)
			
		self.screen.blit(self.scoreboard_msg_img, self.scoreboard_msg_rect)
		
				 
		
