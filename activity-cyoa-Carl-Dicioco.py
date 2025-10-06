# Choose Your Own Adventure
# Carl Dicioco
# 24 September
#
import sys

# Variables
greeting = "Welcome to the game."
print(greeting)
health = 100
inventory = []
visited = []
locations = ["ward", "morgue", "chapel"]

user_name = input("Put your name down below: ")
print(f"Welcome to the game, {user_name}.")

# Start prompt
choice = input("Do you want to start the game now? (yes/no) ").lower()
if choice == "no":
    print("You did not start the game. Play again?")
    sys.exit()
elif choice != "yes":
    print("Invalid answer.")
    sys.exit()

# Starting items
print("\nYou wake up in a dark hallway.")
print("Behind you, there’s an exit door covered with wooden planks.")
print("A heavy padlock keeps it tightly shut.")
print("The floor is cold, and the walls are cracked and dirty.")
print("Dim lights flicker above you.")
print("You see broken hospital signs on the walls.")
print("The place looks abandoned and silent.")
print("You see three things around you:")
print("1. a lighter")
print("2. a drawer key")
print("3. a roll of bandages")

choice1 = input("Which object do you take? (lighter/key/bandages) ").lower()
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

print("\nYou continue walking down the hallway.")
print("Suddenly, you hear glass shatter in a room nearby.")
choice2 = input("Do you want to investigate the noise? (yes/no) ").lower()
if choice2 == "yes":
    print("\nYou slowly push the door open.")
    print("Inside is an abandoned operating room.")
    print(
        "On the floor is a broken glass jar… a dark figure crawls back into the shadows."
    )
    if "key" in inventory:
        inventory.remove("key")
        print("You see a locked drawer. The key fits perfectly.")
        print("Inside is a box of pistol ammo. You might need this eventually.")
        inventory.append("ammo")
    elif "bandages" in inventory:
        print(
            "You notice bloody footprints leading out of the room, as if someone wounded just left."
        )

    choice3 = input("Do you dare look where the dark figure went? (yes/no) ").lower()
    if choice3 == "no":
        print("You decide not to look where it went and hurriedly leave the room.")
    else:
        if "lighter" in inventory:
            print("\nYou use your lighter, driving the shadows away.")
            print("The flame reveals text frantically carved on the wall that reads:")
            print("IT'S TOO LATE.")
        else:
            print("\nYou go to see where the figure has gone.")
            print("You cannot see through the shadows.")
        print("An unclear whisper brushes past your ear.")
        print("You turn around.")
        print("Its face is featureless, smooth and blank, yet staring at you.")
        print("It lunges, hands closing around you, dragging you into darkness.")
        print("You died.")
        sys.exit()
else:
    print("You ignore the noise and keep walking.")

print("\nThe hallway stretches too far… longer than it should.")
print("The lights flicker out one by one, following behind you.")
print("Three paths wait:")
print("The gate to the Psychiatric Ward on your left, a stairwell,")
print("And a wooden door leading to the Chapel.")

