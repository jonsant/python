name = ""

while name != "q":
	
	name = input("Your name? (q for quit) ")
	if name != "q":
		print("Hello " + name + "!")
		with open("ch10-4.txt", "a") as text_file:
			text_file.write(name + " was here!\n")
		
print("Bye!")
