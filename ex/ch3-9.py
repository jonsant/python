

invite_names = ["Bellman", "Cederhök", "Bildoktorn"]
print(invite_names[0] + ", you're invited for dinner.")
print(invite_names[1] + ", you're invited for dinner.")
print(invite_names[2] + ", you're invited for dinner.")

print(invite_names[1] + " can't make it :(\n")

invite_names.remove("Cederhök")
invite_names.insert(1, "Trotsky")

print(invite_names[0] + ", you're invited for dinner.")
print(invite_names[1] + ", you're invited for dinner.")
print(invite_names[2] + ", you're invited for dinner.")

print("Found a bigger table!\n")

invite_names.insert(1,"Bucharin")
invite_names.insert(0, "Diem")
invite_names.append("Friedman")

print(invite_names[0] + ", you're invited for dinner.")
print(invite_names[1] + ", you're invited for dinner.")
print(invite_names[2] + ", you're invited for dinner.")
print(invite_names[3] + ", you're invited for dinner.")
print(invite_names[4] + ", you're invited for dinner.")
print(invite_names[5] + ", you're invited for dinner.")

print("\nCan only invite 2 people.")
popped = invite_names.pop(0)
print("Sorry " + popped)

popped = invite_names.pop(0)
print("Sorry " + popped)

popped = invite_names.pop(0)
print("Sorry " + popped)

popped = invite_names.pop(0)
print("Sorry " + popped)

print("You're still invited " + invite_names[0])
print("You're still invited " + invite_names[1])

# Adding in exercise 9
print("\nCurrently inviting " + str(len(invite_names)) + " people for dinner")

del invite_names[0]
del invite_names[0]

print(invite_names)
