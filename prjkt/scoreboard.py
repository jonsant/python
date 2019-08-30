from pygame.sprite import Group
import pygame.font

class Scoreboard():
	def __init__(self, screen, settings, players, stats):
		
		self.text_color = (255,255,255)
		self.commie_text_color = (155,0,0)
		self.font = pygame.font.SysFont(None, 48)
		
		self.stats = stats
		self.screen = screen
		self.settings = settings
		self.players = players
		self.prep_info_text()
		self.prep_health_scores()

	def reset_scoreboard(self):
		self.prep_info_text()
		self.prep_health_scores()
		self.prep_player_info()

	def prep_info_text(self, msg=""):
		self.scoreboard_msg = msg
		self.scoreboard_msg_img = self.font.render(self.scoreboard_msg, True, self.text_color)
		
		self.scoreboard_msg_rect = self.scoreboard_msg_img.get_rect()
		self.scoreboard_msg_rect.centerx = self.screen.get_rect().centerx
		self.scoreboard_msg_rect.bottom = self.screen.get_rect().bottom - 10

	def prep_health_scores(self):
		for player in self.players:
			if player.player_num == 1:
				
				self.pl1_health_image = self.font.render(str(player.health), True, self.text_color)
					
				# Position the health below the health bar.
				self.pl1_health_rect = self.pl1_health_image.get_rect()
				self.pl1_health_rect.right = self.pl1_health_rect.right + 20
				self.pl1_health_rect.top = self.pl1_health_rect.bottom + 10
			if player.player_num == 2:

				self.pl2_health_image = self.font.render(str(player.health), True, self.text_color)

				# Position the health below the health bar.
				self.pl2_health_rect = self.pl2_health_image.get_rect()
				self.pl2_health_rect.right = self.screen.get_rect().right - 60
				self.pl2_health_rect.top = self.pl2_health_rect.bottom + 10

	def prep_player_info(self, commie_time=0):

		self.pl1_info_image = self.font.render("", True, self.commie_text_color)
		self.pl1_info_rect = self.pl1_info_image.get_rect()

		self.pl2_info_image = self.font.render("", True, self.commie_text_color)
		self.pl2_info_rect = self.pl2_info_image.get_rect()

		for player in self.players:
			if player.player_num == 1:
				if commie_time > 0 and self.stats.current_commie.player_num == 1:
					self.pl1_info_image = self.font.render(str(round(commie_time)), True, self.commie_text_color)
				
					self.pl1_info_rect = self.pl1_info_image.get_rect()
					self.pl1_info_rect.right = self.pl1_info_rect.right + 20
					self.pl1_info_rect.top = self.pl1_health_rect.bottom + 10

			if player.player_num == 2:
				if commie_time > 0 and self.stats.current_commie.player_num == 2:
					self.pl2_info_image = self.font.render(str(round(commie_time)), True, self.commie_text_color)
				
					self.pl2_info_rect = self.pl2_info_image.get_rect()
					self.pl2_info_rect.right = self.screen.get_rect().right - 60
					self.pl2_info_rect.top = self.pl2_health_rect.bottom + 20

	def draw_health_bars(self):
		for player in self.players:
			if player.player_num == 1:
				pos = (20,10, player.health, 25)
				if not self.stats.current_commie == None:
					if self.stats.current_commie.player_num == 1:
						self.screen.blit(self.pl1_info_image, self.pl1_info_rect)
					elif self.stats.current_commie.player_num == 2:
						self.screen.blit(self.pl2_info_image, self.pl2_info_rect)
			if player.player_num == 2:
				pos = (self.screen.get_rect().right - 120, 10, player.health, 25)
			
			pygame.draw.rect(self.screen, self.settings.player_health_color, pos)
			
		self.screen.blit(self.scoreboard_msg_img, self.scoreboard_msg_rect)
		self.screen.blit(self.pl1_health_image, self.pl1_health_rect)
		self.screen.blit(self.pl2_health_image, self.pl2_health_rect)
		
				 
		
