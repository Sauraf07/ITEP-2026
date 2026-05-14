import math
print("At the start")
try:
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd Number : "))
    c = a/b
    math.exp(1000)
except ArithmeticError as a:
    print(f"Arithemetic Error {a}")
except ValueError as a:
    print(a)
except:
    print("Unkonwn Error ")
print("At the end ")