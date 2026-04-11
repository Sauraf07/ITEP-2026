start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num}: {factorial}")