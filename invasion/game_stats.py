class GameStats():
	"""Track statistics for Alien Invasion."""
	
	def __init__(self, my_settings):
		"""Initialize statistics."""
		self.my_settings = my_settings
		self.reset_stats()
		
		# High score should never be reset.
		self.high_score = 0
		self.load_highscore()
		
		# Start Invasion in an inactive state.
		self.game_active = False
		
	def load_highscore(self):
		try:
			with open("hs.inv", "r") as hs_file:
				hs = hs_file.read()
				self.high_score = int(hs)
		except FileNotFoundError:
			print("not found")
		
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.my_settings.ship_limit
		self.score = 0
		self.level = 1
