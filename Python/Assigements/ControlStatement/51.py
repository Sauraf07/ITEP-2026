start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    print(f"Reversed number of {num}: {str(num)[::-1]}")