n = 5
for i in range(1, n+1):
    for j in range(n, n-i, -1):
        print(j, end="")
    print()
