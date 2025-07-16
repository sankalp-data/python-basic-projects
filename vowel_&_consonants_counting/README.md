This Python script takes a word or sentence as input and counts the number of vowels, consonants, and total alphabetic letters.

# How the Program Works

1. Takes input from the user.

2. Initializes counters for:

 - vowels

 - consonants

3. Iterates through each character:

 - Checks if it is a letter using .isalpha().

 - Converts to lowercase and checks if it's a vowel (a, e, i, o, u).

 - If not a vowel, it's counted as a consonant.

4. Prints the total number of letters, vowels, and consonants.

# How to Run

1. Save the file as vowel_&_consonants_counting.py

2. Open terminal or command prompt and run:

 - python vowel_&_consonants_counting.py

3. Input any sentence or word when prompted.

# Concepts Used

 - for loop and string iteration

 - str.isalpha() for alphabet checking

 - str.lower() for case-insensitive comparison

 - Conditional logic

 - String formatting with f-strings