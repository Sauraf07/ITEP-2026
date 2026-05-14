print("At the start.....")
try:
    a = int(input("Enter 1st value : "))
    b = int(input("Enter 2nd value : "))
    c = a / b
    print(f"Result : {c}")
except ZeroDivisionError as e:
    print("Denominator can not be zero...")

except ValueError as e:
    print("Only integers are allowed...")
else:
    print("program Executed Succesfully")

finally:
    print("Finally block executed ")
print("At the End ")