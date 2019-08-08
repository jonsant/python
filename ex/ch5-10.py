current_users = ["kalle", "torleif", "bosse", "inge"]
new_users = ["torbjörn", "TORlEif", "björn", "niklas", "BOsse", "orvar"]

for user in new_users:
	if user.lower() in current_users:
		print("Username already taken")
	else:
		print("Username available")
