while True:
	
	num1 = input("Write a number (q=quit): ")
	if num1 == "q":
		print("Bye!")
		break
	
	try:
		num1 = int(num1)
	except ValueError:
		print("Only numbers!")
	else:
		num2 = input("Write a second number (q=quit): ")
		if num2 == "q":
			print("Bye")
			break
		try:
			num2 = int(num2)
		except ValueError:
			print("Only numbers!")
		else:
			answer = num1+num2
			print(str(num1)
				+ " + " + str(num2)
				+ " = " + str(answer))
	
