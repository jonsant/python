def build_profile(first, last, **user_info):
	"""Build a dictionary containing everythinh we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
	location='princeton',
	field='physics')
	
print(str(user_profile) + "\n")

jag = build_profile('anton', 'thunman jonsson', location="gävle", glasses=True)
print(jag)
