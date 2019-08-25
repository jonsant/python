import pygame
from pygame.sprite import Group
from settings import Settings
from stats import Stats
import funcs as funcs
from player import Player
from button import Button
from menu_msgs import Menu_Msgs
from pygame.sprite import Group
import pygame.font

def game():
	pygame.init()
	
	#init joystick(s)
	pygame.joystick.init()
	joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
	for st in joysticks:
		st.init()
	
	settings = Settings()
	
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Game")
	
	stats = Stats(screen, settings)
	
	player1 = Player(settings, screen, 1, settings.player1_start_pos)
	player2 = Player(settings, screen, 2, settings.player2_start_pos)
	players = [player1, player2]
	
	bullets1 = Group()
	bullets2 = Group()
	bullets = [bullets1, bullets2]
	
	play_button = Button(screen, settings, "play")
	settings_button = Button(screen, settings, "settings")
	menu_buttons = [play_button, settings_button]
	
	#menu msgs
	menu_msgs = Menu_Msgs(settings, screen)
	
	
	
	#clock
	
	clock = pygame.time.Clock()

	while True:
		clock.tick(60)
		
		funcs.check_events(settings, screen, players, menu_buttons, stats, joysticks, bullets, menu_msgs)
		
		if stats.in_game:
			
			player1.update()
			player2.update()
			funcs.update_bullets(bullets, screen)
			
			funcs.check_player_collide(settings, players)
			# ---
		
		funcs.update(screen, settings, players, stats, menu_buttons, bullets, menu_msgs)

game()
