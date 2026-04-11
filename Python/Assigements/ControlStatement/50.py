start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    if str(num) == str(num)[::-1]:
        print(f"{num} is a palindrome.")