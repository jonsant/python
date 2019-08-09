favorite_places = {"kalle": ["paris"], "erik": ["stockholm", "moskva"], "nicke": ["pyonyang"]}

for name, places in favorite_places.items():
	print(name + " : ")
	for place in places:
		print(place)
	print("\n")
