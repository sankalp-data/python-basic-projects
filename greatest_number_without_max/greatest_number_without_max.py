number = int(input("Enter the number of elements you want in list :- "))

lst = []

for i in range(number):

    adding = int(input("Enter the number you want to add in list :- "))

    lst.append(adding)


max = lst[0]

for num in lst[1:]:

    if num>max:

        max = num


print(f"The greatest number is {max}")