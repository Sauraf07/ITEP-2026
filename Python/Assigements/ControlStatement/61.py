start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: "))

for year in range(start_year, end_year + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, end=" ")