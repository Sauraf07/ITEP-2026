import math

num = int(input("Enter a number: "))
original_num = num
sum_of_factorials = sum(math.factorial(int(digit)) for digit in str(num))
if sum_of_factorials == num:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")