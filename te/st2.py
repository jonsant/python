class MinKlass():
	a = "apa"
	def __init__(self):
		if type(self) == MinKlass:
			raise Exception("Ingen instantiering!")

print(MinKlass.a)
mk = MinKlass()
