import pygame
import settings as settings
import sys
from pygame.locals import *

def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			check_keydown_events()
		
		elif event.type == pygame.KEYUP:
			check_keyup_events()
		
def check_keydown_events():
	print("jk")
	
def check_keyup_events():
	print("ll")
	
def update(screen, settings, player1):
	screen.blit(settings.bg,(0,0))
	
	
	player1.blitme()
	
	pygame.display.flip()
