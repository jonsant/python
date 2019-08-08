
pizzas = ["pizza1", "pizza2", "pizza3"]
friend_pizzas = pizzas[:]

pizzas.append("pizza4")
friend_pizzas.append("another pizza")

for pizza in pizzas:
	print("My favorite pizzas are " + pizza)
	
for pizza in friend_pizzas:
	print("My friends favorite pizzas are " + pizza)


