def order_sandwich(*items):
	print("You want a sandwich with: ")
	for item in items:
		print("- " + item)
	print("\n")
		
order_sandwich("butter", "cheese", "cucumber")
order_sandwich("butter", "ham")
order_sandwich("butter")
