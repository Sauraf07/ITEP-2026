year  = int(input("enter the year "))
if year%4==0  and year% 400:
    print(year,"is leap year")
else:
    print(year,"is not leap year")