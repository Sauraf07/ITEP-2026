print("At the start")
try:
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd Number : "))

    c = a/b
    print(f"Result : {c}")
except (ValueError,ZeroDivisionError) as e:
    print("!Opps Somenthing went worng ")

finally:
    print("Finally block executed ")
print("At the end ")