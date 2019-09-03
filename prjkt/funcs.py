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
from bomb import Bomb
import random

_sound_library = {}
def play_sound(path):
	global _sound_library
	sound = _sound_library.get(path)
	if sound == None:
		canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
		sound = pygame.mixer.Sound(canonicalized_path)
		_sound_library[path] = sound
	sound.play()

def check_events(settings, screen, players, menu_buttons, stats, joysticks, bullets, menu_msgs, sb, hearts, commies, hq_doors, pl_bombs, dt, walls):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			if settings.controller_used:
				save_controller_settings(settings)
			sys.exit(0)
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, players, bullets, stats, sb, hearts, commies, hq_doors, pl_bombs, walls)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, settings, screen, players, bullets, stats, sb, hearts, commies, hq_doors, pl_bombs)
			
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_menu_button(settings, mouse_x, mouse_y, menu_buttons, stats, joysticks, screen, menu_msgs, sb, players, bullets, hearts, commies, hq_doors, walls)
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
						if not stats.paused and not stats.someone_won:
							fire(bullets[bulletGroup], settings, screen, player, pl_bombs[1], sb)
				elif event.button == settings.joystick_b:
					if stats.in_game:
						if not stats.paused and not stats.someone_won:
							switch_player_weapon(players[1], sb)
				elif event.button == settings.joystick_start:
					pause_and_start(stats)
			else:
				if event.button == settings.joystick_start:
					initGame(settings, stats, screen, sb, players, bullets, hearts, commies, hq_doors, walls)
					stats.in_game = True
		elif event.type == pygame.JOYBUTTONUP:
			# If there are 3 players, set joystick to control player 3. If two players, control player 2
			if len(players) == 3:
				player = players[2]
				bulletGroup = 2
			elif len(players) == 2:
				player = players[1]
				bulletGroup = 1
			if stats.in_game:
				if event.button == settings.joystick_a:
					if player.arming_bomb:
						fire(bullets[bulletGroup], settings, screen, player, pl_bombs[1], sb)

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

def check_menu_button(settings, mouse_x, mouse_y, menu_buttons, stats, joysticks, screen, menu_msgs, sb, players, bullets, hearts, commies, hq_doors, walls):
	
	for btn in menu_buttons:
		btn_clicked = btn.rect.collidepoint(mouse_x, mouse_y)
	
		if btn_clicked:
			play_sound("button.wav")
			if not stats.in_game:
				if btn.button_type == "play":

					initGame(settings, stats, screen, sb, players, bullets, hearts, commies, hq_doors, walls)
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
					
def initGame(settings, stats, screen, sb, players, bullets, hearts, commies, hq_doors, walls):
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

	for wall in walls:
		wall.fix_wall()

	for door in hq_doors:
		door.init_door()
	
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

		
def check_keydown_events(event, settings, screen, players, bullets, stats, sb, hearts, commies, hq_doors, pl_bombs, walls):
	
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
			if not stats.paused and not stats.someone_won:
				fire(bullets[0], settings, screen, players[0], pl_bombs[0], sb)
		else:
			play_sound("button.wav")
			initGame(settings, stats, screen, sb, players, bullets, hearts, commies, hq_doors, walls)
			stats.in_game = True
	elif event.key == pygame.K_BACKSPACE:
		if stats.in_game:
			if not stats.paused and not stats.someone_won:
				switch_player_weapon(players[0], sb)

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
			if not stats.paused and not stats.someone_won:
				switch_player_weapon(players[1], sb)
	elif event.key == pygame.K_SPACE:
		if stats.in_game:
			if not stats.paused and not stats.someone_won:
				fire(bullets[1], settings, screen, players[1], pl_bombs[1], sb)
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
	
def check_keyup_events(event, settings, screen, players, bullets, stats, sb, hearts, commies, hq_doors, pl_bombs):
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
		pass
	elif event.key == pygame.K_SPACE:
		if players[1].arming_bomb:
			fire(bullets[1], settings, screen, players[1], pl_bombs[1], sb)
	elif event.key == pygame.K_RETURN:
		if players[0].arming_bomb:
			fire(bullets[0], settings, screen, players[0], pl_bombs[0], sb)
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

