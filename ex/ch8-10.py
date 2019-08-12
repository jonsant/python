def show_magicians(magicians):
	magicians = make_great(magicians)
	for magician in magicians:
		print(magician)

def make_great(magicians):
	newMagicians = []
	for magician in magicians:
		newMagicians.append(magician + " the Great")
	return newMagicians
		
magicians = ["copperfield", "penn & teller", "angel"]
show_magicians(magicians)

