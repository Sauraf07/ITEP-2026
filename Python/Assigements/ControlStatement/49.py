start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    sum_factors = sum(i for i in range(1, num) if num % i == 0)
    if sum_factors == num:
        print(f"{num} is a perfect number.")