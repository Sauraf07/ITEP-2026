'''
  Printing exception related information :-
  1. type of exeception
  2. get exception class name
  3. exception name
'''
print("At the start....")
a = int(input("Enter 1st value : ")) # ValueError
b = int(input("Enter 2nd value : ")) # ValueError
try:
  c = a / b
  print(f"Result : {c}")
except ZeroDivisionError as e:
    print("Denominator can not be zero")
print("At the end.......")




