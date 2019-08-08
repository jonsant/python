current_users = ["kalle", "torleif", "bosse", "inge"]
new_users = ["torbjörn", "björn", "niklas", "orvar"]

for user in new_users:
	for us in current_users:
		if user.lower() == us.lower():
			print("Username taken")
		
