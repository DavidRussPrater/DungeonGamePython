#   David Prater
#   Homework 2
#   9/7/2015
#	Simple text based dungeon game with user input

currentRoom = "kitchen"
alive = "true"
keyPressed = ""

while (alive == "true"):
    if (currentRoom == "kitchen"):
        keyPressed = input("You are in the kitchen. There are doors to the west (w), south (s) and east (e).")
        if (keyPressed=="w"):
            currentRoom = "hallway"
        elif (keyPressed=="s"):
            currentRoom = "furnace"
        elif (keyPressed=="e"):
            currentRoom = "living room"
        elif (keyPressed=="q"):
            print ("Goodbye!!")
            break
    elif (currentRoom == "hallway"):
        keyPressed = input("You are in the hallway. There are doors to the south (s) and east (e).")
        if (keyPressed=="s"):
            currentRoom = "library"
        elif (keyPressed=="e"):
            currentRoom = "kitchen"
        elif (keyPressed=="q"):
            print ("Goodbye!")
            break
    elif (currentRoom == "living room"):
        keyPressed = input("You are in the living room. There is a door to the west (west)")
        if (keyPressed=="w"):
            currentRoom = "kitchen"
        elif (keyPressed=="q"):
            print ("Goodbye!")
            break
    elif (currentRoom == "library"):
        print("You are in the library. You found the Princess! You are a hero!")
        print("Goodbye!")
        break
    elif (currentRoom == "furnace"):
        print("Entered the furnace and fry yourself to death!")
        print("Goodbye!")
        break
