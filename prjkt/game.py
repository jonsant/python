import pygame
from pygame.sprite import Group
from settings import Settings
import funcs as funcs

def game():
	pygame.init()

	settings = Settings()

	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Game")

	while True:
		funcs.check_events()
		
		# ---
		
		funcs.update(screen, settings)

game()
