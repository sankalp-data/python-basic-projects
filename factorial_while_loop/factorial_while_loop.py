n = int(input("Enter number please :- "))

if n<0:

    print("INVALID NUMBER!!")

elif n==0 or n==1:

    print("The factorial is 1")


else:
    fac = 1
    i = 1
    while i<=n:

        fac*=i

        i+= 1

    print(f"The Factorial of {n} is {fac}")

