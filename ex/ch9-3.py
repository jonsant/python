class User():
	
	def __init__(self, first_name, last_name, **information):
		self.first_name = first_name
		self.last_name = last_name
		self.info = {}
		for key, val in information.items():
			self.info[key] = val
		
	def describe_user(self):
		print("Name: " + self.first_name + " " + self.last_name)
		if self.info:
			for key, val in self.info.items():
				if key == "ålder":
					print(key + ": " + str(val))
				else:
					print(key + ": " + val)
	
	def greet_user(self):
		print("Hello " + self.first_name + " " + self.last_name)
		
user1 = User("karl", "karlsson")
user2 = User("erik", "eriksson", ålder=88, allergi="pasta", intresse="musik")

users = [user1, user2]

for user in users:
	user.describe_user()
	print("\t")
	user.greet_user()
	print("\n")
	
