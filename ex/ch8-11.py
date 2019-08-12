def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians):
	newMagicians = []
	for magician in magicians:
		newMagicians.append(magician + " the Great")
	return newMagicians
		
magicians = ["copperfield", "penn & teller", "angel"]
magiciansGreat = make_great(magicians[:])
show_magicians(magicians)
print("\n")
show_magicians(magiciansGreat)


