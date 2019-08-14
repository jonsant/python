import json

num = input("Your favorite number?: ")

try:
	num = int(num)
except ValueError:
	print("Only numbers please!")
else:
	filename = "ch10-11.txt"
	with open(filename, "w") as file_obj:
		json.dump(num, file_obj)
		file_obj.write("\n")
	print("Thanks!")
