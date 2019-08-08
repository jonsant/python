print("Vad heter du? ")
namn = input()
print("Hur gammal är du? ")
age = input()
print("Hej, " + namn.title() + "!\n" + age + "??? ojoj!")


if int(age) < 50:
	left = 50 - int(age)
	print("50 om " + str(left) + " år!")
