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
from wall import Wall

def game():

	# Init mixer before pygame to prevent delay
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.mixer.init()
	pygame.init()

	pygame.mixer.music.load("song.mp3")
	pygame.mixer.music.play(-1)

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
	#player3 = Player(settings, screen, 3, pygame.Rect(700, 200, 97,72))
	players = [player1, player2]

	bullets1 = Group()
	bullets2 = Group()
	bullets3 = Group()

	bullets = [bullets1, bullets2]

	hearts = Group()
	commies = Group()
	planes = Group()
	walls = Group()
	wall = Wall(screen, settings, screen.get_rect().left + 150, screen.get_rect().bottom - 150)
	wall2 = Wall(screen, settings, screen.get_rect().right - 150, screen.get_rect().bottom - 150)
	walls.add(wall)
	walls.add(wall2)

	items = [hearts, commies, planes]
	
	play_button = Button(screen, settings, "play")
	settings_button = Button(screen, settings, "settings")
	quit_button = Button(screen, settings, "quit")
	menu_buttons = [play_button, settings_button, quit_button]
	
	#Scoreboard
	sb = Scoreboard(screen, settings, players, stats)
	
	#menu msgs
	menu_msgs = Menu_Msgs(settings, screen)
	
	#clock
	clock = pygame.time.Clock()
	dt = 0

	# timers
	commie_timer = settings.commie_time

	while True:
		
		funcs.check_events(settings, screen, players, menu_buttons, stats, joysticks, bullets, menu_msgs, sb, hearts)

		if stats.in_game:
			if not stats.paused:
				pygame.mixer.music.unpause()
				# If commie exists, countdown
				if not stats.current_commie == None:
					commie_timer -= dt
					sb.prep_player_info(commie_timer)
					if commie_timer <= 0:
						funcs.play_sound("flirp.wav")
						stats.current_commie = None
						commie_timer = settings.commie_time
						sb.prep_player_info()

				""" # Spawn hearts
				if random.randrange(0, 50) < 1:
					
						if len(hearts.sprites()) < 3:
							heart = Heart(screen, settings)
							hearts.add(heart) """

				""" # Spawn commies:
				if random.randrange(0, 50) < 1:
					if len(commies.sprites()) == 0 and stats.current_commie == None:
						commie = Commie(screen, settings)
						commies.add(commie) """
				
				# Spawn planes
				if random.randrange(0, 50) < 1:
					if len(planes.sprites()) < 2:
						plane = Plane(settings, screen, stats)
						planes.add(plane)

				for player in players:
					player.update()
				funcs.update_plane(settings, screen, planes)
				funcs.update_bullets(bullets, screen, players, settings, stats, sb)
				
				funcs.check_player_collide(settings, players)
				funcs.check_bullet_plane_collide(settings, screen, planes, items, players, stats, sb, bullets)
				funcs.check_player_wall_collide(settings, screen, players, walls)
				funcs.check_bullet_wall_collide(settings, screen, bullets, walls)
				funcs.check_player_heart_collide(settings, players, hearts, sb, stats)
				funcs.check_player_commie_collide(settings, players, commies, sb, stats)
				# ---

			else:
				pygame.mixer.music.pause()
				continue
		
		funcs.update(screen, settings, players, stats, menu_buttons, bullets, menu_msgs, sb, items, walls)

		dt = clock.tick(60) / 1000

game()
