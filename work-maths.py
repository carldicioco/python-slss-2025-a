# Machines are good at crunching numbers - faster and more accurately than most humans!
# Create a small program that calculates something useful to you (making you smile is useful).
# It should take user input, at use at least one of the number operators we saw in class: + / * -.

# You may modify one of your previous exercises to include calculations, if you wish.
def main():
    total_hours = float(input("How many hours do you have before bedtime? "))
    homework_hours = float(input("How many hours of homework do you still have? "))

    free_hours = total_hours - homework_hours
    free_minutes = free_hours * 60

    print(f"\nYou have {free_minutes:.0f} minutes of free time left.")

    if free_minutes < 0:
        print("You have to stay up late to finish your homework.")
    elif free_minutes > 0:
        print("You have sufficient time to finish your homework.")


if __name__ == "__main__":
    main()
