unames = ["kalle", "torleif", "bosse", "inge", "admin"]

if len(unames) != 0:

	for name in unames:
		if name == "admin":
			print("Hello admin, see status report?")
		else:
			print("Hello " + name)
else:
	print("Need to find some users!")
