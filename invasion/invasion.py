import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# Initialize game, settings and screen object.
	pygame.init()
	
	my_settings = Settings()
	
	screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
	pygame.display.set_caption("Invasion")
	
	# Make a ship
	ship = Ship(my_settings, screen)
	
	# Start the main loop for the game
	while True:
		
		gf.check_events(ship)
		ship.update()
		gf.update_screen(my_settings, screen, ship)
		
		
run_game()
