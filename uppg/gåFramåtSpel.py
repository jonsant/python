import random

class Enemy():
	def __init__(self, health, power):
		self.health = health
		self.power = power
		self.lives=True

	def info(self):
		print("Enemy health: " + str(self.health))
		if self.lives == True:
			print("Alive: Yes")
		else:
			print("Alive: No")
	def takeahit(self):
		print("Enemy" + " got hit for 10 hp")
		self.health-=10
		if self.health <= 0:
			self.lives=False
			print("Enemy killed")
		else:
			print(str(self.health) + " hp left")
			
class Player():
	def __init__(self, health):
		self.health = health
		self.lives=True
		
	def info(self):
		print("Player: ")
		print("Health: " + str(self.health))
		
	def takeahit(self, enemy):
		self.health-=enemy.power
		print("\nHit by enemy!")
		if self.health <= 0:
			self.lives=False
			print("Game over")
		else:
			print("You have " + str(self.health) + " hp left!")
			
Active=True

while Active:
	print("1. Play")
	print("2. Quit")
	mainChoice = int(input("Choose: "))
	
	if mainChoice == 1:
		
		enemies=[]
		player = Player(100)
		
		while player.lives:
			print("1. Walk")
			if enemies:
				print("2. Hit")
			print("3. Player info")
			if enemies:
				print("4. Show enemies")
				
			choice = int(input("Choose: "))
			if choice == 1:
				if enemies:
					slumpnmr = random.randint(1,9)
					if slumpnmr == 9:
						player.takeahit(enemies[-1])
				slumpnmr = random.randint(1,9)
				if slumpnmr >= 7:
					print("Enemy found!")
					enemies.append(Enemy(
						health=random.randint(1,100),
						power=random.randint(10,40)))
					
			elif choice == 2 and enemies:
				slumpnmr = random.randint(1,9)
				if slumpnmr == 9:
					player.takeahit(enemies[-1])
					if player.lives == False:
						continue
				if enemies[-1].lives:
					enemies[-1].takeahit()
					if enemies[-1].lives == False:
						del enemies[-1]
						
			elif choice == 3:
				player.info()
				
			elif choice == 4:
				print("\n")
				for key,enemy in enumerate(enemies):
					print(str(key+1) + ": " + str(enemy.health) + " hp")
						
			print("\t")
	if mainChoice == 2:
		print("Bye!")
		Active = False
	print("\n")
