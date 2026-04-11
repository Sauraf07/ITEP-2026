n = int(input("Enter the number of terms: "))
for i in range(1, n+1):
    if i % 5 == 0:
        print("Hello", end=" ")
    else:
        print(i, end=" ")