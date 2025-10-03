# Choose Your Own Adventure
# Carl Dicioco
# 24 September
#
# Choose your own adventure story focusing
# on using variables and branching/conditionals
import sys

greeting = "Welcome to the game."
print(greeting)
health = 100
inventory = []
visited = []
locations = ["ward", "morgue", "chapel"]
user_name = input("Put your name down below.")
print(f"Welcome to the game, {user_name}.")
choice = input("Do you want to start the game now? (yes/no)").lower()
if choice == "yes":
    print("\nYou wake up in a dark hallway.")
    print("The floor is cold, and the walls are cracked and dirty.")
    print("Dim lights flicker above you.")
    print("You see broken hospital signs on the walls.")
    print("The place looks abandoned and silent.")
    print("You see three things around you:")
    print("1. a lighter")
    print("2. a drawer key")
    print("3. a roll of bandages")
elif choice == "no":
    print("You did not start the game. Play again?")
    sys.exit()
else:
    print("Invalid answer.")
    sys.exit()
choice1 = input("\nWhich object do you take? (lighter/key/bandages)").lower()
if choice1 == "lighter":
    inventory.append("lighter")
    print("You picked up a lighter. It can be useful for seeing things better.")
elif choice1 == "key":
    inventory.append("key")
    print("You find an unfamiliar key. Its purpose is a mystery to you.")
elif choice1 == "bandages":
    inventory.append("bandages")
    print("You pick up a roll of bandages. These might come in handy later.")
else:
    print("You ignored everything and walked forward.")
print("You continue walking down the hallway.")
print("Suddenly, you hear glass shatter in a room nearby.")
choice2 = input("\nDo you want to investigate the noise? (yes/no)").lower()
if choice2 == "yes":
    print("\nYou slowly push the door open.")
    print("Inside is an abandoned operating room.")
    print(
        "On the floor is a broken glass jar… a dark figure crawls back into the shadows."
    )
    if "key" in inventory:
        inventory.remove("key")
        print("\nYou see a locked drawer. The key fits perfectly.")
        print("Inside is a box of pistol ammo. You might need this eventually.")
    elif "bandages" in inventory:
        print(
            "You notice bloody footprints leading out of the room, as if someone wounded just left."
        )
    choice3 = input("\nDo you dare look where the dark figure went? (yes/no)")
    if choice3 == "no":
        print("\nYou decide to not look where it went.")
        print("You leave the room.")
    else:
        if "lighter" in inventory:
            print("You use your lighter, driving the shadows away")
            print("The flame reveals text frantically carved on the wall that reads:")
            print("IT'S TOO LATE.")
        else:
            print("You go to see where the figure has gone.")
            print("You cannot see through the shadows.")
            print("An unclear whisper brushes past your ear.")
        print("You turn around.")
        print("Its face is featureless, smooth and blank, yet staring at you.")
        print("It lunges, hands closing around you, dragging you into darkness.")
        print("\nYou died.")
        sys.exit()
else:
    print("\nYou ignore the noise and keep walking.")
print("\nThe hallway stretches too far… longer than it should.")
print("The lights flicker out one by one, following behind you.")
print("Three paths wait:")
print("The gate to the Psychiatric Ward on your left, a stairwell,")
print("And a wooden door leading to the Chapel.")
while True:
    choice4 = input("\nWhich path do you take? (ward/stairwell/chapel)").lower()
    if choice4 in visited:
        print("You have already been there. Choose another place.")
    else:
        visited.append(choice4)
        print(f"You go to the {choice4}.")
        if choice4 == "ward":
            print("\nYou walk through the gate.")
            print("It feels cold and empty.")
            print("The doors creak loudly behind you.")
            print("Down the hall, you hear someone crying in one of the rooms.")
            print(
                "You look inside a door's window and see a girl sitting on the floor, crying."
            )
            choice5 = input("\nWhat do you want to do? (comfort/observe/sneak)").lower()
            if choice5 == "comfort":
                print("\nYou open the door.")
                print("Her back is turned to you as she cries softly.")
                print("You step closer and speak gently, trying to console her.")
                print(
                    "She turns around, and you catch a glimpse of her hollow black eyes."
                )
                print(
                    "For a brief moment, she seems to calm… then, without warning, she lunges at you!"
                )
                health -= 30
                print(f"You are scratched and hurt! Health: {health}")
                if "bandages" in inventory:
                    choice6 = input(
                        "\nDo you want to use your bandages? (yes/no)"
                    ).lower()
                    if choice6 == "yes":
                        inventory.remove("bandages")
                        health += 20
                        print("You use your bandages.")
                        print(f"Your health is now: {health}.")
                else:
                    print("You decide not to use your bandages.")
            else:
                print("You observe the girl as she cries.")
                print(
                    "She turns around, and you catch a glimpse of her hollow black eyes."
                )
                print(
                    "For a brief moment, she seems to calm… then, without warning, she lunges at the window!"
                )
                print("\nThe girl disappears into thin air.")
                choice7 = input("\nShe dropped a screwdriver. Do you take it?").lower()
                if choice7 == "yes":
                    print("\nYou took the screwdriver.")
                    print("This can be used to unlock open panels or vents.")
                else:
                    print(
                        "\nYou decide not to take the screwdriver, which is pretty dumb."
                    )
                    print("\nYou walk to the end of the and there seems to be an exit.")
                    print("You try to open it but it seems you need a keycard.")
                    print("You walk back to the gate.")
                    break
        elif choice4 == "chapel":
            print("\nYou open the wooden door to the chapel.")
            print(
                "The room is dark and cold, with broken pews scattered across the floor"
            )
            print("The stained glass windows are boarded with wooden planks")
            print("The candles flicker, though none are lit.")
            print(
                "As you step in, whispers grow louder, and a shadowy figure emerges from the darkness!"
            )
            if "lighter" in inventory:
                print(
                    "You flick your lighter on, revealing its twisted, featureless face."
                )
                print("It recoils from the light as you scramble past it.")
                health -= 20
                print(f"You are scratched by its claws! Health: {health}")
            else:
                print("You have no light source to see it clearly.")
                print("It slams into you from the shadows!")
                health -= 50
                print(f"You are badly hurt! Health: {health}")
