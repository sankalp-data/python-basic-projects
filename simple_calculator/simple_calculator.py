def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "Cannot divide by 0"

    return a/b

print("Simple Calculator\n")
print("Choose Operation\n")
print("1.Want Addition\n")
print("2.Want Subtraction\n")
print("3.Want Division\n")
print("4.Want Multiplication\n") 

reply = input("Choose what you want 1,2,3,4 :")

num1 = float(input("Enter your first number :- "))
num2 = float(input("Enter your second number :- "))

if reply=="1":
    print(f"Result = {add(num1,num2)}")

elif reply=="2":
    print(f"result = {sub(num1,num2)}")


elif reply=="3":
    print(f"result = {division(num1,num2)}")


elif reply=="4":
    print(f"result = {multi(num1,num2)}")


else:
    print("Invalid input")