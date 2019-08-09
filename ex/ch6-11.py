cities = {
	"new york":
		{"country": "usa",
		"population": "8 million",
		"fact": "One of the world's major commercial, financial and cultural centers."},
	"paris":
		{"country": "france",
		"population": "2 million",
		"fact": "Home of the Eiffel Tower."},
	"pyongyang":
		{"country": "north korea",
		"population": "3 million",
		"fact": "Area Code: 2"}
	}
	
for city, infoDict in cities.items():
	print(city + ": ")
	for key, value in infoDict.items():
		print(key + " : " + value)
	
