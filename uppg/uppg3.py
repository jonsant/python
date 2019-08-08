frukter = []

for varv in range(1,4):
	print("Skriv en frukt")
	frukter.append(input().title())

for index, frukt in enumerate(frukter):
	print("På plats " + str(index) +  " finns " + frukt + ".")

