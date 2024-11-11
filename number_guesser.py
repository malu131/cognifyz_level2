import random


def number_guesser():
    print("Welcome to the Number Guesser Game!")

    # Get the range from the user
    try:
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))

        if lower_bound >= upper_bound:
            print("The lower bound must be less than the upper bound. Please restart the game.")
            return

        # Generate a random number within the specified range
        target_number = random.randint(lower_bound, upper_bound)

        print(f"I've chosen a number between {lower_bound} and {upper_bound}. Try to guess it!")

        # Initialize the guess variable
        guess = None

        # Start the guessing loop
        while guess != target_number:
            try:
                guess = int(input("Enter your guess: "))

                # Provide feedback
                if guess < target_number:
                    print("Too low! Try again.")
                elif guess > target_number:
                    print("Too high! Try again.")
                else:
                    print("Congratulations! You guessed the correct number.")
            except ValueError:
                print("Please enter a valid integer.")
    except ValueError:
        print("Please enter valid integers for the bounds.")


# Run the game
number_guesser()
