class GameStats():
	"""Track statistics for Alien Invasion."""
	
	def __init__(self, my_settings):
		"""Initialize statistics."""
		self.my_settings = my_settings
		self.reset_stats()
		
		# Start Invasion in an inactive state.
		self.game_active = False
		
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.my_settings.ship_limit
