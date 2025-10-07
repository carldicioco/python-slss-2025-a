# Methods
# Author: Carl Dicioco
# 6 October

# Ask the user what the weather is like
weather = input("What's the weather like right now?")
if weather.lower().strip("!") == "rainy":
    print("You should bring an umbrella.")
elif weather.lower().strip("!") == "sunny":
    # "SUNNY" "sunny!" "sunny."
    print("You should bring sunscreen.")
else:
    print("I see...")

# Ask the user for their name,
#       remove whitespace from the str
#       capitalize the first letter of each word
name = input("")
