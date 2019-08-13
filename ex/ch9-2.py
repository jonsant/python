class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print("Name: " + self.restaurant_name)
		print("Cuisine Type: " + self.cuisine_type)
		print("\n")
		
	def open_restaurant(self):
		print("Restaurant is open")
		
restaurant1 = Restaurant("Bosses pizzeria", "Pizza")
restaurant2 = Restaurant("Kalles kebab", "Kebab")
restaurant3 = Restaurant("Eriks tacos", "Tacos")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
