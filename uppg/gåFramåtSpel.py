import random

class Enemy():
	def __init__(self, health):
		self.health = health
		self.lives=True

	def info(self):
		print("Information for object:")
		print("Name: " + self.name)
		print("Foods: " + self.food)
		print("Allergies: " + self.allergies)
		print("Other: " + self.other)
		if self.lives == True:
			print("Alive: Yes")
		else:
			print("Alive: No")
	def takeahit(self):
		print("Enemy" + " got hit for 10 hp")
		print(str(self.health) + " hp left")
		self.health-=10
		if self.health <= 0:
			self.lives=False
			print("Enemy killed")
			
class Player():
	def __init__(self, health):
		self.health = health
		self.lives=True
		
	def info(self):
		print("Player: ")
		print("Health: " + str(self.health))
		
	def takeahit(self):
		print("\nHit by enemy!")
		self.health-=10
		if self.health <= 0:
			self.lives=False
			print("Game over")
			
Active=True

while Active:
	print("1. Play")
	print("2. Quit")
	choice = int(input("Choose: "))
	
	if choice == 1:
		
		enemies=[]
		player = Player(100)
		
		while player.lives:
			print("1. Walk")
			if enemies:
				print("2. Hit")
			print("3. Player info")
				
			choice = int(input("Choose: "))
			if choice == 1:
				slumpnmr = random.randint(1,9)
				if slumpnmr >= 7:
					print("Enemy found!")
					enemies.append(Enemy(random.randint(1,100)))
					
			elif choice == 2 and enemies:
				slumpnmr = random.randint(1,9)
				if slumpnmr == 9:
					player.takeahit()
					if player.lives == False:
						break
				if enemies[-1].lives:
					enemies[-1].takeahit()
					if enemies[-1].lives == False:
						del enemies[-1]
						
			elif choice == 3:
				player.info()		
			print("\t")
	if choice == 2:
		Active = False
