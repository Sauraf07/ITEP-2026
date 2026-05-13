print("At the start")
try:
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd Number : "))

    c = a/b
    print(f"Result : {c}")
except ValueError as e:
    print(type(e))
except ZeroDivisionError as e:
    print(type(e))
finally:
    print("Finally block executed ")
print("At the end ")