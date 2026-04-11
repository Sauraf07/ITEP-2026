import math

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in str(num))
    if sum_of_factorials == num:
        print(f"{num} is a Strong number.")