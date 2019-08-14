import json

try:
	with open("ch10-11.txt") as file_obj:
		num = json.load(file_obj)
except FileNotFoundError:
		print("Couldn't find you favorite number!")
else:
	print("I know your favorite number: " + str(num)
		+ "!")
