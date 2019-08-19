
class SuperClass():
	def __init__(self):
		if type(self) == SuperClass:
			raise Exception("<SuperClass> must be subclassed.")

class SubClassOne(SuperClass):
	def __init__(self):
		SuperClass.__init__(self)

class SubSubClass(SubClassOne):
	def __init__(self):
		SubClassOne.__init__(self)

class SubClassTwo(SubClassOne, SuperClass):
	def __init__(self):
		SubClassOne.__init__(self)
		SuperClass.__init__(self)

subC = SubClassOne()

try:
	supC = SuperClass()
except Exception as e:
	print("FAILED: supC = SuperClass() - " + str(e))
else:
	print("SUCCESS: supC = SuperClass()")

try:
	subSubC = SubSubClass()
except Exception as e:
	print("FAILED: subSubC = SubSubClass() - " + str(e))
else:
	print("SUCCESS: subSubC = SubSubClass()")

try:
	subC2 = SubClassTwo()
except Exception as e:
	print("FAILED: subC2 = SubClassTwo() - " + str(e))
else:
	print("SUCCESS: subC2 = SubClassTwo()")
