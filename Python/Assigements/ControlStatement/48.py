start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    print(f"Factors of {num} are: ", end="")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
    print()