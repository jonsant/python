person = {"first_name": "erik", "last_name": "eriksson", "age": 33, "city": "husaby"}

for key, value in person.items():
	if key == "age":
		value = int(value)
		print(key + " " + str(value))
		break
	print(key + " " + value)
