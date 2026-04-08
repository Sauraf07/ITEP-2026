age1 = int(input("Enter 1st age: "))
age2 = int(input("Enter 2nd age: "))
age3 = int(input("Enter 3rd age: "))
if age1> age2 and age1> age3:
    print(age1,"Is grater ")
elif age2> age1 and age2> age3:
    print(age2,"is grater")
else:
    print(age3,"is grater")