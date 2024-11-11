from collections import Counter
import string

def count_words_in_file(file_path):
    # Initialize a Counter to store word counts
    word_counts = Counter()

    try:
        # Open the file and read its content
        with open(file_path, 'r') as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                # Split the line into words and update the Counter
                words = line.split()
                word_counts.update(words)

        # Sort the words alphabetically and display counts
        for word in sorted(word_counts):
            print(f"{word}: {word_counts[word]}")

    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get the file path from the user
file_path = input("Enter the path of the text file: ")
count_words_in_file(file_path)
