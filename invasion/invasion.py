import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	
	# Initialize game, settings and screen object.
	pygame.init() 
	
	my_settings = Settings()
	
	screen = pygame.display.set_mode((my_settings.screen_width, my_settings.screen_height))
	pygame.display.set_caption("Invasion")
	
	explos = []
	
	# Make the Play button.
	play_button = Button(my_settings, screen, "Play")
	
	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(my_settings)
	sb = Scoreboard(my_settings, screen, stats)
	
	# Make a ship, a group of bullets, and a group of aliens.
	ship = Ship(my_settings, screen)
	bullets = Group()
	vBullets = Group()
	aliens = Group()
	
	# Create the fleet of aliens.
	gf.create_fleet(my_settings, screen, ship, aliens)
	
	# Start the main loop for the game
	while True:
		
		
		gf.check_events(my_settings, screen, stats, sb, play_button, ship, aliens, bullets, vBullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(my_settings, screen, stats, sb, ship, aliens, bullets, vBullets, explos)
			gf.update_aliens(my_settings, stats, screen, sb, ship, aliens, bullets, vBullets)
			gf.update_explos(explos)
			
		gf.update_screen(my_settings, screen, stats, sb, ship, aliens, bullets, vBullets, play_button, explos)
		
		
run_game()
