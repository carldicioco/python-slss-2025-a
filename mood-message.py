def create_mood_message(name):
    # Ask the user for their mood
    mood = input(
        "How are you feeling today? (happy/sad/neutral)"
    ).lower()  # convert to lowercase for consistency

    if mood == "happy":
        return f"Hey {name}, great to see you smiling!"
    elif mood == "sad":
        return f"I hope your day gets better, {name}."
    elif mood == "neutral":
        return f"Sometimes you have average days, {name}."
    else:
        return f"Hi {name}, hope you're having a good day."


# Example usage
name = input("What's your name? ")
message = create_mood_message(name)
print(message)
