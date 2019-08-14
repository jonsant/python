import random

class Enemy():
	def __init__(self, health, power, isBoss=False):
		self.health = health
		self.power = power
		self.lives=True
		self.coins = random.randint(1,2)
		self.isBoss = isBoss

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
			print("Enemy killed and dropped " + str(self.coins) + " coins!")
		else:
			print("Enemy hp: " + str(self.health))
			
	def disappear(self):
		print("Enemy disappeared!")
		
class Boss(Enemy):
	
	def __init__(self, health=200, power=40):
		super().__init__(health=200, power=40, isBoss=True)
		self.coins = random.randint(3,7)
		
	def blockHit(self):
		print("Boss blocked it!\n")
			
class Player():
	def __init__(self, health):
		self.health = health
		self.bag = {"Coins": 0}
		self.lives=True
		
	def info(self):
		print("\nPlayer:\nHealth - " + str(self.health))
		for item, value in self.bag.items():
			print(item + " - " + str(value))
		
	def takeahit(self, enemy):
		self.health-=enemy.power
		print("\nHit by enemy!")
		if self.health <= 0:
			self.lives=False
			print("Out of hp!")
			print("Game over")
		else:
			print("You have " + str(self.health) + " hp left!")
	
	def addCoins(self, coins):
		self.bag["Coins"] += coins
		
	def buyHealth(self, coins):
		coins = int(coins)
		if coins <= self.bag.get("Coins"):	
			self.health += coins*10
			self.bag["Coins"] -= coins
			print("Added " + str(coins*10) + " hp!\nTotal hp: " + str(self.health))
		else:
			print("Not enough coins!")
			
Active=True

while Active:
	print("1. Play")
	print("2. Quit")
	mainChoice = input("Choose: ")
	if mainChoice != '':
		mainChoice = int(mainChoice)
	else:
		continue
	print()
	
	if mainChoice == 1:
		
		enemies=[]
		player = Player(100)
		
		while player.lives:
			
			if enemies:
				print("1. Run")
				print("2. Hit")
			else:
				print("1. Walk")
			print("3. Player info")
			if enemies:
				print("4. Show enemies")
			if player.bag.get("Coins") > 0:
				print("5. Buy health")
			print("9. Quit")
				
			choice = input("Choose: ")
			if choice != '':
				choice = int(choice)
			else:
				print()
				continue
			print()
			if choice == 1:
				if enemies:
					
					#Enemy hits player
					slumpnmr = random.randint(1,9)
					if slumpnmr == 9:
						player.takeahit(enemies[-1])
					
					#Player runs away from enemy
					slumpnmr = random.randint(1,5)
					if slumpnmr == 1:
						print("Ran away!")
						del enemies[-1]
				
				#New enemy is found		
				slumpnmr = random.randint(1,9)
				if slumpnmr >= 7:
					if random.randint(1,4) == 1:
						print("Boss found!!")
						enemies.append(Boss())
					else:
						print("Enemy found!")
						enemies.append(Enemy(
							health=random.randint(1,100),
							power=random.randint(10,20)))
			
			#Player hits enemy		
			elif choice == 2 and enemies:
				slumpnmr = random.randint(1,9)
				#Enemy hits back at player
				if slumpnmr == 9:
					player.takeahit(enemies[-1])
					if player.lives == False:
						continue
				#Player hits enemy, or enemy gets killed & removed
				if enemies[-1].lives:
					#If enemy is Boss, it sometimes blocks player
					if enemies[-1].isBoss:
						if random.randint(1,3) == 1:
							enemies[-1].blockHit()
							continue
												
					enemies[-1].takeahit()
					if enemies[-1].lives == False:
						player.addCoins(enemies[-1].coins)
						del enemies[-1]
						
			elif choice == 3:
				player.info()
				
			elif choice == 4:
				for key,enemy in enumerate(enemies):
					print("Enemy " + str(key+1) + ": " + str(enemy.health) + " hp")
			elif choice == 5:
				if player.bag.get("Coins") > 0:
					
					coins = input("How many coins do you wanna use? (1 coin = 10 hp): ")
					if coins != '':
						player.buyHealth(coins)
				
			elif choice == 9:
				break
						
			print("\t")
	if mainChoice == 2:
		print("Bye!")
		Active = False
	print("\n")