def switch_player_weapon(player, sb):
	if player.selected_weapon == player.weapons[-1]:
		player.selected_weapon = player.weapons[0]
	else:
		try:
			wpn_idx = player.weapons.index(player.selected_weapon)
			player.selected_weapon = player.weapons[wpn_idx+1]
		except:
			player.selected_weapon = player.weapons[0]
		
	sb.prep_ammo_info()
			

	play_sound("robot.wav")

	if player.selected_weapon == "missile":
		player.aiming_up = True
	else:
		player.aiming_up = False

	sb.prep_current_weapon()

def fire(bullet_group, settings, screen, player, bomb_group, sb):
	if player.selected_weapon == "bullet" or player.selected_weapon == "missile":
		new_bullet(bullet_group, settings, screen, player)
	elif player.selected_weapon == "bomb":
		if player.ammo["bomb"] > 0:
			if not player.arming_bomb:
				player.arming_bomb = True
			elif player.arming_bomb:
				if player.arming_timer <= 0:
					new_bomb(bomb_group, screen, settings, player.centerx, player.centery, player, True)
					player.ammo["bomb"] -= 1
					player.arming_bomb = False
					player.arming_timer = settings.arming_time
				elif player.arming_timer > 0:
					player.arming_bomb = False
					player.arming_timer = settings.arming_time
		if player.ammo["bomb"] == 0:
			player.weapons.remove("bomb")
			switch_player_weapon(player, sb)
	sb.prep_ammo_info()

def new_bomb(bomb_group, screen, settings, xpos, ypos, player, activated):
	bomb = Bomb(screen, settings, xpos, ypos, player, activated)
	bomb_group.add(bomb)

def new_bullet(bullet_group, settings, screen, player):
	bullet = Bullet(settings, screen, player)
	bullet_group.add(bullet)
	

def update(screen, settings, players, stats, menu_buttons, bullets, menu_msgs, sb, items, walls, hq_doors, explos, pl_bombs, bomb_explos):
	if stats.in_game:
		if stats.current_commie == None:
			screen.blit(settings.in_game_bg,(0,0))
		else:
			screen.blit(settings.in_game_commie_bg, (0,0))

		for hq_door in hq_doors:
			hq_door.blitme()

		for wa in walls.sprites():
			wa.blitme()

		for pl_bomb_group in pl_bombs:
			for bomb in pl_bomb_group.sprites():
				bomb.draw_item()

		for player in players:
			player.blitme()
		
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

		for pl in players:
			for heart in pl.hq_hearts.sprites():
				heart.draw_item()

		for exp in explos:
			exp.draw(screen)

		for b_exp in bomb_explos:
			b_exp.draw(screen)

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

def update_pl_bombs(pl_bombs, bomb_explos, screen):
	for bomb_group in pl_bombs:
		if bomb_group:
			for bomb in bomb_group.sprites():
				if bomb.timer <= 0:
					play_sound("bomb_explosion.wav")
					newExplo = ExplosionSprite(screen, bomb.rect, "bomb", bomb.my_creator)
					expl = Group(newExplo)
					bomb_explos.append(expl)
					bomb_group.remove(bomb)

def update_bomb_explos(bomb_explos, dt):
	if bomb_explos:
		try:
			for idx, exp in enumerate(bomb_explos[:]):
				for ex in exp:
					if ex.index >= 8:
						del bomb_explos[idx]
				exp.update(dt)
		except:
			pass

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
							sb.prep_health_bars()
						else:
							play_sound("hit.wav")
							players_bullets.remove(bullet)
							player.health -= settings.bullet_damage
							sb.prep_health_scores()
							sb.prep_health_bars()
				
def check_bullet_plane_collide(settings, screen, planes, items, players, stats, sb, bullets, explos):
	# For every players bullet group, check for collision with plane
	for bullet_group in bullets:
		collisions = pygame.sprite.groupcollide(planes, bullet_group, False, False)

		for plane, bullets in collisions.items():
			for bullet in bullets[:]:
				if bullet.is_missile:
					play_sound("explode.wav")
					item = plane.release_item(plane.centerx, plane.centery)
					if type(item) == Heart:
						items[0].add(item)
					elif type(item) == Commie:
						items[1].add(item)
					elif type(item) == Bomb:
						items[3].add(item)
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

			if door.ruined:
				pass

			else:
				if door.player.player_num == player.player_num:
					hit = player.rect.colliderect(door.door_trigger_rect)
					
					if hit:
						#door = hq_doors[idx]
						if player.moving_up:
							if door.is_closed:
								player.moving_up = False
								player.centery += 10
								play_sound("door.wav")
								door.open()
							elif door.is_open:
								play_sound("door.wav")
								door.close()
						elif player.moving_down:
							if door.is_closed:
								player.moving_down = False
								player.centery -= 10
								play_sound("door.wav")
								door.open()
							elif door.is_open:
								play_sound("door.wav")
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
					if not door.ruined:
						bullet_group.remove(bullet)


