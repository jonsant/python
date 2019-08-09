import random

numTimes = 0
gameActive = True
slmpnmr = random.randint(1,99)


while gameActive:
	
	
	answer = input("Gissa mitt nummer! ")
	
	if numTimes < 9:
		if int(answer) < slmpnmr:
			print("Högre")
			numTimes += 1
		elif int(answer) > slmpnmr:
			print("Lägre")
			numTimes += 1
		elif int(answer) == slmpnmr:
			print("Rätt! På " + str(numTimes + 1) + " försök!")
			cont = input("Spela igen? J/N")
			if cont == "n":
				gameActive = False
			else:
				slmpnmr = random.randint(1,99)
				numTimes = 0
	elif numTimes >= 9:
		print("Sorry...")
		cont = input("Spela igen? J/N")
		if cont == "n":
			gameActive = False
		else:
			slmpnmr = random.randint(1,99)
			numTimes = 0
