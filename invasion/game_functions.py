import sys
from time import sleep
import pygame
from bullet import Bullet
from vBullet import VBullet
from alien import Alien
from pygame import mixer
from explosion import ExplosionSprite
from pygame.sprite import Group

def check_keydown_events(event, my_settings, screen, ship, bullets, vBullets, stats, sb):
	"""Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(my_settings, screen, ship, bullets)
	elif event.key == pygame.K_v:
		if stats.vBullets_before_ship_lost > 0:
			stats.vBullets_before_ship_lost -= 1
			sb.prep_vBullets_left()
			fire_vBullet(my_settings, screen, ship, vBullets)
		else:
			stats.ships_left -= 1
			sb.prep_ships()
			fire_vBullet(my_settings, screen, ship, vBullets)
	elif event.key == pygame.K_q:
		sys.exit()

def fire_bullet(my_settings, screen, ship, bullets):
	"""Fire a bullet if limit not reached you."""
	# Create a new bullet and add it to the bullets group.
	if len(bullets) < my_settings.bullets_allowed:
		bullet_snd = pygame.mixer.Sound("sound/bullet.wav")
		bullet_snd.play()
		new_bullet = Bullet(my_settings, screen, ship)
		bullets.add(new_bullet)
		
def fire_vBullet(my_settings, screen, ship, vBullets):
	"""Fire a vBullet if limit not reached you."""
	# Create a new bullet and add it to the bullets group.
	if len(vBullets) < my_settings.vBullets_allowed:
		new_bullet = VBullet(my_settings, screen, ship)
		bullet_snd = pygame.mixer.Sound("sound/bullet.wav")
		bullet_snd.play()
		vBullets.add(new_bullet)
		
def check_keyup_events(event, ship):
	"""Respond to keypresses."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(my_settings, screen, stats, sb, play_button, ship, aliens, bullets, vBullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save_highscore(stats)
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, my_settings, screen, ship, bullets, vBullets, stats, sb)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(my_settings, screen, stats, sb, play_button, ship, aliens,
				bullets, mouse_x, mouse_y)
				
def save_highscore(stats):
	try:
		with open("hs.inv", "w") as hs_file:
			hs_file.write(str(round(stats.high_score, -1)))
	except FileNotFoundError:
		print("not found")		
			
