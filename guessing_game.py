import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 100. Try to guess it!")

# Initialize the guess variable
guess = None

# Start the guessing loop
while guess != target_number:
    try:
        # Get user's guess
        guess = int(input("Enter your guess: "))

        # Provide hints based on the guess
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
    except ValueError:
        print("Please enter a valid integer.")

print("Game Over. Thanks for playing!")
