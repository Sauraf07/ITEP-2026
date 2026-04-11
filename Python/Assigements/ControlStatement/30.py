n = int(input("Enter the number of terms: "))
num = 1
sum_series = 0
for i in range(n):
    sum_series += num
    num = num * 10 + 1  # Forming the number by adding 1
print(f"Sum: {sum_series}")