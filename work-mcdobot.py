# Work - McDoBot
# Author: Carl Dicioco
# 6 October

# It asks you if you want fries
# It shoould accept Yes/yes or No/no
# as inputs, and reply appropriately depending on the answer.
# If the user inputs anything else,
# it should repeat back ther answer and
# say that it does not understand.
answer = input("Do you want fries? ").lower()

if answer == "yes":
    print("Okay, fries added!")
elif answer == "no":
    print("Okay, no fries.")
else:
    print(f"I do not understand '{answer}'.")
