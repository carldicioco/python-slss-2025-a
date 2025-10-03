# Choose Your own adventure
# Princeton Vuong
# 24 September

# Choose your own adventure story focusing on using
# variable and branching/conditionals

# Intro
greeting = "Welcome to the diddy dungeon"
print(greeting)

name = input("What shall I call you traveller?")
print(f"Nice to meet you {name}!")

print("Please select a class from the following options.")
print("Mage")
print("Assassin")
print("Warrior")
player_class = input("Which class would you like to select?")

if player_class == "Mage":
    print(f"You chose {player_class}, a long distance class with exeptional power")

elif player_class == "Assassin":
    print(f"You chose {player_class}, a close distance class wit exceptional speed")

elif player_class == "Warrior":
    print(f"You chose {player_class}, a close distance class with exceptional defence")

else:
    print("invalid choice, choose again")


# Problem

# Rising action

# Climax

# Resolution
#
