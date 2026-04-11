sum_of_multiples = 0
for num in range(100, 201):
    if num % 9 == 0:
        sum_of_multiples += num
print(f"Sum of numbers divisible by 9 between 100 and 200: {sum_of_multiples}")