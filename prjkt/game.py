import pygame
from pygame.sprite import Group
from settings import Settings
import funcs as funcs
from player import Player

def game():
	pygame.init()

	settings = Settings()
	
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Game")
	
	player1 = Player(settings, screen, 1, settings.player1_start_pos)
	player2 = Player(settings, screen, 2, settings.player2_start_pos)
	
	clock = pygame.time.Clock()

	while True:
		clock.tick(60)
		
		funcs.check_events(settings, screen, player1, player2)
		
		player1.update()
		player2.update()
		
		funcs.check_player_collide(settings, player1, player2)
		# ---
		
		funcs.update(screen, settings, player1, player2)

game()
