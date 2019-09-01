import pygame
import sys
from pygame.locals import *
from bullet import Bullet
import pygame.font
from player import Player
from pygame.sprite import Group
from heart import Heart
import os
from commie import Commie
from explosion import ExplosionSprite
from heart import Heart

_sound_library = {}
def play_sound(path):
	global _sound_library
	sound = _sound_library.get(path)
	if sound == None:
		canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
		sound = pygame.mixer.Sound(canonicalized_path)
		_sound_library[path] = sound
	sound.play()

def check_events(settings, screen, players, menu_buttons, stats, joysticks, bullets, menu_msgs, sb, hearts, commies):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			if settings.controller_used:
				save_controller_settings(settings)
			sys.exit(0)
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, players, bullets, stats, sb, hearts, commies)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, settings, screen, players)
			
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_menu_button(settings, mouse_x, mouse_y, menu_buttons, stats, joysticks, screen, menu_msgs, sb, players, bullets, hearts, commies)
		elif event.type == pygame.JOYAXISMOTION:
			# If there are 3 players, set joystick to control player 3. If two players, control player 2
			if len(players) == 3:
				player = players[2]
			elif len(players) == 2:
				player = players[1]

			val = round(event.value)
			if stats.in_settings:
				if val == -1:
					if settings.buttons_left == 6:
						settings.joystick_xaxis = event.axis
						settings.buttons_left = 5
						menu_msgs.prep_joystick_setup_msg("Up Control Pad")
					elif settings.buttons_left == 5:
						settings.joystick_yaxis = event.axis
						settings.buttons_left = 4
						menu_msgs.prep_joystick_setup_msg("Select")
			else:
				if event.axis == settings.joystick_xaxis:
					if val == 1:
						player.moving_right = True
						player.direction = "right"
						
					elif val == 0:
						player.moving_right = False
						player.moving_left = False
						
					elif val == -1:
						player.moving_left = True
						player.direction = "left"
						
				elif event.axis == settings.joystick_yaxis:
					if val == 1:
						player.moving_down = True
						player.direction = "down"
					
					elif val == 0:
						player.moving_down = False
						player.moving_up = False
						
					elif val == -1:
						player.moving_up = True
						player.direction = "up"

		elif event.type == pygame.JOYBUTTONDOWN:
			# If there are 3 players, set joystick to control player 3. If two players, control player 2
			if len(players) == 3:
				player = players[2]
				bulletGroup = 2
			elif len(players) == 2:
				player = players[1]
				bulletGroup = 1

			if stats.in_settings:
				if settings.buttons_left == 4:
					settings.joystick_select = event.button
					settings.buttons_left = 3
					menu_msgs.prep_joystick_setup_msg("Start")
				elif settings.buttons_left == 3:
					settings.joystick_start = event.button
					settings.buttons_left = 2
					menu_msgs.prep_joystick_setup_msg("B")
				elif settings.buttons_left == 2:
					settings.joystick_b = event.button
					settings.buttons_left = 1
					menu_msgs.prep_joystick_setup_msg("A")
				elif settings.buttons_left == 1:
					settings.joystick_a = event.button
					settings.controller_used = True
					menu_msgs.prep_main_msg("Controller Setup!")
					settings.show_main_msg = True
					settings.buttons_left = 0
					stats.in_settings = False
					
			elif stats.in_game:
				if event.button == settings.joystick_a:
					if stats.in_game:
						if not stats.paused:
							new_bullet(bullets[bulletGroup], settings, screen, player)
				elif event.button == settings.joystick_b:
					if stats.in_game:
						if not stats.paused:
							play_sound("robot.wav")
							players[1].aiming_up = not players[1].aiming_up
				elif event.button == settings.joystick_start:
					pause_and_start(stats)
			else:
				if event.button == settings.joystick_start:
					initGame(settings, stats, screen, sb, players, bullets, hearts, commies)
					stats.in_game = True
		elif event.type == pygame.JOYBUTTONUP:
			if stats.in_game:
				if event.button == settings.joystick_a:
					#players[1].aiming_up = False
					pass

