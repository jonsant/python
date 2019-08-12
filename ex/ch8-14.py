def make_car(manufacturer, model, **other):
	car = {"manufacturer": manufacturer, "model": model}
	for key, value in other.items():
		car[key] = value
	return car
	
car = make_car("subaru", "outback", color="green", windows=False)
print(car)
