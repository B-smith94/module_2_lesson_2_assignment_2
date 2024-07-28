place = input("Choose a place: forest or cave? ")

if place == "forest": #need to change = to ==
    action = input("climb a tree or cross a river? ") 
    if action == "climb a tree": #need to change = to ==
        print("You found a bird's nest!") 
    elif action == "cross a river":  #change else to elif
        print("You found a boat!")
    else:
        pass
elif place == "cave": #change = to ==
    action = input("Do you light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You easily spot the treasure in the now well-lit cavern!")
    elif action == "proceed in the dark":
        print("You fumble in the dark for hours but cannot find a way forward.")
    else:
        pass
else:
    pass