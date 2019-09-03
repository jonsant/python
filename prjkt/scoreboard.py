from pygame.sprite import Group
import pygame.font
import funcs as funcs

class Scoreboard():
	def __init__(self, screen, settings, players, stats):
		
		self.text_color = (255,255,255)
		self.commie_text_color = (155,0,0)
		self.font = pygame.font.SysFont(None, 44)

		self.commie_image = pygame.image.load(funcs.find_data_file("is_commie2.png"))
		self.commie_image_rect = self.commie_image.get_rect()
		
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
		self.prep_current_weapon()

	def prep_current_weapon(self):
		for player in self.players:
			if player.player_num == 1:
				if player.selected_weapon == "bullet":
					self.pl1_current_weapon_image = pygame.image.load(funcs.find_data_file("standard_bullet.png"))
					self.pl1_current_weapon_image = pygame.transform.rotate(self.pl1_current_weapon_image, 90)
				elif player.selected_weapon == "missile":
					self.pl1_current_weapon_image = pygame.image.load(funcs.find_data_file("missile.png"))
					self.pl1_current_weapon_image = pygame.transform.rotate(self.pl1_current_weapon_image, -90)
				elif player.selected_weapon == "bomb":
					self.pl1_current_weapon_image = pygame.image.load(funcs.find_data_file("bomb_icon.png"))
			elif player.player_num == 2:
				if player.selected_weapon == "bullet":
					self.pl2_current_weapon_image = pygame.image.load(funcs.find_data_file("standard_bullet.png"))
					self.pl2_current_weapon_image = pygame.transform.rotate(self.pl2_current_weapon_image, 90)
				elif player.selected_weapon == "missile":
					self.pl2_current_weapon_image = pygame.image.load(funcs.find_data_file("missile.png"))
					self.pl2_current_weapon_image = pygame.transform.rotate(self.pl2_current_weapon_image, -90)
				elif player.selected_weapon == "bomb":
					self.pl2_current_weapon_image = pygame.image.load(funcs.find_data_file("bomb_icon.png"))

				


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
				self.pl1_health_rect.top = self.pl1_health_rect.top + 8
			if player.player_num == 2:

				self.pl2_health_image = self.font.render(str(player.health), True, self.text_color)

				# Position the health below the health bar.
				self.pl2_health_rect = self.pl2_health_image.get_rect()
				self.pl2_health_rect.right = self.screen.get_rect().right - 60
				self.pl2_health_rect.top = self.pl2_health_rect.top + 8

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
					self.pl1_info_rect.top = self.pl1_health_rect.bottom + 20

					self.commie_image_rect.centery = self.pl1_info_rect.centery
					self.commie_image_rect.centerx = self.pl1_info_rect.centerx + 40

			if player.player_num == 2:
				if commie_time > 0 and self.stats.current_commie.player_num == 2:
					self.pl2_info_image = self.font.render(str(round(commie_time)), True, self.commie_text_color)
				
					self.pl2_info_rect = self.pl2_info_image.get_rect()
					self.pl2_info_rect.right = self.screen.get_rect().right - 60
					self.pl2_info_rect.top = self.pl2_health_rect.bottom + 20

					self.commie_image_rect.centery = self.pl2_info_rect.centery
					self.commie_image_rect.centerx = self.pl2_info_rect.centerx - 30


	def draw_health_bars(self):
		for player in self.players:
			if player.player_num == 1:
				self.pl1_bar_rect = (20,10, player.health, 25)
				pos = self.pl1_bar_rect
				if not self.stats.current_commie == None:
					if self.stats.current_commie.player_num == 1:
						self.screen.blit(self.pl1_info_image, self.pl1_info_rect)
						self.screen.blit(self.commie_image, self.commie_image_rect)
					elif self.stats.current_commie.player_num == 2:
						self.screen.blit(self.pl2_info_image, self.pl2_info_rect)
						self.screen.blit(self.commie_image, self.commie_image_rect)
			if player.player_num == 2:
				self.pl2_bar_rect = (self.screen.get_rect().right - 120, 10, player.health, 25)
				pos = self.pl2_bar_rect
			
			pygame.draw.rect(self.screen, self.settings.player_health_color, pos)
			
		self.screen.blit(self.scoreboard_msg_img, self.scoreboard_msg_rect)
		#self.screen.blit(self.pl1_health_image, self.pl1_health_rect)
		#self.screen.blit(self.pl2_health_image, self.pl2_health_rect)
		self.screen.blit(self.pl2_current_weapon_image,
			(self.pl2_bar_rect[0], self.pl2_bar_rect[1] + 30, self.pl2_health_rect.width, self.pl2_health_rect.height))
		self.screen.blit(self.pl1_current_weapon_image,
			(self.pl1_bar_rect[0], self.pl1_bar_rect[1] + 30, self.pl1_health_rect.width, self.pl1_health_rect.height))
		
				 
		
