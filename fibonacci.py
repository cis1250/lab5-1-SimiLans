#!/usr/bin/env python3
# fibonacci.py

def get_num_terms():
    """ Prompt the user for the number of Fibonacci terms and validate input."""
    while True:
         try:
             num_terms = int(input("Enter the number of Fibonacci terms to display: "))
             if num_terms <= 0:
                print("Please enter a positive integer.")
             else:
                return num_terms
         except ValueError:
                print("Invalid input.Please enter a positive integer.")
          
 def generate_fibonacci(num_terms):
     """Generate a Fibonacci sequence up to the specified number of terms."""
     sequence = []
     a, b = 0, 1
     for _ in range(num_terms):
         sequence.append(a)
         a, b = b, a + b
      return sequence

def print_fibonacci(sequence):
    """ Print the Fibonacci sequence in a redable format."""
    print("\nFibonacci Sequence:")
    print(", ". join(str(num) for num in sequence))

def main():
    """ Main program flow."""
    num_terms = get_num_terms()
    sequence = generate_fibonacci(num_terms)
    print_fibonacci(sequence)

if __name__ == "__main__":
   main()
  

# Fibonacci Sequence Exercise with functions

def get_sentence():
    """Prompt user for a valid sentence (starts with capital, ends with punctuation)."""
    while True:
        sentence = input("Enter a sentence: ").strip()
        if len(sentence) == 0:
            print("Sentence cannot be empty. Try again.")
            continue
        if sentence[0].isupper() and sentence[-1] in ".!?":
            return sentence
        else:
            print("A sentence must start with a capital letter and end with '.', '?', or '!'. Please try again.")


def calculate_frequencies(sentence):
    """Calculate the frequency of each word in the sentence."""
    words = sentence[:-1].lower().split()  # remove punctuation at end and lowercase
    word_list = []
    freq_list = []

    for word in words:
        if word in word_list:
            index = word_list.index(word)
            freq_list[index] += 1
        else:
            word_list.append(word)
            freq_list.append(1)

    return word_list, freq_list


def print_frequencies(words, frequencies):
    """Print words with their corresponding frequencies."""
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")


def main():
    """Main program flow."""
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)


# Run the program
if __name__ == "__main__":
    main()

# TODO: (Read detailed instructions in the Readme file)
