class guest():
    def __init__(self, name, food, allergies, other):
        self.name=name
        self.food=food
        self.allergies=allergies
        self.other=other
        self.lives=True
        self.health=100

    


    def info(self):
        print("Information for object:")
        print("Name: " + self.name)
        print("Foods: " + self.food)
        print("Allergies: " + self.allergies)
        print("Other: " + self.other)
        if self.lives == True:
            print("Alive: Yes")
        else:
            print("Alive: No")
    def takeahit(self):
        print("Someone gone and messed up")
        print(self.name + " got hit for 10 hp")
        self.health-=10
        if self.health <= 0:
            self.lives=False
            print("Guest is dead")
            
    

Active=True
guests=[]
while Active:
    print("1. Lägg till gäst")
    print("2. Visa alla gäster")
    print("3. Slå Johan")
    choice = int(input("Gör ditt val: "))
    if choice == 1:
        name=input("Namn: ")
        food=input("Matpreferenser: ")
        allergies=input("Allergier: ")
        other=input("Övrigt: ")
        guests.append(guest(name,food,allergies,other))
    elif choice == 2:
        print("Visar alla gäster")
        for guest in guests:
            guest.info()
    elif choice == 3:
        for guest in guests:
            if guest.name == "Johan":
                guest.takeahit()