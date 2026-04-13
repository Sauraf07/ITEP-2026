n = 5
for i in range(1, n+1):
    for j in range(1, 2*n):
        print("*" if j==n-i+1 or j==n+i-1 else " ", end="")
    print()
for i in range(n-1, 0, -1):
    for j in range(1, 2*n):
        print("*" if j==n-i+1 or j==n+i-1 else " ", end="")
    print()