def check_play_button(my_settings, screen, stats, sb, play_button, ship, aliens,
	bullets, mouse_x, mouse_y):
	"""Start a new game when the player clicks Play."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		#Reset the game settings.
		my_settings.initialize_dynamic_settings()
		
		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)
		
		# Reset the game statistics.
		stats.reset_stats()
		stats.game_active = True
		
		# Reset the scoreboard images.
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		sb.prep_ships()
		sb.prep_vBullets_left()
		
		# Empty the list of aliens and bullets.
		aliens.empty()
		bullets.empty()
		
		# Create a new fleet and center the ship.
		create_fleet(my_settings, screen, ship, aliens)
		ship.center_ship()

def update_explos(explos):
	if explos:
		for idx, exp in enumerate(explos[:]):
			for ex in exp:
				if ex.index >= 8:
					del explos[idx]
			exp.update()

def update_screen(my_settings, screen, stats, sb, ship, alien, bullets, vBullets, play_button, explos):
	"""Update images on the screen and flip to the new screen."""
	# Redraw the screen during each pass through the loop
	screen.fill(my_settings.bg_color)
	
	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	for vBullet in vBullets.sprites():
		vBullet.draw_bullet()
	
	ship.blitme()
	alien.draw(screen)
	
	# Draw the score information.
	sb.show_score()
	
	# Draw the play button if the game is inactive.
	if not stats.game_active:
		play_button.draw_button()
	
	#exp_group.draw(screen)
	#for expl in explos.sprites():
		#expl.update()
		
	for exp in explos:
		exp.draw(screen)
	
	# Make the most recently drawn screen visible
	pygame.display.flip()
	
def update_bullets(my_settings, screen, stats, sb, ship, aliens, bullets, vBullets, explos):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions.
	bullets.update()
	vBullets.update()
	
	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			
	# Get rid of vBullets that have dissapeared.
	for vBullet in vBullets.copy():
		if vBullet.rect.bottom <= 0:
			vBullets.remove(vBullet)
			
	check_bullet_alien_collisions(my_settings, screen, stats, sb, ship, aliens, bullets, vBullets, explos)
		
def check_bullet_alien_collisions(my_settings, screen, stats, sb, ship, aliens, bullets, vBullets, explos):
	"""Respond to bullet-alien collisions."""
	# Remove any bullets and aliens that have collided.
	bulls = [bullets, vBullets]
	
	b = pygame.sprite.groupcollide(bullets, aliens, False, False)
	for c, d in b.items():
		print(c.rect.x)
		print(c.rect.y)
		newExplo = ExplosionSprite(screen, c.rect)
		expl = Group(newExplo)
		explos.append(expl)
		
	v = pygame.sprite.groupcollide(vBullets, aliens, False, False)
	for c, d in v.items():
		print(c.rect.x)
		print(c.rect.y)
		newExplo = ExplosionSprite(screen, c.rect)
		expl = Group(newExplo)
		explos.append(expl)
	
	bulletCollisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	if bulletCollisions:
		
		explode_snd = pygame.mixer.Sound("sound/explode.wav")
		explode_snd.play()
		for aliens in bulletCollisions.values():
			stats.score += my_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)
		
	vBulletCollisions = pygame.sprite.groupcollide(vBullets, aliens, True, True)
		
	if vBulletCollisions:
		#exp_group.update()
		#exp_group.draw(screen)
		explode_snd = pygame.mixer.Sound("sound/explode.wav")
		explode_snd.play()
		for aliens in vBulletCollisions.values():
			stats.score += my_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)
	
	if len(aliens) == 0:
		# If the entire fleet is destroyed, start a new level.
		vBullets.empty()
		my_settings.increase_speed()
		
		# Increase level.
		stats.level += 1
		sb.prep_level()
		
		create_fleet(my_settings, screen, ship, aliens)

def get_number_aliens_x(my_settings, alien_width):
	"""Determine the number of aliens that fit in a row."""
	available_space_x = my_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(my_settings, ship_height, alien_height):
	"""Determine the number of rows of aliens that fit on the screen."""
	available_space_y = (my_settings.screen_height - (3*alien_height)- ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def create_alien(my_settings, screen, aliens, alien_number, row_number):
	"""Create an alien and place it in the row."""
	alien = Alien(my_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(my_settings, screen, ship, aliens):
	"""Create a full fleet of aliens."""
	# Create an alien and find the number of aliens in a row.
	alien = Alien(my_settings, screen)
	number_aliens_x = get_number_aliens_x(my_settings, alien.rect.width)
	number_rows = get_number_rows(my_settings, ship.rect.height,
		alien.rect.height)
	
	# Create the fleet of aliens.
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(my_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(my_settings, aliens):
	"""Respond appropriately if any aliens have reached an edge."""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(my_settings, aliens)
			break
			
def change_fleet_direction(my_settings, aliens):
	"""Drop the entire fleet and change the fleet's direction."""
	for alien in aliens.sprites():
		alien.rect.y += my_settings.fleet_drop_speed
	my_settings.fleet_direction *= -1

def ship_hit(my_settings, stats, screen, sb, ship, aliens, bullets):
	"""Respond to ship being hit by alien."""
	if stats.ships_left > 0:
	
		# Decrement ships_left.
		stats.ships_left -= 1
		
		# Update scoreboard.
		sb.prep_ships()
		
		# Empty the list of aliens and bullets.
		aliens.empty()
		bullets.empty()
		
		# Create a new fleet and center the ship.
		create_fleet(my_settings, screen, ship, aliens)
		ship.center_ship()
		
		# Pause
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(my_settings, stats, screen, sb, ship, aliens, bullets):
	"""Check if any aliens have reached the bottom of the screen."""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Treat this the same as if the ship got hit.
			ship_hit(my_settings, stats, screen, sb, ship, aliens, bullets)
			break

def update_aliens(my_settings, stats, screen, sb, ship, aliens, bullets, vBullets):
	"""Check if the fleet is at an edge,
		and then update the positions of all aliens in the fleet.
	"""
	check_fleet_edges(my_settings, aliens)
	aliens.update()
	
	# Look for alien-ship collisions.
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(my_settings, stats, screen, sb, ship, aliens, bullets)
		
	# Look for aliens hitting the bottom of the screen.
	check_aliens_bottom(my_settings, stats, screen, sb, ship, aliens, bullets)
	
def check_high_score(stats, sb):
	"""Check to see if there's a new high score."""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
