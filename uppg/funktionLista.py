def lista(txt1,txt2,txt3):
	return [txt1, txt2, txt3]
	
lista = lista("txt1","ttx2","t3")
print(lista)


def math(tal1, tal2, tal3):
	if tal1 == 1:
		return (tal2 + tal3)
	elif tal1 == 2:
		return (tal2 - tal3)
	elif tal1 == 3:
		return (tal2*tal3)
	elif tal1 == 4:
		return (tal2/tal3)
		
result = math(3, 3, 4)
print("\n" + str(result))
