decimal = int(input("Enter a decimal number: "))
binary = ""
while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2
print(f"Binary representation: {binary}")