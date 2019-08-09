person1 = {"first_name": "erik", "last_name": "eriksson", "age": 33, "city": "husaby"}
person2 = {"first_name": "nils", "last_name": "nilsson", "age": 55, "city": "malmö"}
person3 = {"first_name": "palle", "last_name": "pallrasson", "age": 12, "city": "luleå"}

people = [person1, person2, person3]

for person in people:
	for key, value in person.items():
		if key == "age":
			value = int(value)
			print(key + " : " + str(value))
			break
		print(key + " : " + value)
	print("\n")
