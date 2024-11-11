def fibonacci_sequence(n):
    # Create an empty list to store the Fibonacci sequence
    sequence = []

    # Generate the Fibonacci sequence
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # Update a and b for the next term

    return sequence


# Get user input
try:
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        # Get the Fibonacci sequence
        fib_sequence = fibonacci_sequence(num_terms)
        # Display the result
        print("Fibonacci sequence up to", num_terms, "terms:")
        print(fib_sequence)
except ValueError:
    print("Please enter a valid integer.")
