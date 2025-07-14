
#Asking user for input
n = int(input("Enter any valid number :- "))

if n < 0 :
    print("Enter valid number !!")


elif n==0 or n==1:

    print("Factorial is 1")


else:
    fact = 1
    for i in range(2,n+1):

        fact *= i

    print(f"Factorial of {n} is {fact}")