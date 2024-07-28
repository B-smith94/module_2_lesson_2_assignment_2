place = input("Choose a place: forest or cave? ")

if place == "forest": #need to change = to ==
    action = input("climb a tree or cross a river?") 
    if action == "climb a tree": #need to change = to ==
        print("You found a bird's nest!") 
    else: #remove variable--not needed for else statement
        print("You found a boat!")
elif place == "cave": #change = to ==
    action = input("Do you light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You easily spot the treasure in the now well-lit cavern!")
    else:
        print("You fumble in the dark for hours but cannot find a way forward.")