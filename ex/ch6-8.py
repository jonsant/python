pet1 = {"animal": "dog", "ownerName": "peter"}
pet2 = {"animal": "cat", "ownerName": "gilrod"}
pet3 = {"animal": "frog", "ownerName": "yngve"}

pets = [pet1, pet2, pet3]

for pet in pets:
	for key, value in pet.items():
		if key == "age":
			value = int(value)
			print(key + " : " + str(value))
			break
		print(key + " : " + value)
	print("\n")