# Main path selection loop
while True:
    choice4 = input("Which path do you take next? (ward/stairwell/chapel) ").lower()

    # allow stairwell to always be revisited
    if choice4 != "stairwell" and choice4 in visited:
        print("You already went there. Pick somewhere else.")
        continue

    if choice4 not in locations and choice4 != "stairwell":
        print("Invalid choice.")
        continue

    # mark visited locations except stairwell
    if choice4 != "stairwell":
        visited.append(choice4)

    if choice4 == "chapel" and "keycard" in inventory:
        print(
            "\nYou already took the keycard from the vent. The chapel is now inaccessible."
        )
        continue

    print(f"\nYou go to the {choice4}.")

    # Ward path
    if choice4 == "ward":
        print("\nYou walk through the gate to the ward. It feels cold and empty.")
        print("The doors creak loudly behind you.")
        print("Down the hall, you hear someone crying in a locked room.")
        print("You look inside the door's window and see a girl crying beside her bed.")
        choice5 = input("What do you want to do? (comfort/observe) ").lower()
        if choice5 == "comfort":
            print("\nHer back is turned to you as she cries softly.")
            print("You open the door.")
            print("You step closer and speak gently, trying to console her.")
            print("She turns around, and you catch a glimpse of her hollow black eyes.")
            print("For a brief moment, she seems to calm… then lunges at you!")
            health -= 50
            print(f"You are scratched and hurt! Health: {health}")
            if "bandages" in inventory:
                choice6 = input("Do you want to use your bandages? (yes/no) ").lower()
                if choice6 == "yes":
                    inventory.remove("bandages")
                    health += 30
                    print("You use your bandages.")
                    print(f"Your health is now: {health}.")
                else:
                    print("You decide not to use your bandages.")
        else:
            print("You observe the girl as she cries.")
            print("She turns around, and you catch a glimpse of her hollow black eyes.")
            print("For a brief moment, she seems to calm… then lunges at the window!")

        print("The girl disappears into thin air.")
        choice7 = input("She dropped a screwdriver. Do you take it? (yes/no) ").lower()
        if choice7 == "yes":
            inventory.append("screwdriver")
            print(
                "You took the screwdriver. This can be used to unlock panels or vents."
            )
        else:
            print("You decide not to take the screwdriver.")

    # Chapel path
    elif choice4 == "chapel":
        print("You push open the wooden door to the chapel.")
        print(
            "The room is dark and cold, with broken pews and stained glass windows covered with wooden planks."
        )
        print("Candles sit unlit on the altar.")
        print(
            "As you step further in, whispers grow louder, and a shadowy figure emerges from the darkness!"
        )
        # fix this
        if "lighter" in inventory:
            print("\nYou flick your lighter on, revealing its twisted, pale face.")
            print("It recoils from the light as you scramble past it.")
            health -= 30
            print(f"You are scratched by its claws! Health: {health}")
        else:
            print("\nYou have no light source to see it clearly.")
            print("It slams into you from the shadows!")
            health -= 50
            print(f"You are badly hurt! Health: {health}")
            if health <= 0:
                print("You died.")
                sys.exit()

        print("\nAfter a tense moment, the figure retreats into the shadows.")
        print("At the back of the chapel, you notice a floor vent.")

        if "screwdriver" in inventory:
            print("\nLuckily, you have a screwdriver.")
            print("You remove the screws and lift the vent cover.")
            print("Inside, you find a keycard lying in the dust.")
            inventory.append("keycard")
            print("\nYou took the keycard! This can open some type of secured door.")
        else:
            print(
                "\nThe vent is screwed shut. You need something to remove the screws."
            )
            print("Perhaps there’s a tool elsewhere that can help.")
        print("\nThere seems to be a room near the altar.")
        choice12 = input("Do you enter? (yes/no)")
        if choice12 == "yes":
            print("\nYou step inside the room.")
            print("While observing the room, you stumble upon a bottle of Holy Water!")
            inventory.append("holywater")
        else:
            print("You choose not to enter.")
        print("You leave the chapel.")

    # Stairwell path
    elif choice4 == "stairwell":
        while True:
            choice8 = input(
                "\nDo you want to go upstairs or downstairs? (up/down/back)"
            )
            if choice8 == "up":
                print("\nYou choose to go up the stairwell.")
                print("You see a grey metal door labeled 'SECURITY'.")
                print("It seems to have a keycard lock.")
                choice9 = input("Do you enter? (yes/no)")
                if choice9 == "yes":
                    if "keycard" in inventory:
                        print("You glide the keycard over the lock.")
                        print("The door opens!")
                        print("You step inside the security room.")
                        print(
                            "The room is small and cluttered with dusty monitors and control panels."
                        )
                        print(
                            "You see a key lying on a dusty desk. This must be the exit key!"
                        )
                        inventory.append("exitkey")
                        print("A cabinet with a combination lock stands in the corner.")
                        choice13 = input("Do you go to the cabinet? (yes/no)")
                        if choice13 == "yes":
                            code = input("Enter 4-digit code:")
                            while True:
                                if code == "5678":
                                    print("The cabinet opens! You find a pistol!")
                                    inventory.append("pistol")
                                    if "ammo" in inventory:
                                        print("You load the ammo into the pistol.")
                                        break
                                else:
                                    print("Wrong code. The cabinet stays locked.")
                        else:
                            print("\nYou leave the cabinet alone.")

                    else:
                        print("\nYou attempt to open the door.")
                        print("Suddenly, a loud alarm blares through the halls!")
                        print(
                            "You hear heavy footsteps rushing up the stairs toward you."
                        )
                        print(
                            "Before you can run, a masked man appears and drives a knife into your chest."
                        )
                        print("\nYou died.")
                        sys.exit()
                else:
                    print("You choose not to enter.")
            elif choice8 == "down":
                print("\nYou choose to go down the stairwell.")
                print(
                    "At the bottom floor, there is a rusted metal door marked 'MORGUE'"
                )
                choice10 = input("\nDo you enter? (yes/no)")
                if choice10 == "yes":
                    print("\nYou slowly open the morgue's door.")
                    print("The lights are on, but dim, flickering weakly.")
                    print("The room is quiet, filled with rows of cold metal drawers.")
                    print(
                        "You pull a drawer open. The tag on the corpse's wrist reads: 'ID 5678'."
                    )
                    print("There is a hammer on the floor.")
                    choice11 = input("\nDo you pick it up? (yes/no)")
                    if choice11 == "yes":
                        print(
                            "\nYou pick up the hammer. This is useful for removing nails."
                        )
                        inventory.append("hammer")
                    else:
                        print("\nYou leave the hammer on the floor.")
                    print("\nSuddenly, the lights flicker faster!")
                    print(
                        "You turn and see a tall figure, hunched and thin, with long hair hiding its face."
                    )
                    print(
                        "Its movements are slow but deliberate, and it stumbles slightly as it approaches, like a wounded person."
                    )
                    if "holywater" in inventory:
                        print("\nYou grab out the bottle of Holy Water!")
                        print(
                            "It screeches, stumbling back, and then dissolves into mist, disappearing from sight."
                        )
                        print("You leave the morgue.")
                    else:
                        print(
                            "The creature pounces suddenly, knocking you to the floor."
                        )
                        print(
                            "It pins you down, and you feel its cold, crushing weight."
                        )
                        print("Everything fades as its presence consumes you.")
                        print("\nYou died.")
                        sys.exit()
            elif choice8 == "back":
                if "hammer" in inventory and "exitkey" in inventory:
                    print(
                        "\nYou head back to the stairwell and approach the exit door."
                    )
                    print("Using the hammer, you remove the wooden planks.")
                    print("As you put the exit key into the padlock,")
                    print("a withered hand grips your wrist and refuses to let go!")
                    print(
                        "You turn and see a tall masked man with hollow eyes and a bloody coat."
                    )
                    if "pistol" in inventory:
                        gunchoice = input(
                            "Do you want to use your pistol? (yes/no) "
                        ).lower()
                        if gunchoice == "yes":
                            if "ammo" in inventory:
                                print(
                                    "\nYou yank the loaded pistol free, aim at the masked man, and pull the trigger."
                                )
                                print(
                                    "He staggers, but rasps, 'The cult will not fail… even in death.'"
                                )
                                print("He collapses.")
                                print(
                                    "\nYou slide the exit key into the padlock and turn it. The lock clicks open."
                                )
                                print(
                                    "You wrench the boarded door aside and push it wide, then run."
                                )
                                print(
                                    "You burst into an open field, wind tearing at your clothes as you race away into the night."
                                )
                                print("\nGOOD ENDING")
                                sys.exit()
                            else:
                                print("You yank the pistol free, but it’s empty.")
                                print(
                                    "Before you can react, he lunges and drives a knife into you."
                                )
                                break
                        else:
                            print("You decide not to use your gun.")
                            print(
                                "A blow to the back of your head knocks you unconscious."
                            )
                            print(
                                "When you wake, you find yourself on a sacrificial altar outside the hospital, flames flickering all around."
                            )
                            print(
                                "Masked figures chant around you as the same masked man steps forward and plunges a knife into your heart."
                            )
                            print("\nCULT ENDING")
                            sys.exit()
                    else:
                        print(
                            "Unarmed, you try to back away, but he lunges and drives a knife into you."
                        )
                        print("You collapse on the floor.")
                        print(
                            "As everything around you becomes darker, you hear his distorted voice saying:"
                        )
                        print("'You will end up just like them.'")
                        print("\nBAD ENDING")
                        sys.exit()
                else:
                    print("You leave the staircase.")
                    break
