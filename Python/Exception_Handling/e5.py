'''
  Printing exception related information :-
  1. type of exeception
  2. get exception class name
  3. exception name
'''
print("At the start")
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
try:
    c = a/b
    print(f"Result {c}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError : {e}")
print("At the end ")