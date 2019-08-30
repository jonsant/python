import pygame
from pygame.sprite import Group
from settings import Settings
from stats import Stats
import funcs as funcs
from player import Player
from button import Button
from menu_msgs import Menu_Msgs
from pygame.sprite import Group
from scoreboard import Scoreboard
import pygame.font
import random
from heart import Heart
from commie import Commie
from plane import Plane

def game():
	pygame.init()
	
	#init joystick(s)
	pygame.joystick.init()
	joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
	for st in joysticks:
		st.init()
	
	settings = Settings(joysticks)
	
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Game")
	
	stats = Stats(screen, settings)
	
	player1 = Player(settings, screen, 1, settings.player1_start_pos)
	player2 = Player(settings, screen, 2, settings.player2_start_pos)
	player3 = Player(settings, screen, 3, pygame.Rect(700, 200, 97,72))
	players = [player1, player2]

	bullets1 = Group()
	bullets2 = Group()
	bullets3 = Group()

	bullets = [bullets1, bullets2]

	hearts = Group()
	commies = Group()
	planes = Group()

	items = [hearts, commies, planes]
	
	play_button = Button(screen, settings, "play")
	settings_button = Button(screen, settings, "settings")
	quit_button = Button(screen, settings, "quit")
	menu_buttons = [play_button, settings_button, quit_button]
	
	#Scoreboard
	sb = Scoreboard(screen, settings, players)
	
	#menu msgs
	menu_msgs = Menu_Msgs(settings, screen)
	
	#clock
	
	clock = pygame.time.Clock()

	while True:
		clock.tick(60)
		
		funcs.check_events(settings, screen, players, menu_buttons, stats, joysticks, bullets, menu_msgs, sb, hearts)
		
		if stats.in_game:

			# Spawn hearts
			""" if random.randrange(0, 50) < 1:
				
					if len(hearts.sprites()) < 3:
						heart = Heart(screen, settings)
						hearts.add(heart) """

			""" # Spawn commies:
			if random.randrange(0, 50) < 1:
				if len(commies.sprites()) == 0 and stats.current_commie == None:
					commie = Commie(screen, settings)
					commies.add(commie) """

			if random.randrange(0, 50) < 1:
				if len(planes.sprites()) < 2:
					plane = Plane(settings, screen)
					planes.add(plane)

			for player in players:
				player.update()
			funcs.update_plane(settings, screen, planes)
			funcs.update_bullets(bullets, screen, players, settings, stats, sb)
			
			funcs.check_player_collide(settings, players)
			funcs.check_player_heart_collide(settings, players, hearts, sb, stats)
			funcs.check_player_commie_collide(settings, players, commies, sb, stats)
			# ---
		
		funcs.update(screen, settings, players, stats, menu_buttons, bullets, menu_msgs, sb, items)

game()
