num = int(input("Enter a number: "))
original_num = num
reverse_num = 0
while num != 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
if original_num == reverse_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")