start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    n = len(str(num))
    sum_of_powers = sum(int(digit) ** n for digit in str(num))
    if sum_of_powers == num:
        print(f"{num} is an Armstrong number.")