def pause_and_start(stats):
	if not stats.game_over:
		stats.paused = not stats.paused
		play_sound("pause.wav")
	else:
		pygame.mixer.music.load("song.mp3")
		pygame.mixer.music.play(-1)
		play_sound("button.wav")
		stats.in_game = False

def save_controller_settings(settings):
	try:
		with open(find_data_file("controller.txt"), "w") as controller_settings:
			controller_settings.write(str(settings.joystick_xaxis) + "\n")
			controller_settings.write(str(settings.joystick_yaxis) + "\n")
			controller_settings.write(str(settings.joystick_select) + "\n")
			controller_settings.write(str(settings.joystick_start) + "\n")
			controller_settings.write(str(settings.joystick_b) + "\n")
			controller_settings.write(str(settings.joystick_a) + "\n")
	except FileNotFoundError:
		pass

def check_menu_button(settings, mouse_x, mouse_y, menu_buttons, stats, joysticks, screen, menu_msgs, sb, players, bullets, hearts, commies):
	
	for btn in menu_buttons:
		btn_clicked = btn.rect.collidepoint(mouse_x, mouse_y)
	
		if btn_clicked:
			play_sound("button.wav")
			if not stats.in_game:
				if btn.button_type == "play":

					initGame(settings, stats, screen, sb, players, bullets, hearts, commies)
					stats.in_game = True
				elif btn.button_type == "settings":
					if joysticks:
						settings.buttons_left = 6
						settings.show_main_msg = False
						stats.in_settings = True
						menu_msgs.prep_joystick_setup_msg()
					else:
						settings.show_main_msg = True
				elif btn.button_type == "quit":
					if stats.in_settings:
						stats.in_settings = False
					else:
						if settings.controller_used:
							save_controller_settings(settings)
						sys.exit(0)
			elif stats.in_game and stats.someone_won:
				if btn.button_type == "quit":
					stats.in_game = False
					
def initGame(settings, stats, screen, sb, players, bullets, hearts, commies):
	pygame.mixer.music.load("song.mp3")
	pygame.mixer.music.play(-1)

	for player in players:
		player.initialize_player()

	stats.game_over = False
	stats.someone_won = False
	stats.current_commie = None
	stats.commie_timer = settings.commie_time
	sb.reset_scoreboard()

	hearts.empty()
	commies.empty()
	
	#players = []
	#bullets = []

	# variable value to be replaced with whatever the players decide in the menu...
	playernum = 2

	#player1 = Player(settings, screen, 1, settings.player1_start_pos)
	#player2 = Player(settings, screen, 2, settings.player2_start_pos)

	#players.append(player1)
	#players.append(player2)

	#bullets1 = Group()
	#bullets2 = Group()

	#bullets.append(bullets1)
	#bullets.append(bullets2)

	""" if playernum == 3:
		player3 = Player(settings, screen, 3, pygame.Rect(700, 200, 97,72))
		players.append(player3)

		bullets3 = Group()
		bullets.append(bullets3) """
		
	#if playernum == 2:
	#	del players[2]

	
	#stats.in_game = True
	#print(players)

		
