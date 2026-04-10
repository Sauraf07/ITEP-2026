num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enetr the secound number: "))
choice = input("enter your choice (+,>,==)")
if choice == '+':
    print("addition is ",num1+num2)
elif choice == '>':
    print(num1>num2)
elif choice == '==':
    print(num1==num2)