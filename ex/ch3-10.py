vgtbls = ["Gurka", "Tomat", "Morot", "Rova"]
print(str(len(vgtbls)))

print(vgtbls)

vgtbls.sort()
print(vgtbls)

vgtbls.reverse()
print(vgtbls)

print(sorted(vgtbls))

vgtbls.remove("Tomat")
print(vgtbls)

removed = vgtbls.pop()
print("Removed " + removed)

del vgtbls[0]
print(vgtbls)

vgtbls.insert(0, "Gurka")
print(vgtbls)

vgtbls.append("Beta")
