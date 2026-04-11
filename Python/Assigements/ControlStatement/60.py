n = int(input("Enter a number: "))

for i in range(1, n + 1):
    square = i ** 2
    cube = i ** 3
    square_root = i ** 0.5
    print(f"Number: {i}, Square: {square}, Cube: {cube}, Square Root: {square_root:.2f}")