guests = [{
	"phone": "222",
	"name": "evert",
	"food": "sill",
	"allergies": "gluten",
	"drink": "beer",
	"other": "",
	"arrived": False
	},
	{
	"phone": "111",
	"name": "ingvar",
	"food": "makrill",
	"allergies": "",
	"drink": "beer",
	"other": "",
	"arrived": False
	}]

run = True

while run:
	choice = input("1: Add guest, 2: Arrived, 3: quit\n")
	
	#Add
	if choice == "1":
		phone = input("phone")
		name = input("Name? ")
		food = input("Food? ")
		allergies = input("Allergies? ")
		drink = input("Drink? ")
		other = input("Other? ")
		
		guests.append({
			"phone": phone,
			"name": name,
			"food": food,
			"allergies": allergies,
			"drink": drink,
			"other": other,
			"arrived": False
			})
		print(name + " added!\n")
	
	#Arrived
	elif choice == "2":
		if guests:
			phone = input("Phone? ")
			print("\n")
			for guest in guests:
				if phone == guest["phone"]:
					if guest["arrived"] == True:
						print("Already arrived...\n")
					else:	
						guest["arrived"] = True
						for key, info in guest.items():
							if key == "arrived":
								continue
							print(key + " : " + info)
						print("\nWelcome!\n")
				
		else:
			print("Empty!\n")
	#Quit
	elif choice == "3":
		print("Bye!")
		run = False

