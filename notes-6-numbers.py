# Numbers and Operations
# Author: Carl Dicioco
# 5 November 2025

# Work with numbers and operations

# Create an algorithm to gather
# data to find the most popular
# bubble tea place around us

# Version 1


def vote_listed_choices():
    """Display all choices
    5 users vote for their choice
    Results will be printed"""
    CHOICES = [
        "A. Blenz",
        "B. Bubble Queen",
        "C. Sun Tea",
        "D. heytea",
        "E. CoCo",
        "F. Fresh T",
    ]

    # buckets to hold all votes
    blenz = 0
    bubble_queen = 0
    sun_tea = 0
    heytea = 0
    coco = 0
    fresh_t = 0
    spoiled_votes = 0

    # Show all the choices
    print("Vote for your favourite from the list. ")
    print("Give the letter of your choice.")
    for choice in CHOICES:
        print(choice)

    # Ask the user for their choice
    vote = input("Your vote: ").strip(",.?! ").lower()
    # Keep track of a tally
    if vote == "a":
        blenz = blenz + 1
    elif vote == "b":
        bubble_queen += 1
    elif vote == "c":
        sun_tea += 1
    elif vote == "d":
        heytea += 1
    elif vote == "e":
        coco += 1
    elif vote == "f":
        fresh_t += 1
    else:
        spoiled_votes += 1

    # Data analysis
    # Give the raw scores
    print("Voting Results ---")
    print(f"Blenz: {blenz} votes")
    print(f"Bubble Queen: {bubble_queen} votes")
    print(f"Sun Tea: {sun_tea} votes")
    print(f"hey tea: {heytea} votes")
    print(f"CoCo: {coco} votes")
    print(f"Fresh T: {fresh_t} votes")
    print(f"Spoiled votes: {spoiled_votes} votes")
    # Give scores as a percentage
    print("Vote share percentage ---")
    total = blenz + bubble_queen + sun_tea + heytea + coco + fresh_t + spoiled_votes
    print(f"Blenz: {blenz / total * 100} %")
    print(f"Bubble Queen: {bubble_queen / total * 100} %")
    print(f"Sun Tea: {sun_tea / total * 100} %")
    print(f"hey tea: {heytea / total * 100} %")
    print(f"CoCo: {coco / total * 100} %")
    print(f"Fresh T: {fresh_t / total * 100} %")
    print(f"Spoiled votes: {spoiled_votes / total * 100} votes")


# Version 2
# Ask the user to give their
# favourite bubble tea place
# Keep track of a tally
# Data analysis
# Give the raw scores
# Give scores as a percentage


def chip_rater():
    """Help gather data about chip crispness
    and quality."""
    questions = [
        "How crispy is the chip out of 5? 0 is mushy, 5 is crisp.",
        "How did you rate the taste out of 5? 0 is unpalatable, 5 is gourmet.",
        "How fresh would you rate the chip out of 5? 0 is stale, 5 is pristine.",
        "How would you rate the chip out of 5?",
    ]

    # Bucket to hold total ratings
    total_ratings = 0

    # Give the test subject instructions
    print("Take one chip from the bag.")
    print("Eat it mindfully.")
    print("Give your rating.")

    # Ask questions to the subject
    for question in questions:
        print(question)
        # for each question
        # get their rating for that question
        # out of five
        rating = int(input().strip(",.?!"))

        total_ratings += rating

    # Print out the average rating out of five
    average = total_ratings / len(questions)

    print(f"The average is rating is {average} stars!")


def main():
    vote_listed_choices()
    chip_rater()


if __name__ == "__main__":
    main()


def vote_open_choice():
    """Keeps track dynamically of user's choice.
    Note: choices must match text exactly (case is not sensitive)"""

    votes = {}  # holds vote information    key     -> value
    #                           place   -> num votes

    for _ in range(NUM_VOTERS):
        # Ask the user what their fave
        os.system("clear")
        cur_vote = (
            input("What's your favourite local bubbble tea cafe? ")
            .lower()
            .strip(",.?! ")
        )

        # Checks if current place is in the votes dictionary
        # If it doesn't exist, initialize the key-value pair
        if cur_vote not in votes:
            votes[cur_vote] = 1
        else:
            votes[cur_vote] += 1

    # Print the results
    print("-------------------------------------")
    print("Results:")

    # By default, iterating over a dictionary gives you the keys
    for place in votes:
        # Print the raw score and percentage for each key in the dictionary
        percentage = votes[place] / NUM_VOTERS * 100

        print(
            f"{place.capitalize()} votes: {votes[place]} | percentage: {percentage}% of the vote"
        )

    print("-------------------------------------")
