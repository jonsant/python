favNums = {"kalle": [22], "erik": [78, 88, 99], 
	"niklas": [21], "peter": [99], "asgård": [29]}

for name, nums in favNums.items():
	print(name + " : ")
	for num in nums:
		print(num)

