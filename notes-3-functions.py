# Functions
# Author: Carl Dicioco
# 8 October

# function to print "hello"
def say_hello():
    print("hello")


# function to print a personalized hello
def say_hello_nicely(name: str):
    print(f"hello {name}!")


def normalize_input():
    """Takes user input and cleans it up."""
    output = input().lower().strip(",.?! ")
    return output


# Ask the user what the weather is
weather_reply = normalize_input()
print(weather_reply)
