num = input("Enter a number: ")
if len(num) == 1:
    print(f"Number remains the same: {num}")
else:
    new_num = num[-1] + num[1:-1] + num[0]
    print(f"Number after interchanging first and last digits: {new_num}")