def check_keydown_events(event, settings, screen, players, bullets, stats, sb, hearts, commies):
	
	if event.key == pygame.K_RIGHT:
		players[0].moving_right = True
		#players[0].direction = "right"
	elif event.key == pygame.K_LEFT:
		players[0].moving_left = True
		#players[0].direction = "left"
	elif event.key == pygame.K_UP:
		players[0].moving_up = True
		#players[0].direction = "up"
	elif event.key == pygame.K_DOWN:
		players[0].moving_down = True
		#players[0].direction = "down"
	elif event.key == pygame.K_RETURN:
		if stats.in_game:
			if not stats.paused:
				new_bullet(bullets[0], settings, screen, players[0])
		else:
			initGame(settings, stats, screen, sb, players, bullets, hearts, commies)
			stats.in_game = True
	elif event.key == pygame.K_BACKSPACE:
		if stats.in_game:
			if not stats.paused:
				play_sound("robot.wav")
				players[0].aiming_up = not players[0].aiming_up
	elif event.key == pygame.K_a:
		players[1].moving_left = True
		players[1].direction = "left"
	elif event.key == pygame.K_d:
		players[1].moving_right = True
		players[1].direction = "right"
	elif event.key == pygame.K_w:
		players[1].moving_up = True
		players[1].direction = "up"
	elif event.key == pygame.K_s:
		players[1].moving_down = True
		players[1].direction = "down"
	elif event.key == pygame.K_v:
		if stats.in_game:
			if not stats.paused:
				play_sound("robot.wav")
				players[1].aiming_up = not players[1].aiming_up
	elif event.key == pygame.K_SPACE:
		if stats.in_game:
			if not stats.paused:
				new_bullet(bullets[1], settings, screen, players[1])
	elif event.key == pygame.K_q:
		play_sound("button.wav")
		if stats.in_game:
			stats.in_game = False
			pygame.mixer.music.load("song.mp3")
			pygame.mixer.music.play(-1)
		elif stats.in_settings:
			stats.in_settings = False
		else:
			if settings.controller_used:
				save_controller_settings(settings)
			sys.exit()
	
def check_keyup_events(event, settings, screen, players):
	if event.key == pygame.K_RIGHT:
		players[0].moving_right = False
	elif event.key == pygame.K_LEFT:
		players[0].moving_left = False
	elif event.key == pygame.K_UP:
		players[0].moving_up = False
		""" if players[0].moving_right:
			players[0].direction = "right"
		elif players[0].moving_left:
			players[0].direction = "left" """
	elif event.key == pygame.K_DOWN:
		players[0].moving_down = False
	elif event.key == pygame.K_BACKSPACE:
		#players[0].aiming_up = False
		pass
	elif event.key == pygame.K_a:
		players[1].moving_left = False
	elif event.key == pygame.K_d:
		players[1].moving_right = False
	elif event.key == pygame.K_w:
		players[1].moving_up = False
	elif event.key == pygame.K_s:
		players[1].moving_down = False
	elif event.key == pygame.K_v:
		#players[1].aiming_up = False
		pass

def new_bullet(bullet_group, settings, screen, player):
	bullet = Bullet(settings, screen, player)
	bullet_group.add(bullet)
	

def update(screen, settings, players, stats, menu_buttons, bullets, menu_msgs, sb, items, walls, hq_doors, explos):
	if stats.in_game:
		if stats.current_commie == None:
			screen.blit(settings.in_game_bg,(0,0))
		else:
			screen.blit(settings.in_game_commie_bg, (0,0))

		for player in players:
			player.blitme()

		for wa in walls.sprites():
			wa.blitme()

		for hq_door in hq_doors:
			hq_door.blitme()
		
		for players_bullets in bullets:
			for bullet in players_bullets.sprites():
				bullet.blitme()
				
		sb.draw_health_bars()

		if stats.someone_won:			
			for btn in menu_buttons:
				if btn.button_type == "quit":
					btn.draw_quit_button()	
	
		for itemGroup in items:
			for item in itemGroup.sprites():
				item.draw_item()

		for exp in explos:
			exp.draw(screen)

		pygame.display.flip()
	
	elif stats.in_settings:
		screen.blit(settings.settings_bg, (0,0))
		
		menu_msgs.show_settings_msgs()

		for btn in menu_buttons:
				if btn.button_type == "quit":
					btn.draw_quit_button()
		
		pygame.display.flip()
		
	else:
		screen.blit(settings.menu_bg, (0,0))
		
		
		for idx, btn in enumerate(menu_buttons):
			btn.draw_button(idx + 1, len(menu_buttons))
		
		menu_msgs.show_main_menu_msgs()
		
		pygame.display.flip()

def update_doors(hq_doors):
	for door in hq_doors:
		door.update()

