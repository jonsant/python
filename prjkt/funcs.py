import pygame
import settings as settings
import sys
from pygame.locals import *

def check_events(settings, screen, player1, player2):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, player1, player2)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, settings, screen, player1, player2)
		
def check_keydown_events(event, settings, screen, player1, player2):
	if event.key == pygame.K_RIGHT:
		player1.moving_right = True
	elif event.key == pygame.K_LEFT:
		player1.moving_left = True
	elif event.key == pygame.K_UP:
		player1.moving_up = True
	elif event.key == pygame.K_DOWN:
		player1.moving_down = True
	elif event.key == pygame.K_a:
		player2.moving_left = True
	elif event.key == pygame.K_d:
		player2.moving_right = True
	elif event.key == pygame.K_w:
		player2.moving_up = True
	elif event.key == pygame.K_s:
		player2.moving_down = True
	elif event.key == pygame.K_q:
		sys.exit()
	
def check_keyup_events(event, settings, screen, player1, player2):
	if event.key == pygame.K_RIGHT:
		player1.moving_right = False
	elif event.key == pygame.K_LEFT:
		player1.moving_left = False
	elif event.key == pygame.K_UP:
		player1.moving_up = False
	elif event.key == pygame.K_DOWN:
		player1.moving_down = False
	elif event.key == pygame.K_a:
		player2.moving_left = False
	elif event.key == pygame.K_d:
		player2.moving_right = False
	elif event.key == pygame.K_w:
		player2.moving_up = False
	elif event.key == pygame.K_s:
		player2.moving_down = False
	
def update(screen, settings, player1, player2):
	screen.blit(settings.bg,(0,0))
	
	
	player1.blitme()
	player2.blitme()
	
	pygame.display.flip()
	
def check_player_collide(settings, player1, player2):
	hit = player1.rect.colliderect(player2.rect)
	if hit:
		if player1.moving_right:
			player1.moving_right = False
			player1.centerx -= 10
			player1.moving_right = True
		if player1.moving_left:
			player1.moving_left = False
			player1.centerx += 10
			player1.moving_left = True
		if player1.moving_up:
			player1.moving_up = False
			player1.centerx += 10
			player1.moving_up = True
		if player1.moving_down:
			player1.moving_down = False
			player1.centerx -= 10
			player1.moving_down = True
			
		if player2.moving_right:
			player2.moving_right = False
			player2.centerx -= 10
			player2.moving_right = True
		if player2.moving_left:
			player2.moving_left = False
			player2.centerx += 10
			player2.moving_left = True
		if player2.moving_up:
			player2.moving_up = False
			player2.centerx += 10
			player2.moving_up = True
		if player2.moving_down:
			player2.moving_down = False
			player2.centerx -= 10
			player2.moving_down = True
		
