guests = []

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
		
		guests.append({"name": name, "food": food, "allergies": allergies,
			"drink": drink, "other": other, "arrived": False})
		print(name + " added!\n")
	
	#Arrived
	elif choice == "2":
		if guests:
			name = input("Name? ")
			print("\n")
			for guest in guests:
				if guest["name"] == name:
					guest["arrived"] = True
					for key, info in guest.items():
						if key == "arrived":
							continue
						print(key + " : " + info)
					print("welcome!\n")
				
		else:
			print("Empty!\n")
	#Quit
	elif choice == "3":
		print("Bye!")
		run = False
