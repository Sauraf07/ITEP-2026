year = int(input("Enter the year"))
if year%4==0 and year%400 == 0:
    print(year,"is a leap year")
else:
    print(f"{year} is not leap year")