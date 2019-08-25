import pygame
import sys
from pygame.locals import *
from bullet import Bullet
import pygame.font

def check_events(settings, screen, players, menu_buttons, stats, joysticks, bullets, menu_msgs):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, players, bullets)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, settings, screen, players)
			
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_menu_button(settings, mouse_x, mouse_y, menu_buttons, stats, joysticks, screen, menu_msgs)
		elif event.type == pygame.JOYAXISMOTION:
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
						players[1].moving_right = True
						players[1].direction = "right"
						
					elif val == 0:
						players[1].moving_right = False
						players[1].moving_left = False
						
					elif val == -1:
						players[1].moving_left = True
						players[1].direction = "left"
						
				elif event.axis == settings.joystick_yaxis:
					if val == 1:
						players[1].moving_down = True
						players[1].direction = "down"
					
					elif val == 0:
						players[1].moving_down = False
						players[1].moving_up = False
						
					elif val == -1:
						players[1].moving_up = True
						players[1].direction = "up"
		elif event.type == pygame.JOYBUTTONDOWN:
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
					menu_msgs.prep_main_msg("Controller Setup!")
					settings.show_main_msg = True
					settings.buttons_left = 0
					stats.in_settings = False
					
			else:
				if event.button == settings.joystick_a:
					new_bullet(bullets[1], settings, screen, players[1])
			
def check_menu_button(settings, mouse_x, mouse_y, menu_buttons, stats, joysticks, screen, menu_msgs):
	
	for btn in menu_buttons:
		btn_clicked = btn.rect.collidepoint(mouse_x, mouse_y)
	
		if btn_clicked:
			if not stats.in_game:
				if btn.button_type == "play":
					stats.in_game = True
				elif btn.button_type == "settings":
					if joysticks:
						settings.show_main_msg = False
						stats.in_settings = True
					else:
						settings.show_main_msg = True
				elif btn.button_type == "quit":
					sys.exit()
			elif stats.in_game and stats.someone_won:
				if btn.button_type == "quit":
					stats.in_game = False
					
					
		
def check_keydown_events(event, settings, screen, players, bullets):
	
	if event.key == pygame.K_RIGHT:
		players[0].moving_right = True
		players[0].direction = "right"
	elif event.key == pygame.K_LEFT:
		players[0].moving_left = True
		players[0].direction = "left"
	elif event.key == pygame.K_UP:
		players[0].moving_up = True
		players[0].direction = "up"
	elif event.key == pygame.K_DOWN:
		players[0].moving_down = True
		players[0].direction = "down"
	elif event.key == pygame.K_RETURN:
		new_bullet(bullets[0], settings, screen, players[0])
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
	elif event.key == pygame.K_SPACE:
		new_bullet(bullets[1], settings, screen, players[1])
	elif event.key == pygame.K_q:
		sys.exit()
	
def check_keyup_events(event, settings, screen, players):
	if event.key == pygame.K_RIGHT:
		players[0].moving_right = False
	elif event.key == pygame.K_LEFT:
		players[0].moving_left = False
	elif event.key == pygame.K_UP:
		players[0].moving_up = False
	elif event.key == pygame.K_DOWN:
		players[0].moving_down = False
	elif event.key == pygame.K_a:
		players[1].moving_left = False
	elif event.key == pygame.K_d:
		players[1].moving_right = False
	elif event.key == pygame.K_w:
		players[1].moving_up = False
	elif event.key == pygame.K_s:
		players[1].moving_down = False

def new_bullet(bullet_group, settings, screen, player):
	bullet = Bullet(settings, screen, player)
	bullet_group.add(bullet)
	

def update(screen, settings, players, stats, menu_buttons, bullets, menu_msgs, sb):
	if stats.in_game:
		screen.blit(settings.in_game_bg,(0,0))
		
		for player in players:
			player.blitme()
		
		for players_bullets in bullets:
			for bullet in players_bullets.sprites():
				bullet.blitme()
				
		sb.draw_scores()
		
		if stats.someone_won:			
			for btn in menu_buttons:
				if btn.button_type == "quit":
					btn.draw_quit_button()	
	
		pygame.display.flip()
	
	elif stats.in_settings:
		screen.blit(settings.settings_bg, (0,0))
		
		menu_msgs.show_settings_msgs()
		
		pygame.display.flip()
		
	else:
		screen.blit(settings.menu_bg, (0,0))
		
		
		for idx, btn in enumerate(menu_buttons):
			btn.draw_button(idx + 1, len(menu_buttons))
		
		menu_msgs.show_main_menu_msgs()
		
		pygame.display.flip()

def update_bullets(bullets, screen, players, settings, stats, sb):
	for idx, players_bullets in enumerate(bullets):
		players_bullets.update()
		
		# If bullet is outside of screen, remove from group
		for bullet in players_bullets.copy():
			if bullet.rect.bottom <= 0 or bullet.rect.top >= screen.get_rect().bottom or bullet.rect.left >= screen.get_rect().right or bullet.rect.right <= screen.get_rect().left:
				players_bullets.remove(bullet)
	if not stats.someone_won:			
		for idx, players_bullets in enumerate(bullets):
			check_bullet_enemy_collisions(players_bullets, idx, screen, players, settings, stats, sb)

def check_bullet_enemy_collisions(players_bullets, bullet_idx, screen, players, settings, stats, sb):
	for player_idx, player in enumerate(players):
		# If current player is the owner of the bullets, don't check for collisions
		if bullet_idx == player_idx:
			continue
		else:
			collisions = pygame.sprite.spritecollide(player, players_bullets, True)
			if collisions:
				if (player.health - settings.bullet_damage) <= 0:
					stats.someone_won = True
					player.health = 0
					sb.prep_info_text("Player " + str(player.player_num) + " won!")
				else:
					player.health -= settings.bullet_damage
				
	
def check_player_collide(settings, players):
	hit = players[0].rect.colliderect(players[1].rect)
	if hit:
		for player in players:	
			if player.moving_right:
				player.moving_right = False
				player.centerx -= 10
				player.moving_right = True
			if player.moving_left:
				player.moving_left = False
				player.centerx += 10
				player.moving_left = True
			if player.moving_up:
				player.moving_up = False
				player.centerx += 10
				player.moving_up = True
			if player.moving_down:
				player.moving_down = False
				player.centerx -= 10
				player.moving_down = True
		
