guests = {}
run = True

while run:
	choice = input("1: Add guest, 2: Arrived, 3: quit\n")
	
	#Add
	if choice == "1":
		name = input("Name? ")
		food = input("Food? ")
		allergies = input("Allergies? ")
		drink = input("Drink? ")
		other = input("Other? ")
		
		guests[name] = {"name": name, "food": food, "allergies": allergies,
			"drink": drink, "other": other, "arrived": False}
		print(name + " added!\n")
	
	#Arrived
	elif choice == "2":
		if guests:
			name = input("Name? ")
			print("\n")
			
			#Guest already arrived
			if guests[name].get("arrived") == True:
				print("Already here!")
			#Guest not arrived yet
			else:
				guests[name]["arrived"] = True
				for key, val in guests[name].items():
					if key == "arrived":
						continue
					else:
						print(key + " : " + val)
					
			print("\n")
				
		else:
			print("Empty!\n")
	#Quit
	elif choice == "3":
		print("Bye!")
		run = False
	else:
		print("?")

