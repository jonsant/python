should_take_poll = ["kalle", "asgård", "jen", "niklas"]

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
	
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
		language.title() + ".")

print("\n")

for name in should_take_poll:
	if name in favorite_languages:
		print(name + " have already done the poll.")
	else:
		print(name + ", please do the poll.")
