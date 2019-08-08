qubes = []
for val in range(1, 11):
	number = val**3
	qubes.append(number)
	
for qube in qubes:
	print(qube)

print("First 3 items: " + str(qubes[0:3]))

print("3 items: " + str(qubes[3:6]))

print("Last 3 items: " + str(qubes[-3:]))