def update_bullets(bullets, screen, players, settings, stats, sb):
	for idx, players_bullets in enumerate(bullets):
		players_bullets.update()
		
		# If bullet is outside of screen, remove from group
		for bullet in players_bullets.copy():
			if bullet.rect.bottom <= 0 or bullet.rect.top >= screen.get_rect().bottom or bullet.rect.left >= screen.get_rect().right or bullet.rect.right <= screen.get_rect().left:
				players_bullets.remove(bullet)
	# Don't check for bullet collisions if someone already won
	if not stats.someone_won:
		# Check collisions for every players group of bullets.			
		for idx, players_bullets in enumerate(bullets):
			check_bullet_enemy_collisions(players_bullets, idx, screen, players, settings, stats, sb)

	players_alive = []
	for player in players:
		if player.health > 0:
			players_alive.append(player)
		else:
			continue
	if len(players_alive) == 1:
		stats.someone_won = True
		players_alive[0].is_alive = False
		sb.prep_info_text("Player " + str(players_alive[0].player_num) + " won!")

def update_plane(settings, screen, planes):
	planes.update()
	# Remove planes outside of screen
	for plane in planes.copy():
		if plane.rect.bottom <= (0 - plane.rect.height) or plane.rect.top >= screen.get_rect().bottom or plane.rect.left >= screen.get_rect().right or plane.rect.right <= 0:
			planes.remove(plane)

def update_explos(explos, dt):
	if explos:
		try:
			for idx, exp in enumerate(explos[:]):
				for ex in exp:
					if ex.index >= 8:
						del explos[idx]
				exp.update(dt)
		except:
			pass

def check_bullet_enemy_collisions(players_bullets, bullet_idx, screen, players, settings, stats, sb):
	# For every player in the list of players, check if there's any collision
	for player_idx, player in enumerate(players):
		# If current player is the owner of the bullet group, don't check for collisions
		if bullet_idx == player_idx:
			continue
		else:
			collisions = pygame.sprite.spritecollide(player, players_bullets, False)
			if collisions:
				# get bullet owner & check if bullets "is_missile" = true
				for bullet in collisions:
					
					if not bullet.is_missile:
						if (player.health - settings.bullet_damage) <= 0:
							if not stats.current_commie == None and stats.current_commie == bullet.my_creator:
								pygame.mixer.music.load("commie.mp3")
								pygame.mixer.music.play(-1)
							play_sound("hit.wav")
							stats.game_over = True
							player.health = 0
							sb.prep_health_scores()
						else:
							play_sound("hit.wav")
							players_bullets.remove(bullet)
							player.health -= settings.bullet_damage
							sb.prep_health_scores()
				
def check_bullet_plane_collide(settings, screen, planes, items, players, stats, sb, bullets, explos):
	# For every players bullet group, check for collision with plane
	for bullet_group in bullets:
		collisions = pygame.sprite.groupcollide(planes, bullet_group, False, False)

		for plane, bullets in collisions.items():
			for bullet in bullets[:]:
				if bullet.is_missile:
					item = plane.release_item(plane.centerx, plane.centery)
					if type(item) == Heart:
						items[0].add(item)
					elif type(item) == Commie:
						items[1].add(item)
					newExplo = ExplosionSprite(screen, plane.rect)
					expl = Group(newExplo)
					explos.append(expl)
					planes.remove(plane)
				bullets.remove(bullet) 

def check_player_collide(settings, players):
	hit = players[0].rect.colliderect(players[1].rect)
	if hit:
		for player in players:
			if player.moving_up and player.moving_right:
				player.moving_up = False
				player.moving_right = False
				player.centerx -= 10
				player.centery += 10
			elif player.moving_right:
				player.moving_right = False
				player.centerx -= 10
				player.moving_right = True
			elif player.moving_left:
				player.moving_left = False
				player.centerx += 10
				player.moving_left = True
			elif player.moving_up:
				player.moving_up = False
				player.centerx += 10
				player.moving_up = True
			elif player.moving_down:
				player.moving_down = False
				player.centerx -= 10
				player.moving_down = True

