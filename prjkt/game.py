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
	
	player1 = Player(settings, screen, 1)
	player2 = Player(settings, screen, 2)
	
	clock = pygame.time.Clock()

	while True:
		clock.tick(30)
		
		funcs.check_events(settings, screen, player1, player2)
		
		player1.update()
		player2.update()
		
		# ---
		
		funcs.update(screen, settings, player1, player2)

game()
