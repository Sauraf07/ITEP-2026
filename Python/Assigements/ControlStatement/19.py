n = int(input("Enter the number of terms: "))
sum_series = 0
for i in range(1, n+1):
    sum_series += 1/i
print(f"Sum: {sum_series}")