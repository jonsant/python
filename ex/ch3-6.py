
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
