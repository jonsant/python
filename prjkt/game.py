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
	
	player1 = Player(settings, screen)

	while True:
		funcs.check_events()
		
		player1.update()
		
		# ---
		
		funcs.update(screen, settings, player1)

game()
