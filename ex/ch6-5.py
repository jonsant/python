rivers = {"nile": "egypt", "amazon": "brazil", "yangtze": "china"}

for river, country in rivers.items():
	print("The " + river + " runs throught " + country)

print("\n")
	
for river in rivers.keys():
	print(river)

print("\n")

for country in rivers.values():
	print(country)
