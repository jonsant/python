name = input("Your name? ")

with open("ch10-3.txt", "w") as file_obj:
	file_obj.write(name + "\n")
