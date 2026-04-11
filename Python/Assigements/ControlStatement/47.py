start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    print(f"Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print()