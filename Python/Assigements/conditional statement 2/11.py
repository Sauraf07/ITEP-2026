age = int(input("Enter your age: "))
gender = input("Enter your sex ( M or F )")
material = input("marital status ( Y or N ) ")
if gender == 'F':
    print("you will work only in urban areas.")
elif gender == 'M' and (age>=20 and age<=40):
    print("you can work any where") 
elif gender == 'M' and (age>=40 and age<=60):
    print("You can work in Urban areas")
else:
    print("Invalid user..")