This Python script checks whether a given word is a palindrome. A palindrome is a word that reads the same backward as forward (e.g., madam, racecar, level).

# What Is a Palindrome?

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, ignoring spaces, punctuation, and capitalization.

# How the Program Works

1. The user is prompted to enter a word.

2. The program checks whether the input:

 - Contains only alphabetic characters (no spaces, numbers, or special characters).

3. If valid, the script checks:

 - Whether the word is the same when reversed using slicing (word[::-1])

4. Based on the result, it prints:

 - "It's a Palindrome"

 - "Not a Palindrome"

5. "Please enter string without spaces, numbers, special characters and symbols." (for invalid inputs)

# How to Run the Script

1. Save the code to a file named palindrome_checker.py.

2. Run the script in the terminal or any Python environment:

 - python palindrome_checker.py

3. Enter a word when prompte

# Concepts Used

 - String input using input()

 - String slicing ([::-1])

 - Conditional statements (if, else)

 - Input validation using .isalpha()