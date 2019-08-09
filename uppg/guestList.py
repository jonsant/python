vip = ["Erik", "Niklas", "Gunnar"]

name = input("Vad heter du? ")

if name in vip:
	print("Välkommen " + name + "!")
else:
	age = input("Hur gammal är du? ")
	age = int(age)
	if age >= 25:
		print("Välkommen " + name + "!")
	elif age < 25:
		print("Du är för ung " + name + "!")
