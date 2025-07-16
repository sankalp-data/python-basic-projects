This Python script checks whether a given year is a leap year based on the standard leap year rules used in the Gregorian calendar. It also validates that the year is between 1901 and 99999

# What Is a Leap Year?

A leap year is a year with 366 days instead of 365.
Leap year rules:

 - If the year is not divisible by 4 → Not a leap year

 - If the year is divisible by 4 but not by 100 → Leap year

 - If the year is divisible by 100 but not by 400 → Not a leap year

 - If the year is divisible by 400 → Leap year

# How the Program Works

1. The function is_leap(year) checks whether a given year is a leap year.

2. It ensures the year is in a valid range: 1901 ≤ year < 100000.

3. Based on the rules, it returns:

 - True if the year is a leap year

 - False otherwise

4. If the year is out of the valid range, it prints an error message and returns False.

# How to Run the Script

1. Save the code in a file called leap_year_checker.py.

2. Open a terminal or command prompt.

3. Run the script using:

 - python leap_year_checker.py

4. You can modify the call to is_leap() at the bottom to test with different years.

# Concepts Used

 - Function definition and return statements

 - Conditional logic (if, elif, else)

 - Logical operators and modular arithmetic (%)

 - Range validation