def check_player_heart_collide(settings, players, hearts, sb, stats, screen):
	# Check for collisions with hearts for every player
	for player in players:
		# Only let player pick up health if can_take_health
		if player.can_take_health:
			# Check for collisions with non-hq health
			collisions = pygame.sprite.spritecollide(player, hearts, True)

			if collisions:
				play_sound("blip.wav")
				# Add to player health
				if player.health + settings.heart_healing <= 100:
					player.health += settings.heart_healing
					sb.prep_health_scores()
					sb.prep_health_bars()
			
			# Check for collisions with hq health and its owner
			hqHearts = pygame.sprite.spritecollide(player, player.hq_hearts, True)
			if hqHearts:
				play_sound("blip.wav")
				for heart in hqHearts:
					if player.health + settings.heart_healing <= 100:
						player.health += settings.heart_healing
						sb.prep_health_scores()
						sb.prep_health_bars()

			# Check for collisions with hq health and other players
			for players_hq_health_to_check in players:
				if players_hq_health_to_check.player_num == player.player_num:
					continue
				else:
					hqHearts = pygame.sprite.spritecollide(player, players_hq_health_to_check.hq_hearts, True)
					if hqHearts:
						play_sound("blip.wav")
						for heart in hqHearts:
							if player.health + settings.heart_healing <= 100:
								player.health += settings.heart_healing
								sb.prep_health_scores()
								sb.prep_health_bars()
			
		elif not player.can_take_health:
			collisions = pygame.sprite.spritecollide(player, hearts, True)

			# If the player is not the commie
			if not stats.current_commie.player_num == player.player_num:
				if collisions:
					play_sound("blip.wav")
					#if stats.current_commie.health + settings.heart_healing <= 100:
						#stats.current_commie.health += settings.heart_healing
						#sb.prep_health_scores()
					heart = Heart(screen, settings, stats.current_commie.start_pos.centerx, stats.current_commie.start_pos.centery)
					stats.current_commie.hq_hearts.add(heart)



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
			if not collisions[0].ruined:
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
			else:
				#player.speed = 5
				pass

def check_bullet_wall_collide(settings, screen, bullets, walls):
	for bullet_group in bullets:
		collisions = pygame.sprite.groupcollide(walls, bullet_group, False, False)

		for wall, bullets in collisions.items():
			for bullet in bullets[:]:
				if bullet.is_missile:
					continue
				else:
					if not wall.ruined:
						bullet_group.remove(bullet)

def check_player_bomb_collide(settings, players, bombs, sb):
	for player in players:
		collisions = pygame.sprite.spritecollide(player, bombs, True)

		if collisions:
			play_sound("blip.wav")
			# Add to player ammo
			if player.ammo["bomb"] == 0:
				player.weapons.append("bomb")

			player.ammo["bomb"] += 1
			sb.prep_ammo_info()

def check_player_activated_bomb_collide(settings, players, pl_bombs, sb):
	for player in players:
		for bomb_group in pl_bombs:
			collisions = pygame.sprite.spritecollide(player, bomb_group, False)

			
			
def check_player_bomb_explosion_collide(settings, players, bomb_explos, sb):
	for player in players:
		for expl_group in bomb_explos:
			collisions = pygame.sprite.spritecollide(player, expl_group, False)

			if collisions:
				if player.health - settings.bomb_damage <= 0:
					player.health = 0
					sb.prep_health_bars()
					sb.prep_health_scores()					
				else:
					player.health -= settings.bomb_damage
					sb.prep_health_bars()
					sb.prep_health_scores()	
				
def check_explosion_wall_collide(settings, stats, bomb_explos, walls):
	for wall in walls:
		for expl_group in bomb_explos:
			collisions = pygame.sprite.spritecollide(wall, expl_group, False)

			if collisions:
				wall.destroy_wall()

def check_explosion_door_collide(settings, stats, bomb_explos, doors):
	for door in doors:
		for expl_group in bomb_explos:
			collisions = pygame.sprite.spritecollide(door, expl_group, False)

			if collisions:
				door.destroy_door()

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
