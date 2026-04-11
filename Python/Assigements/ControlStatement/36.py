num = int(input("Enter a number: "))
reverse_num = 0
while num != 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print(f"Reversed number: {reverse_num}")