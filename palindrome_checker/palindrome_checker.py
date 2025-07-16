word = input("Enter any word for checking palindrome :- ")

if word.isalpha() == True:

    if word == word[::-1]:

        print("Its a Palindrome")

    else:


        print("Not a Palindrome")

else:

    print("Please enter string without spaces, numbers, special characters and symbols.")