def check_player_door_collide(settings, stats, players, hq_doors):
	for idx, player in enumerate(players):

		for door in hq_doors:
			
			if door.player.player_num == player.player_num:
				hit = player.rect.colliderect(door.door_trigger_rect)
				
				if hit:
					#door = hq_doors[idx]
					if player.moving_up:
						if door.is_closed:
							player.moving_up = False
							player.centery += 10
							door.open()
						elif door.is_open:
							door.close()
					elif player.moving_down:
						if door.is_closed:
							player.moving_down = False
							player.centery -= 10
							door.open()
						elif door.is_open:
							door.close()
			elif not door.player.player_num == player.player_num:
				hit = player.rect.colliderect(door.door_trigger_rect)
				if hit:
					if player.moving_down:
						if door.is_closed:
							player.moving_down = False
							player.centery -= 10
						elif door.is_open:
							continue

def check_bullet_door_collide(settings, stats, bullets, hq_doors):
	for door in hq_doors:
		for bullet_group in bullets:
			bullet = pygame.sprite.spritecollideany(door, bullet_group)
			
			if bullet:
				if not bullet.is_missile:
					bullet_group.remove(bullet)


def check_player_heart_collide(settings, players, hearts, sb, stats, screen):
	# Check for collisions with hearts for every player
	for player in players:
		# Only let player pick up heart if can_take_health
		if player.can_take_health:
			collisions = pygame.sprite.spritecollide(player, hearts, True)

			if collisions:
				play_sound("blip.wav")
				# Add to player health
				if player.health + settings.heart_healing <= 100:
					player.health += settings.heart_healing
					sb.prep_health_scores()
		else:
			collisions = pygame.sprite.spritecollide(player, hearts, True)

			if not stats.current_commie == None:
				if collisions:
					play_sound("blip.wav")
					#if stats.current_commie.health + settings.heart_healing <= 100:
						#stats.current_commie.health += settings.heart_healing
						#sb.prep_health_scores()
					heart = Heart(screen, settings, stats.current_commie.start_pos.centerx, stats.current_commie.start_pos.centery)
					hearts.add(heart)

def check_player_commie_collide(settings, players, commies, sb, stats):
	for player in players:
		collisions = pygame.sprite.spritecollide(player, commies, True)

		if collisions:

			if stats.current_commie == None:

				commies.empty()
			
				play_sound("flirp.wav")
				stats.current_commie = player
				sb.prep_health_scores()

				# Make all players except commie unable to gain health
				for plr in players:
					if plr.player_num == player.player_num:
						continue
					else:
						plr.can_take_health = False

def check_player_wall_collide(settings, screen, players, walls):
	for player in players:
		collisions = pygame.sprite.spritecollide(player, walls, False)

		if collisions:
			if player.moving_up and player.moving_right:
				player.moving_up = False
				player.moving_right = False
				player.centerx -= 10
				player.centery += 10
			elif player.moving_right:
				player.moving_right = False
				player.centerx -= 10
				player.moving_right = True
			elif player.moving_left:
				player.moving_left = False
				player.centerx += 10
				player.moving_left = True
			elif player.moving_up:
				player.moving_up = False
				player.centerx += 10
				player.moving_up = True
			elif player.moving_down:
				player.moving_down = False
				player.centerx -= 10
				player.moving_down = True

def check_bullet_wall_collide(settings, screen, bullets, walls):
	for bullet_group in bullets:
		collisions = pygame.sprite.groupcollide(walls, bullet_group, False, False)

		for wall, bullets in collisions.items():
			for bullet in bullets[:]:
				if bullet.is_missile:
					continue
				else:
					bullet_group.remove(bullet)

def find_data_file(filename):
	if getattr(sys, 'frozen', False):
		# The application is frozen
		datadir = os.path.dirname(sys.executable)
	else:
		# The application is not frozen
		# Change this bit to match where you store your data files:
		if filename == "controller.txt":
			datadir = os.path.dirname(os.path.realpath(filename))
		else:
			datadir = os.path.dirname(os.path.realpath("images/" + filename))
	return os.path.join(datadir, filename)
