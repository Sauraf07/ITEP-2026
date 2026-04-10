num1 = int(input("Enter the 1st number  "))
num2 = int(input("Enter the 2nd number"))
oper = input("Enter the operation to perform (+,-,*,/)")
if oper == '+':
    print("Addition is ",num1+num2)
elif oper == '-':
    print("Sub is ",num1-num2)
elif oper == '*':
    print("Mul is ",num1*num2)
elif oper == '/':
    print("Div is ",num1/num2)
else:
    print("Invalid Options ")